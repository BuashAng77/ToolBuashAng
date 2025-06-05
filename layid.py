import requests
import os, sys
import json
from time import sleep
from datetime import datetime, timedelta
import base64

# Colors
cyan = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
white = "\033[1;37m"
white_bold = "\033[1;37m"
red_bold = "\033[1;31m"
reset = '\033[0m'

# Copyright notice
tool_mark = f"{white_bold}[{red_bold}🐾{white_bold}] {cyan}✈   "
divider = f"{white_bold}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def display_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
{yellow}╔══════════════════════════════════════════════════════╗
{yellow}║                                                      {yellow}║
{yellow}║  {white}██████╗░██╗░░░██╗░█████╗░░██████╗██╗░░██╗           {yellow}║
{yellow}║  {white}██╔══██╗██║░░░██║██╔══██╗██╔════╝██║░░██║           {yellow}║
{yellow}║  {white}██████╦╝██║░░░██║███████║╚█████╗░███████║           {yellow}║
{yellow}║  {white}██╔══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║           {yellow}║
{yellow}║  {white}██████╦╝╚██████╔╝██║░░██║██████╔╝██║░░██║           {yellow}║
{yellow}║  {white}╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝           {yellow}║
{yellow}║                                                      {yellow}║             
{yellow}║  {white}          ░█████╗░███╗░░██╗░██████╗░                {yellow}║
{yellow}║  {white}          ██╔══██╗████╗░██║██╔════╝░                {yellow}║
{yellow}║  {white}          ███████║██╔██╗██║██║░░██╗░                {yellow}║
{yellow}║  {white}          ██╔══██║██║╚████║██║░░╚██╗                {yellow}║
{yellow}║  {white}          ██║░░██║██║░╚███║╚██████╔╝                {yellow}║
{yellow}║  {white}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {yellow}║
{yellow}║                                                      {yellow}║
{yellow}║                                                      {yellow}║
{yellow}║                                                      {yellow}║
{yellow}║              {yellow}Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {yellow}║
{yellow}╚══════════════════════════════════════════════════════╝
"""
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.0005)

display_banner()

# Input Facebook ID
fb_id = input(f"{white_bold}[{red_bold}🐱{white_bold}] {cyan}✈  {green}Enter Facebook ID: ")

cookies = {
    '__cf_bm': 'hCJ70.qlLOmLP4yNJ3T.jU8U_gfpcDM3yKeSq.apXTo-1680193382-0-AXRqj+GxSV8cBESQDO9SQMjV7H0A2R+tRrgVFIKA5xekIcDlqHBeZ4so6MN6pXK4GMo+0TIMns5G6wo8qZaq9BJnZAjfOAUGUQUyQqraD29vAUXcHAcOFGMeb6X0xovVdQ==',
}

headers = {
    'authority': 'golike.com.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'referer': 'https://golike.com.vn/lay-uid-va-kiem-tra-ngay-tao-tai-khoan-facebook/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'user': fb_id,
}

# Fetch data from API
response = requests.get('https://golike.com.vn/func-api.php', params=params, cookies=cookies, headers=headers).json()
uid = response["data"]["uid"]
creation_date = response["data"]["date"]

# Output results
print(f"{white_bold}[{red_bold}🐶{white_bold}] {cyan}✈  {green}UID: {uid}")
print(f"{white_bold}[{red_bold}🐰{white_bold}] {cyan}✈  {green}Creation Date: {creation_date}")