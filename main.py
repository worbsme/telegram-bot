import threading
from flask import Flask
import telebot
import os

# 환경변수에서 토큰 가져오기
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 입장 메시지 삭제
@bot.message_handler(func=lambda message: message.new_chat_members)
def handle_join(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 입장 메시지 삭제됨")
    except Exception as e:
        print("❌ 입장 메시지 삭제 실패:", e)

# 퇴장 메시지 삭제
@bot.message_handler(func=lambda message: message.left_chat_member)
def handle_leave(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 퇴장 메시지 삭제됨")
    except Exception as e:
        print("❌ 퇴장 메시지 삭제 실패:", e)

# Render가 포트 확인할 수 있게 Flask 웹서버 실행
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    threading.Thread(target=run).start()
    print("🤖 Bot is running...")
    bot.polling()
