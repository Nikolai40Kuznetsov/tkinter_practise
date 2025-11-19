from tkinter import *
from tkinter import ttk

amerikans = 0
username = "admin"
password = "12345"

def change_page():
    login_label.pack_forget()
    login_entry.pack_forget()
    password_entry.pack_forget()
    password_label.pack_forget()
    login_button.pack_forget()
    label.pack()  
    button.pack() 

def hate_amerikans():
    global amerikans
    bonus = 1
    amerikans += bonus
    button["text"] = f"Америкосов истреблено: {amerikans}"

def check_data():
    if login_entry.get() == username:
        if password_entry.get() == password:
            change_page()
            exept_label.pack_forget()
        else:
            exept_label.pack()
    else:
            exept_label.pack()

root = Tk()    
ttk.Style().theme_use("classic")
root.title("Приложение на GovnoDvijok")     
root.geometry("400x300") 
root.option_add("*tearOff", FALSE) # выключаем ненужные штрихи во всех меню сразу

file_menu = Menu()
file_menu.add_cascade(label="Сохранить") 
file_menu.add_cascade(label="Сохранить как")
file_menu.add_cascade(label="Открыть")
main_menu = Menu() 
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Изменить")
main_menu.add_cascade(label="Вид")
root.config(menu=main_menu) 

login_label = Label(text="Введите логин") 
login_label.pack()    
login_entry = ttk.Entry() 
login_entry.pack()    
password_label = Label(text="Введите пароль") 
password_label.pack()    
password_entry = ttk.Entry(show='*')
password_entry.pack()
login_button = ttk.Button(text=f"Войти", command=check_data) 
login_button.pack()    
    
exept_label = Label(text="Неверный логин или пароль") 

label = Label(text="Истребитель америкосов")  
button = ttk.Button(text=f"Америкосов истреблено: {amerikans}", command=hate_amerikans)     
root.mainloop()
