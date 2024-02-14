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
@bot.on_message(filters.command(["ocean"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://oceangurukulsapi.classx.co.in/post/userLogin"
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
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    #print(output)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
        "Host": "oceangurukulsapi.classx.co.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
        }
    #print(userid)
    #print(token)
    await editable.edit("**login Successful**")
    # await editable.edit(f"You have these Batches :-\n{raw_text}"
    cour_url = "https://oceangurukulsapi.classx.co.in/get/mycourse?userid="

    res1 = requests.get("https://oceangurukulsapi.classx.co.in/get/mycourse?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        t_name =data['course_name']
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
    html = scraper.get("https://oceangurukulsapi.classx.co.in/get/allsubjectfrmlivecourseclass?courseid=" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    await m.reply_text(subjID)
    #SubiD = input("Enter the Subject Id Show in above Response")

    editable1 = await m.reply_text("**Enter the Subject Id Show in above Response")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text

    res3 = requests.get("https://oceangurukulsapi.classx.co.in/get/alltopicfrmlivecourseclass?courseid=" + raw_text2,"&subjectid=" + raw_text3, headers=hdr1)
    b_data2 = res3.json()['data']
    # print(b_data2)
    vj = ""
    for data in b_data2:
        tids = (data["topicid"])
        idid = f"{tids}&"
        if len(f"{vj}{idid}") > 4096:
            ##await m.reply_text(idid)
            vj = ""
        vj += idid
    #print(vj)
    vp = ""
    for data in b_data2:
        tn = (data["topic_name"])
        tns = f"{tn}&"
        if len(f"{vp}{tn}") > 4096:
            ##await m.reply_text(tns)
            vp = ""
        vp += tns
    #print(vp)
    cool1 = ""
    #BBB = ''
    for data in b_data2:
        t_name = (data["topic_name"])
        tid = (data["topicid"])
        zz = len(tid)
        BBB = f"{'**TOPIC-ID    - TOPIC     - VIDEOS**'}\n"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"
        #hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"
        if len(f'{cool1}{hh}') > 4096:
            cool1 = ""
        cool1 += hh
    await m.reply_text(f'Batch details of **{t_name}** are:\n\n{BBB}\n\n{cool1}')

    editable= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text

    editable3 = await m.reply_text("**Now send the Resolution**")
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    try:
        xv = raw_text4.split('&')
        for y in range(0,len(xv)):
            t =xv[y]

            hdr11 = {
                    "Host": "oceangurukulsapi.classx.co.in",
                    "Client-Service": "Appx",
                    "Auth-Key": "appxapi",
                    "User-Id": userid,
                    "Authorization": token
                    }

            res4 = requests.get("https://oceangurukulsapi.classx.co.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid=" + t + "&start=-1&conceptid=1&courseid=" + raw_text2 + "&subjectid=" + raw_text3,headers=hdr11).json()

            topicid = res4["data"]
            vj = ""
            for data in topicid:
                tids = (data["Title"])
                idid = f"{tids}"
                if len(f"{vj}{idid}") > 4096:
                    vj = ""
                vj += idid

            vp = ""
            for data in topicid:
                tn = (data["download_link"])
                tns = f"{tn}"
                if len(f"{vp}{tn}") > 4096:
                    vp = ""
        # print("Download Links: \n", tns
                vp += tn
            vs = ""
            for data in topicid:
                tn0 = (data["pdf_link"])
                tns0 = f"{tn0}"
                if len(f"{vs}{tn0}") > 4096:
                    vs = ""
            # print("Download Links: \n", tns
                vs += tn0
            cool2 = ""
            #BBB1 = ''
            for data in topicid:
                if data["download_link"]:
                    b64 = (data["download_link"])
                else:
                    b64 = (data["pdf_link"])
                tid = (data["Title"])
                zz = len(tid)
                key = "638udh3829162018".encode("utf8")
                iv = "fedcba9876543210".encode("utf8")
                ciphertext = bytearray.fromhex(b64decode(b64.encode()).hex())
                cipher = AES.new(key, AES.MODE_CBC, iv)
                plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
                #print(plaintext)
                b=plaintext.decode('utf-8')
                cc0 = (f"{tid}:{b}")
                if len(f'{cool2}{cc0}') > 4096:
                    ##await m.reply_text(hh)
                    cool2 = ""
                cool2 += cc0
                mm = "Ocean-Gurukul"
                #await m.reply_text(BBB1, hh)
                
                with open(f'{mm}.txt', 'a') as f:
                    f.write(f"{tid}:{b}\n")
        await m.reply_document(f"{mm}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done") 