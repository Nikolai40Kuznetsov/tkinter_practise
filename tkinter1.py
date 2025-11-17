from tkinter import *
from tkinter import ttk

amerikans = 0

def hate_amerikans():
    global amerikans
    amerikans += 1
    button["text"] = f"Америкосов истреблено: {amerikans}"

root = Tk()     # создаем корневой объект - окно
ttk.Style().theme_use("classic")
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("400x300")    # устанавливаем размеры окна
label = Label(text="Истребитель америкосов") # создаем текстовую метку
label.pack()    # размещаем метку в окне
button = ttk.Button(text=f"Америкосов истреблено: {amerikans}", command=hate_amerikans) # создаем текстовую метку
button.pack()    # размещаем метку в окне
root.mainloop()