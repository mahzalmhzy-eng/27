import datetime
import urllib.request

def get_current_date():
    try:
        
        response = urllib.request.urlopen('http://just-the-time.appspot.com', timeout=3)
        result = response.read().strip().decode('utf-8')
        
        date_str = result.split()[0] 
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception:
       
   
        return datetime.date.today()

expiry_date = datetime.date(2026, 6, 1)


current_date = get_current_date()

if current_date > expiry_date:
    print("-" * 0)
    print(f" لقد انتهت صلاحية الاداة")
    print("راسل المطور لتجديد الاداة")
    print("@iifffr")
    print("-" * 0)
    exit() 
else:
    print("-" * 0)
    
    

import requests
import uuid
from uuid import uuid1,uuid4
from OneClick import Hunter
import stdiomask
import threading
import os
from user_agent import generate_user_agent as elia
import time,os,random
os.system('pip install requests')
os.system('pip install OneClick')
os.system('pip install user_agent')
os.system('pip install stdiomask')
os.system('clear')


Ca = "\033[1;97m" #ابيض
F = '\033[2;32m'  # أخضر

B = '\x1b[38;5;208m'  # برتقالي
E = '\033[1;31m'  # أحمر
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
Ca = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.

y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\x1b[38;5;208m'

def show_logo():
   
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    logo_alasfar = B + """
    
    
    
    
    
    
    
    
    



 █████╗ ██╗      █████╗ ███████╗███████╗ █████╗ ██████╗ 
██╔══██╗██║     ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
███████║██║     ███████║███████╗█████╗  ███████║██████╔╝
██╔══██║██║     ██╔══██║╚════██║██╔══╝  ██╔══██║██╔══██╗
██║  ██║███████╗██║  ██║███████║██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
"""
                       
    logoso = z + """
 ██████╗██╗      █████╗ ███████╗███████╗                
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝                
██║     ██║     ███████║███████╗███████╗                
██║     ██║     ██╔══██║╚════██║╚════██║                
╚██████╗███████╗██║  ██║███████║███████║                
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                
"""
    print(logo_alasfar)
    print(logoso)

if __name__ == "__main__":
    show_logo()

uid=str(uuid.uuid4())
true=0
false=0
chk=0
error=0

logo=F+ '''
╔═════════════════════════════════════════════════════════════════╗
║           _            __              _____ _                ║
║     /\   | |          / _|            / ____| |               ║
║    /  \  | | __ _ ___| |_ __ _ _ __  | |    | | __ _ ___ ___  ║
║   / /\ \ | |/ _` / __|  _/ _` | '__| | |    | |/ _` / __/ __| ║
║  / ____ \| | (_| \__ \ || (_| | |    | |____| | (_| \__ \__ \ ║
║ /_/    \_\_|\__,_|___/_| \__,_|_|     \_____|_|\__,_|___/___/ ║
║                                                               ║
║                                                               ║
║                                                               ║
╚═════════════════════════════════════════════════════════════════╝
'''
tok= input(X+'TOKEN TELEGRAM : '+f)
id= input(Y+'ID TELEGRAM : '+B)
photo_url = "https://t.me/alsafrzn/2"  
rd = requests.get(
    f'https://api.telegram.org/bot{tok}/sendphoto?chat_id={id}&photo={photo_url}&caption='
    '«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»\n'
    '\n الاداة شغالة ✅'
    '\n افضل اداة يوزرات بس تحتاج VPN'
    '\n المطور الاصفر كلاس'
    '\n يوزري {@iifffr}'
    '\n قناتي {@viokill}'
    '\n«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»«»'
)


def hh():
    uk= [Z,X,F,f]
    global true,false,chk,error,uid,logo
    
    while True:
        col= random.choice(uk)
        col1= random.choice(uk)
        col2= random.choice(uk)
   
        th = time.ctime()
        v1= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v2 =''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v3= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v4 = ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v5= ''.join(random.choice('1234567890')for i in range(1))
        v6= ''.join(random.choice('1234567890')for i in range(1))
        user1 = v1+v1+v2+v2+v3
        user2 = v1+v1+v2+v2+v3
        usse= [user1,user2]
        user= random.choice(usse)
 
        url='https://i.instagram.com/api/v1/accounts/create/'
        hea={
            'Host': 'i.instagram.com',
            'cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
            'x-ig-capabilities': 'AQ==',
            'cookie2': '$Version=1',
            'x-ig-connection-type': 'WIFI',
            'user-agent': Hunter.Services(),
            'content-type': 'application/x-www-form-urlencoded',
            'content-length': '159',

        }
        data={
            'password':'qqwwaassddffgghh4455',
            'device_id':uid,
            'guid':uid,
            'email':'ll9678785@gmail.com',
            'username':user,
        }
        res=requests.post(url,headers=hea,data=data,proxies=None).text
        

        
        if '{"account_created": false, "errors": {"email": ["Another account is using the same email."]}, "status": "ok", "error_type": "email_is_taken"}'in res:
            os.system('cls'if os.name=='nt'else'clear')
            true+=1
            chk+=1
            print(f'''{z}​ ╔═════ ≪ °❈° ≫ ═════╗
​جـمـيـع الـحـقـوق لـدى الأصـفـر كـلاس
​╚═════ ≪ °❈° ≫ ═════╝
  
        {F}تم الصيد : {Ca}[{true}]{E}يوزر مستخدم : {Ca}[{false}]
                {z}محظور لو لا : {E}[True]''')
            hit = f'''

صيد جديد✅👏
اليوزر : {user}
قناتي : (@viokill)

'''
            requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={hit}')
        
        elif 'Please wait a few minutes before you try again.'in res:
            os.system('cls'if os.name=='nt'else'clear')
            error+=1
            chk+=1
            print(f'''{z}​ ╔═════ ≪ °❈° ≫ ═════╗
​جـمـيـع الـحـقـوق لـدى الأصـفـر كـلاس
​╚═════ ≪ °❈° ≫ ═════╝
  
        {F}تم الصيد : {Ca}[{true}]{E}يوزر مستخدم : {Ca}[{false}]
                {z}محظور لو لا : {E}[True]''')
           
        else:
            
            os.system('cls'if os.name=='nt'else'clear')
            chk+=1
            false+=1
            print(f'''{z}​ ╔═════ ≪ °❈° ≫ ═════╗
​جـمـيـع الـحـقـوق لـدى الأصـفـر كـلاس
​╚═════ ≪ °❈° ≫ ═════╝
  
        {F}تم الصيد : {Ca}[{true}]{E}يوزر مستخدم : {Ca}[{false}]
                {z}محظور لو لا : {F}[False]''')
threads = []
for i in range(30):  
    t = threading.Thread(target=hh)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
