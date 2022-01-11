if __name__=="__main__":
    import listen as li
    li.app.run(host='127.0.0.1',port=5701)
    exit()
print("init module...")
import json
#import requests
import httpx as requests
import re
#import random
import io
import os
from PIL import Image
def textcolor(code='0'):
        return '\033[%sm'%code
log=None
print("init NsfwScan Ai...")
import nsfw
nsfws=["hentai","porn","sexy"]
isnsfw=40.0
print("Finish.")
class bot:
    # pattern = re.compile(r"""\[CQ:image,file=([a-zA-z]+://[^\s&,]*),type=[A-Za-z]{1,5}(,id=4000)[1-5]\]""")
    pimg = re.compile(r"""\[CQ:image,file=([A-Za-z0-9]+).image,url=([a-zA-z]+://[^\s&\]]*)\]""")
    def loadlog():
        global log
        try:
            log=[requests.get('http://127.0.0.1:5700/get_login_info').json()["data"],requests.get('http://127.0.0.1:5700/get_guild_service_profile').json()["data"]]
        except requests.ConnectError as rece:
            log=None
            print(textcolor('1;37;44')+r'* WARNING:ConnectError'+textcolor())
            print(rece)
    #登陆者QQ信息
    loadlog()
    def keyword(Type,message,allmssage,uid,gid=None):
        #Type:消息类型（私聊：1，群聊：2，频道：3），message：消息，uid:QQ号，gid：群号/频道号
        if log == None: bot.loadlog()
        scans=bot.nsfwscan(message=message)
        for scan in scans:
            print(bot.nsfwif(scans[scan]))
        print(scans)
        if Type==3 and uid!=log[1]["tiny_id"] and gid==["2307805s1636521595","1780294"]:
            url='http://127.0.0.1:5700/send_guild_channel_msg?guild_id='+gid[0]+"&channel_id="+gid[1]+"&message="+message
            requests.get(url)
    def nsfwscan(message):
        imgs=bot.pimg.findall(message)
        reimgs={}
        if imgs != []:
            for i in imgs:
                img=Image.open(io.BytesIO(requests.get(i[1]).content))
                insfw=nsfw.get_tasks(img)
                reimgs[i]=insfw
        return reimgs
    def nsfwif(insfw):
        nsfwflag=False
        for j in nsfws:
            if insfw.get(j) >= isnsfw:
                nsfwflag=True
        return nsfwflag
