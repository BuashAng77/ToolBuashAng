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
missing = False
for module_name, pip_name in required_packages.items():
    try:
        __import__(module_name)
    except ImportError:
        print(f"Đang cài đặt thư viện thiếu: {pip_name} ...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            missing = True
        except Exception as e:
            print(f"Cài thư viện {pip_name} thất bại: {e}")
            missing = True
if missing:
    print("\nĐã cài đặt thư viện cần thiết.")
    print("Vui lòng **chạy lại tool**.")
    sys.exit()
import json
import os
import time
import random
import cloudscraper
import requests
import socket
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore, init
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

init()  # Initialize colorama

# Lists for icons
animal_emojis = ["🐶", "🐱", "🐻", "🦁", "🐼", "🐯", "🐷", "🐻‍❄️", "🐭", "🦊"]
account_icons = ["♥️", "🔥", "🌸", "⚡", "💮", "🌼", "💡", "🔔"]
dynamic_icons = ["⏳", "🔄", "💌", "⌛"]
colors = [
    "\033[1;31m",  # Red
    "\033[1;32m",  # Green
    "\033[1;33m",  # Yellow
    "\033[1;34m",  # Blue
    "\033[1;35m",  # Magenta
    "\033[1;36m",  # Cyan
    "\033[1;97m",  # White
]

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=10)
    except OSError:
        print("\033[1;31mMạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng ❌")
        quit()

def initialize_files():
    """Tạo file Authorization.txt và token.txt nếu chưa tồn tại."""
    files = ["Authorization.txt", "token.txt"]
    for file_name in files:
        if not os.path.exists(file_name):
            try:
                with open(file_name, "w") as f:
                    f.write("")  # Tạo file rỗng
                print(f"\033[1;32mĐã tạo file {file_name} thành công! ✅")
            except Exception as e:
                print(f"\033[1;31mLỗi khi tạo file {file_name}: {e} ❌")
                quit()

def load_credentials():
    """Đọc Authorization và Token từ file, trả về giá trị hoặc chuỗi rỗng nếu file rỗng."""
    initialize_files()  # Đảm bảo file tồn tại
    try:
        with open("Authorization.txt", "r") as auth_file, open("token.txt", "r") as token_file:
            author = auth_file.read().strip()
            token = token_file.read().strip()
        return author, token
    except Exception as e:
        print(f"\033[1;31mLỗi khi đọc file: {e} ❌")
        return "", ""

def save_credentials(author, token):
    """Lưu Authorization và Token vào file."""
    try:
        with open("Authorization.txt", "w") as auth_file, open("token.txt", "w") as token_file:
            auth_file.write(author)
            token_file.write(token)
        print("\033[1;32mĐã lưu Authorization và Token vào file! ✅")
    except Exception as e:
        print(f"\033[1;31mLỗi khi lưu file: {e} ❌")
        quit()

