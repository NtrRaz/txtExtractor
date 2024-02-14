#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE
#  Code edited By Cryptostark
import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode

@bot.on_message(filters.command(["pw"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Auth code** in this manner otherwise bot will not respond.\n\nSend like this:-  **AUTH CODE**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {

            'Host': 'api.penpencil.xyz',

            'authorization': f"Bearer {raw_text1}",

            'client-id': '5eb393ee95fab7468a79d189',

            'client-version': '12.84',

            'user-agent': 'Android',

            'randomid': 'e4307177362e86f1',

            'client-type': 'MOBILE',

            'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',

            'content-type': 'application/json; charset=UTF-8',

        # 'content-length': '89',

        # 'accept-encoding': 'gzip' ,
    }

    params = {
       'mode': '1',
       'filter': 'false',
       'exam': '',
       'amount': '',
       'organisationId': '5eb393ee95fab7468a79d189',
       'classes': '',
       'limit': '20',
       'page': '1',
       'programId': '',
       'ut': '1652675230446', 
    }
    await editable.edit("**You have these Batches :-\n\nBatch ID : Batch Name**")
    response = requests.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch=(data["name"])
        #batchId=(data["_id"])
        aa=f"```{data['name']}```  :  ```{data['_id']}\n```"
        await m.reply_text(aa)
    #time.sleep(2)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await editable1.edit("subject : subjectId")
    vj=""
    for data in response2:
       #topic=(data["subject"])
        #topic_id=(data["_id"])
        #idid=f"{topic_id}&"
        bb=f"{data['_id']}&"
        await m.reply_text(bb)
    vj=""
    for data in response2:
        tids = (data['_id'])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
    editable2= await m.reply_text("**Enter this to download full batch :-**\n```{vj}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await m.reply_text("**Enter resolution**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    
    #await m.reply_text("**Enter Title**")
    #input0: Message = await bot.listen(editable.chat.id)
    #raw_text0 = input0.text

    editable4= await m.reply_text("Now send the **Thumb url** Eg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    try:
        xv = raw_text4.split('&')

        for y in range(0,len(xv)):
            t =xv[y]
            params1 = {'page': '1','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response3 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params1, headers=headers).json()["data"]
            
            params2 = {'page': '2','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response4 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params2, headers=headers).json()["data"]
            
            params3 = {'page': '3','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response5 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params3, headers=headers).json()["data"]
            
            params4 = {'page': '4','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response6 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            #await m.reply_text(response3)
            try:
                for data in response3:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response4:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response5:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                     f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response6:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            await m.reply_document(f"{batch}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    