import subprocess
import sys

required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper",
    "pytz": "pytz",
    "fake_useragent": "fake-useragent"
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
    
import subprocess
import sys
import os
import json
import socket
import time
import base64
import requests
import pytz
import threading
from datetime import datetime, timedelta
from colorama import Fore, init
from rich.console import Console

# Khởi tạo console và clear màn hình
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
console = Console()

# Đường dẫn tới file chứa key trên GitHub
KEYS_JSON_URL = "https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/key.json"
LOCAL_KEY_FILE = "key_gitcode_xworld.json"

# Biến toàn cục
current_key = None
key_valid = True
lock = threading.Lock()

# Tùy chỉnh base64-65
def encode_b64_65(data):
    base = base64.b64encode(data.encode()).decode()
    return base.replace("=", "*")  # thay = thành *

def decode_b64_65(data):
    base = data.replace("*", "=")
    return base64.b64decode(base.encode()).decode()

# Kiểm tra mạng
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=10)
    except OSError:
        sys.exit(1)
kiem_tra_mang()

# In banner ngày giờ
def banner():
    current_time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%d/%m/%Y %H:%M:%S')
    print(f"""
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
""")
banner()

# Thời gian hiện tại
def get_current_time():
    return datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))

# Lấy key từ GitHub
def get_keys_from_github():
    try:
        response = requests.get(KEYS_JSON_URL, timeout=10)
        if response.status_code == 200:
            text = response.text
            if text.strip().startswith("{") or text.strip().startswith("["):
                return json.loads(text)
            else:
                cleaned = text[text.find("{"):text.rfind("}")+1]
                return json.loads(cleaned)
        return {"key": []}
    except:
        return {"key": []}

# Kiểm tra key và lấy thời gian hết hạn
def check_key_github(input_key):
    keys_data = get_keys_from_github()
    now = get_current_time()
    for key_data in keys_data.get("key", []):
        if not isinstance(key_data, dict):
            continue
        if key_data.get("key") == input_key and key_data.get("status") == "active":
            expires_at = key_data.get("expires_at")
            try:
                exp_time = datetime.fromisoformat(expires_at).replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
                if now <= exp_time:
                    return True, exp_time
                else:
                    return False, None
            except:
                continue
    return False, None

# Tính thời gian còn lại
def calculate_remaining_time(expires_at):
    now = get_current_time()
    time_diff = expires_at - now
    if time_diff.total_seconds() <= 0:
        return "Key đã hết hạn."
    days = time_diff.days
    hours, rem = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"Key còn lại: {days} ngày {hours} giờ {minutes} phút {seconds} giây."

# Lưu key mã hóa
def save_key_to_file(key):
    encoded = encode_b64_65(key)
    with open(LOCAL_KEY_FILE, "w") as f:
        json.dump({"key": encoded}, f)

# Đọc key từ file
def load_key_from_file():
    if not os.path.exists(LOCAL_KEY_FILE):
        return None
    try:
        with open(LOCAL_KEY_FILE, "r") as f:
            data = json.load(f)
        return decode_b64_65(data.get("key", ""))
    except:
        return None

# Kiểm tra key định kỳ
def check_key_expiry_periodically():
    global key_valid
    while key_valid:
        with lock:
            if current_key:
                is_valid, expires_at = check_key_github(current_key)
                if not is_valid or (expires_at and expires_at < get_current_time()):
                    key_valid = False
                    os._exit(0)
        time.sleep(60)

# Nhập an toàn
def safe_input(prompt):
    while True:
        try:
            return console.input(prompt)
        except EOFError:
            console.print("[bold red]Ctrl+D bị chặn! Vui lòng nhập lại.[/bold red]")
        except KeyboardInterrupt:
            console.print("[bold red]Ctrl+C bị chặn![/bold red]")

