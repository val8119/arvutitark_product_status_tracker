import tkinter

window = tkinter.Tk()

window.title("Arvutitark")

window.resizable(0, 0)

window.geometry("200x50")

# window.wm_iconbitmap('Icon.ico')


def callback():
    print("Button clicked!")


text = tkinter.Label(window, text="Product status has changed!")

btn = tkinter.Button(window, text="Click Me", command=callback)
btn.pack()

window.mainloop()
