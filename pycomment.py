import os 
import pyautogui
import time



 
os.system('clear')

print ('''       \033[0;31m    WELCOM  TO 

 ____         ____                                     _   
|  _ \ _   _ / ___|___  _ __ ___  _ __ ___   ___ _ __ | |_ 
| |_) | | | | |   / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __|
|  __/| |_| | |__| (_) | | | | | | | | | | |  __/ | | | |_ 
|_|    \__, |\____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__|
       |___/                                                  
                                                            v1.0  
                                                              By Ahmad Saoud @ Mal4D   
                                                              
                                                               ''')
                                                              
a = input (
'  \033[0;34m[i] Enter Your comment: ' + ' '
)
b = input (' \033[0;32m [i] Enter Number for your comment:  ')
print('''
\033[0;33m[!] Operation has benn Started
   ''')
time.sleep(2)
for i in range (int(b)):

   time.sleep(1.5)
   pyautogui.typewrite(a +' ')
   pyautogui.hotkey('Enter')
   

