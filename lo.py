import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
import subprocess
import datetime
import asyncio
import os
import requests
import time
from p_bar import progress_bar
import aiohttp
import tgcrypto
import aiofiles
import concurrent.futures
import subprocess
from pyrogram.types import Message
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import asyncio 
import pyrogram
from pyrogram import Client, filters, idle
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from logging.handlers import RotatingFileHandler
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

def exec(cmd):
        process = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = process.stdout.decode()
        error = process.stderr.decode()
        if error:
          #print(f'[error]\n{error}')
          return f'[error]\n{error}'
        if stdout:
          print(f'[stdout]\n{output}')
        #err = process.stdout.decode()
def pull_run(work, cmds):
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
        fut = executor.map(exec,cmds)
        for result in results:
	        print(result) 
bot = Client(
  "CW",
  bot_token= "6917084113:AAFOK37UIoEQLtY2HYu5UeF77cIF4BfGnwk",
  api_id= 27097807 ,
  api_hash= "9fd790a9cb1f639c921d941621d2959d" 
)

@bot.on_message(filters.command(["down"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    #s = requests.Session()
    global cancel
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    hdr = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    # 'Content-Length': '72',
    'Host': 'ignitedminds.live',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
    }

    info = {
  "api_key": "kdc123",
  "mobilenumber": "7618089571",
  "password": "yvikash880"
  }
    headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Content-Length': '72',
    'Host': 'ignitedminds.live',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
}

    data = '{api_key:kdc123,mobilenumber:7618089571,password:yvikash880}'

    response = requests.post('https://ignitedminds.live/android/User/login_user', headers=headers, data=data)
    print(response.content)
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    #info["mobilenumber"] = raw_text.split("*")[0]
    #info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    res = requests.post('https://ignitedminds.live/android/User/login_user', headers=hdr, data=info).text
    print(res)
    try:
      output = res.json()
      userid = output["id"]
      token = output["connection_key"]
      await editable.edit("**login Successful**")
    except:
      await editable.edit("**Check Back Response**")
    """  
    hdr = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    # 'Content-Length': '72',
    'Host': 'ignitedminds.live',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
}
    data = '{api_key:kdc123,mobilenumber:7618089571,password:yvikash880}'

    #response = requests.post('https://ignitedminds.live/android/User/login_user', headers=headers, data=data)

    b_data = res1.json()
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
        mm = "Rgvikramjeet"
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            raw_text3 =xv[y]
            res3 = requests.get("https://rgvikramjeetapi.classx.co.in/get/alltopicfrmlivecourseclass?courseid=" + raw_text2,"&subjectid=" + raw_text3, headers=hdr1)
            b_data2 = res3.json()['data']
            for data in b_data2:
              t_name = (data["topic_name"])
              tid = (data["topicid"])
              hdr11 = {
                      "Host": "rgvikramjeetapi.classx.co.in",
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
                      mtext = f"{tid}:{url}\n"
                      open(f"{mm} - {course_title}.txt", "a").write(mtext)
                except Exception as e:
                  error = f"{tid} : {e}"
                  await m.reply_text(error)
                  continue
        await prog.delete(True)        
        await m.reply_document(f"{mm} - {course_title}.txt",caption = f"```{mm} - {course_title}```" )
        os.remove(f"{mm} - {course_title}.txt")
    except Exception as e:
        await m.reply_text(str(e)) """
        
async def main():
        await bot.start()
        bot_info  = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
asyncio.get_event_loop().run_until_complete(main())
LOGGER.info(f"<---Bot Stopped-->")
            #continue