# === CHẠY TOOL ===
def run_tool():
    global current_key, key_valid

    # Thử đọc key đã lưu
    cached_key = load_key_from_file()
    if cached_key:
        is_valid, expires_at = check_key_github(cached_key)
        if is_valid:
            current_key = cached_key
            key_valid = True
            remaining_time = calculate_remaining_time(expires_at)
            console.print(f"[bold green]{remaining_time}[/bold green]")
            time.sleep(6)
            sys.exit(0)
        else:
            console.print("[bold red]Key đã hết hạn. Vui lòng mua lại key![/bold red]")
            try:
                os.remove(LOCAL_KEY_FILE)
            except:
                pass
            key_valid = False

    # Nếu chưa có key hoặc key đã hết hạn
    console.print("[bold yellow]Vui lòng nhập key hợp lệ từ GitHub.[/bold yellow]")

    while True:
        nhap_key = safe_input("[bold blue][[bold red]NHẬP KEY[/bold red]][/bold blue][bold yellow]==>> [/bold yellow]").strip()
        is_valid, expires_at = check_key_github(nhap_key)
        if is_valid:
            current_key = nhap_key
            save_key_to_file(nhap_key)
            remaining_time = calculate_remaining_time(expires_at)
            console.print(f"\n[bold green]{remaining_time}[/bold green]")
            time.sleep(6)
            sys.exit(0)
        else:
            console.print("\n[bold red]Key không hợp lệ hoặc đã hết hạn. Vui lòng thử lại![/bold red]")
            time.sleep(2)

# Gọi hàm chạy chính
try:
    run_tool()
except Exception as e:
    sys.exit(1)
import requests
import json
import time
import re
import os
from fake_useragent import UserAgent
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.prompt import Prompt

# Khởi tạo console và user-agent
console = Console()
ua = UserAgent()

# ======================= ĐĂNG NHẬP & LƯU THÔNG TIN =========================
def show_auth_panel():
    text = Text("LOGIN XWORLD", style="bold italic bright_cyan", justify="center")
    panel = Panel(text, border_style="bright_cyan")
    console.clear()
    console.print(panel)

def extract_credentials(url):
    user_id_pattern = r"userId=(\d+)"
    secret_key_pattern = r"secretKey=([a-f0-9]+)"
    user_id_match = re.search(user_id_pattern, url)
    secret_key_match = re.search(secret_key_pattern, url)
    return user_id_match.group(1) if user_id_match else None, secret_key_match.group(1) if secret_key_match else None

def save_to_file(user_id, secret_key):
    payload = {"user_id": int(user_id), "user_secret_key": secret_key}
    with open("login_xworld.py", "w") as file:
        file.write("PAYLOAD = " + repr(payload) + "\n")

def load_payload_from_file():
    try:
        with open("login_xworld.py", "r") as file:
            content = file.read()
            match = re.search(r"PAYLOAD\s*=\s*({.*})", content)
            return json.loads(match.group(1).replace("'", '"')) if match else None
    except FileNotFoundError:
        return None

def show_credentials_panel(user_id, secret_key):
    content = f"[bold bright_green]user_id:[/bold bright_green] [bold bright_cyan]{user_id}[/bold bright_cyan]\n" \
              f"[bold bright_yellow]user_secret_key:[/bold bright_yellow] [bold bright_cyan]{secret_key}[/bold bright_cyan]"
    panel = Panel(content, border_style="bold bright_cyan", title="Thông tin đăng nhập", title_align="center")
    console.print(panel)

def login_handler():
    while True:
        show_auth_panel()
        payload = load_payload_from_file()
        if payload:
            show_credentials_panel(payload['user_id'], payload['user_secret_key'])
        else:
            console.print("[bold red]Chưa có thông tin đăng nhập![/bold red]")
        choice = input("Bạn có muốn đổi user_id với user_secret_key (y/n): ").strip().lower()
        if choice == "y":
            url = input("Vui lòng nhập link có chứa userId và secretKey: ").strip()
            user_id, secret_key = extract_credentials(url)
            if user_id and secret_key:
                save_to_file(user_id, secret_key)
                console.print("[bold green]✅ Thông tin đã được cập nhật vào login_xworld.py[/bold green]")
            else:
                console.print("[bold red]❌ Không tìm thấy userId hoặc secretKey trong link.[/bold red]")
        else:
            break
    return payload

