
from tkinter import *  
import datetime as dt  
import time  
import winsound as ws  
  

def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
  
 
guiWindow = Tk()  
guiWindow.title("Alarm Clock")  
guiWindow.geometry("464x200")  
guiWindow.config(bg = "#78BBF6")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = Label(  
    guiWindow,  
    text = "Set time in 24-hour format!",  
    fg = "white",  
    bg = "#63468B",  
    font = ("Arial", 15)  
    ).place(  
        x = 0,  
        y = 160  
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour     Minute     Second",  
    font = 60,  
    fg = "white",  
    bg = "#87BDD8"  
    ).place(  
        x = 220,  
        y = 10  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 50  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FF0000",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 53  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FF0000",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FF0000",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  
   
submit = Button(  
    guiWindow,  
    text = "Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 140,  
        y = 100  
        )  
   
guiWindow.mainloop()  