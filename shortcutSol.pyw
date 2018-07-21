import tkinter as tk
import tkinter.ttk as ttk
import os
import re
from tkinter import messagebox as msgbox


def exitProgram():
    tkChoice = tk.Tk()
    tkChoice.wm_title("Exit Program")
    tkChoice.resizable(False, False)

    lab = tk.Label(tkChoice, text="Do you wanna really exit from the program?")
    butt1 = ttk.Button(tkChoice, text="Yes", command=lambda: os._exit(0))
    butt2 = ttk.Button(tkChoice, text="No", command=tkChoice.destroy)

    lab.grid(row=0, column=0, columnspan=2)
    butt1.grid(row=1, column=0)
    butt2.grid(row=1, column=1)

    tkChoice.mainloop()


class mainTk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        solvingFrame = SolvingFrame(self)
        solvingFrame.pack()

        self.wm_title("Shortcut Program")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", exitProgram)
        self.iconbitmap(default=r"superman.ico")

class SolvingFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        os.system("wmic logicaldisk get deviceid > deviceIDs.txt")
        deviceList = []
        with open("deviceIDs.txt", "r") as file:
            deviceList = file.readlines()
        deviceList = deviceList[2:len(deviceList)-2]
        drivers = []
        for i in range(0, len(deviceList)):
            if i%2==0:
                drivers.append(deviceList[i][1:2] + ":")
        
        lab = tk.Label(self, text="Select your injuring drive")
        self.select = ttk.Combobox(self, justify="left", state="readonly", values=drivers)
        self.butt = ttk.Button(self, text="Start", command=lambda: self.doGob(master))

        lab.pack()
        self.select.pack()
        self.butt.pack()
    def doGob(self, master):
        theDriver = self.select.get()

        if theDriver == "":
            msgbox.showerror("ERROR MESSAGE", "You didn't specify any DRIVE")
        else:
            try:
                cmdValue = os.system("attrib -h -r -s /S /D {0}\*.*".format(theDriver))
                if cmdValue==0:
                    for name in os.listdir("{0}".format(theDriver)):
                        if re.search(".lnk", name):
                            os.remove("{0}\{1}".format(theDriver, name))

                    msgbox.showinfo("INFO MESSAGE", "Your Drive Isn't Injured Anymore\n=> Scan Your Drive With An Antivirus <=")
                    
                    self.butt.destroy()
                    lab = tk.Label(self, text="Your driver isn't injured anymore\n=> Scan your drive with an antivirus <=")
                    lab.pack()
                    butt = ttk.Button(self, text="Close", command=lambda: os._exit(0))
                    butt.pack()
                    master.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
                else:
                    assert 5/0
            except:
                msgbox.showerror("ERROR MESSAGE", "An Error Has Been Occurred During The Working")
                self.butt.destroy()
                lab = tk.Label(self, text="A problem has been occured during the working")
                lab.pack()
                butt = ttk.Button(self, text="Close", command=lambda: os._exit(0))
                butt.pack()
                master.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
            



progVar = mainTk()
progVar.mainloop()
        
