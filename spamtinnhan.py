import requests
import os
import socket
from time import sleep
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init()

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# Get local IP address
ip = socket.gethostbyname(socket.gethostname())
th = '- - - - - - - - - - - - - - - - - - - - - - - - -'

def ban():
    print(f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.YELLOW}║                                                      ║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}██████╗░██╗░░░██║░█████╗░░██████╗██╗░░██║           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}██████╦╝██║░░░██║███████║╚█████╗░███████║           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║                                                      {Fore.YELLOW}║{Style.RESET_ALL}             
{Fore.YELLOW}║  {Fore.CYAN}          ░█████╗░███╗░░██║░██████╗░                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}          ██╔══██╗████╗░██║██╔════╝░                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}          ███████║██╔██╗██║██║░░██╗░                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║  {Fore.CYAN}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║                                                      {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║                                                      {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║                                                      {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}║              {Fore.GREEN}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ⌛            {Fore.YELLOW}║{Style.RESET_ALL}
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}
""")

ban()

# Input prompts with consistent coloring
id = input(f'{Fore.GREEN}[❣] ✈ Nhập id người cần gử(sử dụng tool lấy ID)i: {Style.RESET_ALL}')
while True:
    ck = input(f'{Fore.GREEN}[❣] ✈ Nhập cookie facebook: {Style.RESET_ALL}')
    try:
        get = requests.get(
            f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',
            headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cookie': ck,
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1'
            }
        ).text
        fb_dtsg = get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest = get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    except:
        print(f'{Fore.RED}Cookie sai!!{Style.RESET_ALL}')

nd = input(f'{Fore.GREEN}[❣] ✈ Nhập nội dung: {Style.RESET_ALL}')
so_luong = int(input(f'{Fore.GREEN}[❣] ✈ Nhập số tin nhắn muốn gửi: {Style.RESET_ALL}'))
delay = int(input(f'{Fore.GREEN}[❣] ✈ Nhập delay (khuyến cáo trên 10s): {Style.RESET_ALL}'))

# Headers for message sending
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {'icm': '1'}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}

# List of distinct colors for cycling
colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, 
    Fore.CYAN, Fore.WHITE, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, 
    Fore.LIGHTCYAN_EX
]

# Send messages with unique colors
for i in range(1, so_luong + 1):
    # Select color based on index, cycling through the list
    current_color = colors[(i - 1) % len(colors)]
    response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(f'{current_color}{i} Send Success | {nd}{Style.RESET_ALL}')
    sleep(delay)