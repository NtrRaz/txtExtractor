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
from requests_toolbelt.utils import dump
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
def decode(tn):
  key = "638udh3829162018".encode("utf8")
  iv = "fedcba9876543210".encode("utf8")
  ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  url=plaintext.decode('utf-8')
  return url
@bot.on_message(filters.command(["rgvikramjeet"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    s = requests.Session()
    global cancel
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://rgvikramjeetapi.classx.co.in/post/userLogin"
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
        "Host": "rgvikramjeetapi.classx.co.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
        }
    await editable.edit("**login Successful**")
    cour_url = "https://rgvikramjeetapi.classx.co.in/get/mycourse?userid="
    res1 = s.get("https://rgvikramjeetapi.classx.co.in/get/mycourse?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
      t_name =data['course_name']
      FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
      aa = f" ```{data['id']}```  - **{data['course_name']}**\n\n"
      if len(f'{cool}{aa}') > 4096:
        print(aa)
        cool = ""
      cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    await editable1.delete(True)
    html = scraper.get("https://rgvikramjeetapi.classx.co.in/get/course_by_id?id=" + raw_text2,headers=hdr1).json()
    course_title = html["data"][0]["course_name"]
    scraper = cloudscraper.create_scraper()
    html = scraper.get("https://rgvikramjeetapi.classx.co.in/get/allsubjectfrmlivecourseclass?courseid=" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    cool = ""
    vj = ""
    for sub in subjID:
      subjid = sub["subjectid"]
      idid = f"{subjid}&"
      subjname = sub["subject_name"]
      aa = f" ```{subjid}```  -  **{subjname}**\n\n"
      cool += aa
      vj += idid
    await editable.edit(cool)
    editable1= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    await editable1.delete(True)
    prog = await editable.edit("**Extracting Videos Links Please Wait  📥 **")
    try:
      output_dict = {}
      videos_dict = {}
      mm = "Rgvikramjeet"
      xv = raw_text3.split('&')
      for y in range(0,len(xv)):
        raw_text3 =xv[y]
        res3 = requests.get("https://rgvikramjeetapi.classx.co.in/get/alltopicfrmlivecourseclass?courseid=" + raw_text2,"&subjectid=" + raw_text3, headers=hdr1)
        b_data2 = res3.json()['data']
        for data in b_data2:
          t_name = (data["topic_name"])
          tid = (data["topicid"])
          hdr11 = {"Host": "rgvikramjeetapi.classx.co.in",
                  "Client-Service": "Appx",
                  "Auth-Key": "appxapi",
                  "User-Id": userid,
                  "Authorization": token
                  }
          par = {
              'courseid': raw_text2,'subjectid': raw_text3,'topicid': tid,'start': '-1'}
          res6 = requests.get('https://rgvikramjeetapi.classx.co.in/get/allconceptfrmlivecourseclass', params=par, headers=hdr11).json()
          b_data3 = res6['data']
          for data in b_data3:
            cid = (data["conceptid"])
            par2 = {
            'courseid': raw_text2,'subjectid': raw_text3,'topicid': tid,'conceptid': cid,'start': '-1'
             }
            res4 = requests.get('https://rgvikramjeetapi.classx.co.in/get/livecourseclassbycoursesubtopconceptapiv3', params=par2, headers=hdr11).json()
            try:
              topicid = res4["data"]
              for data in topicid:
                tn = (data["download_link"])
                tid = (data["Title"])
                url = decode(tn)
                videos_dict[tid] = url
                mtext = f"{tid}:{url}\n"
                open(f"{mm} - {course_title}.txt", "a").write(mtext)
              output_dict[t_name] = videos_dict   
            except Exception as e:
              error = f"{tid} : {e}"
              await m.reply_text(error)
              continue
      await prog.delete(True)  
      await m.reply_document(f"{course_title}.json",caption = f"```{mm} - {course_title}.json```" )
      await m.reply_document(f"{mm} - {course_title}.txt",caption = f"```{mm} - {course_title}```" )
      os.remove(f"{mm} - {course_title}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    