import pyautogui
import time
import ctypes
import sys
import os

#macros-----USER CHANGE VALUES HERE-------------
button_loc = {
    "Continue" : (1732,1008),
    "Ready" : (1618,968),
    "Bloodweb" : (680,560),
    "OK" : (1410,665),
    "Menu-start" : (306,110),
    "Menu-killer":(307,216),
    "Menu-surv"  :(313,313)
}
#--------DONT CHANGE ANYTHING BELOW-------------
#-----Unless you know what you are doing--------

cx,cy = button_loc["Continue"]
rx,ry = button_loc["Ready"]
bx,by = button_loc["Bloodweb"]
ox,oy = button_loc["OK"]
sx,sy = button_loc["Menu-start"]
kx,ky = button_loc["Menu-killer"]
ux,uy = button_loc["Menu-surv"]


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
    print("Make sure: ")
    print("2.UI_Scale in Graphic Settings is 100%")
    print("3.Set keybinding \"Running\" \"Turn left\" \"Forward\" to left mouse")
    print("4.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("survBot Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()

    while(1):
        pyautogui.moveTo(x=sx,y=sy,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=ux,y=uy,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(2)
        pyautogui.moveTo(x=cx,y=cy,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=ox,y=oy,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=rx,y=ry,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.mouseDown()
        time.sleep(20)
        pyautogui.mouseUp()
    return 0

#bloodwebbot section-------------------------------------------------
def bloodweb_bot(dbdwindow):
    print("---DBD BLOODWEB BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: ")
    print("1.UI_Scale in Graphic Settings is 100%")
    print("2.Bloodweb is open")
    print("3.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("Bloodweb_bot is Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()
    
    while(1):
        time.sleep(3)
        pyautogui.mouseDown(x=bx,y=by)
        time.sleep(1)
        pyautogui.mouseUp(x=bx,y=by)
    return 0 

def killer_bot(dbdwindow):
    print("---DBD Killer Farming BOT---\n-------Made By 7urtle-------\n----------------------------\n")
    print("Make sure: ")
    print("1.UI_Scale in Graphic Settings is 100%")
    print("3.Game is Windowed Fullscreen in 1920*1080 res\n")
    time.sleep(1)
    input("Press ENTER to start") 
    print(green_text("Killerbot is Running......\nCtrl+C to stop"))
    time.sleep(1)
    dbdwindow.activate()

    while(1):
        time.sleep(2)
        pyautogui.moveTo(x=cx,y=cy,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=ox,y=oy,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=rx,y=ry,duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        
        pyautogui.moveTo(x=sx,y=sy,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x=kx,y=ky,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()
        #---Loop1
        time.sleep(2)
        pyautogui.mouseDown(button='right')
        time.sleep(3.4)
        pyautogui.mouseUp(button='right')
        pyautogui.keyDown('w')
        time.sleep(0.3)
        pyautogui.keyUp('w')
        pyautogui.click(x=rx,y=ry)
        time.sleep(1.7)
        pyautogui.click(x=cx,y=cy)
        pyautogui.keyDown('q')
        time.sleep(1.7)
        pyautogui.click(x=cx,y=cy)
        pyautogui.keyUp('q')
        time.sleep(1.7)
        #---Loop2
        pyautogui.mouseDown(button='right')
        time.sleep(3.4)
        pyautogui.mouseUp(button='right')
        pyautogui.keyDown('w')
        time.sleep(0.3)
        pyautogui.keyUp('w')
        pyautogui.click(x=cx,y=cy)
        time.sleep(1.7)
        pyautogui.click(x=cx,y=cy)
        pyautogui.keyDown('q')
        time.sleep(1.7)
        pyautogui.click(x=cx,y=cy)
        pyautogui.keyUp('q')
        time.sleep(3)
        #--Ctrl Power
        pyautogui.keyDown('ctrl')
        time.sleep(3)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
    return 0

if __name__ == "__main__":
    os.system('cls')
    #check admin
    if(not is_admin()): 
        print(red_text("Run as admin,Try again"))
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
    print("1.Bloodweb Autoclick\n2.Killer Farmbot\n3.Survivor Farmbot")  
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
            
        

        

    
