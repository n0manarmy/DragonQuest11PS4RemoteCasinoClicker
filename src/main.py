import random
import time
import win32api
import win32con
import win32gui

def main():
    windowName = "PS4 Remote Play" #find Remote Play Window
    while(True): #While remote play window active, sleep 1sec then press enter
        if(windowActive(windowName)):
            time.sleep(random.uniform(.5, 1)) #sleep between .5sec and 1sec
            keyStroke('ENTER') #call keyStroke function with key ENTER
        else:
            print(windowName + " is not active. waiting till window active. Ctrl +C to stop running")
            time.sleep(3) #sleep for 3 seconds
    exit()

def windowActive(windowName):
    windowID = win32gui.FindWindow(None, windowName) #get windowID for windowName
    activeWindow = win32gui.GetForegroundWindow()
    if windowID != activeWindow: #if window not found, return false which exits
        print("Window Not Active!")
        return False
    else:
        print("Window Active!") #window found, while loop in main will proceed.
        return True

def keyStroke(KEY):
    if KEY == 'ENTER':
        win32api.keybd_event(0x0D, 0, 0, 0) #keycode for enter pressed down
        time.sleep(random.uniform(0.25, 0.75)) #wait between .25 and .75 with key down
        win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0) #keycode for enter button released

if __name__ == '__main__':
    main()
