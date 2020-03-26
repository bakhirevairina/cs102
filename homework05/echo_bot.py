import telebot


access_token = '1052022342:AAGDSuJcn1EJ98Y815_0ZFIkUYATqZfXG-g'
telebot.apihelper.proxy = {'https': 'https://182.253.232.105:8080'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()