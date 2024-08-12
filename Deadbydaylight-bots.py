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
    
def pink_text(text):
    return f"\033[38;2;176;72;111m{text}\033[0m"
def aqua_text(text):
    return f"\033[38;2;7;229;237m{text}\033[0m"     
def green_text(text):
    return f"\033[38;2;0;255;0m{text}\033[0m"
def red_text(text):
    return f"\033[38;2;255;0;0m{text}\033[0m"

#survbot section-------------------------------------------------
def surv_bot(dbdwindow):
    print("---DBD SURVIVOR FARM BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: \n1.Game is in English")
    print("2.UI_Scale in Graphic Settings is 100%")
    print("3.Set keybinding \"Running\" \"Turn left\" \"Forward\" to left mouse")
    print("4.Game is Windowed Fullscreen in 1920*1080 res\n")
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

#bloodwebbot section-------------------------------------------------
def bloodweb_bot(dbdwindow):
    print("---DBD BLOODWEB BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: \n1.Game is in English")
    print("2.UI_Scale in Graphic Settings is 100%")
    print("3.Bloodweb is open")
    print("4.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("Bloodweb_bot is Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()
    
    while(1):
        time.sleep(3)
        pyautogui.mouseDown(x=680,y=560)
        time.sleep(1)
        pyautogui.mouseUp(x=680,y=560)
    return 0 

def killer_bot(dbdwindow):
    print("---DBD Killer Farming BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: \n1.Game is in English")
    print("2.UI_Scale in Graphic Settings is 100%")
    print("3.Bloodweb is open")
    print("4.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("Killerbot is Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()

    while(1):
        time.sleep(5)
        pyautogui.click(x=1743,y=923)
        time.sleep(1)
        pyautogui.click(x=1732,y=1008)
        time.sleep(3)
        #---Loop1
        pyautogui.mouseDown(button='right')
        time.sleep(3.6)
        pyautogui.mouseUp(button='right')
        pyautogui.keyDown('w')
        time.sleep(0.3)
        pyautogui.keyUp('w')
        pyautogui.click(x=1732,y=1008)
        time.sleep(1.7)
        pyautogui.click(x=1732,y=1008)
        pyautogui.keyDown('q')
        time.sleep(1.7)
        pyautogui.click(x=1732,y=1008)
        pyautogui.keyUp('q')
        time.sleep(1.7)
        #---Loop2
        pyautogui.mouseDown(button='right')
        time.sleep(3.6)
        pyautogui.mouseUp(button='right')
        pyautogui.keyDown('w')
        time.sleep(0.3)
        pyautogui.keyUp('w')
        pyautogui.click(x=1732,y=1008)
        time.sleep(1.7)
        pyautogui.click(x=1732,y=1008)
        pyautogui.keyDown('q')
        time.sleep(1.7)
        pyautogui.click(x=1732,y=1008)
        pyautogui.keyUp('q')
        time.sleep(1.7)
        #--Ctrl Power
        pyautogui.keyDown('ctrl')
        time.sleep(3)
        pyautogui.keyUp('ctrl')
    return 0

if __name__ == "__main__":
    os.system('cls')
    #check admin
    if(not is_admin()): 
        print(red_text("Run start_up.bat as admin"))
        print("Press Enter to close...")
        input()
        sys.exit()

    #check dbd_process
    dbd_hwnd = pyautogui.getWindowsWithTitle('DeadByDaylight')
    if dbd_hwnd == []:
        print(red_text("DBD is not running, Open the game and retry."))
        time.sleep(3)
        sys.exit()

    a = 0
    print(pink_text("""██████╗ ███████╗ █████╗ ██████╗ ██████╗ ██╗   ██╗██████╗  █████╗ ██╗   ██╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗  
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝  
██║  ██║█████╗  ███████║██║  ██║██████╔╝ ╚████╔╝ ██║  ██║███████║ ╚████╔╝ ██║     ██║██║  ███╗███████║   ██║     
██║  ██║██╔══╝  ██╔══██║██║  ██║██╔══██╗  ╚██╔╝  ██║  ██║██╔══██║  ╚██╔╝  ██║     ██║██║   ██║██╔══██║   ██║     
██████╔╝███████╗██║  ██║██████╔╝██████╔╝   ██║   ██████╔╝██║  ██║   ██║   ███████╗██║╚██████╔╝██║  ██║   ██║     
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝    ╚═╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝     
██████╗  ██████╗ ████████╗███████╗                                                                               
██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝                                                                               
██████╔╝██║   ██║   ██║   ███████╗                                                                               
██╔══██╗██║   ██║   ██║   ╚════██║                                                                               
██████╔╝╚██████╔╝   ██║   ███████║        ██████╗ ██╗   ██╗    ███████╗██╗   ██╗██████╗ ████████╗██╗     ███████╗
╚═════╝  ╚═════╝    ╚═╝   ╚══════╝        ██╔══██╗╚██╗ ██╔╝    ╚════██║██║   ██║██╔══██╗╚══██╔══╝██║     ██╔════╝
█████╗█████╗█████╗█████╗█████╗█████╗█████╗██████╔╝ ╚████╔╝         ██╔╝██║   ██║██████╔╝   ██║   ██║     █████╗  
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝██╔══██╗  ╚██╔╝         ██╔╝ ██║   ██║██╔══██╗   ██║   ██║     ██╔══╝  
                                          ██████╔╝   ██║          ██║  ╚██████╔╝██║  ██║   ██║   ███████╗███████╗
                                          ╚═════╝    ╚═╝          ╚═╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝"""))
    print('Github Page:',aqua_text('https://github.com/7urtle/Deadbydaylight-Farming-Bot\n\n'))
    print("1.Bloodweb Autoclick\n2.Killer Farmbot\n3.Survivot Farmbot")  
    while(a == 0):
        Sel = input(green_text("Choose a number:\n"))
        if(Sel == '1'):
            bloodweb_bot(dbd_hwnd[0])
            a=1
        elif(Sel == '2'):
            killer_bot(dbd_hwnd[0])
            a=1
        elif(Sel == '3'):
            surv_bot(dbd_hwnd[0])
            a=1
        else:
            print("unknown value, type again")
            
        

        

    
