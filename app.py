import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x300')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.letreiro = ctk.CTkLabel(master=self, text='Descubra seu Anjo', font=('Agency FB',45))
        self.letreiro.grid(row=0, column=0)

if __name__ == '__main__':
    App().mainloop()
