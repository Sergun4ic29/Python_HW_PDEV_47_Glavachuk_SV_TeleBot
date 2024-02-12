
import telebot
from config import keys,TOKEN
from utils import APIException,CriptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message:telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет товарищ, {message.from_user.first_name}, рад приветствовать тебя в этом самом полензном телеграмм боте, \n \
                                        для того что что бы узнать все команды набери команду (\help)")

@bot.message_handler(commands=["help"])
def send_welcome(message:telebot.types.Message):
    text = ("Для работы в данном боте необходимо ввести команду в следующем формате:\n <имя валюты>\n \
<в какую валюту перевести> \n <количество переводимой валюты>\n \
что бы увидеть список всех доступных валют введите (\ values)")
    bot.reply_to(message,text)

@bot.message_handler(commands=["values"])
def values(message:telebot.types.Message):
    text = "Доступаные валюты:"
    for key in keys.keys():
        text = '\n'.join((text,key))
    bot.reply_to(message,text)




@bot.message_handler(content_types=["text"])
def convertion (message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Слишком много параметров')
        quot, base, amount = values
        total_base = CriptoConverter.get_price(quot,base,amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quot} в {base} - {total_base}'
        bot.send_message(message.chat.id,text)
bot.polling(non_stop=True)