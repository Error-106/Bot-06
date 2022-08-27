import json
import bot
from fastapi import * #from flask import *#Flask,request,redirect,url_for,abort
bot=bot.bot
post={}
app = FastAPI()
#监听端口，获取QQ信息
@app.route('/', methods=["POST"])
def post_data():
    if  not request.data:   #检测是否有数据
        if "fail" in post : post["fail"]+=1
        else: post["fail"]=1
        return redirect(url_for('error')),401
    data=request.json
	#'下面的data.get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
    if data.get('message_type')=='private':# 如果是私聊信息
        if 'private' in post : post['private']+=1
        else: post['private']=1
        uid = data['sender']['user_id']# 获取信息发送者的 QQ号码
        message = data['message']  # 获取原始信息
        bot.keyword("1",message,data,uid)  # 将 Q号和原始信息传到我们的后台
    elif data.get('message_type')=='group':# 如果是群聊信息
        if 'group' in post : post['group']+=1
        else: post['group']=1
        gid = data['group_id'] # 获取群号
        uid = data['sender']['user_id'] # 获取信息发送者的 QQ号码
        message = data['message'] # 获取原始信息
        bot.keyword("2",message,data,uid, gid)# 将 Q号和原始信息传到我们的后台
    elif data.get('message_type')=='guild':# 如果是频道信息
        if 'guild' in post : post['guild']+=1
        else: post['guild']=1
        gid = [data['guild_id'],data['channel_id']]# 获取频道号
        uid = data['sender']['user_id'] # 获取信息发送者的 频道ID
        message = data['message'] # 获取原始信息
        bot.keyword("3",message,data,uid, gid)# 将 频道ID和原始信息传到我们的后台            
    if "OK" in post : post["OK"]+=1
    else: post["OK"]=1
    return 'OK'
@app.route('/', methods=["GET"])
def get():
    return "PyQQ Ver. 1-by Error-106 Debug:post" + str(post)
@app.route('/error')
def error():
    abort(401)
if __name__ == '__main__':
    # 此处的 host和 port对应上面 yml文件的设置
    app.run(debug=True,host='127.0.0.1',port=5701)