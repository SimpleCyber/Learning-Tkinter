from tkinter import *

def get_digit(digit):
    # print(digit)
    # fetching the data from the screen
    current = result_label['text']
    new = current +str(digit)
    result_label.config(text=new)


# clear
def clear():
    result_label.config(text='')

# get operator
first_number =second_number =operator =None
def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')


# get answer
def get_result():
    global first_number, operator, second_number
    second_number = int(result_label['text'])
    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator=='-' :
        result_label.config(text=str(first_number-second_number))
    elif operator=='*' :
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number/second_number,2)))






root =Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background='black')

# designer grid method
result_label = Label(root , text='', bg='black',fg='white')
result_label.grid(row=0, column=0,columnspan=5, pady=(40,25), sticky='w')
result_label.config(font=('vardana',30,'bold'))


btn7 =Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('vardana',16))

btn8 =Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('vardana',16))

btn9 =Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('vardana',16))

btnplus =Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2 ,command=lambda :get_operator('+'))
btnplus.grid(row=1, column=3)
btnplus.config(font=('vardana',16))


# row 2

btn4 =Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('vardana',16))

btn5 =Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('vardana',16))

btn6 =Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('vardana',16))

btnsub =Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_operator('-'))
btnsub.grid(row=2, column=3)
btnsub.config(font=('vardana',16))


# row 3
btn1 =Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('vardana',16))

btn2 =Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('vardana',16))

btn2 =Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(3))
btn2.grid(row=3, column=2)
btn2.config(font=('vardana',16))

btnmul =Button(root, text='x', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_operator('*'))
btnmul.grid(row=3, column=3)
btnmul.config(font=('vardana',16))



# row 4
btnclr =Button(root, text='C', bg='#00a65a', fg='white', width=5, height=2, command=lambda :clear())
btnclr.grid(row=4, column=0)
btnclr.config(font=('vardana',16))

btn0 =Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('vardana',16))

btnequal =Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_result())
btnequal.grid(row=4, column=2)
btnequal.config(font=('vardana',16))

btndiv =Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2,command=lambda :get_operator('/'))
btndiv.grid(row=4, column=3)
btndiv.config(font=('vardana',16))


root.mainloop()