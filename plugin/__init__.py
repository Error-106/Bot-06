import plugin.anti_nsfw as nsfw
from PIL import Image
import re
class plugin():
    # pattern = re.compile(r"""\[CQ:image,file=([a-zA-z]+://[^\s&,]*),type=[A-Za-z]{1,5}(,id=4000)[1-5]\]""")
    pimg = re.compile(r"""\[CQ:image,file=([A-Za-z0-9]+).image,url=([a-zA-z]+://[^\s&\]]*)\]""")
    def keyword(Type,message,allmssage,uid,gid=None): #Type:消息类型（私聊：1，群聊：2，频道：3），message：消息，uid:QQ号，gid：群号/频道号
        if Type=="2":
            scans=plugin.nsfwscan(message=message)
            scansflag=False
            for scan in scans:
                if plugin.nsfwif(scans[scan]):
                    scansflag=True
            if scansflag:
                pass
            print(scans)
#        if Type==3 and uid!=log[1]["tiny_id"] and gid==["2307805s1636521595","1780294"]:
#            url='http://127.0.0.1:5700/send_guild_channel_msg?guild_id='+gid[0]+"&channel_id="+gid[1]+"&message="+message
#            requests.get(url)
    def nsfwscan(message):
        imgs=plugin.pimg.findall(message)
        reimgs={}
        if imgs != []:
            for i in imgs:
                print(i)
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

