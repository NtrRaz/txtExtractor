import subprocess 
from textwrap import dedent
from subprocess import getstatusoutput
from typing import BinaryIO, Union
from get_video_info import get_video_attributes, get_video_thumb
import requests
import concurrent.futures
cmd = [
  "yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/_lW8dfxks14' -o './downloads/435946586/0001 ir.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'",
  "yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/P2k2J65pbnE' -o './downloads/435946586/0002 Physics  मापन एवं मात्रक ＃2 Group D, UP ir.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'",
  "yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/Vgn-WPizr1Q' -o './downloads/435946586/0001 Physicsr.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'",
  "yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/XX3QNTSkg60' -o './downloads/435946586/0002 Physics.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'",
  "yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/BTBTrpiIh7Q' -o './downloads/435946586/0003 Physic.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'"
]
def exec(cmd):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stderr)
       

        #err = process.stdout.decode()
def pull_run(work, cmds):
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
        print("Waiting for tasks to complete")
        fut = executor.map(exec,cmds)
exec("yt-dlp --socket-timeout 30 -R 25 --no-warning 'https://m.youtube.com/shorts/_lW8dfxks14' -o './downloads/435946586/0001 ir.%(ext)s' -f '18/b[height<=144]/bv[height<=144]+ba/b/bv+ba' --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 18 -j 36'")