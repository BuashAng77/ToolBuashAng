import json
import os
import time
import cloudscraper
import requests
from datetime import datetime
from colorama import Fore, Style, init
from rich.table import Table
from rich.console import Console
from PIL import Image
from io import BytesIO
from pystyle import Colorate
from rich.panel import Panel
from rich.text import Text
import random

# Khởi tạo colorama
init(autoreset=True)
console = Console()

# Định nghĩa màu trực tiếp trong mã
PRIMARY = Fore.YELLOW
TEXT = Fore.WHITE
SUCCESS = Fore.GREEN
ERROR = Fore.RED
INFO = Fore.CYAN
PROMPT = Fore.MAGENTA
RESET = Style.RESET_ALL

def format_color(text, color):
    """Định dạng văn bản với màu được chỉ định."""
    return f"{color}{text}{RESET}"

def highlight(text, color=PRIMARY):
    """Tô sáng văn bản với màu chính hoặc màu được chỉ định."""
    return f"{Style.BRIGHT}{color}{text}{RESET}"

cookie_file = "twitter_cookie.txt"

# Banner
banner = f"""
{PRIMARY}╔══════════════════════════════════════════════════════╗
{PRIMARY}║                                                      {PRIMARY}║
{PRIMARY}║  {TEXT}██████╗░██╗░░░██║░█████╗░░██████╗██╗░░██║           {PRIMARY}║
{PRIMARY}║  {TEXT}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {PRIMARY}║
{PRIMARY}║  {TEXT}██████╦╝██║░░░██║███████║╚█████╗░███████║           {PRIMARY}║
{PRIMARY}║  {TEXT}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {PRIMARY}║
{PRIMARY}║  {TEXT}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {PRIMARY}║
{PRIMARY}║  {TEXT}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {PRIMARY}║
{PRIMARY}║                                                      {PRIMARY}║             
{PRIMARY}║  {TEXT}          ░█████╗░███╗░░██║░██████╗░                {PRIMARY}║
{PRIMARY}║  {TEXT}          ██╔══██╗████╗░██║██╔════╝░                {PRIMARY}║
{PRIMARY}║  {TEXT}          ███████║██╔██╗██║██║░░██╗░                {PRIMARY}║
{PRIMARY}║  {TEXT}          ██╔══██║██║╚████║██║░░╚██╗                {PRIMARY}║
{PRIMARY}║  {TEXT}          ██║░░██║██║░╚███║╚██████╔╝                {PRIMARY}║
{PRIMARY}║  {TEXT}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {PRIMARY}║
{PRIMARY}║                                                      {PRIMARY}║
{PRIMARY}║              {PRIMARY}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ⌛            {PRIMARY}║
{PRIMARY}╚══════════════════════════════════════════════════════╝
"""

list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0

# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class API_PRO5_BYBUASHANG:
    def banner(self):
        os.system('title TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG')
        os.system("cls" if os.name == "nt" else "clear")
        print(banner)
    
    def ndp_delay_tool(self, p):
        """Hàm xử lý delay countdown và hiển thị thời gian còn lại."""
        while p > 1:
            print(f"{format_color(f'Đang chờ: {p-1} giây còn lại...', INFO)}", end="\r")
            time.sleep(1)
            p -= 1
        print(f"{format_color('Hoàn tất chờ, tiếp tục tạo page...', INFO)}")
    
    def getthongtinfacebook(self, cookie: str):
        headers_get = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'viewport-width': '1184',
            'cookie': cookie
        }
        try:
            print(f"{format_color('Đang Tiến Hành Check Live', INFO)}", end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers=headers_get).url
            get_dulieu_profile = requests.get(url=url_profile, headers=headers_get).text
        except:
            return False
        
        try:
            # Kiểm tra và lấy uid từ cookie
            if 'c_user=' not in cookie:
                return False
            uid_get = cookie.split('c_user=')[1].split(';')[0] if len(cookie.split('c_user=')) > 1 else None
            
            if not uid_get:
                return False
            
            # Lấy fb_dtsg và jazoest
            fb_dtsg_parts = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')
            jazoest_parts = get_dulieu_profile.split('{"name":"jazoest","value":"')
            if len(fb_dtsg_parts) > 1 and len(jazoest_parts) > 1:
                fb_dtsg_get = fb_dtsg_parts[1].split('"},')[0]
                jazoest_get = jazoest_parts[1].split('"},')[0]
            else:
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0] if ',"f":"' in get_dulieu_profile else None
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0] if '&jazoest=' in get_dulieu_profile else None
                if not fb_dtsg_get or not jazoest_get:
                    return False
            
            # Lấy name và username
            name_parts = get_dulieu_profile.split('<title>')
            if len(name_parts) > 1:
                name_get = name_parts[1].split('</title>')[0]
            else:
                return False
            
            username_get = url_profile.split('facebook.com/')[1].split('?')[0] if 'facebook.com/' in url_profile else 'unknown'
            return name_get, uid_get, fb_dtsg_get, jazoest_get, username_get
        except:
            return False
    
    def UpAvt(self, cookie, id_page, link_anh):
        try:
            response = requests.get(link_anh)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img = img.resize((200, 200), Image.LANCZOS)
            img_bytes = BytesIO()
            img.save(img_bytes, format='JPEG')
            img_bytes.name = 'avatar.jpg'
            
            headers_upload = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'origin': 'https://www.facebook.com',
                'referer': f'https://www.facebook.com/{id_page}/settings/?tab=profile',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'cookie': cookie
            }
            
            files = {
                'file': ('avatar.jpg', img_bytes.getvalue(), 'image/jpeg')
            }
            data = {
                'profile_id': id_page,
                'source': 'profile_edit',
                'fb_dtsg': self.getthongtinfacebook(cookie)[2],
                'jazoest': self.getthongtinfacebook(cookie)[3]
            }
            
            response = requests.post(
                'https://www.facebook.com/api/graphql/',
                headers=headers_upload,
                data={'variables': json.dumps({
                    'input': {
                        'file_id': '0',
                        'profile_id': id_page,
                        'source': 'PROFILE_PHOTO',
                        'client_mutation_id': '1'
                    }
                })},
                files=files
            )
            
            if response.status_code == 200 and response.text and 'data' in response.json():
                print(f"{format_color(f'╰─> UP_AVT_SUCCESS | [UID PAGE: {id_page}]', SUCCESS)}")
                return True
            else:
                print(f"{format_color(f'╰─> UP_AVT_ERROR | [UID PAGE: {id_page}] | {response.text}', ERROR)}")
                return False
        except Exception as e:
            print(f"{format_color(f'╰─> UP_AVT_ERROR | [UID PAGE: {id_page}] | ERROR: {str(e)}', ERROR)}")
            return False
    
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        global dem
        headers_reg = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            'cookie': cookie
        }
        data_reg = {
            'av': uid,
            '__user': uid,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"Reg Auto By Buash Ang","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            global dem
            dem += 1
            return idpage, namepage
        except:
            print(f"{format_color('Reg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!', ERROR)}")
            return False, None
    
    def UpdateBioPage(self, cookie, id_page, fb_dtsg, jazoest, bio):
        headers_update = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{id_page}/settings/?tab=about',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-fb-friendly-name': 'ProfileCometAboutAppSectionQuery',
            'cookie': cookie
        }
        data_update = {
            'av': id_page,
            '__user': id_page,
            '__a': '1',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'variables': f'{{"input":{{"about":"{bio}","page_id":"{id_page}","client_mutation_id":"1"}}}}',
            'server_timestamps': 'true',
            'doc_id': '5069381243170066'
        }
        try:
            response = requests.post('https://www.facebook.com/api/graphql/', headers=headers_update, data=data_update, timeout=20)
            if response.status_code == 200 and response.text and 'data' in response.json():
                print(f"{format_color(f'╰─> UPDATE_BIO_SUCCESS | [UID PAGE: {id_page}] | BIO: {bio}', SUCCESS)}")
                return True
            else:
                print(f"{format_color(f'╰─> UPDATE_BIO_ERROR | [UID PAGE: {id_page}] | {response.text}', ERROR)}")
                return False
        except Exception as e:
            print(f"{format_color(f'╰─> UPDATE_BIO_ERROR | [UID PAGE: {id_page}] | ERROR: {str(e)}', ERROR)}")
            return False

# =========================== [ START TOOL ] ===========================
dpcutevcl = API_PRO5_BYBUASHANG()
dpcutevcl.banner()
print(f"{PRIMARY}─" * 50)
print(f"{format_color('[ENTER - ĐỂ DỪNG NHẬP]', INFO)}")
while True:
    stt += 1
    cookie_fb = input(f"{format_color(f'VUI LÒNG NHẬP COOKIE THỨ [{stt}]: ', PROMPT)}")
    if cookie_fb == '':
        break
    checklive = dpcutevcl.getthongtinfacebook(cookie_fb)
    if checklive != False:
        name, uid, fb_dtsg, jazoest, username = checklive
        print(f"{format_color(f'Name Facebook: {name} | Username: {username}', TEXT)}")
        list_clone.append(f'{cookie_fb}|{name}|{uid}|{fb_dtsg}|{jazoest}|{username}')
        print(f"{PRIMARY}─" * 50)
    else:
        stt -= 1
        print(f"{format_color(f'Cookie {cookie_fb.split('c_user=')[1].split(';')[0] if 'c_user=' in cookie_fb and len(cookie_fb.split('c_user=')) > 1 else cookie_fb}, Die Or Out Vui Lòng Kiểm Tra Lại!!', ERROR)}")

