import ctypes
from win10toast import ToastNotifier
from time import sleep

lib=ctypes.windll.kernel32
toast=ToastNotifier()

time=int(str(lib.GetTickCount64())[:-3])    #calculates the system uptime
mins,sec=divmod(time,60)                    #get seconds
hours,mins=divmod(mins,60)                  #get minutes
days,hours_prev=divmod(hours,24)            #get hours

f=open('scheduler.txt','r')
l=list()
for i in f:
    l.append(int(i))
h=l[0]
m=l[1]

alert="Take a Break"
alert1="Thanks for taking a Break"
msg="U exceeded secheduled screentime...Take a break of"+str(m)+"minute(s)"
msg1="U have another break scheduled after another"+str(h)+"hour(s)"

while(True):
    time=int(str(lib.GetTickCount64())[:-3])    #calculates the system uptime
    mins,sec=divmod(time,60)                    #get seconds
    hours,mins=divmod(mins,60)                  #get minutes
    days,hours=divmod(hours,24)                 #get hours
    #print(hours,mins,sec,sep=":")
    if(hours_prev+h==hours):
        mins_prev+=h
        toast.show_toast(alert,msg,duration=5)
        print('Screen locked time:',mins)
        for i in range(m*60):
            ctypes.windll.user32.LockWorkStation()
            sleep(1)
        toast.show_toast(alert1,msg1,duration=5)
        print('Screen Unlocked time:',mins)
        