# ============================ CÀI ĐẶT SETTINGS ===============================
def load_settings():
    settings = {
        "code": "",
        "remaining_turns": 5  # Giá trị mặc định (ngưỡng tiến độ)
    }

    while True:
        text = Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center")
        panel = Panel(text, border_style="bright_cyan")
        console.print(panel)  # Không xóa màn hình

        table = Table(title="", show_header=True, header_style="bold cyan")
        table.add_column("STT", justify="center", style="bold")
        table.add_column("Mục", justify="left", style="bold")
        table.add_column("Giá trị", justify="center", style="bold")

        table.add_row("1", "Gitcode", f"[bold cyan]{settings['code'] or 'Chưa nhập'}[/bold cyan]")
        table.add_row("2", "Còn bao nhiêu lượt thì nhập", f"[bold cyan]{settings['remaining_turns']}[/bold cyan]")

        console.print(table)

        edit_choice = Prompt.ask("Bạn muốn sửa mục nào?  hoặc nhấn Enter để tiếp tục", default="")
        if not edit_choice:
            if not settings["code"]:
                console.print("[bold red]Gitcode không được để trống! Vui lòng nhập gitcode.[/bold red]")
                continue
            break

        try:
            edit_index = int(edit_choice)
            if edit_index == 1:
                settings["code"] = Prompt.ask("Nhập gitcode: ", default=settings["code"])
            elif edit_index == 2:
                while True:
                    try:
                        settings["remaining_turns"] = int(Prompt.ask("Còn bao nhiêu lượt còn lại thì nhập", default=str(settings["remaining_turns"])))
                        break
                    except ValueError:
                        console.print("[bold red]Vui lòng nhập số hợp lệ cho số giây![/bold red]")
            else:
                console.print("[bold red]Số không hợp lệ! Vui lòng chọn 1 hoặc 2.[/bold red]")
        except ValueError:
            console.print("[bold red]Vui lòng nhập số hợp lệ![/bold red]")

    return settings