# Updated banner with current date/time
banner = f"""
{Fore.LIGHTYELLOW_EX}╔══════════════════════════════════════════════════════╗
{Fore.LIGHTYELLOW_EX}║                                                      {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}██████╗░██╗░░░██╗                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}██╔══██╗██║░░░██║                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}██████╦╝╚██╗░██╔╝                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}██╔══██╗░╚████╔╝░                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}██████╦╝░░╚██╔╝░░                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}╚═════╝░░░░╚═╝░░░                                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║                                                      {Fore.LIGHTYELLOW_EX}║             
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}████████╗░█████╗░░█████╗░██╗░░░░░                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}░░░██║░░░██║░░██║██║░░██║██║░░░░░                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}░░░██║░░░██║░░██║██║░░██║██║░░░░░                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}░░░██║░░░╚█████╔╝╚█████╔╝███████╗                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTWHITE_EX}░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝                   {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║                                                      {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTRED_EX}▶ Nhóm   : {Fore.LIGHTCYAN_EX}https://zalo.me/g/wdopga629              {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTGREEN_EX}▶ Wed bán VPS : {Fore.LIGHTMAGENTA_EX}Bvzone.cloud                        {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║  {Fore.LIGHTRED_EX}▶ Admin : {Fore.LIGHTBLUE_EX}Thành Trần                                {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║                                                      {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║                                                      {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}║              {Fore.LIGHTYELLOW_EX}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ⌛            {Fore.LIGHTYELLOW_EX}║
{Fore.LIGHTYELLOW_EX}╚══════════════════════════════════════════════════════╝
{Fore.RESET}
"""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║       \033[1;33m  ĐĂNG NHẬP GOLIKE        \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

# Kiểm tra mạng
kiem_tra_mang()
scraper = cloudscraper.create_scraper()

# Đọc Authorization và Token từ file
author, token = load_credentials()

if not author or not token:
    # Nếu file rỗng hoặc chưa có dữ liệu, yêu cầu người dùng nhập
    author = input("\033[1;32mNHẬP AUTHORIZATION: \033[1;33m").strip()
    token = input("\033[1;32mNHẬP T (Token): \033[1;33m").strip()
    if not author or not token:
        print("\033[1;31mAuthorization hoặc Token không được để trống! ❌")
        quit()
    save_credentials(author, token)
else:
    # Nếu đã có dữ liệu, cho phép người dùng giữ nguyên hoặc nhập mới
    print(f"\033[1;32m       Nhấn Enter để vào TOOL với Authorization và Token hiện tại")
    print(f"\033[38;2;0;220;255m               HOẶC ")
    select = input(f"\033[1;32mNhập AUTHORIZATION {Fore.RED}(tại đây) \033[1;32mđể vào acc khác: \033[1;33m").strip()
    kiem_tra_mang()
    if select:
        author = select
        token = input("\033[1;32mNhập T (Token): \033[1;33m").strip()
        if not author or not token:
            print("\033[1;31mAuthorization hoặc Token không được để trống! ❌")
            quit()
        save_credentials(author, token)

# Cập nhật headers
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/tiktok-account',
        headers=headers,
        json=json_data
    ).json()
    return response

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception:
        return {}

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
  'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception:
        return {}

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }
        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception:
        pass

def dsacc():
    console = Console()
    if chontktiktok.get("status") != 200:
        console.print("[bold red]Authorization hoặc T sai ❌[/]")
        quit()
    
    # Kiểm tra và chuẩn hóa dữ liệu
    if not chontktiktok["data"] or not isinstance(chontktiktok["data"], list):
        console.print("[bold red]Dữ liệu tài khoản không hợp lệ hoặc trống! ❌[/]")
        quit()
    
    # Create a Rich table
    table = Table(title="Danh Sách Tài Khoản TikTok", title_style="blink #FFFFFF ", show_lines=True)
    table.add_column("STT", justify="center", style="blink #C82E31", no_wrap=True)
    table.add_column("Tài Khoản username", justify="left", style="blink yellow")
    table.add_column("Account ID", justify="left", style="blink green")
    table.add_column("Lần Cuối Làm Nhiệm Vụ", justify="center", style="bold #00B2BF")  # Cột hiển thị updated_at
    table.add_column("Trạng Thái Tài Khoản", justify="center", style="bold #79378B")
    
    # Populate the table with account data
    for i in range(len(chontktiktok["data"])):
        unique_username = str(chontktiktok["data"][i].get("unique_username", "N/A"))
        account_id = str(chontktiktok["data"][i].get("id", "N/A"))
        status = chontktiktok["data"][i].get("status", "N/A")
        # Xử lý updated_at
        updated_at_raw = chontktiktok["data"][i].get("updated_at", "N/A")
        updated_at_display = "N/A"
        if updated_at_raw != "N/A":
            try:
                updated_at = datetime.strptime(updated_at_raw, "%Y-%m-%dT%H:%M:%S.%fZ")
                updated_at_formatted = updated_at.strftime("%d/%m/%Y %H:%M:%S")
                # Tính số ngày cách nhau
                current_time = datetime.now()
                delta_days = (current_time - updated_at).days
                updated_at_display = f"{updated_at_formatted} (số ngày: {delta_days})"  # Giữ định dạng như yêu cầu
            except:
                updated_at_display = updated_at_raw  # Giữ nguyên nếu không parse được
        # Chuyển đổi trạng thái số 1 thành "Hoạt Động" và thêm icon
        status_display = f"Hoạt Động {random.choice(account_icons)}" if str(status) == "1" else str(status)
        table.add_row(
            str(i + 1),
            unique_username,
            account_id,
            updated_at_display,  # Hiển thị giá trị updated_at với số ngày
            status_display
        )
    
    # Print the table
    console.print(table)

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║   \033[1;33m   DANH SÁCH ACC TIKTOK       \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

chontktiktok = chonacc()
dsacc()
print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True:
    try:
        luachon = int(input("\033[1;32mChọn tài khoản TIKTOK: \033[1;33m"))
        while luachon > len(chontktiktok["data"]):
            luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        break
    except:
        print("\033[1;31mSai Định Dạng ❌")

while True:
    try:
        delay = int(input(f"\033[1;32mDelay: \033[1;33m"))
        break
    except:
        print("\033[1;31mSai Định Dạng ❌")

while True:
    try:
        doiacc = int(input(f"\033[1;32mThất bại bao nhiêu lần thì đổi acc: \033[1;33m"))
        break
    except:
        print("\033[1;31mNhập Vào 1 Số ❌")

print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m  CHỌN LOẠI NHIỆM VỤ        \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")
print("\033[1;36m[1] \033[1;32mFollow")
print("\033[1;36m[2] \033[1;32mLike")
print("\033[1;36m[3] \033[1;32mCả hai (\033[1;33mFollow và Like\033[1;32m)")
while True:
    try:
        loai_nhiem_vu = int(input("\033[1;32mChọn loại nhiệm vụ: \033[1;33m"))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3! ❌")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số ❌")

