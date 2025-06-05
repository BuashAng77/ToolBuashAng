import requests
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for cross-platform color support
init(autoreset=True, convert=True)  # Convert=True ensures Windows compatibility

# Define characters for animation
chars = " ➤ [«/»] >>>"

# Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# ASCII banner with bright color scheme
banner = f"""
{Fore.YELLOW}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗
{Fore.YELLOW}{Style.BRIGHT}║                                                      {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}██████╗░██╗░░░██╗░█████╗░░██████╗██╗░░██║           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}██████╦╝██║░░░██║███████║╚█████╗░███████║           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║                                                      {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ░█████╗░███╗░░██║░██████╗░                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ██╔══██╗████╗░██║██╔════╝░                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ███████║██╔██╗██║██║░░██╗░                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.BLUE}{Style.BRIGHT}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║                                                      {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}║  {Fore.GREEN}{Style.BRIGHT}📅 Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}                        {Fore.YELLOW}{Style.BRIGHT}║
{Fore.YELLOW}{Style.BRIGHT}╚══════════════════════════════════════════════════════╝

{Fore.YELLOW}{Style.BRIGHT}==========================================================
{Fore.RED}{Style.BRIGHT}🐾 {Fore.CYAN}{Style.BRIGHT}Admin: {Fore.WHITE}{Style.BRIGHT}BUASH ANG DZAI
{Fore.RED}{Style.BRIGHT}⚙️ {Fore.CYAN}{Style.BRIGHT}Device Limit: {Fore.GREEN}{Style.BRIGHT}1/*
{Fore.YELLOW}{Style.BRIGHT}==========================================================
{Fore.MAGENTA}{Style.BRIGHT}                📢 [Announcement] 📢
{Fore.CYAN}{Style.BRIGHT}🛠️ {Fore.WHITE}{Style.BRIGHT}TOOL IS UNDER UPDATE PROCESS
{Fore.YELLOW}{Style.BRIGHT}==========================================================
{Fore.BLUE}{Style.BRIGHT}                🚀 TIKTOK FOLLOWER BOOST TOOL 🚀
"""

# Print banner with animation
for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0005)

def buff_follow(username):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    while True:
        try:
            # Fetch session from TikFollowers
            access = requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
            session = access.cookies.get('ci_session')
            if not session:
                print(f'{Fore.RED}{Style.BRIGHT}❌ [N-TOOL] Error: Could not retrieve session for @{username} 🐱')
                time.sleep(5)
                continue

            headers.update({'cookie': f'ci_session={session}'})
            token = access.text.split("csrf_token = '")[1].split("'")[0]
            data = '{"type":"follow","q":"@'+username+'","google_token":"t","token":"'+token+'"}'
            search = requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()

            if search.get('success'):
                data_follow = search['data']
                data = '{"google_token":"t","token":"'+token+'","data":"'+data_follow+'","type":"follow"}'
                send_follow = requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()

                if send_follow.get('o') == 'Success!' and send_follow.get('success') and send_follow.get('type') == 'success':
                    print(f'{Fore.GREEN}{Style.BRIGHT}✅ [BUASH ANG DZAI VCL] Successfully boosted TikTok followers for @{username} 🐶')
                elif send_follow.get('o') == 'Oops...' and not send_follow.get('success') and send_follow.get('type') == 'info':
                    try:
                        wait_time = send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                        minutes = wait_time.split(' Minutes')[0]
                        seconds = int(minutes) * 60
                        for i in range(seconds, 0, -1):
                            print(f'{Fore.YELLOW}{Style.BRIGHT}⏳ [] Please wait {i} seconds for @{username}... 🐰', end='\r')
                            time.sleep(1)
                        continue
                    except:
                        print(f'{Fore.RED}{Style.BRIGHT}❌ [BUASH ANG DZAI VCL] Unknown error for @{username} 🐱')
                        continue
                else:
                    print(f'{Fore.RED}{Style.BRIGHT}❌ [BUASH ANG DZAI VCL] Unknown error for @{username} 🐱')
                    continue
            else:
                print(f'{Fore.RED}{Style.BRIGHT}❌ [BUASH ANG DZAI VCL] Error: No data found for @{username} 🐱')
                time.sleep(5)
                continue
        except Exception as e:
            print(f'{Fore.RED}{Style.BRIGHT}❌ [BUASH ANG DZAI VCL] Unknown error for @{username}: {str(e)} 🐱')
            time.sleep(5)
            continue

if __name__ == '__main__':
    usernames = input(f'{Fore.CYAN}{Style.BRIGHT}📝 [BUASH ANG DZAI VCL] Enter TikTok usernames (without @) separated by commas: 🐾 ').split(',')
    with ThreadPoolExecutor(max_workers=len(usernames)) as executor:
        for username in usernames:
            executor.submit(buff_follow, username.strip())