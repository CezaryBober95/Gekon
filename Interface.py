import tkinter as tk

#todo: connect all class here
#todo: add plots, point board,make buttons to start observation

class Application:

    def __init__(self, master):
        self.master = master
        master.title("The Gekon Project")
        width_value=master.winfo_screenwidth()
        height_value=master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width_value,height_value))

        self.Frame1 = tk.Frame(master,width=width_value/2,height=height_value/2, bg="blue")
        self.Frame1.grid(row=0, column=0)
        #Label1 =tk.Label(self.Frame1, text="Okienko 1")
        #Label1.pack()


        self.Frame2 = tk.Frame(master,width=width_value/2,height=height_value/2, bg="red")
        self.Frame2.grid(row=0, column=1)


        self.Frame3 = tk.Frame(master,width=width_value/2,height=height_value/2, bg="green")
        self.Frame3.grid(row=1, column=0)


        self.Frame4 = tk.Frame(master,width=width_value/2,height=height_value/2, bg="yellow")
        self.Frame4.grid(row=1, column=1)



root= tk.Tk()
GUI=Application(master=root)
root.mainloop()