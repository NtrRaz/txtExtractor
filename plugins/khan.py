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
import time



@bot.on_message(filters.command(["khan"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://api.penpencil.xyz/v1/oauth/token"  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    
    headers = {
            'Host': 'api.penpencil.xyz',
            'authorization': 'Bearer c5c5e9c5721a1c4e322250fb31825b62f9715a4572318de90cfc93b02a8a8a75',
            'client-id': '5f439b64d553cc02d283e1b4',
            'client-version': '21.0',
            'user-agent': 'Android',
            'randomid': '385bc0ce778e8d0b',
            'client-type': 'MOBILE',
            'device-meta': '{APP_VERSION:19.0,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.khansirofficial}',
            'content-type': 'application/json; charset=UTF-8'}

    info = {
  "username": "",
  "otp": "",
  "organizationId": "5f439b64d553cc02d283e1b4",
  "password": "",
  "client_id": "system-admin",
  "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
  "grant_type": "password"}
    info["username"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    s = requests.Session()
    response = s.post(url = rwa_url, headers=headers, json=info, timeout=10)
    if response.status_code == 200:
        data = response.json()
        token = data["data"]["access_token"]
        await editable.edit(f"**Login Successful:** ```{token}```")
    else:
         await m.reply_text("Go back to response")
    headers = {
            'Host': 'api.penpencil.xyz',
            'authorization': f"Bearer {token}",
            'client-id': '5f439b64d553cc02d283e1b4',
            'client-version': '21.0',
            'user-agent': 'Android',
            'randomid': '385bc0ce778e8d0b',
            'client-type': 'MOBILE',
            'device-meta': '{APP_VERSION:19.0,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.khansirofficial}',
            'content-type': 'application/json; charset=UTF-8',
    }
    params = {
       'mode': '1',
       'batchCategoryIds': '619bedc3394f824a71d8e721',
       'organisationId': '5f439b64d553cc02d283e1b4',
       'page': '1',
       'programId': '5f476e70a64b4a00ddd81379',
    }
    response = s.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    cool = ""
    mm = "KhanSir"
    for data in response:
        FFF = "**BATCH-ID  -  BATCH NAME**"
        #batch=(data["name"])
        aa = f" ```{data['_id']}```      - **{data['name']}**\n\n"
        #aa=f"```{data['name']}```  :  ```{data['_id']}\n```"
        if len(f'{cool}{aa}') > 4096:
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    #await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = s.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]
    response3 = s.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
   
    batch = response2['name']
    vj=""
    for data in response3:
        tids = data['_id']
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            vj = ""
        vj+=tids
    await editable1.edit(f"**Send the Subject id :-**\n```{vj}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    response02 = s.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{raw_text4}/topics?page=1', headers=headers).json()["data"]
    
    cool2 = ""
    vj = ""
    for dat in response02:
        FF = "**SUBJECT-ID - SUBJECT NAME - TOTAL VIDEOS - PDFS**"
        aa = f" ```{dat['_id']}```- **{dat['name']} - {dat['videos']} - {dat['notes']}**\n\n"
        idid=f"{dat['_id']}&"
        if len(f"{vj}{idid}")>4096:
            vj = ""
        vj+= idid     
        cool2 += aa
    await editable1.edit(f'{"**You have these Subjects in this Batch:-**"}\n\n{FF}\n\n{cool2}')
    editable2 = await m.reply_text(f"**Enter this to download full batch :-**\n```{vj}```")
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xv = raw_text5.split('&')
    for y in range(0,len(xv)):
      t =xv[y].strip()
      html3 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page=1&tag="+t+"&contentType=videos",headers=headers).content
      ff = json.loads(html3)
      tpage = (ff["paginate"])["totalCount"]//ff["paginate"]["limit"]+2
      print("Total page:",tpage)
      for i in range(1,tpage)[::-1]:
        html4 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page="+str(i)+"&tag="+t+"&contentType=videos",headers=headers).json()["data"]
        html4.reverse()
        #break
        for dat in html4:
          try:
            class_title=(dat["topic"])
            class_url=dat["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
            cc = f"{dat['topic']}:{dat['url']}"
            with open(f"{mm}-{batch}.txt", 'a') as f:
                f.write(f"{class_title}:{class_url}\n")
          except KeyError:
            pass
    await m.reply_document(f"{mm}-{batch}.txt")
    """

        print("Downloading pdfs")     
        response5 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page=1&tag="+t+"&contentType=notes",headers=headers).json()
        tpage = response5["paginate"]["totalCount"]//response5["paginate"]["limit"]+2
        print(tpage)
        for i in range(1,tpage)[::-1]:
          response6 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page="+str(i)+"&tag="+t+"&contentType=notes",headers=headers).json()["data"]
          for data in response6:
            try:
              title=(data["homeworkIds"][0]["topic"])
              baseurl= data["homeworkIds"][0]["attachmentIds"][0]["baseUrl"]
              key = data["homeworkIds"][0]["attachmentIds"][0]["key"]
            except KeyError:
              pass
              with open(f"{batch}.txt", 'a') as f:
                  f.write(f"{title}:{baseurl}{key}\n")
    await m.reply_text("Done")
    """


