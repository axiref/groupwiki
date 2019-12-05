import re
import telebot
from config import TOKEN
import wikipedia
from urllib.parse import unquote
regexp = r'^\[\[(.+?)\]\]|\{\{(.+?)\}\}$'

bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("zh")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if (message.chat.type == 'private'):
        bot.send_message(message.chat.id, '使用[[]]或{{}}提供到中文維基百科的連結')

@bot.message_handler(commands=['version'])
def help(message):
    if (message.chat.type == 'private'):
        bot.reply_to(message, "https://github.com/axiref/groupwiki")

@bot.message_handler(regexp=regexp)
def search_keyword(message):
    m = re.search(regexp, message.text)
    keyword = m[1] or m[2]
    if not keyword: return
    try:
        result = wikipedia.page(keyword)
        bot.reply_to(message, unquote(result.url), parse_mode="markdown")
    except wikipedia.exceptions.PageError:
        bot.reply_to(message, '没找到结果')

if __name__ == '__main__':
    print('Service is running...')
    bot.polling()