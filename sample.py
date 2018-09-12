# -*- coding: utf-8 -*-
import TuringRobot as tr
import WeatherFinder as wf
import FFXIV as ff
def onQQMessage(bot, contact, member, content):
    answer = tr.answer(content)
    if '@ME' in content:
        bot.SendTo(contact, answer)
    if '-天气' in content:
        city = content[3:]
        weather = wf.findweather(city)
        bot.SendTo(contact,weather)
    if '-词条' in content:
        wiki = content[3:]
        end = ff.searchwiki(wiki)
        bot.SendTo(contact, end)
    if '-物品' in content:
        wiki = content[3:]
        end = ff.searchitems(wiki)
        bot.SendTo(contact, end)
    if '-获得' in content:
        wiki = content[4:]
        end = ff.searchget(wiki)
        bot.SendTo(contact, end)
