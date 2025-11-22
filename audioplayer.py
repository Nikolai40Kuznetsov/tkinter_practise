import tkinter as tk
from tkinter import ttk
import pygame

window = tk.Tk()
window.title("Плеер")
window.tk.call("source", "breeze-dark/breeze-dark.tcl")
ttk.Style().theme_use("breeze-dark")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.25)
window_height = int(window_width * (10 / 8))
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
window.configure(bg="#20B2AA")
window.overrideredirect(True)
window.resizable(False, False)

playlist_panel = None

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(r"")
    pygame.mixer.music.play()
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def create_round_button(parent, label, command=None):
    canvas = tk.Canvas(parent, width=64, height=64, bg="#20B2AA", highlightthickness=0)
    canvas.create_oval(4, 4, 60, 60, fill="#122FAA", outline="#444444")
    canvas.create_text(32, 32, text=label, fill="white", font=("Segoe UI", 12, "bold"))
    if command:
        canvas.bind("<Button-1>", lambda e: command())
    return canvas

def toggle_playlist():
    global playlist_panel
    if playlist_panel and playlist_panel.winfo_exists():
        playlist_panel.destroy()
        playlist_panel = None
    else:
        playlist_panel = tk.Toplevel(window)
        playlist_panel.title("Список музыки")
        playlist_panel.geometry(f"{window_width}x{window_height}+{x_pos - window_width}+{y_pos}")
        playlist_panel.configure(bg="#20B2AA")
        playlist_panel.overrideredirect(True)
        playlist_panel.resizable(False, False)
        add_btn = ttk.Button(playlist_panel, text="Добавить музыку")
        add_btn.pack(pady=20)

def toggle_transparency_slider():
    global playlist_panel
    if getattr(window, "transparency_panel", None) and window.transparency_panel.winfo_exists():
        window.transparency_panel.destroy()
        window.transparency_panel = None
    else:
        panel_width = 200
        panel_height = 80
        panel_x = x_pos + window_width // 2 - panel_width // 2
        panel_y = y_pos - panel_height - 10
        window.transparency_panel = tk.Toplevel(window)
        window.transparency_panel.geometry(f"{panel_width}x{panel_height}+{panel_x}+{panel_y}")
        window.transparency_panel.configure(bg="#20B2AA")
        window.transparency_panel.overrideredirect(True)
        window.transparency_panel.attributes("-topmost", True)
        label = tk.Label(window.transparency_panel, text="Прозрачность", font=("Segoe UI", 10), bg="#7DF9FF", fg="white")
        label.pack(pady=(10, 0))
        def update_alpha(val):
            alpha = float(val) / 100
            window.attributes("-alpha", alpha)
        alpha_slider = ttk.Scale(window.transparency_panel, from_=30, to=100, orient="horizontal", command=update_alpha)
        alpha_slider.set(window.attributes("-alpha") * 100)
        alpha_slider.pack(pady=(5, 10))

settings_btn = create_round_button(window, "⚙", command=toggle_transparency_slider)
settings_btn.place(relx=0.97, rely=0.02, anchor="ne")

cover = tk.Label(window, text="Здесь могла быть ваша картинка", font=('Segoe UI', 14), bg="#7DF9FF", fg="white")
cover.pack(pady=(20, 5))

author = tk.Label(window, text="Исполнитель", font=('Segoe UI', 14), bg="#7DF9FF", fg="white")
author.pack(pady=(20, 5))

name = tk.Label(window, text="Название песни", font=('Segoe UI', 14), bg="#7DF9FF", fg="white")
name.pack(pady=(20, 5))

progress = ttk.Scale(window, from_=0, to=100, orient="horizontal", length=200)
progress.pack(pady=5)

time_label = tk.Label(window, text="69:52", font=('Segoe UI', 10), bg="#7DF9FF", fg="white")
time_label.pack(pady=(0, 10))

button_frame = tk.Frame(window, bg="#20B2AA")
button_frame.pack(pady=10)

btn_music = create_round_button(button_frame, "📁", toggle_playlist)
btn_prev = create_round_button(button_frame, "⏮")
btn_pause = create_round_button(button_frame, "⏸", command=play_music)
btn_next = create_round_button(button_frame, "⏭")
btn_pin = create_round_button(button_frame, "📌", lambda: window.attributes("-topmost", not window.attributes("-topmost")))

btn_music.grid(row=0, column=0)
btn_prev.grid(row=0, column=1)
btn_pause.grid(row=0, column=2)
btn_next.grid(row=0, column=3)
btn_pin.grid(row=0, column=4)

window.bind("<Escape>", lambda e: window.destroy())
window.mainloop()
  