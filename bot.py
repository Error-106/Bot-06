if __name__=="__main__":
    raise("Please run bot from listen")
print("init module...")
import json
#import requests
import httpx as requests
import re
#import random
import io
#import os
import plugin
from PIL import Image
def textcolor(code='0'):
        return '\033[%sm'%code
log=None
class bot(plugin.plugin):
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
