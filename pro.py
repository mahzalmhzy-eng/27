#import os
#os.system('pip install OneClick')
#os.system('pip install stdiomask')
#os.system('pip install requests')
#os.system('pip install random')
#os.system('pip install threading ')
#os.system('pip install time')
#os.system ("pip install uuid ")
#os.system ("pip install user_agent")
#os.system ("pip install bs4")()
import requests
import uuid
from uuid import uuid1,uuid4
from OneClick import Hunter
import stdiomask
import time,os,random
import threading
from user_agent import generate_user_agent
print(('\033[94m' + '╔' + '═' * 38 + '╗') + 
      '\n\033[92m  • DeCoDe By DEMO •\n\033[93m  | @shlhom • | @shlhom  ' + 
      '\n\033[94m' + '╚' + '═' * 38 + '╝')
uid=str(uuid.uuid4())
true=0
false=0
chk=0
error=0
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
logo=F+ '''

██╗░░██╗░██████╗░█████╗░
██║░░██║██╔════╝██╔══██╗
███████║╚█████╗░██║░░██║
██╔══██║░╚═══██╗██║░░██║
██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═════╝░░╚════╝░
'''
id= input(F+'ID : '+Ca)
tok= input(F+'Token : '+Ca)
def hh():
    uk= [Z,X,F,f]
    global true,false,chk,error,uid,logo
    
    while True:
        col= random.choice(uk)
        col1= random.choice(uk)
        col2= random.choice(uk)
        print(('\033[94m' + '╔' + '═' * 38 + '╗') + 
      '\n\033[92m  • تخمط نا&ج امك •\n\033[93m  | @shlhom • | @shlhom  ' + 
      '\n\033[94m' + '╚' + '═' * 38 + '╝')
        th = time.ctime()
        v1= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v2 =''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v3= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v4 = ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v5= ''.join(random.choice('1234567890')for i in range(1))
        v6= ''.join(random.choice('1234567890')for i in range(1))
        user1 = v1+v1+'.'+v2+v3
        user2 = v1+'.'+v2+v3+v3
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
        #print(res);exit()

        
        if '{"account_created": false, "errors": {"email": ["Another account is using the same email."]}, "status": "ok", "error_type": "email_is_taken"}'in res:
            os.system('cls'if os.name=='nt'else'clear')
            true+=1
            chk+=1
            print(f'''{col}{logo}
                {col}<<{col1}TO-{col2}IN-{col}US-{col1}V1>>
  
        {F}USER True : {Ca}[{true}]{E}USER False : {Ca}[{false}]
                {z}RUN VPN : {F}[False]''')
            hit = f'''

☆ HI NEW HIT 
☆UserName : {user}
☆BY : @shlhom

'''
            requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={hit}')
        
        elif 'Please wait a few minutes before you try again.'in res:
            os.system('cls'if os.name=='nt'else'clear')
            error+=1
            chk+=1
            print(f'''{col}{logo}
                {col}<<{col1}TO-{col2}IN-{col}US-{col1}V1>>
  
        {F}USER True : {Ca}[{true}]{E}USER False : {Ca}[{false}]
                {z}RUN VPN : {E}[True]''')
            exit()
        else:
            
            os.system('cls'if os.name=='nt'else'clear')
            chk+=1
            false+=1
            print(f'''{col}{logo}
                {col}<<{col1}TO-{col2}IN-{col}US-{col1}V1>>
  
        {F}USER True : {Ca}[{true}]{E}USER False : {Ca}[{false}]
                {z}RUN VPN : {F}[False]''')
threads = []
for i in range(10):  
    t = threading.Thread(target=hh)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
