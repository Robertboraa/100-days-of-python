import tkinter

def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f} km")

window = tkinter.Tk()
window.title("Miles to KM")

entry = tkinter.Entry(window)
entry.grid(row=0, column=0, padx=10, pady=10)

tkinter.Label(window, text="miles").grid(row=0, column=1)

tkinter.Button(window, text="Calculate", command=calculate).grid(row=1, column=0)

result_label = tkinter.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2)

window.mainloop()