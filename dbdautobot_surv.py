import pyautogui
import time
import ctypes
import sys
import os
#1920*1080 - res:
#1732 1008 - Continue 
#1743 923  - Ready

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def green_text(text):
    return f"\033[38;2;0;255;0m{text}\033[0m"

def surv_bot(dbdwindow):
    print("---DBD SURVIVOR FARM BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: \n1.Game is in English")
    print("2.Set keybinding \"Running\" \"Turn left\" \"Forward\" to left mouse")
    print("3.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("survBot Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()

    while(1):
        time.sleep(5)
        pyautogui.click(x=1743,y=923)
        time.sleep(1)
        pyautogui.click(x=1732,y=1008)
        time.sleep(5)
        pyautogui.mouseDown()
        time.sleep(20)
        pyautogui.mouseUp()
    return 0

def bloodweb_bot():

    return 0 

def killer_bot():

    return 0

if __name__ == "__main__":
    os.system('cls')
    #check admin
    if(not is_admin()): 
        input("Run start_up.bat as admin\nPress Enter to close...")
        sys.exit()

    #check dbd_process
    dbd_hwnd = pyautogui.getWindowsWithTitle('DeadByDaylight')
    if dbd_hwnd == []:
        print("DBD is not running, Open the game and retry.")
        time.sleep(3)
        sys.exit()

    a = 0
    print("1.Bloodweb Autoclick(undone)\n2.Killer Farmbot(undone)\n3.Survivot Farmbot")  
    while(a == 0):
        Sel = input()
        if(Sel == '1'):
            bloodweb_bot(dbd_hwnd)
            a=1
        elif(Sel == '2'):
            killer_bot(dbd_hwnd)
            a=1
        elif(Sel == '3'):
            surv_bot(dbd_hwnd[0])
            a=1
        else:
            print("unknown value, type again")
            
        

        

    
