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

        self.Frame1 = tk.Frame(master,width=500,height=700, bg="#708090")
        self.Frame1.grid(row=0,column=0)

        self.Entry1 =tk.Entry(self.Frame1,width=30,bg="blue")
        self.Entry1.grid(row=1,column=0, padx=10, pady=5)
        #self.Entry2 = tk.Entry(self.Frame1, width=30)
        #self.Entry2.grid(row=2, column=0, padx=10, pady=5)

        self.days=[("1",1),("2",2),("3",3)]
        self.RB1= tk.Radiobutton(text=self.days)
        self.RB1.grid(row=2, column=0)


root= tk.Tk()
GUI=Generator_GUI(master=root)
root.mainloop()