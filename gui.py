from tkinter import *
import webbrowser
import db
import threading as th
import companies.supermicro


class gui(Tk):
    """GUI representation of the database showing all jobs posting collected into a listbox"""

    def __init__(self, master=None):
        self.root = master
        self.init_page()


    def init_page(self):
        """intializes all page's features such as listbox"""
        self.items = db.getList()
        self.sm = companies.supermicro.supermicro()
        self.companies = {self.sm}
        self.root.geometry("500x500")
        self.root.listbox = Listbox(self.root)
        self.threading()
        self.repopulate(self.items)

    def repopulate(self, items):
        """destroys and then populates items from database into listbox"""
        print("repopulate")
        thisdict = {}
        self.root.listbox.delete(0, END)
        for  idx, item in enumerate(items):
            self.root.listbox.insert(idx, item[0] + " " + str(item[1]))
            thisdict[item[0] + " " + str(item[1])] = item[3]
        self.root.listbox.pack()
        def callback(event):
            webbrowser.open_new_tab(thisdict.get(self.root.listbox.get(self.root.listbox.curselection())))
        self.root.listbox.bind("<<ListboxSelect>>", callback)

    def threading(self):
        """initiates worker thread"""
        t1=th.Thread(target=self.work)
        t1.start()

    def work(self):
        """background thread that checks for whether a posting has been added"""
        for company in self.companies:
            if company.run():
                self.items = db.getList()  
        self.repopulate(self.items)
        self.root.after(5000, self.work)

    def exit(self):
        """destroys window"""
        self.destroy()


