#alarm
import datetime
import playsound

alarmhr=int(input("Enter the hour:"))
alarmmin=int(input("Enter the min:"))
alarmam=input("am/pm:")

if alarmam=="pm":
    alarmhr+=12


while True:
    if alarmhr==datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print("Playing")
        playsound.playsound(r"C:\Users\91984\Desktop\dogs.mp3")
        break    