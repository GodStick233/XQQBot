import json
import requests
import re
def answer(ask):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    body = {
	    "reqType":0,
        "perception": {
            "inputText": {
                "text": ""
            }
        },
        "userInfo": {
            "apiKey": "a3b4d5419b864fcb8ad26b3f6eca44b0",
            "userId": "319278"
        }
    }
    body['perception']['inputText']['text'] = ask
    data = json.dumps(body)
    response = requests.post(url, data = data)
    retext = response.text
    answ = re.compile('{.*?results":.*?values.*?text":"(.*?)"}', re.S)
    text = re.findall(answ, retext)
    return text

