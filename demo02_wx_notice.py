import json
import requests

# 面向对象的app小程序发送消息
class WxTools():
    def __init__(self,app_id,app_secret):
        self.app_id=app_id
        self.app_secret=app_secret

    def get_access_token(self):
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url).json()
        access_token = resp.get("access_token")
        return access_token

    def sned_wx_customer_msg(self,open_id,msg="target in view"):
        url = f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={self.get_access_token()}"
        req_data = {
            "touser": open_id,
            "msgtype": "text",
            "text":
                {
                    "content": msg
                }
        }
        requests.post(url, data=json.dumps(req_data, ensure_ascii=False))
wx_Tools= WxTools("wx362221bafa1da332","9bac4deb22cc28885e528af77c11cae6")
wx_Tools.sned_wx_customer_msg("okMRV62j4Czg1yT3k_SBI1hMu4us")