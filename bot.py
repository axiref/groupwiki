import re
import telebot
from config import TOKEN
import wikipedia
from urllib.parse import unquote

bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("zh")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '你好，将我添加到群里，然后发送[[关键词]]就能得到维基百科结果了')

@bot.message_handler()
def echo(message):
    match = re.match("^\[\[(.*?)\]\]$", message.text)
    if (match and match[1]):
        keyword = match[1]
        try:
            result = wikipedia.page(keyword)
            bot.reply_to(message, "[%s](%s)" % (unquote(result.url), result.url), parse_mode="markdown")
        except wikipedia.exceptions.PageError:
            bot.reply_to(message, '没找到结果')

if __name__ == '__main__':
    bot.polling()