x_like, y_like, x_follow, y_follow = None, None, None, None
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║       \033[1;33m  ADB tự động             \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")
print(f"\033[1;36m[1] Có")
print(f"\033[1;36m[2] Không")
adbyn = input(f"\033[1;32mNhập lựa chọn: \033[1;33m")
if adbyn == "1":
    def setup_adb():
        config_file = "adb_config.txt"
        like_coords_file = "toa_do_tim.txt"
        follow_coords_file = "toa_do_follow.txt"
        print(f"{Fore.MAGENTA}═══════════════════════════════════")
        print("\033[1;33mBạn có thể xem video hướng dẫn kết nối ADB")
        print("\033[1;33mLink video: \033[38;2;0;220;255mhttps://youtu.be/vcWNzu2XRSE?si=_jFVm9nhSkNGBK_-\033[0m")
        ip = input("\033[1;32mNhập IP của thiết bị ví dụ (192.168.1.2): \033[1;33m")
        adb_port = input("\033[1;32mNhập port của thiết bị ví dụ (39327): \033[1;33m")
        x_like, y_like, x_follow, y_follow = None, None, None, None
        if os.path.exists(like_coords_file):
            with open(like_coords_file, "r") as f:
                coords = f.read().split("|")
                if len(coords) == 2:
                    x_like, y_like = coords
                    print(f"\033[1;32mĐã tìm thấy tọa độ nút tim: X={x_like}, Y={y_like}")
        if os.path.exists(follow_coords_file):
            with open(follow_coords_file, "r") as f:
                coords = f.read().split("|")
                if len(coords) == 2:
                    x_follow, y_follow = coords
                    print(f"\033[1;32mĐã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
        if not os.path.exists(config_file):
            print("\033[1;36mLần đầu chạy, nhập mã ghép nối (6 SỐ) và port ghép nối.\033[0m")
            pair_code = input("\033[1;32mNhập mã ghép nối 6 số ví dụ (322763): \033[1;33m")
            pair_port = input("\033[1;32mNhập port ghép nối ví dụ (44832): \033[1;33m")
            with open(config_file, "w") as f:
                f.write(f"{pair_code}|{pair_port}")
        else:
            with open(config_file, "r") as f:
                pair_code, pair_port = [s.strip() for s in f.read().split("|")]
        print("\n\033[1;36m  Đang ghép nối với thiết bị\033[0m")
        os.system(f"adb pair {ip}:{pair_port} {pair_code}")
        time.sleep(2)
        print("\033[1;36m  Đang kết nối ADB\033[0m")
        os.system(f"adb connect {ip}:{adb_port}")
        time.sleep(2)
        devices = os.popen("adb devices").read()
        if ip not in devices:
            print(f"{Fore.RED} Kết nối thất bại ❌{Fore.WHITE}")
            exit()
        print("\033[1;35m╔═════════════════════════════════╗")
        print("\033[1;35m║     \033[1;33m  NHẬP TỌA ĐỘ NÚT         \033[1;35m║")
        print("\033[1;35m╚═════════════════════════════════╝")
        if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
            x_follow = input("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")
            y_follow = input("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")
            with open(follow_coords_file, "w") as f:
                f.write(f"{x_follow}|{y_follow}")
        if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
            x_like = input("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m")
            y_like = input("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m")
            with open(like_coords_file, "w") as f:
                f.write(f"{x_like}|{y_like}")
        return x_like, y_like, x_follow, y_follow
    x_like, y_like, x_follow, y_follow = setup_adb()
elif adbyn == "2":
    pass

dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("\033[1;37m════════════════════════════════════════════════════════════")
print("\033[1;31m| \033[1;36mSTT \033[1;37m| \033[1;33mThời gian \033[1;37m| \033[1;32mStatus \033[1;37m| \033[1;31mType job \033[1;37m| \033[1;32mID Acc \033[1;37m| \033[1;32mXu \033[1;37m| \033[1;33mTổng       ")
print("\033[1;37m════════════════════════════════════════════════════════════")

icon_index = 0
while True:
    if checkdoiacc >= doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["unique_username"])  # Sử dụng unique_username thay vì nickname
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m  Acc Tiktok {dsaccloi} gặp vấn đề ⚠️")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print("\033[1;36mĐang chờ chọn tài khoản mới...")
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32mChọn tài khoản mới: \033[1;33m"))
                while luachon > len(chontktiktok["data"]):
                    luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner)
                print("\033[1;37m════════════════════════════════════════════════════════════")
                print("\033[1;31m| \033[1;36mSTT \033[1;37m| \033[1;33mThời gian \033[1;37m| \033[1;32mStatus \033[1;37m| \033[1;31mType job \033[1;37m| \033[1;32mID Acc \033[1;37m| \033[1;32mXu \033[1;37m| \033[1;33mTổng       ")
                print("\033[1;37m════════════════════════════════════════════════════════════")
                break
            except:
                print("\033[1;31mSai Định Dạng ❌")
    
    print(f'\033[1;35m🐥BUASH ANG Đang Tìm Nhiệm Vụ Cho Bạn💸', end="\r")
    icon_index = (icon_index + 1) % len(dynamic_icons)
    time.sleep(0.5)
    
    max_retries = 3
    retry_count = 0
    nhanjob = None
    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception:
            retry_count += 1
            time.sleep(1)
    if not nhanjob or retry_count >= max_retries:
        continue
    
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]
    
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue
    
    try:
        if adbyn == "1":
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else:
            subprocess.run(["termux-open-url", link])
        for remaining in range(3, 0, -1):
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")
    except Exception:
        baoloi(ads_id, object_id, account_id, job_type)
        continue
    
    if job_type == "like" and adbyn == "1" and x_like and y_like:
        os.system(f"adb shell input tap {x_like} {y_like}")
    elif job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os.system(f"adb shell input tap {x_follow} {y_follow}")
    
    for remaining_time in range(delay, -1, -1):
        color = colors[remaining_time % len(colors)]
        animal = random.choice(animal_emojis)
        print(f"\r{color}🐥BUASH ANG | ĐẸP TRAI VCL AHIHI| {remaining_time}s {animal}", end="")
        time.sleep(1)
    print("\r                          \r", end="")
    
    print(f"\033[1;35m🐥Buash Ang Đang Nhận Tiền Cho Bạn 💰{dynamic_icons[icon_index % len(dynamic_icons)]}", end="\r")
    icon_index = (icon_index + 1) % len(dynamic_icons)
    time.sleep(0.5)
    
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass
        attempts += 1
    
    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
        chuoi = (f"\033[1;31m| \033[1;36m{dem}"
                 f" \033[1;37m| \033[1;33m{h}:{m}:{s} ⌛"
                 f" \033[1;37m| \033[1;32msuccess ✅"
                 f" \033[1;37m| \033[1;31m{job_type} 🔥"
                 f" \033[1;37m| \033[1;32mẚn ID 🐥"
                 f" \033[1;37m| \033[1;32m+{tien} 💸"
                 f" \033[1;37m| \033[1;33m{tong} 💰")
        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("                                              ", end="\r")
            print(f"\033[1;31mNhận tiền thất bại ({doiacc}|{checkdoiacc}) ❌", end="\r")
            time.sleep(1)
            checkdoiacc += 1
        except:
            print("                                              ", end="\r")
            print(f"\033[1;31mNhận tiền thất bại ({doiacc}|{checkdoiacc}) ❌", end="\r")
            time.sleep(1)
            checkdoiacc += 1
