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
import os
import sys
import json
import base64
import uuid
import time
import socket
import random
import string
from datetime import datetime, timedelta
from random import randint
from time import sleep, strftime
import requests
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from pystyle import Write, Colors
from rich.console import Console
from rich.text import Text
import pytz

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
console = Console()

# Kiểm tra kết nối mạng
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=10)
    except OSError:
        console.print("[bold red]Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.[/bold red]")
        sys.exit(1)
kiem_tra_mang()

# Hàm hiển thị banner
def banner():
    print(f"""{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
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
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
""")    
banner()

# Hàm lấy link rút gọn từ YeuMoney
def get_shortened_link_yeumoney(url):
    token = "e08f033dc21da1dbc122f1bc883f61ba343fa5ff0b2816de7c32ab137b44e112"
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi: {e}"

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

# Hàm tạo key
def generate_key(is_admin=False):
    if is_admin:
        return "BUASHANGKEYVIP"
    else:
        return f"BUASHANGDZAI-{generate_random_key(10)}"

# Hàm lấy thời gian từ module datetime và pytz
def get_current_time_from_api():
    try:
        tz = pytz.timezone("Asia/Ho_Chi_Minh")
        current_time = datetime.now(tz)
        return current_time.replace(tzinfo=None)
    except Exception as e:
        console.print(f"[bold red]Lỗi khi lấy thời gian hệ thống: {e}[/bold red]")
        return datetime.now()

# Hàm mã hóa thời gian thành base64
def encode_time(dt):
    epoch = int(dt.timestamp())
    return base64.b64encode(str(epoch).encode()).decode()

# Hàm giải mã thời gian từ base64
def decode_time(encoded):
    epoch = int(base64.b64decode(encoded).decode())
    return datetime.fromtimestamp(epoch)

# Hàm lưu key vào file
def save_key_to_file(key):
    timestamp = get_current_time_from_api()
    expiry_time = timestamp + timedelta(hours=12)
    encoded_timestamp = encode_time(timestamp)
    encoded_expiry = encode_time(expiry_time)
    with open("key.txt", "w") as f:
        f.write(f"{key} | {encoded_timestamp} | {encoded_expiry}\n")

# Hàm kiểm tra và xóa key nếu đã hết hạn
def clean_expired_key():
    if not os.path.exists("key.txt"):
        return    
    updated_lines = []
    current_time = get_current_time_from_api()    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, encoded_timestamp, encoded_expiry = line.strip().split(" | ")
                expiry = decode_time(encoded_expiry)
                if key.startswith("BUASHANGKEYVIP") or current_time <= expiry:
                    updated_lines.append(line)
            except:
                continue    
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key đã lưu
def check_stored_key():
    clean_expired_key()
    if not os.path.exists("key.txt"):
        return None, None, None    
    current_time = get_current_time_from_api()
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, encoded_timestamp, encoded_expiry = line.strip().split(" | ")
                stored_key = stored_key.strip()
                expiry = decode_time(encoded_expiry)
                if stored_key == "BUASHANGKEYVIP":
                    return stored_key, stored_key, None
                elif stored_key.startswith("BUASHANGDZAI-") and current_time <= expiry:
                    return stored_key, stored_key, expiry
            except:
                continue
    return None, None, None

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    clean_expired_key()
    if key == "BUASHANGKEYVIP":
        return True
    elif key == expected_key:
        return True
    return False

# Hàm tính thời gian còn lại
def format_time_remaining(expiry, current_time):
    time_diff = expiry - current_time
    total_seconds = int(time_diff.total_seconds())
    if total_seconds <= 0:
        return "Hết hạn"
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours} giờ {minutes} phút {seconds} giây"

# Hàm xử lý Ctrl+D
def safe_input(prompt):
    while True:
        try:
            return console.input(prompt)
        except EOFError:
            console.print("")
        except KeyboardInterrupt:
            console.print("")

