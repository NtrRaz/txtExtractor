import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from pprint import pprint
def decrypt(enc):
        enc = b64decode(enc)
        key = '%!$!%_$&!%F)&^!^'.encode('utf-8') ##Must Be 16 char for AES128
        iv =  '#*y*#2yJ*#$wJv*v'.encode('utf-8') #16 char for AES128
        cipher = AES.new(key, AES.MODE_CBC,iv)
        plaintext =  unpad(cipher.decrypt(enc),AES.block_size)
        b = plaintext.decode('utf-8')
        return b
headers = {
    'Host': 'e-utkarsh.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://e-utkarsh.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

token = requests.get('https://e-utkarsh.com/web/home/get_states', headers=headers).json()["token"]
#print(token)

cookies = {
    'csrf_name': token,
    'ci_session': '2gv2cbei167fr9m4g87mbmvbnkjs19d4',
}
headers = {
    'Host': 'e-utkarsh.com',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://e-utkarsh.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://e-utkarsh.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = "csrf_name="+token+"&mobile=9648658531&url=0&password=abc12345&submit=LogIn&device_token=null"
log = requests.post('https://e-utkarsh.com/web/Auth/login', headers=headers, cookies=cookies, data=data).json()["response"]
#decrypt = decrypt(log)
#print(decrypt)
datas = "type=Batch&csrf_name="+ token +"&sort=0"
res3 = requests.post('https://e-utkarsh.com/web/Profile/my_course', headers=headers, cookies=cookies, data=datas).json()["response"]
f = open("demofile2.txt", "a")
f.write(res3)
f.close()
print(res3)
decryp= decrypt(res3)
print(decryp)
