from tkinter import *
import math
from decimal import *

f_num = s_num = op = result = None

def backspace():
    global result
    field.delete(len(field.get())-1, END)
    if field.get() == "" :
        field.insert(0,0) 
    # In case we backspace two-or-more-digit numbers as the result is set, we adapt the result accordingly     
    result = result // 10 if result != None and (result >= 10 or result <= -10) else None


def convert_scientific_notation():
    global result
    if len(field.get()) >= 20:
        result = "{:.6E}".format(result)
        field.delete(0,END)
        field.insert(0, result)


def invert():
    if len(field.get()) == 20 and Decimal(field.get()) > 0:
        return 
    try:
        val = Decimal(field.get()) * (-1)
        clear()
        if val % 1 == 0:
            field.insert(0, int(val))
        else: 
            field.insert(0, val)
    except:
        invalidate("Sign Inverting Error") 

def clear(reset = False):
    global result, op
    if reset == True:
        f_num = None
        s_num = None
        op = None
    toggleFieldBlock(False)
    field.delete(0, END)
    result = None
    



def insert(key):
    if len(field.get()) >= 20:
        return 
    elif key == '.' or key == "-":
        if result != None:
            clear()
        if field.get() == "" and key == ".":
            field.insert(0,0)
        field.insert(len(field.get()), key)
    elif field.get() != "0":
        if result != None:
            clear()
        field.insert(len(field.get()), key)
    else:
        field.delete(len(field.get())-1, END)
        field.insert(len(field.get()), key)
    
def operation(key):
    global f_num, s_num, op
    
    try:
        if key == "×":
            if field.get() != "":
                f_num = Decimal(field.get())
            clear()
            op = "×"
        elif key == "+":
            if field.get() != "":
                f_num = Decimal(field.get())
            clear()
            op = "+"
        elif key == "-":
            if field.get() != "":
                f_num = Decimal(field.get())
            clear()
            op = "-"
        elif key == "/":
            if field.get() != "":
                f_num = Decimal(field.get())
            clear()
            op = "/"
    except:
        invalidate("Operation Error")


def equals():

    global f_num, s_num,result

    try:
        if op == "+":
            if result != None:
                f_num = Decimal(result)
                clear()
                result = f_num + s_num
            else: 
                s_num = Decimal(field.get())
                clear()
                result = f_num + s_num
        elif op == "-":
            if result != None:
                f_num = Decimal(result)
                clear()
                result = f_num - s_num
            else :
                s_num = Decimal(field.get())
                clear()
                result = f_num - s_num
        elif op == "×":
            if result != None:
                f_num = Decimal(result)
                clear()
                result = f_num * s_num
            else :
                s_num = Decimal(field.get())
                clear()
                result = f_num * s_num
        elif op == "/":
            if result != None:
                f_num = Decimal(result)
                clear()
                result = f_num / s_num
            else :
                s_num = Decimal(field.get())
                clear()
                result = f_num / s_num

        # For the Decimal points. Ex.: 4.0 -> 4
        if result % 1 == 0:
            field.insert(0, int(result))
        else:
            field.insert(0, result)

        convert_scientific_notation()
    except:
        invalidate("Invalid Calculation")

def square_root():
    try:
        result = math.sqrt(Decimal(field.get()))
        clear()
        if result % 1 == 0:
            field.insert(0, int(result))
        else:
            field.insert(0, result)
    except:
        invalidate("Square Root Error")


    
def invalidate(error):
    clear() 
    field.insert(0,error)
    toggleFieldBlock(True)
    result = f_num = s_num = None    

    

def toggleFieldBlock(block):
    if block == True:
        field.config(state='disabled')
    else:
        field.config(state='normal')
    

if __name__ == '__main__':

    root = Tk()
    root.title("Calculator")
    root.resizable(0,0)

    # Field for input / output  /width=16
    field = Entry(root, width=20, fg="black", bg="#abbab1", font="Verdana 20", justify="right")
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
    button_c = Button(root,text="C", relief=GROOVE, padx=10,pady=10,command=lambda: clear(True))
    button_multiply = Button(root,text="×", relief=GROOVE, padx=10,pady=10,command=lambda: operation("×"))
    button_substract = Button(root,text="-", relief=GROOVE, padx=10,pady=10,command=lambda: operation("-"))
    button_equals = Button(root,text="=", relief=GROOVE, padx=10,pady=10,command=equals)
    button_divide = Button(root,text="/", relief=GROOVE, padx=10,pady=10,command=lambda: operation("/"))
    button_add = Button(root,text="+", relief=GROOVE, padx=10,pady=10,command=lambda: operation("+"))
    button_sign = Button(root,text="+/-", relief=GROOVE, padx=10,pady=10,command=lambda: invert())
    button_decimal = Button(root,text=".", relief=GROOVE, padx=10, pady=10,command=lambda: insert("."))
    button_square_root = Button(root,text="√x", relief=GROOVE, padx=10, pady=10,command=lambda: square_root())
    button_backspace = Button(root,text="⌫", relief=GROOVE, padx=10, pady=10,command=lambda: backspace())
    
    
    # Place buttons in grid
    button_backspace.grid(row=1,column=0, sticky="nsew")
    button_c.grid(row=1,column=1, sticky="nsew")
    button_square_root.grid(row=1,column=2, sticky="nsew")
    button_divide.grid(row=1,column=3, sticky="nsew")

    button_7.grid(row=2,column=0, sticky="nsew")
    button_8.grid(row=2,column=1, sticky="nsew")
    button_9.grid(row=2,column=2, sticky="nsew")
    button_multiply.grid(row=2,column=3, sticky="nsew")    

    button_4.grid(row=3,column=0, sticky="nsew")
    button_5.grid(row=3,column=1, sticky="nsew")
    button_6.grid(row=3,column=2, sticky="nsew")
    button_substract.grid(row=3,column=3, sticky="nsew")    

    button_1.grid(row=4,column=0, sticky="nsew")
    button_2.grid(row=4,column=1, sticky="nsew")
    button_3.grid(row=4,column=2, sticky="nsew")
    button_add.grid(row=4,column=3, sticky="nsew")    

    button_sign.grid(row=5,column=0, sticky="nsew")
    button_0.grid(row=5,column=1, sticky="nsew")
    button_decimal.grid(row=5,column=2, sticky="nsew")
    button_equals.grid(row=5,column=3, sticky="nsew")    


    # keyboard inputs
    
    root.bind("0", lambda _: insert(0))
    root.bind("1", lambda _: insert(1))
    root.bind("2", lambda _: insert(2))
    root.bind("3", lambda _: insert(3))
    root.bind("4", lambda _: insert(4))
    root.bind("5", lambda _: insert(5))
    root.bind("6", lambda _: insert(6))
    root.bind("7", lambda _: insert(7))
    root.bind("8", lambda _: insert(8))
    root.bind("9", lambda _: insert(9))

    root.bind("+", lambda _:operation("+"))
    root.bind("-", lambda _:operation("-"))
    root.bind("*", lambda _:operation("×"))
    root.bind("/", lambda _:operation("/"))

    root.bind("<Return>", lambda _: equals())
    root.bind(".", lambda _: insert("."))
    root.bind("<BackSpace>", lambda _: backspace())
    root.bind("<Delete>", lambda _: clear(True))
    root.bind("<Escape>", lambda _: root.destroy())

    # Disables the ability to click in the Entry
    field.bind("<1>", lambda _: "break")
    

    root.mainloop()

    
        
    



