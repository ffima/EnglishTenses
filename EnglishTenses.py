import tkinter as tk

root = tk.Tk()
root.title('English Tenses')
root.iconbitmap('./assets/icon.ico') # need help

# window size
window_width = 1300
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.mainloop()