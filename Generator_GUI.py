import tkinter as tk

#TODO:add entry for name
#todo: radiobuttons for choose numer of observations
#todo:progress bar
#todo: button "Generate"

class Generator:

    def __init__(self, master):
        self.master = master
        master.title("Observations generator")
        width_value=master.winfo_screenwidth()
        height_value=master.winfo_screenheight()
        #master.geometry("%dx%d+0+0" % (width_value,height_value))
        master.geometry("500x700+400+50")

        self.Frame1 = tk.Frame(master,width=500,height=700, bg="#708090")
        self.Frame1.grid(row=0, column=0)

root= tk.Tk()
GUI=Generator(master=root)
root.mainloop()