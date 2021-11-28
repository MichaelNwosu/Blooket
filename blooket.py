#do pip install pyautogui
#for this to work
#do pip install webbrowser
#for this to work
import pyautogui
import time
import random
import webbrowser

print("""
                        INSTRUCTIONS
_______________________________________________________________________                
Using the link to the set below is  reccomended for this to work 
but you can also use any set that has all of the question set as correct.
PS - play the set in host mode.
⬇
https://www.blooket.com/set/619508d102453e7074dcd9a9
""")

num = int(input("Questions Answserd: "))
time.sleep(2)

summ=num*3

for i in range(summ):
    pyautogui.press("space")
    time.sleep(0.2)
    pyautogui.press("1")
    time.sleep(0.2)

