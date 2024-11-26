import customtkinter as ctk
import tkinter


class App(ctk.CTk):
    def __init__(self):
        super().__init__() 

        #self.ctk_font = ctk.CTkFont(family=custom_font, size=20, weight="bold")       
        self.custom_font = tkinter.font.Font(family="Chicle", size=14, file='src/fonts/Chicle-Regular.ttf')

        self.geometry('500x300')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.letreiro = ctk.CTkLabel(master=self, text='Descubra seu Anjo', font=self.custom_font)
        self.letreiro.grid(row=0, column=0)

if __name__ == '__main__':
    App().mainloop()
