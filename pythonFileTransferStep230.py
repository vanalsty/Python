import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import shutil




class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450,200))
        self.master.title('Check Files for Transfer')
        self.master.config(bg='#F0F0F0')

    

        #Browse Buttons
        
        self.btnBrowOne = Button(self.master, text="Source", width=14, height=1,command=self.browseSource)
        self.btnBrowOne.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowOne = Button(self.master, text="Destination", width=14, height=1,command=self.browseDestination)
        self.btnBrowOne.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        #Folder destination/Entry fields
        
        self.txtSource = Entry(self.master,text='', font=("Helvetica",16), fg='black', bg='white')
        self.txtSource.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.txtDestination = Entry(self.master,text='', font=("Helvetica",16), fg='black', bg='white')
        self.txtDestination.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)


        #Operation buttons, Check and Close
        
        self.btnCheck = Button(self.master, text="Check for files", width=14, height=2,fg='black', bg='lightgray', command=self.Check)
        self.btnCheck.grid(row=2, column=0, padx=(30,0), pady=(20,0))

        self.btnMove = Button(self.master, text="Move files", width=14, height=2,fg='black', bg='lightgray', command=self.Move)
        self.btnMove.grid(row=2, column=1, padx=(15,0), pady=(20,0))

        self.btnClose = Button(self.master, text="Close Program", width=14, height=2, fg='black', bg='lightgray',command=self.Close)
        self.btnClose.grid(row=2, column=2, padx=(15,0), pady=(20,0),)



    def Close(self):
        self.master.destroy()
   
    def browseSource(self):
        self.varFolder=tk.filedialog.askdirectory()
        self.txtSource.insert(0,self.varFolder)
        

    def browseDestination(self):
        self.varDestination=tk.filedialog.askdirectory()
        self.txtDestination.insert(0,self.varDestination)

    def Move(self):
        spath=self.txtSource.get()
        path=os.listdir()
        dpath=self.txtDestination.get()
        for filename in os.listdir(spath):
            if filename.endswith('.txt'):
                shutil.move(spath+'/'+filename, dpath)
                print(filename)
                continue
            else:
                continue

        
    def Check(self):
        spath=self.txtSource.get()
        path=os.listdir()
        dpath=self.txtDestination.get()
        for filename in os.listdir(spath):
            if filename.endswith('.txt'):
                print(filename)
                paths=os.path.join(spath, filename)
                print(os.path.getmtime(paths))
                continue
            else:
                continue


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
