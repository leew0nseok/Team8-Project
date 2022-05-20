import telepot
from telegram.ext import MessageHandler, Filters, Updater

token = "5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4"
bot = telepot.Bot(token)

chat_id = '5081938343'

bot.sendMessage(chat_id, "hihihi")

# updater 업데이트 사항이 있으면 가져옴
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def handler(update, context): 
    user_text = update.message.text 
    if user_text == "안녕": 
        bot.sendMessage(chat_id, "안녕")
    elif user_text == "뭐해":
        bot.sendMessage(chat_id, "뭐")
    else:
        bot.sendMessage(chat_id, user_text)
        
 
new_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(new_handler) # new_handler 추가

updater.start_polling()#폴링 시작(업데이트 받아오기)