# ============================ API NHẬN CODE ===============================
def exchange_code(code, payload):
    random_user_agent = ua.random
    headers = {
        'authority': 'web3task.3games.io',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': random_user_agent,
        'xb-language': 'vi-VN',
    }

    if payload:
        headers.update({
            'user-id': str(payload.get('user_id', '')),
            'user-secret-key': payload.get('user_secret_key', '')
        })

    json_data = {
        'code': code,
        'os_ver': 'android',
        'platform': 'h5',
        'appname': 'app',
    }

    try:
        response = requests.post(
            'https://web3task.3games.io/v1/task/redcode/exchange',
            headers=headers,
            json=json_data,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            data = result.get("data") or {}
            value = data.get("value", 0)
            currency = data.get("currency", "build")
            # Kiểm tra lỗi không nhận được code
            if value == 0 and result.get("message"):
                return False, None, None, result.get("message", "Không nhận được code")
            return True, value, currency, None
        else:
            try:
                result = response.json()
                error_message = result.get("message", f"Lỗi API. Status code: {response.status_code}")
                return False, None, None, error_message
            except ValueError:
                return False, None, None, f"Lỗi API. Status code: {response.status_code}"

    except Exception as e:
        return False, None, None, f"Lỗi kết nối: {e}"

# ============================ LẤY DỮ LIỆU & HIỂN THỊ =========================
def fetch_and_display(code, payload, remaining_turns):
    console.clear()  # Xóa màn hình khi chạy
    if not code:
        console.print("[bold red]Lỗi: Gitcode trống! Vui lòng nhập lại settings.[/bold red]")
        settings_table = Table(title="", show_header=True, header_style="bold cyan")
        settings_table.add_column("STT", justify="center", style="bold")
        settings_table.add_column("Mục", justify="left", style="bold")
        settings_table.add_column("Giá trị", justify="center", style="bold")
        settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
        settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
        settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
        console.print(settings_panel)
        return False, load_settings()

    random_user_agent = ua.random
    headers = {
        'authority': 'web3task.3games.io',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        'country-code': 'vn',
        'origin': 'https://xworld-app.com',
        'referer': 'https://xworld-app.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': random_user_agent,
        'xb-language': 'vi-VN',
    }

    json_data = {
        'code': code,
        'os_ver': 'android',
        'platform': 'h5',
        'appname': 'app',
    }

    if payload:
        json_data.update({
            'user_id': payload.get('user_id'),
            'secret_key': payload.get('user_secret_key')
        })

    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.post(
                'https://web3task.3games.io/v1/task/redcode/detail',
                headers=headers,
                json=json_data,
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()
                data = result.get("data") or {}

                code = data.get("code", "N/A")
                value = data.get("value", 0)
                currency = data.get("currency", "build")
                user_cnt = data.get("user_cnt", 0)
                progress = data.get("progress", 0)

                # Tính toán tiến độ còn lại (trừ ngược lại: user_cnt - progress)
                progress_minus_user = user_cnt - progress

                # Kiểm tra điều kiện kích hoạt API nhận code
                reward_received = False
                reward_value = None
                reward_currency = None
                error_message = None
                exchange_called = False
                if progress_minus_user <= remaining_turns and code != "N/A":
                    exchange_called = True
                    retry_count_exchange = 0
                    max_retries_exchange = 3
                    while retry_count_exchange < max_retries_exchange:
                        reward_received, reward_value, reward_currency, error_message = exchange_code(code, payload)
                        if reward_received or not error_message or "Lỗi kết nối" in error_message or "Status code" in error_message:
                            break
                        retry_count_exchange += 1
                        console.print(f"[red]Lỗi: {error_message} (Thử lại {retry_count_exchange}/{max_retries_exchange})[/]")
                        time.sleep(1)

                # Hiển thị bảng Rich
                table = Table.grid(padding=(0, 1))
                table.add_column(justify="right", style="cyan", no_wrap=True)
                table.add_column(justify="left", style="white")

                table.add_row("Code", f"[bold yellow]{code}[/]")
                table.add_row("Giá trị", f"[bold green]{value:,.0f} {currency}[/]")
                table.add_row("Tiến độ", f"[bold]{user_cnt}[/] / [bold]{progress}[/] ([bold]{abs(progress_minus_user)}[/])")
                table.add_row("Bạn nhận được", f"[bold green]{reward_value:,.0f} {reward_currency}[/]" if reward_received else f"[bold red]{error_message or 'đuma anh Buash Ang chưa nhận code đâu đợi tí đê!!!'}[/]")

                panel = Panel(table, title="", box=box.ROUNDED, border_style="cyan")
                console.print(panel)

                # Nếu API nhận code được gọi (thành công hoặc thất bại) hoặc progress_minus_user == 0, xử lý
                if (exchange_called or progress_minus_user == 0) and code != "N/A":
                    if reward_received:
                        console.print("[bold yellow]Yêu cầu nhập lại settings![/bold yellow]")
                        settings_table = Table(title="", show_header=True, header_style="bold cyan")
                        settings_table.add_column("STT", justify="center", style="bold")
                        settings_table.add_column("Mục", justify="left", style="bold")
                        settings_table.add_column("Giá trị", justify="center", style="bold")
                        settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
                        settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
                        settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
                        console.print(settings_panel)
                        return False, load_settings()
                    else:
                        console.print("[bold yellow]Yêu cầu nhập lại settings![/bold yellow]")
                        settings_table = Table(title="", show_header=True, header_style="bold cyan")
                        settings_table.add_column("STT", justify="center", style="bold")
                        settings_table.add_column("Mục", justify="left", style="bold")
                        settings_table.add_column("Giá trị", justify="center", style="bold")
                        settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
                        settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
                        settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
                        console.print(settings_panel)
                        return False, load_settings()
                return True, None  # Tiếp tục vòng lặp nếu code là "N/A"
            else:
                console.print(f"[red]Lỗi API detail. Status code: {response.status_code}[/]")
                try:
                    result = response.json()
                    error_message = result.get("message", "Không có thông báo lỗi cụ thể")
                    console.print(f"[red]Thông báo lỗi từ API: {error_message}[/]")
                except ValueError:
                    console.print("[red]Không thể phân tích phản hồi API.[/]")
                console.print("[bold yellow]Yêu cầu nhập lại settings![/bold yellow]")
                settings_table = Table(title="", show_header=True, header_style="bold cyan")
                settings_table.add_column("STT", justify="center", style="bold")
                settings_table.add_column("Mục", justify="left", style="bold")
                settings_table.add_column("Giá trị", justify="center", style="bold")
                settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
                settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
                settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
                console.print(settings_panel)
                return False, load_settings()

        except requests.exceptions.ReadTimeout:
            retry_count += 1
            console.print(f"[red]Lỗi kết nối: Read timed out (Thử lại {retry_count}/{max_retries})[/]")
            if retry_count == max_retries:
                console.print("[bold yellow]Yêu cầu nhập lại settings![/bold yellow]")
                settings_table = Table(title="", show_header=True, header_style="bold cyan")
                settings_table.add_column("STT", justify="center", style="bold")
                settings_table.add_column("Mục", justify="left", style="bold")
                settings_table.add_column("Giá trị", justify="center", style="bold")
                settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
                settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
                settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
                console.print(settings_panel)
                return False, load_settings()
            time.sleep(1)  # Đợi 1 giây trước khi thử lại
            continue
        except Exception as e:
            console.print(f"[red]Lỗi kết nối hoặc xử lý: {e}[/]")
            console.print("[bold yellow]Yêu cầu nhập lại settings![/bold yellow]")
            settings_table = Table(title="", show_header=True, header_style="bold cyan")
            settings_table.add_column("STT", justify="center", style="bold")
            settings_table.add_column("Mục", justify="left", style="bold")
            settings_table.add_column("Giá trị", justify="center", style="bold")
            settings_table.add_row("1", "Gitcode", f"[bold cyan]{code or 'Chưa nhập'}[/bold cyan]")
            settings_table.add_row("2", "Còn bao nhiêu giây", f"[bold cyan]{remaining_turns}[/bold cyan]")
            settings_panel = Panel(settings_table, border_style="bright_cyan", title=Text("Cài đặt Settings", style="bold italic bright_cyan", justify="center"))
            console.print(settings_panel)
            return False, load_settings()

# ============================ CHƯƠNG TRÌNH CHÍNH ============================
def main():
    # Xử lý đăng nhập
    payload = login_handler()

    # Cài đặt settings ban đầu
    settings = load_settings()
    console.print("[bold green]Đã tải cài đặt thành công![/bold green]")
    
    # Lấy gitcode và remaining_turns từ settings
    code = settings["code"]
    remaining_turns = settings["remaining_turns"]

    # Chạy lặp liên tục
    while True:
        continue_loop, new_settings = fetch_and_display(code, payload, remaining_turns)
        if new_settings:
            code = new_settings["code"]
            remaining_turns = new_settings["remaining_turns"]
            console.print("[bold green]Đã tải cài đặt mới thành công![/bold green]")
        elif not continue_loop:
            break
        time.sleep(0.9)  # Lặp lại sau mỗi 0.9 giây

if __name__ == "__main__":
    main()