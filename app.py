import customtkinter as ctk
from pyglet import font,options


class Resultado(ctk.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry('400x200')
        self.after(100, self.lift)

        self.lb_teste = ctk.CTkLabel(master=self,text='teste')

        self.lb_teste.grid(row=1,column=0)

class App(ctk.CTk):
    def __init__(self):
        super().__init__() 
        options['win32_gdi_font'] = True
        self.geometry('500x300')
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0,1), weight=1)
        self.toplevel_resul = None

        font.add_file('Chicle-Regular.ttf')
        self.vDt_nasc = ctk.StringVar()

        self.letreiro = ctk.CTkLabel(master=self,text='Descubra seu Anjo',font=('Chicle',48))
        self.lb_dt_nasc = ctk.CTkLabel(master=self,text='Data de Nascimento',font=('Chicle',18))
        self.in_dt_nasc = ctk.CTkEntry(master=self,font=('Chicle',18),textvariable=self.vDt_nasc)
        self.bt_show = ctk.CTkButton(master=self,text='Buscar',font=('Chicle',18),command=lambda:self.get_info())

        self.letreiro.grid(row=0, column=0, columnspan=2)
        self.lb_dt_nasc.grid(row=1,column=0,sticky='e',padx=5)
        self.in_dt_nasc.grid(row=1,column=1,sticky='w',padx=5)
        self.bt_show.grid(row=2, column=0, columnspan=2,pady=15)

    def get_info(self):
        #print(f'{self.vDt_nasc.get()}')
        if self.toplevel_resul is None or not self.toplevel_resul.winfo_exists():
            self.toplevel_resul = Resultado(self)
            self.toplevel_resul.after(0,self.toplevel_resul.lift)
        else: pass
            


if __name__ == '__main__':
    App().mainloop()
