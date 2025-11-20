from tkinter import *
from tkinter import ttk

def rename():
    if play_button["text"] == "Пуск":
        play_button["text"] = "Пауза"
    elif play_button["text"] == "Пауза":
        play_button["text"] = "Пуск"

def summon_playlist():
    playlist = Tk()
    playlist.title("Плейлист")
    playlist.geometry("200x600")

def set_transparent():
    root.attributes("-alpha", time_slider.get() / 100)

def summon_settings():
    settings = Tk()
    settings.title("Настройки")
    settings.geometry("200x200")
    name_label = Label(settings, text="Прозрачность")  
    name_label.grid(row=0, column=0)
    time_slider = Scale(settings, orient=HORIZONTAL, length=100, from_=1.0, to=100.0, command=set_transparent) 
    time_slider.grid(row=1, column=0)

root = Tk()    
ttk.Style().theme_use("classic")
root.title("Плеер на GovnoDvijok") 
root.option_add("*tearOff", FALSE) # выключаем ненужные штрихи во всех меню сразу
root.geometry("800x600") 
img_label = Label(text="Здесь могла быть ваша картинка")  
img_label.grid(row=0, column=2)
singer_label = Label(text="Исполнитель")  
singer_label.grid(row=1, column=2)
name_label = Label(text="Название")  
name_label.grid(row=2, column=2)
time_slider = Scale(orient=HORIZONTAL, length=100, from_=1.0, to=100.0) 
time_slider.grid(row=3, column=2)
list_button = Button(text="Плейлист", command=summon_playlist)  
list_button.grid(row=4, column=0)
back_button = Button(text="Предыдущая песня")  
back_button.grid(row=4, column=1)
play_button = Button(text="Пуск", command=rename)
print(play_button["text"])  
play_button.grid(row=4, column=2)
next_button = Button(text="Следующая песня")  
next_button.grid(row=4, column=3)
pin_button = Button(text="Закрепить")  
pin_button.grid(row=4, column=4)
settings_button = Button(text="Настройки", command=summon_settings)  
settings_button.grid(row=0, column=4)
root.mainloop()
