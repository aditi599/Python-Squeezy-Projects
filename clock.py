from tkinter import  *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('ClockByAditiButTimeIsAllYours')
root.geometry("500x300")
root.configure(bg='pink')
def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text =string)
    lbl.after(1000,time)

lbl=Label(root,font=('serif',30,'bold'),background='yellow',foreground='grey')
lbl.pack(anchor='center')

time()
mainloop()