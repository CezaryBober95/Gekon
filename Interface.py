import tkinter as tk

#todo: connect all class here
#todo: add plots, point board,make buttons to start observation
#todo: MENU bar with help how to add file with observation
#TODO: PANDAS !!!
class Interface:

    def __init__(self, master):
        self.master = master
        master.title("The Gekon Project")
        width_value=master.winfo_screenwidth()
        height_value=master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width_value,height_value))

        self.Frame1 = tk.LabelFrame(master,text="Temperature",width=width_value/2,height=height_value/2, bg="#708090")
        self.Frame1.grid(row=0, column=0,ipadx=15)
        self.Frame2 = tk.LabelFrame(master,text="Frame2",width=width_value/2,height=height_value/2, bg="#708090")
        self.Frame2.grid(row=0, column=1,ipadx=15)
        self.Frame3 = tk.LabelFrame(master,text="Score board",width=width_value/2,height=height_value/2, bg="#708090")
        self.Frame3.grid(row=1, column=0,ipadx=8,ipady=8)
        self.Frame4 = tk.LabelFrame(master,text="Buttons",width=width_value/2,height=height_value/2, bg="#708090")
        self.Frame4.grid(row=1, column=1,ipadx=15)

#Frame1-> temperature plot for 1 or 2 animals

#Frame2->

#Frame3-> score board for position
        for i in range(8):
            for j in range(8):
                tk.Button(self.Frame3,text="score",width=12,height=2).grid(row=i,column=j)

#Frame4-> buttons

root= tk.Tk()
#root.resizable(width=False, height=False)
GUI=Interface(master=root)
root.mainloop()