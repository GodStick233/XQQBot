import requests
import cv2
import random
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
url = 'http://202.118.120.84:7001/ACTIONLOGON.APPPROCESS'
urlx = 'http://202.118.120.84:7001/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
r = requests.get(url)
s = requests.session()
vcodeimage = s.get(urlx)
randomname = random.randint(0,100)
with open(str(randomname)+'.jpg', 'wb') as file:
    file.write(vcodeimage.content)
#testimage = cv2.imread(str(randomname)+'.jpg')
#cv2.imshow('1',testimage)
#cv2.waitKey(0)
vcode = pytesseract.image_to_string(Image.open(str(randomname)+'.jpg'))
Data ={'Agnomen':vcode,
'Password':'#',
'WebUserNO':'#'}
login = s.post(url,Data)
Class = s.get('http://202.118.120.84:7001/ACTIONQUERYSTUDENTSCHEDULEBYSELF.APPPROCESS')
soup = BeautifulSoup(Class.text, 'html.parser')
#print(soup)
print(soup.get_text())