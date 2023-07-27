from tkinter import *
import webbrowser
import db
import threading as th
import companies.supermicro
import time


items = db.getList()
sm = companies.supermicro.supermicro()

win = Tk()
win.geometry("500x500")

listbox = Listbox(win)

def repopulate(items):
    print("repopulate")
    thisdict = {}
    listbox.delete(0, END)
    for  idx, item in enumerate(items):
        listbox.insert(idx, item[0] + " " + str(item[1]))
        thisdict[item[0] + " " + str(item[1])] = item[3]
        # listbox.insert(idx, item)
    listbox.pack()
    def callback(event):
        webbrowser.open_new_tab(thisdict.get(listbox.get(listbox.curselection())))
    listbox.bind("<<ListboxSelect>>", callback)


def threading():
    t1=th.Thread(target=work)
    t1.start()

def work():
    if sm.run():
        items = db.getList()
        repopulate(items)
    win.after(5000, work)

threading()
repopulate(items)
win.mainloop()