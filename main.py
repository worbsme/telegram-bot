import threading
from flask import Flask
import telebot
import os

# 봇 설정
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 입장/퇴장 메시지 삭제
@bot.message_handler(func=lambda message: message.new_chat_members)
def handle_join(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 입장 메시지 삭제됨")
    except Exception as e:
        print("❌ 입장 메시지 삭제 실패:", e)

@bot.message_handler(func=lambda message: message.left_chat_member)
def handle_leave(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 퇴장 메시지 삭제됨")
    except Exception as e:
        print("❌ 퇴장 메시지 삭제 실패:", e)

# Flask로 가짜 웹서버 실행 (Render가 포트 스캔할 때 통과시키기 위해)
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is alive"

def run():
    app.run(host='0.0.0.0', port=10000)

# Flask는 스레드로 돌리고, 봇은 메인 쓰레드에서 실행
if __name__ == "__main__":
    threading.Thread(target=run).start()
    print("🤖 Bot is running...")
    bot.polling()
