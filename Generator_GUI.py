import tkinter as tk
import Generator

#todo:progress bar
#todo: progress bar

class Generator_GUI:

    def __init__(self, master):
        self.master = master
        master.title("Generator")
        master.geometry("238x326+475+50")

        self.Frame1 = tk.LabelFrame(master,text="Supervisor:",width=10,height=20, bg="#708090")
        self.Frame1.grid(row=0,column=0,ipadx=15)
        self.Frame2 = tk.LabelFrame(master,text="Numbers of hourly observations", width=50, height=20, bg="#708090")
        self.Frame2.grid(row=2, column=0,ipadx=8)
        self.Frame3 = tk.LabelFrame(master,text="Numbers of observation days", width=50, height=20, bg="#708090")
        self.Frame3.grid(row=3, column=0,ipadx=35)
        self.Frame4 = tk.LabelFrame(master, text="Summary before generation", width=50, height=20, bg="#708090")
        self.Frame4.grid(row=4, column=0,columnspan=3,ipadx=38)
        self.Frame5 = tk.LabelFrame(master, text="Animal name:", width=10, height=20, bg="#708090")
        self.Frame5.grid(row=1, column=0,ipadx=15)
        self.Frame6 = tk.LabelFrame(master, width=10, height=20, bg="#708090")
        self.Frame6.grid(row=5, column=0, ipadx=15)

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
        #self.obs.set(1)
        '''for text,mode in self.in_hour:
            tk.Radiobutton(self.Frame2,text=text,variable=self.obs,value=mode).pack()'''
        self.RB1=tk.Radiobutton(self.Frame2, text="1",indicatoron = 0,width=4, variable=self.obs, value=1).grid(row=0,column=0,sticky="E")
        self.RB2=tk.Radiobutton(self.Frame2, text="2",indicatoron = 0,width=4, variable=self.obs, value=2).grid(row=0,column=1)
        self.RB3=tk.Radiobutton(self.Frame2, text="4",indicatoron = 0,width=4, variable=self.obs, value=4).grid(row=0,column=2)
        self.RB4=tk.Radiobutton(self.Frame2, text="6",indicatoron = 0,width=4, variable=self.obs, value=6).grid(row=0,column=3)
        self.RB5=tk.Radiobutton(self.Frame2, text="12",indicatoron = 0,width=4, variable=self.obs, value=12).grid(row=0,column=4)
        self.RB6=tk.Radiobutton(self.Frame2, text="60",indicatoron = 0,width=3, variable=self.obs, value=60).grid(row=0,column=5)

#--------------------------------------------------------------------------------
        '''self.in_days = [
            (1,1),
            (2,2),
            (3,3)
        ]'''
        self.days=tk.IntVar()
        #self.days.set(1)
        '''for text,mode in self.in_days:
            tk.Radiobutton(self.Frame3,text=text,variable=self.days,value=mode).pack()'''
        self.RB7 = tk.Radiobutton(self.Frame3, text="1",indicatoron = 0,width=6, variable=self.days, value=24).grid(row=0, column=0)
        self.RB8 = tk.Radiobutton(self.Frame3, text="2",indicatoron = 0,width=6, variable=self.days, value=48).grid(row=0, column=1)
        self.RB9 = tk.Radiobutton(self.Frame3, text="3",indicatoron = 0,width=6, variable=self.days, value=72).grid(row=0, column=2)
# --------------------------------------------------------------------------------
        def click(value,value1,value2):
            sumFrame1=tk.Label(self.Frame4,text=value)
            sumFrame1.pack(side=tk.LEFT,padx=10, pady=10)
            sumFrame2=tk.Label(self.Frame4, text=value1)
            sumFrame2.pack(side=tk.LEFT,padx=10, pady=10)
            sumFrame3=tk.Label(self.Frame4, text=value2)
            sumFrame3.pack(side=tk.LEFT,padx=10, pady=10)
            #sumFrame4=tk.Label(self.Frame4, text=value3)
            #sumFrame4.pack(side=tk.LEFT,padx=10, pady=10)
            return (value,value1,value2)

        self.Button1=tk.Button(self.Frame4,text="Summary",bg="yellow",command=lambda :click(self.Entry2.get(),self.Entry1.get(),self.obs.get()*self.days.get()))
        self.Button1.pack()
        self.ButtonStart = tk.Button(self.Frame6, text="Generate",bg="green")
        self.ButtonStart.pack(side=tk.TOP,padx=73)
        self.ButtonStart = tk.Button(self.Frame6, text="Finish",bg="red",fg="black",command=root.destroy)
        self.ButtonStart.pack(side=tk.BOTTOM,padx=73)


root= tk.Tk()
root.resizable(width=False, height=False)
GUI=Generator_GUI(master=root)
root.mainloop()