import json
import requests
#天气预报api
def findweather(city):
    html = requests.get('https://free-api.heweather.com/s6/weather/now?location='+city+'&key=#你的apikey')
    weather = html.json()
    cityweather = city+'市现在的天气为：'+weather['HeWeather6'][0]['now']['cond_txt']+'，气温为：'+weather['HeWeather6'][0]['now']['tmp']+'摄氏度'
    return cityweather