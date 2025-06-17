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

    table.add_row("1", "GOLIKE Ig", "ADB Tự Động | Ấn Tay","Hoạt động")    
    table.add_row("2", "GOLIKE TWITTER", "Cookie","Hoạt Động")        
    table.add_row("3", "golike LinkedIn", "Cookie","Đang Update")    
    
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
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/demoig.py').text
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
              code = requests.get('https://raw.githubusercontent.com/BuashAng77/ToolBuashAng/main/demolink.py').text
              exec(code, globals())
            except:
              sys.exit()
        
        
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()
