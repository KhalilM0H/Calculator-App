import tkinter as tk

memory = []

def calculate(): 
    try: 
        expression = entry.get()
        result = eval(expression) 
        memory.append(result)
        output_label.config(text=f"Result: {round(result, 3)}") 
    except Exception as e: 
        output_label.config(text=f"Error: Invalid Syntax. Try again.")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.pack()

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

output_label = tk.Label(root, text="Result:")
output_label.pack()

root.mainloop()