# Tiến Hành Nhập Setting Reg Page
print(f"{PRIMARY}─" * 50)
luachon = input(f"{format_color('BẠN MUỐN REG PAGE XONG UP AVT KHÔNG? [Y/N]: ', PROMPT)}")
print(f"{PRIMARY}─" * 50)
print(f"{format_color('[ENTER - ĐỂ DỪNG NHẬP]', INFO)}")
while True:
    stt2 += 1 
    link_img = input(f"{format_color(f'VUI LÒNG NHẬP LINK ẢNH THỨ [{stt2}]: ', PROMPT)}")
    if link_img == '':
        break
    list_img.append(link_img)
print(f"{PRIMARY}─" * 50)
slpage = int(input(f"{format_color('BẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL: ', PROMPT)}"))
print(f"{PRIMARY}─" * 50)
delay = int(input(f"{format_color('VUI LÒNG NHẬP DELAY REG PAGE: ', PROMPT)}"))
print(f"{PRIMARY}─" * 50)

# Đặt bio cố định
list_bio = ["Reg Auto By Buash Ang"]

# Tạo bảng rich
table = Table(title="Kết Quả Reg Pro5")
table.add_column("STT", justify="center", style="yellow")
table.add_column("Username", justify="center", style="white")
table.add_column("ID Page", justify="center", style="white")
table.add_column("Time", justify="center", style="yellow")

# Tiến Hành Chạy Tool
dpcutevcl.banner()
print(f"{PRIMARY}─" * 50)
print(f"{format_color(f'Đã Tìm Thấy: {str(len(list_clone))} Cookie', INFO)}")
print(f"{format_color(f'Đã Tìm Thấy: {str(len(list_img))} Link Image', INFO)}")
print(f"{PRIMARY}─" * 50)
while True:
    for dulieuclone in list_clone:
        cookie, name, uid, fb_dtsg, jazoest, username = dulieuclone.split('|')
        idpage, namepage = dpcutevcl.RegPage(cookie, name, uid, fb_dtsg, jazoest)
        if idpage:
            current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            table.add_row(str(dem), username, idpage, current_time)
            console.print(table)
            
            if luachon == 'Y' or luachon == 'y':
                link_anh = 'https://photo.znews.vn/w660/Uploaded/lce_jwqqc/2022_12_12/stream_2022_12_12T202958.838_1.jpg'
                try:
                    if dpcutevcl.UpAvt(cookie, idpage, link_anh):
                        print(f"{format_color(f'╰─> UP_AVT_SUCCESS | [UID PAGE: {idpage}]', SUCCESS)}")
                    else:
                        print(f"{format_color(f'╰─> UP_AVT_SKIPPED | [UID PAGE: {idpage}] - Không cập nhật avatar', INFO)}")
                except Exception as e:
                    print(f"{format_color(f'╰─> UP_AVT_ERROR | [UID PAGE: {idpage}] | ERROR: {str(e)}', ERROR)}")
            
            bio = list_bio[0]
            try:
                if dpcutevcl.UpdateBioPage(cookie, idpage, fb_dtsg, jazoest, bio):
                    print(f"{format_color(f'╰─> UPDATE_BIO_SUCCESS | [UID PAGE: {idpage}] | BIO: {bio}', SUCCESS)}")
                else:
                    print(f"{format_color(f'╰─> UPDATE_BIO_SKIPPED | [UID PAGE: {idpage}]', INFO)}")
            except Exception as e:
                print(f"{format_color(f'╰─> UPDATE_BIO_ERROR | [UID PAGE: {idpage}] | ERROR: {str(e)}', ERROR)}")
        
        dpcutevcl.ndp_delay_tool(delay)  # Gọi hàm delay với hiển thị thời gian
        if dem == slpage:
            console.print(Panel(f"[bold yellow]Hoàn thành {dem} trang![/bold yellow]", title="Kết thúc"))
            input(f"{format_color(f'Done {dem}, Page </> ENTER ĐỂ EXIT', INFO)}")
            exit()