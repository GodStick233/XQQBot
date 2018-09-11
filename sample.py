# -*- coding: utf-8 -*-
import TuringRobot as tr
import WeatherFinder as wf
def onQQMessage(bot, contact, member, content):
    answer = tr.answer(content)
    if '@ME' in content:
        bot.SendTo(contact, answer)
    if '-天气' in content:
        city = content[3:]
        weather = wf.findweather(city)
        bot.SendTo(contact,weather)
