import customtkinter as ctk
from pyglet import font,options
from util import images as i


class Resultado(ctk.CTkToplevel):
    def __init__(self, parent, variable):
        super().__init__(parent)
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)
        self.geometry('700x500')
        self.after(100, self.lift)        

        self.lb_nome = ctk.CTkLabel(master=self,text=f'{variable.get()}',font=('Chicle',48))
        self.lb_imagem = ctk.CTkLabel(master=self,text='',image=i.Imamish)

        self.lb_nome.grid(row=0,column=0,columnspan=2)
        self.lb_imagem.grid(row=1,column=0,columnspan=2)

class App(ctk.CTk):
    def __init__(self):
        super().__init__() 
        options['win32_gdi_font'] = True
        self.geometry('500x300')
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)
        self.toplevel_resul = None

        font.add_file('src/fonts/Chicle-Regular.ttf')
        self.vDt_nasc = ctk.StringVar()

        self.letreiro = ctk.CTkLabel(master=self,text='Descubra seu Anjo',font=('Chicle',48))
        self.lb_dt_nasc = ctk.CTkLabel(master=self,text='Data de Nascimento',font=('Chicle',18))
        self.in_dt_nasc = ctk.CTkEntry(master=self,font=('Chicle',18),textvariable=self.vDt_nasc)
        self.bt_show = ctk.CTkButton(master=self,text='Buscar',font=('Chicle',18),command=lambda:self.open_toplevel())

        self.letreiro.grid(row=0, column=0, columnspan=2)
        self.lb_dt_nasc.grid(row=1,column=0,sticky='e',padx=5)
        self.in_dt_nasc.grid(row=1,column=1,sticky='w',padx=5)
        self.bt_show.grid(row=2, column=0, columnspan=2,pady=15)

    def open_toplevel(self):
        # Pass the main app variable to Toplevel
        toplevel_window = Resultado(self, self.vDt_nasc)
        toplevel_window.grab_set()  # Optional: makes the toplevel window modal
            


if __name__ == '__main__':
    App().mainloop()
