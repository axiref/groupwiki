import re
import telebot
from config import TOKEN
import wikipedia
from urllib.parse import unquote

bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("zh")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '使用[[]]或{{}}提供到中文維基百科的連結')

@bot.message_handler()
def echo(message):
    m = re.match("\[\[(.*?)\]\]|\{\{(.*?)\}\}", message.text)
    if (m is not None):
        if (m[1] or m[2]):
            keyword = m[1] or m[2]
            try:
                result = wikipedia.page(keyword)
                bot.reply_to(message, "[%s](%s)" % (unquote(result.url), result.url), parse_mode="markdown")
            except wikipedia.exceptions.PageError:
                bot.reply_to(message, '没找到结果')

if __name__ == '__main__':
    print('Service is running...')
    bot.polling()