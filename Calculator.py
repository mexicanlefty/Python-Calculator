from tkinter import *


root = Tk()
root.title("Bruno's Calculator")

operation_number = 0
current_number_sum = 0
current_number_minus = 0
current_number_division = 0
current_number_multiply = 0

e = Entry(root, width = 50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_click(number, entry):
        current_number = e.get()
        e.delete(0, END)
        e.insert(0, str(current_number) + str(number))


def sum_click():
    global current_number_sum, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_sum = e.get()
        if current_number_sum != "":
            e.delete(0, END)
            operation_number = 1
        else:
            print("please input a number")
            pass
    elif operation_number == 1:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_sum):
            current_number_sum = float(current_number_sum) + float(new_current_number)
            e.insert(0, current_number_sum)
        else:
            current_number_sum = int(current_number_sum) + int(new_current_number)
            e.insert(0, str(current_number_sum))

def minus_click():
    global current_number_minus, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_minus = e.get()
        if current_number_minus != "":
            e.delete(0, END)
            operation_number = 2
        else:
            print("please input a number")
            pass
    elif operation_number == 2:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_minus):
            current_number_minus = float(current_number_minus) - float(new_current_number)
            e.insert(0, current_number_minus)
        else:
            current_number_minus = int(current_number_minus) - int(new_current_number)
            e.insert(0, str(current_number_minus))

def multiply_click():
    global current_number_multiply, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_multiply = e.get()
        if current_number_multiply != "":
            e.delete(0, END)
            operation_number = 3
        else:
            print("please input a number")
            pass
    elif operation_number == 3:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_number_multiply):
            current_number_multiply = float(current_number_multiply) * float(new_current_number)
            e.insert(0, current_number_multiply)
        else:
            current_number_multiply = int(current_number_multiply) * int(new_current_number)
            e.insert(0, str(current_number_multiply))

def division_click():
    global current_number_division, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_division = e.get()
        if current_number_division != "":
            e.delete(0, END)
            operation_number = 4
        else:
            print("please input a number")
            pass
    elif operation_number == 4:
        new_current_number = e.get()
        e.delete(0,END)

        try:
            if "." in str(current_number_division):
                current_number_division = float(current_number_division) / float(new_current_number)
                e.insert(0, current_number_division)
            else:
                current_number_division = int(current_number_division) / int(new_current_number)
                e.insert(0, str(current_number_division))
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

def toPowerof():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 5
    else:
        print("please input a number")
        pass

def positive_negative():
    try:
        current_number = e.get()
        e.delete(0, END)
        if "." in current_number:
            e.insert(0, -(float(current_number)))
        else:
            e.insert(0, -(int(current_number)))
    except:
        print("There is no number")
        pass

def delete():
    try:
        current_number = e.get()
        e.delete(0, END)
        current_number = current_number[:-1]
        e.insert(0, current_number)
    except:
        print("No number to delete")
        pass

def add_point():
    current_number = e.get()
    if "." in current_number:
        print("Number already has a point")
        pass
    else:
        if current_number != "":
            current_number = str(current_number) + str(".")
            e.delete(0,END)
            e.insert(0, current_number)
        else:
            current_number = "0."
            e.insert(0, current_number)

def equals_click():
    global current_number_sum, current_number_minus, current_number_multiply, operation_number
    current_number = e.get()
    e.delete(0, END)
    if operation_number == 0:
        e.insert(0,current_number)
        print("nothing to do")
    elif operation_number == 1:
        if "." in str(current_number_sum):
            e.insert(0, float(current_number_sum) + float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_sum) + int(current_number))
            operation_number = 0
    elif operation_number == 2:
        if "." in current_number_minus:
            e.insert(0, float(current_number_minus) - float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_minus) - int(current_number))
            operation_number = 0
    elif operation_number == 3:
        if "." in current_number_multiply:
            e.insert(0, float(current_number_multiply) * float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_multiply) * int(current_number))
            operation_number = 0
    elif operation_number == 4:

        try:
            if "." in current_number_division:
                e.insert(0, float(current_number_division) / float(current_number))
                operation_number = 0
            else:
                e.insert(0, int(current_number_division) / int(current_number))
                operation_number = 0
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

    elif operation_number == 5:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** int(current_number))
            operation_number = 0

def clear_entry():
    global current_number_sum, current_number_minus, current_number_multiply,current_number_division, operation_number
    operation_number = 0
    current_number_sum = 0
    current_number_multiply = 0
    current_number_minus = 0
    current_number_division = 0
    e.delete(0, END)

button_powerto = Button(root, borderwidth=2, text="xY",padx=36, pady=20, command= lambda: toPowerof()).grid(row=5, column=2)
button_point = Button(root, borderwidth=2, text=".", padx=41, pady=20, command= lambda: add_point()).grid(row=5, column=1)

button_sum = Button(root, borderwidth=2, text="+", padx=37, pady=20, command= lambda: sum_click()).grid(row=3, column=3)
button_equals = Button(root, borderwidth=2, text="=", padx=36, pady=20, command= lambda: equals_click()).grid(row=5, column=3)
button_clear = Button(root, borderwidth=2, text="CE", padx=37, pady=20,command= lambda: clear_entry()).grid(row=4, column=0)

button_minus = Button(root, borderwidth=2, text="-", padx=38, pady=20, command= lambda: minus_click()).grid(row=2, column=3)
button_multiply = Button(root, borderwidth=2, text="X", padx=37, pady=20, command= lambda: multiply_click()).grid(row=1, column=3)
button_negative_positive = Button(root, borderwidth=2, text="+/-", padx=37, pady=20, command= lambda: positive_negative()).grid(row=4, column=2)

button_divide = Button(root, borderwidth=2, text="/", padx=38, pady=20, command= lambda: division_click()).grid(row=4, column=3)
button_del = Button(root, borderwidth=2, text="DEL",fg='red', padx=34, pady=20, command= lambda: delete()).grid(row=5, column=0)
button_0 = Button(root, borderwidth=2, text="0", padx=40, pady=20, command=lambda: button_click(0, e)).grid(row=4, column=1)

button_1 = Button(root, borderwidth=2, text="1", padx=40, pady=20, command=lambda: button_click(1, e)).grid(row=3, column=0)
button_2 = Button(root, borderwidth=2, text="2", padx=40, pady=20, command=lambda: button_click(2, e)).grid(row=3, column=1)
button_3 = Button(root, borderwidth=2, text="3", padx=40, pady=20, command=lambda: button_click(3, e)).grid(row=3, column=2)

button_4 = Button(root, borderwidth=2, text="4", padx=40, pady=20, command=lambda: button_click(4, e)).grid(row=2, column=0)
button_5 = Button(root, borderwidth=2, text="5", padx=40, pady=20, command=lambda: button_click(5, e)).grid(row=2, column=1)
button_6 = Button(root, borderwidth=2, text="6", padx=40, pady=20, command=lambda: button_click(6, e)).grid(row=2, column=2)

button_7 = Button(root, borderwidth=2, text="7", padx=40, pady=20, command=lambda: button_click(7, e)).grid(row=1, column=0)
button_8 = Button(root, borderwidth=2, text="8", padx=40, pady=20, command=lambda: button_click(8, e)).grid(row=1, column=1)
button_9 = Button(root, borderwidth=2, text="9", padx=40, pady=20, command=lambda: button_click(9, e)).grid(row=1,column=2)



root.mainloop()
