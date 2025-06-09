import json
import os
import time
import requests
from datetime import datetime
from colorama import Fore, init
from rich.table import Table
from rich.console import Console

# Khởi tạo colorama và rich
init(autoreset=True)
console = Console()

cookie_file = "twitter_cookie.txt"

# Định nghĩa màu sắc cho đầu ra
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
vang = "\033[1;33m\033[1m"

hack = "\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> "

# Banner
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
{Fore.YELLOW}║              {Fore.YELLOW}Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
"""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)

# Hàm lấy link rút gọn từ YeuMoney
def get_shortened_link_yeumoney(url):
    token = "e08f033dc21da1dbc122f1bc883f61ba343fa5ff0b2816de7c32ab137b44e112"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            shortened_url = response.text.strip()
            if shortened_url.startswith("http"):  # Kiểm tra xem có phải là URL hợp lệ
                return shortened_url
            else:
                return f"Lỗi: Phản hồi từ API không phải là URL hợp lệ - {shortened_url}"
        else:
            return f"Lỗi: Mã trạng thái {response.status_code} - {response.text}"
    except requests.Timeout:
        return "Lỗi: Hết thời gian kết nối tới API YeuMoney!"
    except requests.RequestException as e:
        return f"Lỗi: Không thể kết nối tới API YeuMoney - {str(e)}"

# Vòng lặp để tiếp tục rút gọn link
while True:
    # Sử dụng tool
    link = input(f"{hack}NHẬP LINK CẦN RÚT GỌN (hoặc nhấn Enter để thoát): {vang}")

    # Kiểm tra nếu người dùng nhấn Enter (chuỗi rỗng) thì thoát
    if not link:
        print(f"{hack}{trang}Đã thoát chương trình!")
        break

    # Rút gọn URL với YeuMoney API
    shortened_link = get_shortened_link_yeumoney(link)

    if shortened_link.startswith("Lỗi"):
        print(f"{hack}{trang}Lỗi: {vang}{shortened_link}")
    else:
        print(f"{hack}{xanh_la}LINK RÚT GỌN CỦA BẠN LÀ: {vang}{shortened_link}")

    # Hỏi người dùng có muốn tiếp tục không
    continue_choice = input(f"{hack}Bạn có muốn tiếp tục rút gọn link khác không? (y/n): {vang}")
    if continue_choice.lower() != 'y':
        print(f"{hack}{trang}Đã thoát chương trình!")
        break