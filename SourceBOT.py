#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8

import time
import random
import datetime
from PythonColorize import *
import telepot

## Credits
## Created By: Paulo Martins(RexyDeveloper)
## And Codec_ne

## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")
bot = telepot.Bot('add key aqui')
NomeBot = "Tal"

## BOT LANG
info_id = "Nome: *{}*\nUsuário: {}\nID: `{}`"
dados = "O Dado parou no número: 🎲 `{}`"

def handle(msg):
### BOT PARAMTS
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    message_id = msg['message_id']
    print(colors.lg_red + t + colors.lg_blue + ' Mensagem executada: %s' % colors.lg_red + texto + colors.nocolor)

### BOT COMANDOS
    if texto == '/dados':
        bot.sendMessage(chat_id, dados.format(random.randint(1,6)), "Markdown")
    elif texto == '/hora':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif texto == '/start':
        bot.sendMessage(chat_id, "Bot iniciado")
    elif texto == '/stop':
        bot.sendMessage(chat_id, "Bot parou")
    elif texto == '/id':
        bot.sendMessage(chat_id, info_id.format(from_first_name, from_username,  str(from_id)), "Markdown")

### Executando
print(colors.lg_red + t + colors.lg_cyan + NomeBot + " iniciado")
time.sleep(2)
bot.message_loop(handle)
while 1:
    time.sleep(10)
