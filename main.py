import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

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

print("🤖 Bot is running…")
bot.polling()
