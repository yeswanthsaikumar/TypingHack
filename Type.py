
import time
import pyautogui

def startTyping(tab):

    pyautogui.press('enter')    

    start = tab.find_element_by_class_name('wgreen')
    data = tab.find_elements_by_class_name('wblack')

    pyautogui.typewrite(start.text)

    for i in range(len(data)):
        ty = data[i].text
        if len(ty) == 0 :
            pyautogui.press('space')
        else :
            pyautogui.typewrite(list(ty) , interval=0.01)#here this method is not working for very small values <0.0001

    pyautogui.press('enter')
