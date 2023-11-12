from flask import Flask
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
# from dotenv import load_dotenv
import os


# 載入環境變數
# load_dotenv()

app = Flask(__name__)

# 設定 Line Bot 的 Channel Access Token 和 Channel Secret
# line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

# # 設定 Bit.ly 的 Access Token
# BITLY_ACCESS_TOKEN = os.getenv('BITLY_ACCESS_TOKEN')

# domain root
@app.route('/')
def home():
    return 'Hello, World!'


# @app.route("/webhook", methods=['POST'])
# def callback():
#     # X-Line-Signature 是用來確認請求是由 Line 伺服器發送的
#     signature = request.headers['X-Line-Signature']

#     # 取得請求的內容
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     try:
#         # 驗證簽名，若驗證失敗則拋出 InvalidSignatureError
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # 取得使用者傳來的文字訊息
#     user_message = event.message.text
    
#     # 回覆相同的文字 + 請輸入網址
#     reply_message = user_message + "，請輸入網址"

#     # 若使用者輸入的內容是網址，則使用 Bit.ly API 縮短網址
#     if user_message.startswith("http"):
#         shortened_url = shorten_url(user_message)
#         reply_message = f"輸入的網址已縮短為：{shortened_url}"

#     # 回覆訊息給使用者
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=reply_message)
#     )

# def shorten_url(long_url):
#     # 使用 Bit.ly API 縮短網址
#     url = "https://api-ssl.bitly.com/v4/shorten"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {BITLY_ACCESS_TOKEN}"
#     }
#     data = {
#         "long_url": long_url
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     shortened_url = response.json()["id"]
#     return shortened_url

if __name__ == "__main__":
    app.run()
