# -*- coding: utf-8 -*-
import TuringRobot as tr
def onQQMessage(bot, contact, member, content):
    answer = tr.answer(content)
    if '@ME' in content:
        bot.SendTo(contact, answer)
