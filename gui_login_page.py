from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from model.model import ModelTables, ModelCreate, ModelRead

# atribição as imagens: "https://www.flaticon.com/br/autores/icongeek26"

class App(ctk.CTk, ModelTables, ModelCreate, ModelRead):
    def __init__(self):
      self.app = ctk.CTk()
      self.wind_config()
      self.frame_image()
      self.frame_login()

      self.app.mainloop()


    def wind_config(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.app.geometry('670x400')
        self.app.resizable(False, False)
        self.app.title('Painel de acesso')
        self.app.iconbitmap(r'img\imagem_tela_login.ico')


    def frame_image(self):
       img = ctk.CTkImage(light_image= Image.open(r'img\imagem_tela_login.png'), size=(256, 256))
       self.lb_img = ctk.CTkLabel(self.app, image=img, text='Sistema de Automação de\nRegistros Contábeis - SIAUTO', font=('Roboto', 18, 'bold'), compound='bottom')
       self.lb_img.pack(side='left', fill='both', expand='yes')



    def autenticar(self):
      chave = self.autenticarUsuario(self.en_name.get(), self.en_password.get())
      
      if chave == 'Autenticado':
          self.app.destroy()
          print('Autenticado')

      elif chave == 'Não Autenticado':
         messagebox.showerror(title='Erro', message='Usuário ou senha inválidos.')
         print('Não Autenticado')


    def frame_login(self):
       self.frame = ctk.CTkFrame(self.app, width=350, height=396, corner_radius=10)
       self.frame.pack(side='right', padx= 10, pady= 10)

       img = ctk.CTkImage(light_image= Image.open(r'img\imagem_tela_login_user.png'), size=(64, 64))
       lb_img = ctk.CTkLabel(self.frame, image=img, text='')
       lb_img.place(x= 145, y= 12)

       self.en_name = ctk.CTkEntry(self.frame, placeholder_text='Usuário', width= 200, font=('Roboto', 16))
       self.en_name.place(x=80, y=105)

       self.en_password = ctk.CTkEntry(self.frame, placeholder_text='Senha', width= 200, font=('Roboto', 16), show='*')
       self.en_password.place(x=80, y=150)

       bt_to_enter = ctk.CTkButton(self.frame, text='Entrar', width= 200, corner_radius=6, font=('Roboto', 16), command= self.autenticar)
       bt_to_enter.place(x=80, y=190) #y=250

       bt_new_user = ctk.CTkButton(self.frame, text='Cadastre-se', width= 200, corner_radius=6, font=('Roboto', 16), fg_color='green', hover_color='darkgreen', command= self.frame_form_register_nwe_user)
       bt_new_user.place(x=80, y=340)#place(x=80, y=340) x= 185 y=250


    def frame_form_register_nwe_user(self):
       self.frame.pack_forget()
       self.criarTabelaUsuario()

       self.frame_form = ctk.CTkFrame(self.app, width=350, height=396, corner_radius=10)
       self.frame_form.pack(side='right', padx= 10, pady= 10)

       #formulario de Registro de novo usuário
       lb_title = ctk.CTkLabel(self.frame_form, text='Formulário de Cadastro', font=('Roboto', 22, 'bold'), text_color='white')
       lb_title.place(x= 50, y= 5)

       en_name = ctk.CTkEntry(self.frame_form, placeholder_text='Nome Completo', width= 250, font=('Roboto', 16))
       en_name.place(x=50, y=50)

       en_pseudo = ctk.CTkEntry(self.frame_form, placeholder_text='Nome usuário', width= 250, font=('Roboto', 16))
       en_pseudo.place(x=50, y=90)

       en_cpf = ctk.CTkEntry(self.frame_form, placeholder_text='CPF', width= 250, font=('Roboto', 16))
       en_cpf.place(x=50, y=130)

       en_email = ctk.CTkEntry(self.frame_form, placeholder_text='E-mail institucional', width= 250, font=('Roboto', 16))
       en_email.place(x=50, y=170)

       en_office = ctk.CTkEntry(self.frame_form, placeholder_text='Cargo ou função', width= 250, font=('Roboto', 16))
       en_office.place(x=50, y=210)

       opt_setor = ctk.CTkOptionMenu(self.frame_form, values=['Selecione o setor','COTCE', 'COPMC'], font=('Roboto', 16), width=250, fg_color='#343638', button_color='#343638', button_hover_color='#212121', dropdown_font=('Roboto', 16))
       opt_setor.place(x=50, y=250)

       en_password = ctk.CTkEntry(self.frame_form, placeholder_text='Senha', width= 250, font=('Roboto', 16), show='*')
       en_password.place(x=50, y=290)

       bt_confirm_register = ctk.CTkButton(self.frame_form, text='Cadastrar', width= 100, corner_radius=6, font=('Roboto', 16), fg_color='green', hover_color='darkgreen', command= lambda: self.cadastrarTabelaUsuario(en_name.get(), en_pseudo.get(), en_cpf.get(), en_email.get(), en_office.get(), opt_setor.get(), en_password.get()))
       bt_confirm_register.place(x=80, y=330)

       bt_back_page_login = ctk.CTkButton(self.frame_form, text='Voltar', width= 20, corner_radius=6, font=('Roboto', 16), fg_color='red', hover_color='darkred', command= lambda: (self.frame_form.pack_forget(), self.frame_login()))
       bt_back_page_login.place(x=200, y=330)#place(x=80, y=340)





if __name__ == "__main__":
   app = App()