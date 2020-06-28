import tkinter as tk

#TODO:add entry for name
#todo: radiobuttons for choose numer of observations
#todo:progress bar
#todo: button "Generate"

class Generator_GUI:

    def __init__(self, master):
        self.master = master
        master.title("Observations generator")
        #width_value=master.winfo_screenwidth()
        #height_value=master.winfo_screenheight()
        #master.geometry("%dx%d+0+0" % (width_value,height_value))
        master.geometry("500x700+475+50")
        #master.geometry("500x700+0+0")

        self.Frame1 = tk.Frame(master,width=500,height=200, bg="#708090")
        self.Frame1.grid(row=0,column=0)
        self.Frame2 = tk.Frame(master, width=500, height=200, bg="green")
        self.Frame2.grid(row=1, column=0)
        self.Frame3 = tk.Frame(master, width=500, height=200, bg="blue")
        self.Frame3.grid(row=2, column=1)

        self.Entry1 =tk.Entry(self.Frame1,text="Nazwa osobnika: ",width=30)
        self.Entry1.grid(row=1,column=2, padx=10, pady=5)
        #self.Entry2 = tk.Entry(self.Frame1, width=30)
        #self.Entry2.grid(row=2, column=0, padx=10, pady=5)

        self.in_hour = [
            (1, "1"),
            (2, 2),
            (4, 4),
            (6, 6),
            (12,12),
            (60,60),
        ]
        self.pizza=tk.StringVar()
        self.pizza.set("Wygenerujesz: ")

        for text,mode in self.in_hour:
            tk.Radiobutton(self.Frame2,text=text,variable=self.pizza,value=mode).pack()

        def click(value):
            sumFrame=tk.Label(self.Frame3,text=value)
            sumFrame.pack()

        self.Button1=tk.Button(self.Frame3,text="Generate",command=click(self.pizza.get()))
        self.Button1.pack()


root= tk.Tk()
GUI=Generator_GUI(master=root)
root.mainloop()