
import tkinter as tk

# Main window
root = tk.Tk()
root.title("My Colorful Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#101426")

expression = ""

# Calculator display
display = tk.Entry(
    root,
    font=("Arial", 28, "bold"),
    bg="#252E4D",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    justify="right",
    bd=0,
    state="readonly"
)
display.pack(fill="x", padx=20, pady=25, ipady=18)


def update_display():
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, expression)
    display.config(state="readonly")


def press(value):
    global expression

    if expression in ["Invalid expression", "Cannot divide by zero"]:
        expression = ""

    expression += str(value)
    update_display()


def clear():
    global expression
    expression = ""
    update_display()


def backspace():
    global expression
    expression = expression[:-1]
    update_display()


def calculate():
    global expression

    try:
        result = eval(
            expression.replace("×", "*").replace("÷", "/"),
            {"__builtins__": {}},
            {}
        )

        expression = str(result)
        update_display()

    except ZeroDivisionError:
        expression = "Cannot divide by zero"
        update_display()

    except Exception:
        expression = "Invalid expression"
        update_display()


# Button layout
buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

# Button colours
colors = {
    "C": "#E84D78",
    "⌫": "#8055E8",
    "÷": "#8055E8",
    "×": "#8055E8",
    "-": "#8055E8",
    "+": "#8055E8",
    "=": "#1677F2"
}

# Button frame
frame = tk.Frame(root, bg="#101426")
frame.pack(expand=True, fill="both", padx=15, pady=10)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):

        if value == "":
            continue

        color = colors.get(value, "#39466B")

        if value == "C":
            command = clear
        elif value == "⌫":
            command = backspace
        elif value == "=":
            command = calculate
        else:
            command = lambda v=value: press(v)

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 19, "bold"),
            bg=color,
            fg="#FFFFFF",
            activebackground="#A18AFF",
            activeforeground="#FFFFFF",
            bd=0,
            relief="flat",
            command=command,
            cursor="hand2"
        )

        if value == "0":
            button.grid(
                row=r, column=c,
                columnspan=2,
                sticky="nsew",
                padx=5, pady=5
            )
        else:
            button.grid(
                row=r, column=c,
                sticky="nsew",
                padx=5, pady=5
            )

for r in range(5):
    frame.grid_rowconfigure(r, weight=1)

for c in range(4):
    frame.grid_columnconfigure(c, weight=1)

# Run calculator
root.mainloop()
