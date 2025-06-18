import json
import os
import time
import random
import cloudscraper
import requests
from datetime import datetime
from colorama import Fore, init
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

init()  # Initialize colorama

# Lists for icons (giữ nguyên)
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

# Các hàm tiện ích như kiem_tra_mang, initialize_files, load_credentials, save_credentials, save_instagram_cookie, load_instagram_cookie giữ nguyên
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
    # Tạo instagram_cookie.txt riêng, chỉ khi cần
    if not os.path.exists("instagram_cookie.txt"):
        try:
            with open("instagram_cookie.txt", "w") as f:
                f.write("")
            print("\033[1;32mĐã tạo file instagram_cookie.txt thành công! ✅")
        except Exception as e:
            print(f"\033[1;31mLỗi khi tạo file instagram_cookie.txt: {e} ❌")
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

def save_instagram_cookie(instagram_cookie):
    """Lưu Instagram Cookie vào file."""
    try:
        with open("instagram_cookie.txt", "w") as cookie_file:
            cookie_file.write(instagram_cookie)
        print("\033[1;32mĐã lưu Instagram Cookie vào file! ✅")
    except Exception as e:
        print(f"\033[1;31mLỗi khi lưu file instagram_cookie.txt: {e} ❌")
        quit()

def load_instagram_cookie():
    """Đọc Instagram Cookie từ file, trả về chuỗi rỗng nếu file rỗng."""
    try:
        with open("instagram_cookie.txt", "r") as cookie_file:
            return cookie_file.read().strip()
    except Exception as e:
        print(f"\033[1;31mLỗi khi đọc file instagram_cookie.txt: {e} ❌")
        return ""

# Cập nhật headers cho Instagram API với các giá trị động
def update_instagram_headers(instagram_cookie):
    """Cập nhật headers cho Instagram API với cookie."""
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': instagram_cookie,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-asbd-id': '129477',
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
    }
    # Trích xuất csrftoken từ cookie
    if 'csrftoken=' in instagram_cookie:
        headers['x-csrftoken'] = instagram_cookie.split('csrftoken=')[1].split(';')[0]
    else:
        headers['x-csrftoken'] = ''
    headers['x-ig-www-claim'] = 'hmac.AR1Jw2LrciyrzAQskwSVGREElPZZJZjW74y38oTjDnNHOu9e'
    headers['x-instagram-ajax'] = '1014868636'
    return headers

def check_instagram_cookie(instagram_cookie, username):
    """Kiểm tra xem cookie Instagram có hợp lệ hay không."""
    ses = requests.Session()
    headers = update_instagram_headers(instagram_cookie)
    ses.headers.update(headers)
    try:
        # Gửi yêu cầu đến endpoint lấy thông tin người dùng
        url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
        response = ses.get(url)
        if response.status_code == 200 and '"status":"ok"' in response.text:
            print(f"\033[1;32mCookie hợp lệ cho tài khoản {username} ✅")
            return True
        else:
            print(f"\033[1;31mCookie không hợp lệ cho tài khoản {username}. Status: {response.status_code}, Response: {response.text} ❌")
            return False
    except Exception as e:
        print(f"\033[1;31mLỗi khi kiểm tra cookie: {str(e)} ❌")
        return False

