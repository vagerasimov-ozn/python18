# Эхо бот
import telebot
token ='1314753973:AAEakhIYZyNrflyMbnBofRnHGy42N-KAgF0'

bot =telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()