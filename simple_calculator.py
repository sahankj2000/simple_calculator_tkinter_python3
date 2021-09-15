'''
Author : Sahan KJ
Mail : sahan.k.j2000@gmail.com
Date : 16/09/2021
'''

from tkinter import *
from tkinter.font import Font
import re

root = Tk()
root.title('Simple Calculator')

e = Entry(root,font=Font(size=30),justify='right',borderwidth=5)
e.grid(row=0,column=0,columnspan=3,sticky='nsew',padx=2,pady=2)
e.focus_set()

def insert(string,index,key):
    return string[:index] + key + string[index:]

def remove(string,index):
    return string[:index]+string[index+1:]

def convert(x):
    x = re.sub('√+','√',x)
    x = re.sub('\++','+',x)
    x = re.sub('-+','-',x)
    x = re.sub('/+','/',x)
    x = re.sub('\*+','*',x)
    x = re.sub('x+','*',x)
    x = re.sub('÷+','/',x)
    x = re.sub('\^+','^',x)
    x = x.replace('x','*')
    x = x.replace('÷','/')
    x = x.replace('^','**')
    x = str(x)
    for i in range(len(x)):
        if x[i] == '√':
            if x[i+1].isdigit():
                temp = i+1
                while temp+1<len(x) and (x[temp+1].isdigit() or x[temp+1] == '.'):
                    temp +=1
                x = insert(x,temp+1,'**0.5')
            elif x[i+1] == '(':
                count = 0
                for j in range(i+1,len(x)):
                    if x[j] == '(':
                        count +=1
                    elif x[j] == ')':
                        count -= 1
                    if count ==0:
                        x = insert(x,j+1,'**0.5')
                        break
                if count!=0:
                    return 'Error'
            else:
                return 'Error'
            x = remove(x,i)
    return x

def setOut(x):
    e.insert(END,str(x))

global cl
cl = False

def getcl():
    return cl

def click(x):
    if getcl():
        clear()
        global cl
        cl = False
    setOut(x)

def delete():
    disp = e.get()[:-1]
    e.delete(0, END)
    e.insert(0,disp)

def clear():
    e.delete(0, END)
    disp = ''

chars = ['0','1','2','3','4','5','6','7','8','9','+','-','x','√','/','÷','*','^','(',')','=','.']

def getString():
    return e.get()

def equate():
    string = getString()
    temp = True
    for each in string:
        if each not in chars:
            clear()
            setOut('CharacterError')
            temp = False
    if temp:
        clear()
        tt = True
        for i in range(1,len(string)):
            if string[i] == '√' and string[i-1].isdigit():
                tt = False
        con = convert(string)
        if tt and con != 'Error':
            try:
                out = eval(con)
                setOut(out)
            except ZeroDivisionError as e:
                setOut('ZeroDivisionError')
            except SyntaxError as s:
                setOut('SyntaxError')
            except Exception:
                setOut('SyntaxError')
        else:
            setOut('SyntaxError')
    global cl
    cl = True

# Defining buttons
button_1 = Button(root,text='1',padx=40,command=lambda:click(1),font=Font(size=40),borderwidth=3)
button_2 = Button(root,text='2',padx=40,command=lambda:click(2),font=Font(size=40),borderwidth=3)
button_3 = Button(root,text='3',padx=40,command=lambda:click(3),font=Font(size=40),borderwidth=3)
button_4 = Button(root,text='4',command=lambda:click(4),font=Font(size=40),borderwidth=3)
button_5 = Button(root,text='5',command=lambda:click(5),font=Font(size=40),borderwidth=3)
button_6 = Button(root,text='6',command=lambda:click(6),font=Font(size=40),borderwidth=3)
button_7 = Button(root,text='7',command=lambda:click(7),font=Font(size=40),borderwidth=3)
button_8 = Button(root,text='8',command=lambda:click(8),font=Font(size=40),borderwidth=3)
button_9 = Button(root,text='9',command=lambda:click(9),font=Font(size=40),borderwidth=3)
button_0 = Button(root,text='0',command=lambda:click(0),font=Font(size=40),borderwidth=3)
button_add = Button(root,text='+',command=lambda:click('+'),font=Font(size=40),borderwidth=3)
button_sub = Button(root,text='-',padx=40,command=lambda:click('-'),font=Font(size=40),borderwidth=3)
button_mul = Button(root,text='x',command=lambda:click('x'),font=Font(size=40),borderwidth=3)
button_div = Button(root,text='÷',command=lambda:click('÷'),font=Font(size=40),borderwidth=3)
button_equ = Button(root,text='=',command=equate,font=Font(size=40),borderwidth=3)
button_dot = Button(root,text='.',command=lambda:click('.'),font=Font(size=40),borderwidth=3)
button_ob = Button(root,text='(',padx=40,command=lambda:click('('),font=Font(size=40),borderwidth=3)
button_cb = Button(root,text=')',command=lambda:click(')'),font=Font(size=40),borderwidth=3)
button_power = Button(root,text='^',command=lambda:click('^'),font=Font(size=40),borderwidth=3)
button_root = Button(root,text='√',command=lambda:click('√'),font=Font(size=40),borderwidth=3)
button_clear = Button(root,text='C',command=clear,font=Font(size=40),borderwidth=3)
button_del = Button(root,text='←',command=delete,font=Font(size=40),borderwidth=3)

# Adding buttons to grid
button_1.grid(row=3,column=0,sticky='nsew',padx=2,pady=2)
button_2.grid(row=3,column=1,sticky='nsew',padx=2,pady=2)
button_3.grid(row=3,column=2,sticky='nsew',padx=2,pady=2)
button_sub.grid(row=3,column=3,sticky='nsew',padx=2,pady=2)
button_ob.grid(row=3,column=4,sticky='nsew',padx=2,pady=2)

button_4.grid(row=2,column=0,sticky='nsew',padx=2,pady=2)
button_5.grid(row=2,column=1,sticky='nsew',padx=2,pady=2)
button_6.grid(row=2,column=2,sticky='nsew',padx=2,pady=2)
button_mul.grid(row=2,column=3,sticky='nsew',padx=2,pady=2)
button_root.grid(row=2,column=4,sticky='nsew',padx=2,pady=2)

button_7.grid(row=1,column=0,sticky='nsew',padx=2,pady=2)
button_8.grid(row=1,column=1,sticky='nsew',padx=2,pady=2)
button_9.grid(row=1,column=2,sticky='nsew',padx=2,pady=2)
button_div.grid(row=1,column=3,sticky='nsew',padx=2,pady=2)
button_power.grid(row=1,column=4,sticky='nsew',padx=2,pady=2)

button_0.grid(row=4,column=1,sticky='nsew',padx=2,pady=2)
button_dot.grid(row=4,column=0,sticky='nsew',padx=2,pady=2)
button_equ.grid(row=4,column=2,sticky='nsew',padx=2,pady=2)
button_add.grid(row=4,column=3,sticky='nsew',padx=2,pady=2)
button_cb.grid(row=4,column=4,sticky='nsew',padx=2,pady=2)

button_del.grid(row=0,column=3,sticky='nsew',padx=2,pady=2)
button_clear.grid(row=0,column=4,sticky='nsew',padx=2,pady=2)

root.bind('<Return>',lambda event: equate())
root.bind('<Escape>',lambda event: clear())
photo = PhotoImage(file = 'icon.png')
root.iconphoto(False, photo)
root.resizable(False,False)
root.mainloop()