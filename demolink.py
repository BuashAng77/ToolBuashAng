import json
import os
import time
import random
import cloudscraper
import requests
import socket
from datetime import datetime
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
    """Tạo file Authorization.txt, token.txt, và linkedin_cookie.txt nếu chưa tồn tại."""
    files = ["Authorization.txt", "token.txt", "linkedin_cookie.txt"]
    for file_name in files:
        if not os.path.exists(file_name):
            try:
                with open(file_name, "w") as f:
                    f.write("")
                print(f"\033[1;32mĐã tạo file {file_name} thành công! ✅")
            except Exception as e:
                print(f"\033[1;31mLỗi khi tạo file {file_name}: {e} ❌")
                quit()

def load_credentials():
    """Đọc Authorization và Token từ file."""
    initialize_files()
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

def load_linkedin_cookie():
    """Đọc LinkedIn Cookie từ file."""
    try:
        with open("linkedin_cookie.txt", "r") as cookie_file:
            return cookie_file.read().strip()
    except Exception as e:
        print(f"\033[1;31mLỗi khi đọc file linkedin_cookie.txt: {e} ❌")
        return ""

def save_linkedin_cookie(linkedin_cookie):
    """Lưu LinkedIn Cookie vào file."""
    try:
        with open("linkedin_cookie.txt", "w") as cookie_file:
            cookie_file.write(linkedin_cookie)
        print("\033[1;32mĐã lưu LinkedIn Cookie vào file! ✅")
    except Exception as e:
        print(f"\033[1;31mLỗi khi lưu file linkedin_cookie.txt: {e} ❌")
        quit()

banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╗░██╗░░░██╗░█████╗░░██████╗██╗░░██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╦╝██║░░░██║███████║╚█████╗░███████║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║             
{Fore.YELLOW}║  {Fore.WHITE}          ░█████╗░███╗░░██║░██████╗░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██╗████╗░██║██╔════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ███████║██╔██╗██║██║░░██╗░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ⌛            {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
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
    author = input("\033[1;32mNHẬP AUTHORIZATION: \033[1;33m").strip()
    token = input("\033[1;32mNHẬP T (Token): \033[1;33m").strip()
    if not author or not token:
        print("\033[1;31mAuthorization hoặc Token không được để trống! ❌")
        quit()
    save_credentials(author, token)
else:
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

# Cập nhật headers cho GoLike API
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Referer': 'https://app.golike.net/account/manager/linkedin',
}

def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/linkedin-account',
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
            'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs',
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
            'account_id': account_id,
            'ads_id': ads_id
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs',
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
            'provider': 'linkedin',
            'fb_id': account_id,
            'error_type': 6,
        }
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        json_data2 = {
            'linkedin_users_advertising_id': ads_id,
            'object_id': object_id,
            'linkedin_account_id': account_id,
            'type': loai,
        }
        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception:
        pass

