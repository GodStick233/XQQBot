# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
        bot.SendTo(member,'Hello world!')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    elif content == '[@ME]  你是谁':
        bot.SendTo(member,'我是许慎爸爸')