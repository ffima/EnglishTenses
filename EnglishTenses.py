import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

root = ttk.Window(themename= "flatly")
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

# home page

frame = ttk.Frame(root)
frame.pack(expand=True, fill="both", padx=20, pady=20)
tenses = [
    ["I speak English", "I am speaking English", "I have spoken English", "I have been speaking English"],
    ["I spoke English", "I was speaking English", "I had spoken English", "I had been speaking English"],
    ["I will speak English", "I will be speaking English", "I will have spoken English", "I will have been speaking English"]
]

# headers
column_headers = ["Simple", "Continuous", "Perfect", "Perfect Continuous"]
row_headers = ["Present", "Past", "Future"]

for j, header in enumerate(column_headers):
    label = ttk.Label(frame, text=header, font="Calibri 14 bold", anchor="center")
    label.grid(row=0, column=j + 1, padx=5, pady=5, sticky="nsew")

for i, header in enumerate(row_headers):
    label = ttk.Label(frame, text=header, font="Calibri 14 bold", anchor="center")
    label.grid(row=i + 1, column=0, padx=5, pady=5, sticky="nsew")

# tenses buttons
for i, row in enumerate(tenses):
    for j, tense in enumerate(row):
        button = ttk.Button(frame, text=tense, command=lambda t=tense: open_tense_tab(t))
        button.grid(row=i + 1, column=j + 1, padx=5, pady=5, sticky="nsew")

# grid config
for i in range(len(tenses) + 1):
    frame.grid_rowconfigure(i, weight= 1, uniform="row", minsize=100) #need help!!

for j in range(len(tenses[0]) + 1):
    frame.grid_columnconfigure(j, weight= 0, uniform="column", minsize=100) #need help!!

# tense tab
def open_tense_tab(tense):
    tab = tk.Toplevel(root)
    tab.title(f'{tense} Tab')

    # tense tab size
    tab_width = 1300
    tab_height = 800
    tab.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # content
    label = ttk.Label(tab, text=f"{tense}", font="Calibri 20 bold")
    label.pack(pady=20)

    # usage button
    usage_button = ttk.Button(tab, text="Usage", command=lambda: open_usage_tab(tense))
    usage_button.pack(pady=10)

    #markers button
    markers_button = ttk.Button(tab, text="Markers", command=lambda: print("Markers clicked"))
    markers_button.pack(pady=10)


# usage tab
def open_usage_tab(tense):
    usage_tab = tk.Toplevel(root)
    usage_tab.title(f'{tense} Usage')
    # usage tab size
    usage_tab_width = 800
    usage_tab_height = 600
    usage_tab.geometry(f'{usage_tab_width}x{usage_tab_height}+{center_x}+{center_y}') #need help center

    label = ttk.Label(usage_tab, text=f"Usage for {tense}", font="Calibri 16")
    label.pack(pady=20)

# run
root.mainloop()