def perform_instagram_action(object_id, job_type, instagram_cookie, username):
    """Thực hiện hành động Follow hoặc Like trên Instagram bằng cookie."""
    # Kiểm tra cookie trước khi thực hiện hành động
    if not check_instagram_cookie(instagram_cookie, username):
        print("\033[1;31mCookie không hợp lệ, vui lòng nhập cookie mới! ❌")
        new_cookie = input("\033[1;32mNhập Instagram Cookie mới: \033[1;33m").strip()
        if not new_cookie:
            print("\033[1;31mCookie không được để trống! ❌")
            return False, ""
        save_instagram_cookie(new_cookie)
        return False, new_cookie  # Trả về cookie mới để cập nhật

    ses = requests.Session()
    ses.headers.update(update_instagram_headers(instagram_cookie))
    
    try:
        if job_type == "follow":
            url = f"https://www.instagram.com/api/v1/friendships/create/{object_id}/"
            data = {
                'container_module': 'profile',
                'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                'user_id': object_id,
            }
            response = ses.post(url, data=data)
            if response.status_code == 200 and '"status":"ok"' in response.text:
                print(f"\033[1;32mFollow thành công cho user_id: {object_id} ✅")
                return True, instagram_cookie
            else:
                print(f"\033[1;31mFollow thất bại cho user_id: {object_id}. Status: {response.status_code}, Response: {response.text} ❌")
                return False, instagram_cookie
        elif job_type == "like":
            url = f"https://www.instagram.com/api/v1/web/likes/{object_id}/like/"
            response = ses.post(url, data={})
            if response.status_code == 200 and '"status":"ok"' in response.text:
                print(f"\033[1;32mLike thành công cho media_id: {object_id} ✅")
                return True, instagram_cookie
            else:
                print(f"\033[1;31mLike thất bại cho media_id: {object_id}. Status: {response.status_code}, Response: {response.text} ❌")
                return False, instagram_cookie
        else:
            print(f"\033[1;31mLoại job không hỗ trợ: {job_type} ❌")
            return False, instagram_cookie
    except Exception as e:
        print(f"\033[1;31mLỗi khi thực hiện {job_type}: {str(e)} ❌")
        return False, instagram_cookie

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'instagram',
            'fb_id': account_id,
            'error_type': 6,
        }
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        json_data2 = {
            'instagram_users_advertising_id': ads_id,
            'object_id': object_id,
            'instagram_account_id': account_id,
            'type': loai,
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
            headers=headers,
            json=json_data2,
        )
        print(f"\033[1;33mĐã bỏ qua job {ads_id} với lý do: Tôi đã làm Job này rồi ⚠️")
    except Exception as e:
        print(f"\033[1;31mLỗi khi báo lỗi job {ads_id}: {str(e)} ❌")

# Các hàm khác như chonacc, nhannv, hoanthanh, dsacc giữ nguyên
def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/instagram-account',
        headers=headers,
        json=json_data
    ).json()
    return response

def nhannv(account_id):
    try:
        params = {
            'instagram_account_id': account_id,
            'data': 'null',
        }
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/instagram/jobs',
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
            'instagram_account_id': account_id,
            'instagram_users_advertising_id': ads_id,
            'async': True,
            'data': 'null'
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception:
        return {}

def dsacc():
    console = Console()
    if choninstagram.get("status") != 200:
        console.print("[bold red]Authorization hoặc T sai ❌[/]")
        quit()
    
    if not choninstagram["data"] or not isinstance(choninstagram["data"], list):
        console.print("[bold red]Dữ liệu tài khoản không hợp lệ hoặc trống! ❌[/]")
        quit()
    
    table = Table(title="Danh Sách Tài Khoản Instagram", title_style="blink #FFFFFF ", show_lines=True)
    table.add_column("STT", justify="center", style="blink #C82E31", no_wrap=True)
    table.add_column("Tài Khoản username", justify="left", style="blink yellow")
    table.add_column("Account ID", justify="left", style="blink green")
    table.add_column("Lần Cuối Làm Nhiệm Vụ", justify="center", style="bold #00B2BF")
    table.add_column("Trạng Thái Tài Khoản", justify="center", style="bold #79378B")
    
    for i in range(len(choninstagram["data"])):
        username = str(choninstagram["data"][i].get("instagram_username", "N/A"))
        account_id = str(choninstagram["data"][i].get("id", "N/A"))
        status = choninstagram["data"][i].get("status", "N/A")
        updated_at_raw = choninstagram["data"][i].get("updated_at", "N/A")
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

# Main program
banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╗░██╗░░░██║░█████╗░░██████╗██╗░░██║           {Fore.YELLOW}║
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

kiem_tra_mang()
scraper = cloudscraper.create_scraper()

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

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Referer': 'https://app.golike.net/account/manager/instagram',
}

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("\033[1;35m╔═════════════════════════════════╗")
print("\033[1;35m║   \033[1;33m   DANH SÁCH ACC INSTAGRAM    \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════╝")

