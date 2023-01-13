from extensions import ServiceConverter
from config import TOKEN, VALUES
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(msg):
    info = f"Привет, {msg.from_user.first_name}!\nИнструкция по использованию:\nВведите название валюты которую хотите конвертировать, далее название валюты в которую хотите ее получить и количество валюты\nФормат: ВАЛЮТА-1 ВАЛЮТА-2 КОЛ-ВО ВАЛЮТА-1 (RUB THB 1000)"
    bot.send_message(msg.chat.id, info)

@bot.message_handler(commands=['values'])
def info(msg):
    total = ""
        
    for currency in VALUES:
        total +=currency+" "
    bot.send_message(msg.chat.id, f'{total}- валюты которые вы можете конвертировать')

@bot.message_handler()
def convert(msg):
    text = msg.text
    text = text.split(' ')
    if len(text) != 3:
        bot.send_message(msg.chat.id, "Вы неправльно ввели формат входных данных... введите команду /help для получения инструкций")
        return
    quote, base, total = text
    intTotal = 0
    try:
        intTotal = float(total)
    except:
        bot.send_message(msg.chat.id, "Количество валюты должно быть прописано числом")
        return

    if intTotal < 0:
        bot.send_message(msg.chat.id, "Количество валюты  не может быть отрицательным")
        return
       
    try:
        if VALUES[quote] and VALUES[base]:
            amount = ServiceConverter.getPrice(quote, base, intTotal)
            bot.send_message(msg.chat.id, f'Перевод {total} {quote} в {base} = {amount} {base}')
    except  KeyError:
        return bot.send_message(msg.chat.id, f'неизвестная валюта(ы) или наш бот не может с ней работать...')
    
    

print("bot start")
bot.polling(non_stop=True)