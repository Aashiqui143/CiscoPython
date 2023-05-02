import pyautogui as py
import time
import random
time.sleep(4)
list1=["one","two","three","four","five","six","seven","eight","nine","ten"]
for num in range(10):
    num=random.choice(list1)
    py.typewrite("Hi - {}".format(num))
    py.press("Enter")
    time.sleep(2)


