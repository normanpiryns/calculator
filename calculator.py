from tkinter import *

f_num, s_num, op, result = None, None, None, None

def backspace():
    field.delete(len(field.get())-1, END)

def clear():
    global result
    field.delete(0, END)
    result = None

def insert(key):
    if field.get() != "0":
        if result != None:
            clear()
        field.insert(len(field.get()), key)
    else:
        backspace()
        field.insert(len(field.get()), key)
    
def operation(key):
    global f_num, s_num, op
    
    if key == "×":
        if field.get() != "":
            f_num = int(field.get())
        clear()
        op = "×"
    elif key == "+":
        if field.get() != "":
            f_num = int(field.get())
        clear()
        op = "+"
    elif key == "-":
        if field.get() != "":
            f_num = int(field.get())
        clear()
        op = "-"
    elif key == "/":
        if field.get() != "":
            f_num = int(field.get())
        clear()
        op = "/"

def equals():
    global f_num, s_num,result

    if op == "+":
        if result != None:
            f_num = result
            clear()
            result = f_num + s_num
        else: 
            s_num = int(field.get())
            clear()
            result = f_num + s_num
    elif op == "-":
        if result != None:
            f_num = result
            clear()
            result = f_num - s_num
        else :
            s_num = int(field.get())
            clear()
            result = f_num - s_num
    elif op == "×":
        if result != None:
            f_num = result
            clear()
            result = f_num * s_num
        else :
            s_num = int(field.get())
            clear()
            result = f_num * s_num
    elif op == "/":
        if result != None:
            f_num = result
            clear()
            result = f_num / s_num
        else :
            s_num = int(field.get())
            clear()
            result = f_num / s_num
    field.insert(0, result)
    

    
    

if __name__ == '__main__':

    root = Tk()
    root.title("Calculator")
    root.resizable(0,0)

    # Field for input / output
    field = Entry(root, width=16, fg="black", bg="#abbab1", font="Verdana 20", justify="right")
    field.grid(row=0,columnspan=4,padx=10,pady=10)

    # Define buttons
    button_0 = Button(root,text="0", relief=GROOVE, padx=10,pady=10, command=lambda: insert(0))
    button_1 = Button(root,text="1", relief=GROOVE, padx=10,pady=10,command=lambda: insert(1))
    button_2 = Button(root,text="2", relief=GROOVE, padx=10,pady=10,command=lambda: insert(2))
    button_3 = Button(root,text="3", relief=GROOVE, padx=10,pady=10,command=lambda: insert(3))
    button_4 = Button(root,text="4", relief=GROOVE, padx=10,pady=10,command=lambda: insert(4))
    button_5 = Button(root,text="5", relief=GROOVE, padx=10,pady=10,command=lambda: insert(5))
    button_6 = Button(root,text="6", relief=GROOVE, padx=10,pady=10,command=lambda: insert(6))
    button_7 = Button(root,text="7", relief=GROOVE, padx=10,pady=10,command=lambda: insert(7))
    button_8 = Button(root,text="8", relief=GROOVE, padx=10,pady=10,command=lambda: insert(8))
    button_9 = Button(root,text="9", relief=GROOVE, padx=10,pady=10,command=lambda: insert(9))
    button_c = Button(root,text="C", relief=GROOVE, padx=10,pady=10,command=clear)
    button_multiply = Button(root,text="×", relief=GROOVE, padx=10,pady=10,command=lambda: operation("×"))
    button_substract = Button(root,text="-", relief=GROOVE, padx=10,pady=10,command=lambda: operation("-"))
    button_equals = Button(root,text="=", relief=GROOVE, padx=10,pady=10,command=equals)
    button_divide = Button(root,text="/", relief=GROOVE, padx=10,pady=10,command=lambda: operation("/"))
    button_add = Button(root,text="+", relief=GROOVE, padx=10,pady=10,command=lambda: operation("+"))
    
    # Place buttons in grid
    button_7.grid(row=1,column=0, sticky="nsew")
    button_8.grid(row=1,column=1, sticky="nsew")
    button_9.grid(row=1,column=2, sticky="nsew")
    button_c.grid(row=1,column=3, sticky="nsew")

    button_4.grid(row=2,column=0, sticky="nsew")
    button_5.grid(row=2,column=1, sticky="nsew")
    button_6.grid(row=2,column=2, sticky="nsew")
    button_multiply.grid(row=2,column=3, sticky="nsew")    

    button_1.grid(row=3,column=0, sticky="nsew")
    button_2.grid(row=3,column=1, sticky="nsew")
    button_3.grid(row=3,column=2, sticky="nsew")
    button_substract.grid(row=3,column=3, sticky="nsew")    

    button_add.grid(row=4,column=0, sticky="nsew")
    button_0.grid(row=4,column=1, sticky="nsew")
    button_divide.grid(row=4,column=2, sticky="nsew")
    button_equals.grid(row=4,column=3, sticky="nsew")    

    
    



    root.mainloop()