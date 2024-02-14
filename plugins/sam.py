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

@bot.on_message(filters.command(["samyak"]) & ~filters.edited)
async def account(bot: Client, m: Message):
    global cancel
    s = requests.Session()
    cancel = False
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**" )
    rwa_url = "https://samyak.teachx.in/pages/login2"
    hdr = {"Auth-Key": "appxapi",
           "User-Id": "-2",
           "Authorization": "",
           "User_app_category": "",
           "Language": "en",
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "233",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "okhttp/4.9.1"
          }
    info = {"email": "", "password": ""}
    #7355971781*73559717
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    
    res = s.post(rwa_url, data=info, headers=hdr)
    output = res.json()
    #print(output)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    #await m.reply_text(f"```{token}```")
    hdr1 = {
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'User-ID': userid,
    'auth-key': 'appxapi',
    'client-service': 'Appx'
}

    await editable.edit("**login Successful**")
    # await editable.edit(f"You have these Batches :-\n{raw_text}"
    res1 = s.get(f'https://samyakapi.teachx.in/get/mycourseweb?userid={userid}', headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        t_name1 =data['course_name']
        FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa = f" ```{data['id']}```      - **{data['course_name']}**\n\n"
        # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    # sub_id_url="https://rgvikramjeetapi.classx.co.in/get/allsubjectfrmlivecourseclass?courseid="
    scraper = cloudscraper.create_scraper()
    html = scraper.get("https://samyakapi.teachx.in/get/allsubjectfrmlivecourseclass?courseid=" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    cool = ""
    vj = ""
    for sub in subjID:
      subjid = sub["subjectid"]
      idid = f"{subjid}&"
      subjname = sub["subject_name"]
      aa = f" ```{subjid}```      - **{subjname}**\n\n"
      cool += aa
      vj += idid
    await m.reply_text(cool)
    editable= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            raw_text3 =xv[y]
            res3 = s.get("https://samyakapi.teachx.in/get/alltopicfrmlivecourseclass?courseid=" + raw_text2 + "&subjectid=" + raw_text3, headers=hdr1)
            b_data2 = res3.json()['data']
            for data in b_data2:
                t_name = (data["topic_name"])
                tid = (data["topicid"])
                print(tid,t_name)
                hdr2 = {
        'Authorization': token,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'User-ID': userid,
        'auth-key': 'appxapi',
        'client-service': 'Appx'
    }
                res4 = requests.get("https://samyakapi.teachx.in/get/livecourseclassbycoursesubtopconceptapiv3?courseid="+raw_text2+"&subjectid="+raw_text3+"&topicid="+tid+"&start=-1",headers=hdr2).json()
                topicid = res4["data"]
                cool2 = ""
                for data in topicid:
                    mm = "Samayak Ias"
                    tid = (data["Title"])
                    with open(f'{mm} - {t_name1}.txt', 'a') as f:
                      if len(data["download_link"])>0:
                          b64 = (data["download_link"])
                          #b65 = f"{data["Title"]}:{data["download_link"]}
                          inf = {"link":b64}
                          mid = s.post('https://samyak.teachx.in/pages/decrypt', headers=hdr,data=inf).text
                          urlv = "https://cdn.jwplayer.com/manifests/"+mid
                          f.write(f"{tid}:{urlv}\n")
                      if len(data["pdf_link"])>0:
                          b64 = (data["pdf_link"])
                          inf = {"link":b64}
                          urlv = s.post('https://samyak.teachx.in/pages/decrypt', headers=hdr,data=inf).text
                          f.write(f"{tid}:{urlv}\n")
                      else:
                        pass
        await m.reply_document(f"{mm} - {t_name1}.txt")
    except Exception as e:
      await m.reply_text(str(e))
    os.remove(f"{mm} - {t_name1}.txt")
   