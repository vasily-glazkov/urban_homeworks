import tkinter


window = tkinter.Tk()

window.title('Проводник')

window.geometry('400x400')

window.resizable(True, True)
text = tkinter.Label(window, text='Файл', height=5, width=20, background='silver')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл')
button_select.grid(column=1, row=2)
window.mainloop()

