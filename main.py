def cal():
    a = S1.get()
    b = S2.get()
    c = E1.get()
    c = int(c)
    if a == "Euro":
        if b == "Dollar":
            c = c * 1.11
        if b == "Dinar":
            c = c * 0.34
        if b == "Rupees":
            c = c * 92.04
        if b == "Japanese Yan":
            c = c * 115.91
    if a == "Dollar":
        if b == "Euro":
            c = c * 0.90
        if b == "Dinar":
            c = c * 0.31
        if b == "Rupees":
            c = c * 83.25
        if b == "Japanese Yan":
            c = c * 141.03
    if a == "Dinar":
        if b == "Dollar":
            c = c * 3.25
        if b == "Euro":
            c = c * 2.94
        if b == "Rupees":
            c = c * 270.92
        if b == "Japanese Yan":
            c = c * 458.95
    if a == "Rupees":
        if b == "Dollar":
            c = c * 0.012
        if b == "Dinar":
            c = c * 0.0037
        if b == "Euro":
            c = c * 0.011
        if b == "Japanese Yan":
            c = c * 1.70
    if a == "Japanese Yan":
        if b == "Dollar":
            c = c * 0.0071
        if b == "Dinar":
            c = c * 0.0022
        if b == "Rupees":
            c = c * 0.59
        if b == "Euro":
            c = c * 0.0064
    c = str(c)
    L6.config(text=c)


def cle():
    S1.delete(0, END)
    S2.delete(0, END)
    E1.delete(0, END)
    L6.config(text="           ")
    S1.focus()


from tkinter import *
from tkinter import ttk

con = Tk()
con.geometry("400x300+500+150")
con.title("Currency convertor")
con["background"] = "Light pink"
Currency = ("Euro", "Dollar", "Dinar", "Japanese Yan", "Rupees")
S1 = ttk.Combobox(values=Currency, font=("Times", 12))
S2 = ttk.Combobox(values=Currency, font=("Times", 12))
L1 = Label(text="Currency Convertor", font=("Times", 16), bg="Light pink")
L2 = Label(text="Select the input currency ", font=("Times", 13), bg="Light pink")
L3 = Label(text="Enter the amount", font=("Times", 13), bg="Light pink")
L4 = Label(text="Select the output currency ", font=("Times", 13), bg="Light pink")
L5 = Label(text="Converted amount ", font=("Times", 13), bg="Light pink")
L6 = Label(text="                                       ")
B1 = Button(text="Convert", font=("Times", 10), activebackground="Sky blue", command=cal)
B2 = Button(text="Clear", font=("Times", 10), activebackground="Sky blue", command=cle)
E1 = Entry(font=("Times", 10))
L1.place(x=130, y=5)
L2.place(x=5, y=50)
L3.place(x=5, y=90)
L4.place(x=5, y=130)
L5.place(x=5, y=180)
L6.place(x=200, y=180)
E1.place(x=200, y=90)
S1.place(x=200, y=50)
S2.place(x=200, y=130)
B1.place(x=10, y=220)
B2.place(x=80, y=220)
con.mainloop()
