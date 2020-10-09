from tkinter import *
import sys
import time

def times() :
    main_time=time.strftime("%H : %M : %S")
    clock.config(text=main_time)
    clock.after(100,times)


root=Tk()
root.geometry("500x250")
root.title("Digital Clock By -Savan Vaghela")
root.resizable(0,0)
clock=Label(root,font=('times',50,"bold"),bg="lightgrey",fg='black')
clock.grid(row=2,column=4,pady=70,padx=85)
times()

root.mainloop()
