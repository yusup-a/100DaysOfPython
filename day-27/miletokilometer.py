from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

user_entry = Entry(width=10)
user_entry.grid(row=0, column=1)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

def calculate():
    num_miles = int(user_entry.get())
    num_kilometers = round(num_miles * 1.609, 3)
    answer_label.config(text=num_kilometers)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()