import tkinter as tk

#TODO:add entry for name
#todo: radiobuttons for choose numer of observations
#todo:progress bar
#todo: button "Generate"
#todo: progress bar

class Generator_GUI:

    def __init__(self, master):
        self.master = master
        master.title("Observations generator")
        master.geometry("500x700+475+50")

        self.Frame1 = tk.LabelFrame(master,text="Supervisor:",width=10,height=20, bg="#708090")
        self.Frame1.grid(row=0,column=0,ipadx=15)
        self.Frame2 = tk.LabelFrame(master,text="Numbers of hourly observations", width=50, height=20, bg="#708090")
        self.Frame2.grid(row=2, column=0,ipadx=8)
        self.Frame3 = tk.LabelFrame(master,text="Numbers of observation days", width=50, height=20, bg="#708090")
        self.Frame3.grid(row=3, column=0,ipadx=34.4)
        self.Frame4 = tk.LabelFrame(master, text="Summary before generation", width=50, height=20, bg="#708090")
        self.Frame4.grid(row=4, column=0,columnspan=3,ipadx=38)
        self.Frame5 = tk.LabelFrame(master, text="Animal name:", width=10, height=20, bg="#708090")
        self.Frame5.grid(row=1, column=0,ipadx=15)

        self.Entry1 =tk.Entry(self.Frame5,width=30)
        self.Entry1.grid(row=0,column=0,sticky="N", padx=10, pady=5)
        self.Entry2 = tk.Entry(self.Frame1, width=30)
        self.Entry2.grid(row=0, column=1, padx=10, pady=5)
# --------------------------------------------------------------------------------
        '''self.in_hour = [
            (1, 1),
            (2, 2),
            (4, 4),
            (6, 6),
            (12,12),
            (60,60)
        ]'''
        self.obs=tk.IntVar()
        self.obs.set(1)
        '''for text,mode in self.in_hour:
            tk.Radiobutton(self.Frame2,text=text,variable=self.obs,value=mode).pack()'''
        self.RB1=tk.Radiobutton(self.Frame2, text="1", variable=self.obs, value=1).grid(row=0,column=0,sticky="E")
        self.RB2=tk.Radiobutton(self.Frame2, text="2", variable=self.obs, value=2).grid(row=0,column=1)
        self.RB3=tk.Radiobutton(self.Frame2, text="4", variable=self.obs, value=4).grid(row=0,column=2)
        self.RB4=tk.Radiobutton(self.Frame2, text="6", variable=self.obs, value=6).grid(row=0,column=3)
        self.RB5=tk.Radiobutton(self.Frame2, text="12", variable=self.obs, value=12).grid(row=0,column=4)
        self.RB6=tk.Radiobutton(self.Frame2, text="60", variable=self.obs, value=60).grid(row=0,column=5)

#--------------------------------------------------------------------------------
        '''self.in_days = [
            (1,1),
            (2,2),
            (3,3)
        ]'''
        self.days=tk.IntVar()
        self.days.set(1)
        '''for text,mode in self.in_days:
            tk.Radiobutton(self.Frame3,text=text,variable=self.days,value=mode).pack()'''
        self.RB7 = tk.Radiobutton(self.Frame3, text="1", variable=self.obs, value=1).grid(row=0, column=0)
        self.RB8 = tk.Radiobutton(self.Frame3, text="2", variable=self.obs, value=2).grid(row=0, column=1)
        self.RB9 = tk.Radiobutton(self.Frame3, text="3", variable=self.obs, value=3).grid(row=0, column=2)
# --------------------------------------------------------------------------------
        def click(value):
            sumFrame=tk.Label(self.Frame4,text=value)
            sumFrame.pack()

        self.Button1=tk.Button(self.Frame4,text="Generate",command=click(self.obs.get()))
        self.Button1.pack()


root= tk.Tk()
GUI=Generator_GUI(master=root)
root.mainloop()