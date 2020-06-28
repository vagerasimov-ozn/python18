import telebot
token ='1314753973:AAEakhIYZyNrflyMbnBofRnHGy42N-KAgF0'
import random

divizi = ["Ozon такой хороший","как же я люблю Ozon","Всегда только там заказываю"]
divizismile = [1,2,3]
emoji = ['👍','🙏','🥰','🐒']

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_ozon_message(message):
    if message.text == "OZON":
        message.text = random.choice(divizi)
        bot.send_message(message.chat.id, message.text)
    else:
        smile = random.choice(divizismile)
        emji = random.choice(emoji)
        message.text = emji*smile
        bot.send_message(message.chat.id, message.text)

bot.infinity_polling()