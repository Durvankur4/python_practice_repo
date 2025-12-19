import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
]

right_symbols = ["÷", "*", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# window setup
window = tk.Tk()
window.resizable(False, False)
window.title("calculator app")

# frame setup
frame = tk.Frame(window)
label = tk.Label(
    frame,
    font=("Arial", 20),
    text="0",
    anchor="e",
    background=color_black,
    foreground=color_white,
    height=4,
    width=8,
)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# A(operator)b
A = "0"
b = None
operator = None


def clear_all():
    global A, operator
    A = "0"
    # B = None
    operator = None


def remove_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def handle_top_symbols(value, current):
    if value == "AC":
        clear_all()
        label.config(text="0")
    elif value == "+/-":
        result = float(current) * -1
        label.config(text=remove_decimal(result))
    elif value == "%":
        num = float(current) / 100
        label.config(text=remove_decimal(num))


def calculate(op, operand_a, operand_b):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "÷": lambda a, b: a / b,
        "*": lambda a, b: a * b,
    }
    return remove_decimal(operations[op](float(operand_a), float(operand_b)))


def handle_equals():
    if A is not None and operator is not None:
        b = label.cget("text")
        result = calculate(operator, A, b)
        label.config(text=result)
    clear_all()


def handle_operator(value):
    global A, operator
    if operator is None:
        A = label.cget("text")
        label.config(text="0")
    operator = value


def handle_number(value):
    current = label.cget("text")
    if current == "0":
        label.config(text=value)
    else:
        label.config(text=current + value)


def button_clicked(value):
    if value in top_symbols:
        handle_top_symbols(value, label.cget("text"))
    elif value == "=":
        handle_equals()
    elif value in "÷*-+":
        handle_operator(value)
    elif value == ".":
        pass
    elif value in "0123456789":
        handle_number(value)


for i in range(row_count):
    for j in range(column_count):
        value = button_values[i][j]
        button = tk.Button(
            frame,
            font=("Arial"),
            text=value,
            height=4,
            width=8,
            command=lambda x=value: button_clicked(x),
        )
        button.grid(row=i + 1, column=j)


frame.pack()
window.mainloop()
