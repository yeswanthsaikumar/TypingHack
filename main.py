import requests
import time
from selenium import webdriver
import pyautogui 
import Type 


tab = webdriver.Chrome()

tab.get('https://www.ratatype.com/typing-test/test/')


Type.startTyping(tab)