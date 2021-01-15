import webbrowser
import pyautogui as magic
from datetime import datetime
import time
import sys
import yaml

sys.tracebacklimit=0

settings_path="setting.yaml"
with open(settings_path) as f:
    settings = yaml.load(f, Loader=yaml.FullLoader)
   
alltimings = settings['alltimings']
timing = alltimings['starttime']
endtime = alltimings['endtime']
columns = alltimings['range']

google_meet = settings["google meets"]
link = google_meet["link"]
code = google_meet['code']




def preemeeting():
    print('Going to enter the meeting')
    magic.press('tab')
    magic.press('tab')
    magic.press('tab')
    magic.press('tab')
    magic.press('enter')
    magic.press('tab')
    magic.press('enter')
    magic.press('tab')
    magic.press('tab')
    magic.press('tab')
    magic.press('enter')
    waitingforend()

def entermeeting():
    blank = magic.locateCenterOnScreen('core\stream.png')
    magic.moveTo(blank)
    magic.click()
    magic.click()
    magic.press('tab')
    magic.press('tab')
    magic.press('tab')
    magic.press('enter')
    time.sleep(10)
    waiting()
    
def waiting():
    wait = magic.locateCenterOnScreen('core\waiting-for-meeting.png')
    if wait == None:
        preemeeting()
    else:
        magic.hotkey('ctrl', 'r')
        print('Waiting for the meeting to be started by the teacher')
        k = True
        while k == True:
            if wait == None:
                preemeeting()
            else:
                magic.hotkey('ctrl', 'r')
                time.sleep(15)
                
def googlemeets():
    print('Waiting for the start time')
    while True:
        curr = datetime.now().strftime("%H:%M")
        for now in timing:
            if now == curr:
                i = 0
                while i <= columns:
                    if curr == timing[i]:
                        print(i)
                        break
                    i += 1
                a = i-1
                if link == [] and code == []:
                    webbrowser.get('windows-default').open('https://classroom.google.com')
                    time.sleep(15)
                    for z in range(0,3):
                        magic.press('tab')
                    if i == 0:
                        magic.press('enter')
                    else:
                        for b in range(0,i):
                            magic.press('tab')
                            magic.press('tab')
                            magic.press('tab')
                            magic.press('tab')
                        magic.press('enter')
                    time.sleep(10)
                    entermeeting()
                elif link == []:
                    webbrowser.get('windows-default').open('https://meet.google.com/')
                    time.sleep(15)
                    textbox= magic.locateCenterOnScreen('core\enter-meeting-id.png')
                    magic.moveTo(textbox)
                    magic.click()
                    magic.write(code[a])
                    magic.press('enter')
                    time.sleep(10)
                    preemeeting()
                elif code == []:
                    webbrowser.get('windows-default').open(link[a])
                    time.sleep(15)
                    preemeeting()
                else:
                    print('Please enter either the meeting code or the meeting link')



def waitingforend():
    print('waiting for the end time')
    while True:
        curr2 = datetime.now().strftime("%H:%M")
        for now2 in endtime:
            if now2 == curr2:
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('tab')
                magic.press('enter')
                time.sleep(2)
                magic.hotkey('alt', 'f4')
                googlemeets()
            else:
                time.sleep(2)
                

                    
googlemeets()