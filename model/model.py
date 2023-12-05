import sqlite3
from tkinter import messagebox
from model.modelConect import ModelConection


class ModelTables(ModelConection):
    def criarTabelaUsuario(self):
        self.conectBase()
        sql_query = 'CREATE TABLE IF NOT EXISTS tbl_usuario ("ID_USUARIO" INTEGER, "NOME_COMPLETO" TEXT NOT NULL, "NOME_USUARIO" TEXT NOT NULL, "CPF" TEXT NOT NULL, "EMAIL" TEXT NOT NULL, "CARGO" TEXT NOT NULL, "SETOR" TEXT NOT NULL, "SENHA" TEXT NOT NULL, PRIMARY KEY ("ID_USUARIO" AUTOINCREMENT));'
        self.conn.execute(sql_query)
        self.conn.commit()

        return print('Tabela usuario criada com sucesso.')


class ModelCreate(ModelConection):
    def cadastrarTabelaUsuario(self, nome, pseudo, cpf, email, cargo, setor, senha):
        try:
            self.conectBase()
            sql_query = 'INSERT INTO tbl_usuario (NOME_COMPLETO, NOME_USUARIO, CPF, EMAIL, CARGO, SETOR, SENHA) VALUES (?, ?, ?, ?, ?, ?, ?);'
            sql_args = (nome, pseudo.upper(), cpf, email, cargo, setor, senha)
            self.conn.execute(sql_query, sql_args)
            self.conn.commit()
        except Exception as erro:
            print(f'Erro: {erro}')
            messagebox.showerror(title='Erro', message='Não foi possível cadastrar um novo usário.')
        
        else:
            messagebox.showinfo(title='Sucesso', message=f'Usuario {nome} foi cadstrado com sucesso.')
            return print('Usuario cadstrado com sucesso.')
            


class ModelRead(ModelConection):
    def autenticarUsuario(self, user, password):
        try:
            self.conectBase()
            sql_query = f'SELECT NOME_USUARIO, SENHA FROM tbl_usuario WHERE NOME_USUARIO="{user}" AND SENHA="{password}";'
            self.seach = self.cursor.execute(sql_query).fetchall()

            if self.seach == []:
                print('Preencha os campos para efetuar o login.')
                messagebox.showerror(title='Erro', message='Preencha o campo usuário ou senha.')

            elif user == self.seach[0][3] and password == self.seach[0][4]:
                messagebox.showinfo(title='Bem vindo!', message=f'Seja bem vindo(a), {user}.')
                return 'Autenticado'
            
            else:
                return 'Não Autenticado'
        except Exception as erro:
            messagebox.showwarning(title='Atenção', message='Você não possuí cadastro.')


class ModelDelete():
    pass