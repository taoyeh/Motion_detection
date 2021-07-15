import json
import requests



# 面向过程的app小程序发送消息
app_id="wx362221bafa1da332"
app_secret="9bac4deb22cc28885e528af77c11cae6"
url=f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}"
resp=requests.get(url).json()
access_token=resp.get("access_token")

url=f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}"
open_id="okMRV62j4Czg1yT3k_SBI1hMu4us"
req_data={
    "touser":open_id,
    "msgtype":"text",
    "text":
    {
         "content":"Hello World"
    }
}
requests.post(url,data=json.dumps(req_data,ensure_ascii=False).encode('UTF-8'))