choninstagram = chonacc()
dsacc()
print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True:
    try:
        luachon = int(input("\033[1;32mChọn tài khoản INSTAGRAM: \033[1;33m"))
        while luachon > len(choninstagram["data"]):
            luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
        account_id = choninstagram["data"][luachon - 1]["id"]
        username = choninstagram["data"][luachon - 1]["instagram_username"]  # Lấy username để kiểm tra cookie
        instagram_cookie = load_instagram_cookie()
        if instagram_cookie:
            print(f"\033[1;32mCookie Instagram hiện tại: \033[1;33m{instagram_cookie[:50]}... (đã cắt bớt để hiển thị)")
            print("\033[1;36m[1] \033[1;32mSử dụng cookie cũ")
            print("\033[1;36m[2] \033[1;32mNhập cookie mới")
            cookie_choice = input("\033[1;32mNhập lựa chọn (1/2): \033[1;33m")
            if cookie_choice == "2":
                instagram_cookie = input("\033[1;32mNhập Instagram Cookie mới: \033[1;33m").strip()
                if not instagram_cookie:
                    print("\033[1;31mInstagram Cookie không được để trống! ❌")
                    quit()
                save_instagram_cookie(instagram_cookie)
            elif cookie_choice != "1":
                print("\033[1;31mLựa chọn không hợp lệ, sử dụng cookie cũ! ❌")
        else:
            print("\033[1;31mChưa có Instagram Cookie! Vui lòng nhập cookie mới.")
            instagram_cookie = input("\033[1;32mNhập Instagram Cookie mới: \033[1;33m").strip()
            if not instagram_cookie:
                print("\033[1;31mInstagram Cookie không được để trống! ❌")
                quit()
            save_instagram_cookie(instagram_cookie)
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
        dsaccloi.append(choninstagram["data"][luachon - 1]["instagram_username"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m  Acc Instagram {dsaccloi} gặp vấn đề ⚠️")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print("\033[1;36mĐang chờ chọn tài khoản mới...")
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input("\033[1;32mChọn tài khoản mới: \033[1;33m"))
                while luachon > len(choninstagram["data"]):
                    luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại ❌: \033[1;33m"))
                account_id = choninstagram["data"][luachon - 1]["id"]
                username = choninstagram["data"][luachon - 1]["instagram_username"]
                instagram_cookie = load_instagram_cookie()
                if instagram_cookie:
                    print(f"\033[1;32mCookie Instagram hiện tại: \033[1;33m{instagram_cookie[:50]}... (đã cắt bớt để hiển thị)")
                    print("\033[1;36m[1] \033[1;32mSử dụng cookie cũ")
                    print("\033[1;36m[2] \033[1;32mNhập cookie mới")
                    cookie_choice = input("\033[1;32mNhập lựa chọn (1/2): \033[1;33m")
                    if cookie_choice == "2":
                        instagram_cookie = input("\033[1;32mNhập Instagram Cookie mới: \033[1;33m").strip()
                        if not instagram_cookie:
                            print("\033[1;31mInstagram Cookie không được để trống! ❌")
                            quit()
                        save_instagram_cookie(instagram_cookie)
                    elif cookie_choice != "1":
                        print("\033[1;31mLựa chọn không hợp lệ, sử dụng cookie cũ! ❌")
                else:
                    print("\033[1;31mChưa có Instagram Cookie! Vui lòng nhập cookie mới.")
                    instagram_cookie = input("\033[1;32mNhập Instagram Cookie mới: \033[1;33m").strip()
                    if not instagram_cookie:
                        print("\033[1;31mInstagram Cookie không được để trống! ❌")
                        quit()
                    save_instagram_cookie(instagram_cookie)
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
        print(f"\033[1;31mKhông nhận được job, thử lại... ❌")
        continue
    
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]
    
    if job_type not in ["follow", "like"]:
        baoloi(ads_id, object_id, account_id, job_type)
        print(f"\033[1;31mLoại job không hỗ trợ: {job_type} ❌")
        continue
    
    # Thực hiện hành động Follow hoặc Like
    action_success, new_cookie = perform_instagram_action(object_id, job_type, instagram_cookie, username)
    if new_cookie != instagram_cookie:
        instagram_cookie = new_cookie  # Cập nhật cookie mới
    if not action_success:
        baoloi(ads_id, object_id, account_id, job_type)
        print("                                              ", end="\r")
        print(f"\033[1;31mThực hiện {job_type} thất bại ({doiacc}|{checkdoiacc}) ❌")
        time.sleep(1)
        checkdoiacc += 1
        continue
    
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
        h = f"0{hour}" if hour < 10 else hour
        m = f"0{minute}" if minute < 10 else minute
        s = f"0{second}" if second < 10 else second
        chuoi = (f"\033[1;31m| \033[1;36m{dem}"
                 f" \033[1;37m| \033[1;33m{h}:{m}:{s} ⌛"
                 f" \033[1;37m| \033[1;32msuccess ✅"
                 f" \033[1;37m| \033[1;31m{job_type} 🔥"
                 f" \033[1;37m| \033[1;32m{account_id} 🐥"
                 f" \033[1;37m| \033[1;32m+{tien} 💸"
                 f" \033[1;37m| \033[1;33m{tong} 💰")
        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        baoloi(ads_id, object_id, account_id, job_type)
        print("                                              ", end="\r")
        print(f"\033[1;31mNhận tiền thất bại ({doiacc}|{checkdoiacc}) ❌")
        time.sleep(1)
        checkdoiacc += 1