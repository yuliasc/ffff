#Калькулятор
from tkinter import*
root= Tk()
root.geometry(f"340x240")
root.config(bg='#8c8c8c')
root.title('Калькулятор')
root.resizable(width=False,height=False)
photo = PhotoImage(file="C:/Users/Юлія/PycharmProjects/pythonProject7/images.png")
root.iconphoto(False,photo)
def oper(sym):
    b = pole.get()
    pole.delete(0, END)
    if sym == "/" and b[-1] == "0":
        pole.insert(0, "Ділити на нуль не можна!")
    elif sym == "=":
        if "/" in b and b[-1] == "0":
            pole.insert(0, "Ділити на нуль не можна!")
        else:
            result = str(eval(b))
            pole.insert(0, result)
    else:
        pole.insert(0, str(eval(b)) + sym)


def kalc(sym):
    if sym == 'CE':
        pole.delete(0, END)
        pole.insert(0, 0)
    elif sym == "<-":
        pole.delete(len(pole.get()) - 1)
        if pole.get() == "":
            pole.insert(0, 0)
    elif sym == "." and pole.get().count(".") == 0:
        pole.insert(END, ".")
    elif sym in "+-*/":
        s = pole.get()
        if s[-1] in "+-*/":
            s = s[0:-1] + sym
            pole.delete(0, END)
            pole.insert(0, s)
        elif "+" in s or "-" in s or "*" in s or "/":
            oper(sym)
        else:
            s = s + sym
            pole.delete(0, END)
            pole.insert(0, s)

    elif sym == "=":
        oper(sym)
    else:
        if pole.get() == "0":
            pole.delete(0, END)
        pole.insert(END, sym)
        if sym in "0123456789":
            pole.insert(END, sym)

for i in range(4):
    root.grid_columnconfigure(i,minsize=80)
pole = Entry(root, font=("None", 16),bd=2, bg="#ffb3d1", fg="#000000")
pole.grid(column=0, row=0, columnspan=4,stick="we" )
pole.insert(0,"0")
k_n = Button(root, font=("None", 16), bd=2, bg="#ffcce0", fg="#000000", text="+", compound="center", command=lambda: kalc("+"))
k_n.grid(row=1, column=0, stick="we")
k_n1 = Button(root, font=("None", 16), bd=2, bg="#ffcce0", fg="#000000",text="-", compound="center", command=lambda: kalc("-"))
k_n1.grid(row=1, column=1, stick="we")

k_n2 = Button(root, font=("None", 16),bd=2, bg="#ffcce0", fg="#000000", text="*", compound="center", command=lambda: kalc("*"))
k_n2.grid(row=1, column=2, stick="we")

k_n3 = Button(root, font=("None", 16),bd=2, bg="#ffcce0", fg="#000000", text="/", compound="center", command=lambda: kalc("/"))
k_n3.grid(row=1, column=3, stick="we")

k_n8 = Button(root, font=("None", 16), bd=2, bg="#ffe6ff", fg="#000000",text="1", compound="center", command=lambda: kalc("1"))
k_n8.grid(row=2, column=0, stick="we")

k_n9 = Button(root, font=("None", 16),bd=2, bg="#ffe6ff", fg="#000000", text="2", compound="center", command=lambda: kalc("2"))
k_n9.grid(row=2, column=1, stick="we")

k_n10 = Button(root, font=("None", 16), bd=2, bg="#ffe6ff", fg="#000000",text="3", compound="center", command=lambda: kalc("3"))
k_n10.grid(row=2, column=2, stick="we")

k_n11 = Button(root, font=("None", 16), bd=2, bg="#f5d6eb", fg="#000000",text="CE", compound="center", command=lambda: kalc("CE"))
k_n11.grid(row=2, column=3, stick="we")

k_n12 = Button(root, font=("None", 16),bd=2, bg="#ffe6ff", fg="#000000", text="4", compound="center", command=lambda: kalc("4"))
k_n12.grid(row=3, column=0, stick="we")

k_n13 = Button(root, font=("None", 16),bd=2, bg="#ffe6ff", fg="#000000", text="5", compound="center", command=lambda: kalc("5"))
k_n13.grid(row=3, column=1, stick="we")

k_n14 = Button(root, font=("None", 16), bd=2, bg="#ffe6ff", fg="#000000",text="6", compound="center", command=lambda: kalc("6"))
k_n14.grid(row=3, column=2, stick="we")

k_n15 = Button(root, font=("None", 16),bd=2, bg="#f5d6eb", fg="#000000", text="<-", compound="center", command=lambda: kalc("<-"))
k_n15.grid(row=3, column=3, stick="we")

k_n16 = Button(root, font=("None", 16),bd=2, bg="#ffe6ff", fg="#000000", text="7", compound="center", command=lambda: kalc("7"))
k_n16.grid(row=4, column=0, stick="we")

k_n17 = Button(root, font=("None", 16),bd=2, bg="#ffe6ff", fg="#000000", text="8", compound="center", command=lambda: kalc("8"))
k_n17.grid(row=4, column=1, stick="we")

k_n18 = Button(root, font=("None", 16), bd=2, bg="#ffe6ff", fg="#000000",text="9", compound="center", command=lambda: kalc("9"))
k_n18.grid(row=4, column=2, stick="we")

k_n19 = Button(root, font=("None", 16), bd=2,bg="#f5d6eb", fg="#000000",text="=", compound="center", command=lambda: kalc("="))
k_n19.grid(row=4, column=3, stick="we")

k_n20 = Button(root, font=("None", 16), bd=2, bg="#ffe6ff", fg="#000000", text="0", compound="center", command=lambda: kalc("0"))
k_n20.grid(row=5, column=1, ipadx=24, ipady=2)

root.mainloop()

