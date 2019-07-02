from tkinter import *
import time
from playsound import playsound

#TODO 23 May 2019 : add pause or work display

#=====BACKEND=====
def main():
        #main function
        #input = none
        #output = none
        T = int(e.get())
        mmt.set("work")
        timer(45)
        checker()
        if T > 1:
                for i in range(1,T):
                        mmt.set("pause")
                        timer(15)
                        checker()
                        mmt.set("work")
                        timer(45)
                        checker()

def checker():
        #check if play sound or not
        #input : none
        #output : none
        if check.get() == 1:
                playsound("alarme.mp3")
        else:
                time.sleep(2)

def timer(n):
        #timer function
        #input : n=number of minutes
        #output : none
        global t
        dt = time.time()
        tps = time.time()-dt
        s = str(int(tps%60))
        m = str(int(tps//60))
        while tps < n*60-2:
                tps = time.time()-dt
                s = str(int(tps%60))
                m = str(int(tps//60))
                t.set(m+":"+s)
                root.update()

#=====FRONTEND=====
root = Tk()
root.title("Work Time")

l1 = Label(root,text="Hours of work :")
l1.grid(row=0,column=0)

e = Entry(root)
e.grid(row=0,column=1)

l2 = Label(root,text="Allow ringing ?")
l2.grid(row=1,column=0)

check = IntVar()
c = Checkbutton(root,variable=check)
c.grid(row=1,column=1)

t = StringVar()
l3 = Label(root,textvariable=t)
l3.grid(row=3,column=0)

mmt = StringVar()
l4 = Label(root,textvariable=mmt)
l4.grid(row=3,column=1)

b = Button(root,text="GO",command=main)
b.grid(row=2,column=1)

root.mainloop()