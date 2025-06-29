import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.new_chat_members or message.left_chat_member)
def handle_join_leave(message):
    bot.delete_message(message.chat.id, message.message_id)

print("🤖 Bot is running…")
bot.polling()
