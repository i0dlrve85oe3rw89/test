#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot


bot = telebot.TeleBot('1012369969:AAHk2zKjTv6m_gvA7bEYQWN-aiDn2xd9UbU')


@bot.message_handler(commands=['start'])
def send_krol_cool(message):
    bot.send_message(message.chat.id, 'hi.')


bot.polling()