# ======= Chạy Tool =======
try:
    admin_key = "BUASHANGKEYVIP"
    stored_key, user_key, expiry = check_stored_key()
    
    # Nếu không có key còn hạn, yêu cầu vượt link và nhập key
    if not stored_key:
        user_key = generate_key(is_admin=False)
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white] [bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red] [bold green]: {short_link}[/bold green]")
        
        while True:
            nhap_key = safe_input("[bold blue][[bold red]NHẬP KEY[/bold red]][/bold blue][bold yellow]==>> [/bold yellow]").strip()
            if is_valid_key(nhap_key, user_key):
                save_key_to_file(nhap_key)
                console.print("\n[bold green]Key hợp lệ! Đang vào Tool...[/bold green]", end="\r")
                time.sleep(3)
                print("\033[F\033[K" * 3, end="")
                break
            else:
                console.print("\n[bold red]Key không hợp lệ. Vui lòng vượt link để lấy key![/bold red]", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")
    else:
        link_can_rut = f"https://flowing-silo-450510-e1.web.app/key/?ma={user_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        if expiry:
            current_time = get_current_time_from_api()
            time_remaining = format_time_remaining(expiry, current_time)
            console.print(f"[bold green]Key [bold blue]{stored_key}[/bold blue] còn hạn (Thời gian còn lại: [bold yellow]{time_remaining}[/bold yellow]). Đang vào Tool...[/bold green]")
        else:
            console.print(f"[bold green]Key [bold blue]{stored_key}[/bold blue] là key vĩnh viễn. Đang vào Tool...[/bold green]")
        time.sleep(6)
        print("\033[F\033[K" * 4, end="")

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")

# Xóa màn hình và vào tool
os.system("cls" if os.name == "nt" else "clear")
console.print("[bold green]Đã vào Tool thành công![/bold green]")

import subprocess
import sys
required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper"
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
import os
import sys
import json
import base64
import uuid
import time
import socket
import random
import string
from datetime import datetime, timedelta
from random import randint
from time import sleep, strftime
import requests
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from pystyle import Write, Colors
from rich.console import Console
from rich.text import Text
init(autoreset=True)
os.system('cls' if os.name=='nt' else 'clear')
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
cam = "\033[38;5;208m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"
listck = []
listjob = []
import socket
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")
kiem_tra_mang()
def banner():
        print(f"""{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╗░██╗░░░██╗░█████╗░░██████╗██╗░░██╗           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╦╝██║░░░██║███████║╚█████╗░███████║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║             
{Fore.YELLOW}║  {Fore.WHITE}          ░█████╗░███╗░░██╗░██████╗░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██╗████╗░██║██╔════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ███████║██╔██╗██║██║░░██╗░.               {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
""")    
banner()
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import init, Fore
import os, time
init(autoreset=True)
console = Console()
def clear():
    os.system("clear" if os.name != "nt" else "cls")
def show_menu():
    table = Table(title="   TOOL BUASH ANG DZAI", box=box.SQUARE_DOUBLE_HEAD, style="white")
    table.add_column("STT", style="blink bright_Yellow", justify="center")
    table.add_column("Tên Tool", style="blink bright_green", justify="left")
    table.add_column("Mô tả", style="bold #FF4500")
    table.add_column("Trạng Thái", style="blink cyan")

    table.add_row("1", "GOLIKE TIKTOK", "ADB Tự Động | Ấn Tay","Hoạt động")    
    table.add_row("2", "GOLIKE TWITTER", "Cookie","Hoạt Động")        
    table.add_row("3", "Buff view tiktok", "tăng view","Đang Update")    
    table.add_row("4", "TDS FACEBOOK", "Cookie","Đang Update")
    table.add_row("5", "TDS TIKTOK", "Auto click","Đang Update")
    table.add_row("7", "DOS WEBSITE ", "Đánh Sập Wed","Hoạt Động")
    table.add_row("6", "SPAM ", "Nhây Số Điện Thoại","Hoạt Động")
    table.add_row("8", "Tạo Page Facebook ", "Pro 5 + Avatar + Đa Luồng","Hoạt Động")
    table.add_row("9", "Yeumony ", "Tạo Link Rút Gọn Bằng Yeumony","Hoạt Động")
    console.print(table)
def main():
    while True:
        clear()
        banner()
        show_menu()
        try:
            choice = input(f"\n\033[1;35mNhập STT: {Fore.CYAN}").strip()
        except KeyboardInterrupt:
            console.print("\n[red]Thoát...[/]")
            break
        kiem_tra_mang()
        if choice == "1":
            try: 
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/tiktokgolike.py').text
              exec(code, globals())
            except:
              sys.exit()  
        elif choice == "2":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/xgolike.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "3":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/view.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "4":
            try: 
              print(f"{Fore.RED}Chưa cập nhập, vui lòng chọn tool online")
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/hoangminhthieu2008/Thtool/refs/heads/main/tdsfb').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "5":
            try:
              print(f"{Fore.RED}Chưa cập nhập, vui lòng chọn tool online")
              exit()
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/hoangminhthieu2008/Thtool/refs/heads/main/tdstt').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "6":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/SMS.py').text
              exec(code, globals())
              sys.exit()
            except:
              sys.exit()
        elif choice == "7":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/dos.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "8":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/Pro5+avt+dalong.py').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "9":
            try:
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/taolinkrutgon.py').text
              exec(code, globals())
            except:
              sys.exit()
        
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()
