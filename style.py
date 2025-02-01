import ttkbootstrap as ttk

# конфигурирем стили как вайб имеется
def configure_button_style():
    present_style = ttk.Style()
    present_style.configure("Present.TButton", font=("Calibri", 10),background="#E6A8D7")

    past_style = ttk.Style()
    past_style.configure("Past.TButton", font=("Calibri", 15), background="#1CA9C9")

    future_style = ttk.Style()
    future_style.configure("Future.TButton", font=("Calibri", 30), background="#464531")
