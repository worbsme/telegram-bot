import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 새로 들어온 사람의 메시지 삭제
@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(f"입장 메시지 삭제 실패: {e}")

# 나간 사람의 메시지 삭제
@bot.message_handler(content_types=['left_chat_member'])
def handle_left_member(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(f"퇴장 메시지 삭제 실패: {e}")

print("🤖 Bot is running...")
bot.infinity_polling()
