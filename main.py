import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 입장 메시지 삭제
@bot.message_handler(content_types=['new_chat_members'])
def delete_join(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 입장 메시지 삭제 성공")
    except Exception as e:
        print("❌ 입장 메시지 삭제 실패:", e)

# 퇴장 메시지 삭제
@bot.message_handler(content_types=['left_chat_member'])
def delete_leave(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print("✅ 퇴장 메시지 삭제 성공")
    except Exception as e:
        print("❌ 퇴장 메시지 삭제 실패:", e)

print("🤖 봇 실행 중…")
bot.infinity_polling()
