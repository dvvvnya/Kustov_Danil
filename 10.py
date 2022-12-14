from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk 
from tkinter.messagebox import showinfo

#калькулятор
def calc():
    a = float(txt1.get())
    b = float(txt2.get())
    c = combo.get()
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a / b
    res.configure(text=result)


#выбор
states = [0, 0, 0]
def c1():
    states[0] = 1 - states[0]


def c2():
    states[1] = 1 - states[1]


def c3():
    states[2] = 1 - states[2]


def check():
    if states[0]:
        showinfo(title="Info", message="Вы выбрали первый вариант!")
    elif states[1]:
        showinfo(title="Info", message="Вы выбрали второй вариант!")
    elif states[2]:
        showinfo(title="Info", message="Вы выбрали третий вариант!")

#считывание файла
def file():
    with open('D:\КустовДанилАндреевич_УМ-222_vvod.txt', 'r', encoding='utf-8-sig') as f:
        text.insert('1.0', f.read())

#окно
window = Tk()
window.title('Кустов Данил Андреевич')
window.geometry('400x400')


#вкладки
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Выбор') 
tab_control.add(tab3, text='Текст')

#1
txt1 = Entry(tab1, width=10)
txt1.grid(column=0, row=0)
txt2 = Entry(tab1, width=10)
txt2.grid(column=3, row=0)
combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.current(1) 
combo.grid(column=1, row=0)
but1 = Button(tab1, text='Результат', command=calc)
but1.grid(column=4, row=0)
res = Label(tab1, text=' ')
res.grid(column=5, row=0)

#2
rad1 = Checkbutton(tab2, text='Первый', command=c1)
rad1.grid(column=0,row=0)
rad2 = Checkbutton(tab2, text='Второй', command=c2)
rad2.grid(column=1,row=0)
rad3 = Checkbutton(tab2, text='Третий', command=c3)
rad3.grid(column=2,row=0)
but2 = Button(tab2, text='Выбрать', command=check)
but2.grid(column=1,row=1)

#3
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Загрузить')
menu.add_cascade(label='Файл', menu=new_item, command=file)
window.config(menu=menu)

text = Text(tab3, width=50, height=10, bg="white", fg='blue')
text.pack()


tab_control.pack(expand=1, fill='both')
window.mainloop()

