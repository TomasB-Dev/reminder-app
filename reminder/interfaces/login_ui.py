import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Reminder')
        self.geometry("1280x720")
        self.configure(fg_color='red')
def start():
    app = App()
    app.mainloop()