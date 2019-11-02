import tkinter as tk

root = tk.Tk()
root.title("Графическая программа на Python")
root.geometry("120x175")
root.configure(background='#444')

esche_knopka = tk.Button(text="Зеленая кнопка", bg="green")


ramka_s_knopkami = tk.LabelFrame(root, text="Кнопочки").place(x=0, y=200)


input_value = " "

def btn_press(text):
    global input_value
    if '0' <= text <= '9':
        input_value += text
        pole_vvoda.configure(text=input_value)

pole_vvoda = tk.Label(root, text='', width=10, font="Times 16")
pole_vvoda.grid(row=5, column=1, columnspan=3)

btn1 = tk.Button(
	ramka_s_knopkami,
	text='1',
	font="Times 16",
	command=lambda: btn_press('1')
)
btn2 = tk.Button(
	ramka_s_knopkami,
	text='2',
	font="Times 16",
	command=lambda: btn_press('2')
)
btn3 = tk.Button(
	ramka_s_knopkami,
	text='3',
	font="Times 16",
	command=lambda: btn_press('3')
)
btn4 = tk.Button(
	ramka_s_knopkami,
	text='4',
	font="Times 16",
	command=lambda: btn_press('4')
)
btn5 = tk.Button(
	ramka_s_knopkami,
	text='5',
	font="Times 16",
	command=lambda: btn_press('5')
)
btn6 = tk.Button(
	ramka_s_knopkami,
	text='6',
	font="Times 16",
	command=lambda: btn_press('6')
)
btn7 = tk.Button(
	ramka_s_knopkami,
	text='7',
	font="Times 16",
	command=lambda: btn_press('7')
)
btn8 = tk.Button(
	ramka_s_knopkami,
	text='8',
	font="Times 16",
	command=lambda: btn_press('8')
)
btn9 = tk.Button(
	ramka_s_knopkami,
	text='9',
	font="Times 16",
	command=lambda: btn_press('9')
)

btn0 = tk.Button(
	ramka_s_knopkami,
	text='0',
	font="Times 16",
	command=lambda: btn_press('0')
)

btn1.grid(row=0,column=1, )
btn2.grid(row=0,column=2, )
btn3.grid(row=0,column=3, )
btn4.grid(row=1,column=1, )
btn5.grid(row=1,column=2, )
btn6.grid(row=1,column=3, )
btn7.grid(row=2,column=1, )
btn8.grid(row=2,column=2, )
btn9.grid(row=2,column=3, )
btn0.grid(row=3, column=2, )


root.mainloop()