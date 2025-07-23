from tkinter import  *
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

my_label = Label(text= "I am a Label", font= ("Arial", 24, "bold"))
my_label.grid(row=0, column= 0)

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column= 1)
button.config(padx=20, pady= 20)


button2 = Button(text="New Button", command=button_clicked)
button2.grid(row=0, column= 2)

input = Entry(width=10)
input.grid(row=2, column= 3)

window.mainloop()