import requests
import random
import time
import datetime
import bs4
import selenium
import webbrowser
import pyautogui 


webbrowser.open('https://www.ratatype.com/typing-test/test/')

time.sleep(4)
pyautogui.press('enter')    

res = requests.get('https://www.ratatype.com/typing-test/test/')
    
soup = bs4.BeautifulSoup(res.content , 'html5lib')#make tree data structure to traverse and scrap from the html file   

data = soup.select('.mainTxt')[0].getText()

print(data)

pyautogui.typewrite(str(data) , pause=0.5)

pyautogui.press('enter')

