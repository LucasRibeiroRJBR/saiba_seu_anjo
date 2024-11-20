import customtkinter as ctk
from util import fontes
import sqlite3

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #self.geometry('300x300')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.letreiro = ctk.CTkLabel(master=self,text='Descubra seu Anjo',font=fontes.f_principal())

        self.letreiro.grid(row=0,column=0)

if __name__ == '__main__':
    App().mainloop()