def dsacc():
    console = Console()
    if chonlinkedin.get("status") != 200:
        console.print("[bold red]Authorization hoặc T sai ❌[/]")
        quit()
    
    if not chonlinkedin["data"] or not isinstance(chonlinkedin["data"], list):
        console.print("[bold red]Dữ liệu tài khoản không hợp lệ hoặc trống! ❌[/]")
        quit()
    
    table = Table(title="Danh Sách Tài Khoản LinkedIn", title_style="blink #FFFFFF ", show_lines=True)
    table.add_column("STT", justify="center", style="blink #C82E31", no_wrap=True)
    table.add_column("Tài Khoản username", justify="left", style="blink yellow")
    table.add_column("Account ID", justify="left", style="blink green")
    table.add_column("Lần Cuối Làm Nhiệm Vụ", justify="center", style="bold #00B2BF")
    table.add_column("Trạng Thái Tài Khoản", justify="center", style="bold #79378B")
    
    for i in range(len(chonlinkedin["data"])):
        username = str(chonlinkedin["data"][i].get("name", "N/A"))
        account_id = str(chonlinkedin["data"][i].get("id", "N/A"))
        status = chonlinkedin["data"][i].get("status", "N/A")
        updated_at_raw = chonlinkedin["data"][i].get("updated_at", "N/A")
        updated_at_display = "N/A"
        if updated_at_raw != "N/A":
            try:
                updated_at = datetime.strptime(updated_at_raw, "%Y-%m-%dT%H:%M:%S.%fZ")
                updated_at_formatted = updated_at.strftime("%d/%m/%Y %H:%M:%S")
                current_time = datetime.now()
                delta_days = (current_time - updated_at).days
                updated_at_display = f"{updated_at_formatted} (số ngày: {delta_days})"
            except:
                updated_at_display = updated_at_raw
        status_display = f"Hoạt Động {random.choice(account_icons)}" if str(status) == "1" else str(status)
        table.add_row(
            str(i + 1),
            username,
            account_id,
            updated_at_display,
            status_display
        )
    
    console.print(table)

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║   \033[1;33m   DANH SÁCH ACC LINKEDIN    \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

chonlinkedin = chonacc()
dsacc()
print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True:
    try:
        luachon = int(input("\033[1;32mChọn tài khoản LINKEDIN: \033[1;33m"))
        while luachon > len(chonlinkedin["data"]):
            luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
        account_id = chonlinkedin["data"][luachon - 1]["id"]
        linkedin_cookie = load_linkedin_cookie()
        if linkedin_cookie:
            print(f"\033[1;32mCookie LinkedIn hiện tại: \033[1;33m{linkedin_cookie[:50]}... (đã cắt bớt để hiển thị)")
            print("\033[1;36m[1] \033[1;32mSử dụng cookie cũ")
            print("\033[1;36m[2] \033[1;32mNhập cookie mới")
            cookie_choice = input("\033[1;32mNhập lựa chọn (1/2): \033[1;33m")
            if cookie_choice == "2":
                linkedin_cookie = input("\033[1;32mNhập LinkedIn Cookie mới: \033[1;33m").strip()
                if not linkedin_cookie:
                    print("\033[1;31mLinkedIn Cookie không được để trống! ❌")
                    quit()
                save_linkedin_cookie(linkedin_cookie)
            elif cookie_choice != "1":
                print("\033[1;31mLựa chọn không hợp lệ, sử dụng cookie cũ! ❌")
        else:
            print("\033[1;31mChưa có LinkedIn Cookie! Vui lòng nhập cookie mới.")
            linkedin_cookie = input("\033[1;32mNhập LinkedIn Cookie mới: \033[1;33m").strip()
            if not linkedin_cookie:
                print("\033[1;31mLinkedIn Cookie không được để trống! ❌")
                quit()
            save_linkedin_cookie(linkedin_cookie)
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
        dsaccloi.append(chonlinkedin["data"][luachon - 1]["name"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m  Acc LinkedIn {dsaccloi} gặp vấn đề ⚠️")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print("\033[1;36mĐang chờ chọn tài khoản mới...")
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32mChọn tài khoản mới: \033[1;33m"))
                while luachon > len(chonlinkedin["data"]):
                    luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
                account_id = chonlinkedin["data"][luachon - 1]["id"]
                linkedin_cookie = load_linkedin_cookie()
                if linkedin_cookie:
                    print(f"\033[1;32mCookie LinkedIn hiện tại: \033[1;33m{linkedin_cookie[:50]}... (đã cắt bớt để hiển thị)")
                    print("\033[1;36m[1] \033[1;32mSử dụng cookie cũ")
                    print("\033[1;36m[2] \033[1;32mNhập cookie mới")
                    cookie_choice = input("\033[1;32mNhập lựa chọn (1/2): \033[1;33m")
                    if cookie_choice == "2":
                        linkedin_cookie = input("\033[1;32mNhập LinkedIn Cookie mới: \033[1;33m").strip()
                        if not linkedin_cookie:
                            print("\033[1;31mLinkedIn Cookie không được để trống! ❌")
                            quit()
                        save_linkedin_cookie(linkedin_cookie)
                    elif cookie_choice != "1":
                        print("\033[1;31mLựa chọn không hợp lệ, sử dụng cookie cũ! ❌")
                else:
                    print("\033[1;31mChưa có LinkedIn Cookie! Vui lòng nhập cookie mới.")
                    linkedin_cookie = input("\033[1;32mNhập LinkedIn Cookie mới: \033[1;33m").strip()
                    if not linkedin_cookie:
                        print("\033[1;31mLinkedIn Cookie không được để trống! ❌")
                        quit()
                    save_linkedin_cookie(linkedin_cookie)
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
    
    print(f"\033[1;32mNhiệm vụ {dem+1}: Mở link này và thực hiện {job_type}: \033[1;33m{link}")
    input("\033[1;36mNhấn Enter sau khi hoàn thành nhiệm vụ trong trình duyệt...")
    
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
            if nhantien and nhantien.get("success"):
                break
        except:
            pass
        attempts += 1
    
    if nhantien and nhantien.get("success"):
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        h = f"{local_time.tm_hour:02d}"
        m = f"{local_time.tm_min:02d}"
        s = f"{local_time.tm_sec:02d}"
        chuoi = (f"\033[1;31m| \033[1;36m{dem}"
                 f" \033[1;37m| \033[1;33m{h}:{m}:{s} ⌛"
                 f" \033[1;37m| \033[1;32msuccess ✅"
                 f" \033[1;37m| \033[1;31m{job_type} 🔥"
                 f" \033[1;37m| \033[1;32m{ads_id} 🐥"
                 f" \033[1;37m| \033[1;32m+{tien} 💸"
                 f" \033[1;37m| \033[1;33m{tong} 💰")
        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, job_type)
            print("                                              ", end="\r")
            print(f"\033[1;31mNhận tiền thất bại ({doiacc}|{checkdoiacc}) ❌", end="\r")
            time.sleep(1)
            checkdoiacc += 1
        except:
            print("                                              ", end="\r")
            print(f"\033[1;31mNhận tiền thất bại ({doiacc}|{checkdoiacc}) ❌", end="\r")
            time.sleep(1)
            checkdoiacc += 1