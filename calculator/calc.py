import tkinter as tk

# Create the main window
window = tk.Tk()
window.title('Calculator')
window.geometry("300x350")
window.resizable(False, False)

# Create entry fields
num1_entry = tk.Entry(window, width=20)
num1_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

num2_entry = tk.Entry(window, width=20)
num2_entry.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

result_entry = tk.Entry(window, width=20, state='readonly')
result_entry.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Create labels
num1_label = tk.Label(window, text="Введите первое число:")
num1_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

num2_label = tk.Label(window, text="Введите второе число:")
num2_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
button_add = tk.Button(window, text='+', width="2", height="2", command=lambda: calculate('+'))
button_add.grid(row=4, column=0, padx=5, pady=5)

button_sub = tk.Button(window, text='-', width="2", height="2", command=lambda: calculate('-'))
button_sub.grid(row=4, column=1, padx=5, pady=5)

button_mult = tk.Button(window, text='x', width=5, command=lambda: calculate('*'))
button_mult.grid(row=4, column=2, padx=5, pady=5)

button_div = tk.Button(window, text='/', width="2", height="2", command=lambda: calculate('/'))
button_div.grid(row=4, column=3, padx=5, pady=5)


def calculate(operator):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
        result_entry.config(state='readonly')
        num1_entry.delete(0, tk.END)  # Clear the first number entry
        num2_entry.delete(0, tk.END)  # Clear the second number entry
    except ValueError:
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Неверный ввод")
        result_entry.config(state='readonly')
    except ZeroDivisionError:
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Нельзя делить на ноль")
        result_entry.config(state='readonly')


window.mainloop()
