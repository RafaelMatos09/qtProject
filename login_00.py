from PyQt5 import *
import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import uic


def faz_login():
    tela_1.label_2.setText("Checando login!")
    nome_usuario = tela_1.lineEdit.text()
    senha = tela_1.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute(
            "SELECT senha FROM cadastro WHERE login ='{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        banco.close()
    except:
        tela_1.label_2.setText("Erro ao validar o login")

    if senha == senha_bd[0][0]:
        tela_1.close()
        tela_logado.show()
        tela_logado.label.setText(f'Bem vindo {nome_usuario} !')
    else:
        tela_1.label_2.setText("Dados de login incorretos!")


def logout():
    tela_logado.close()
    tela_1.show()


def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" +
                           nome+"','"+login+"','"+senha+"')")

            banco.commit()
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")


app = QtWidgets.QApplication([])
tela_1 = uic.loadUi("tela_1.ui")
tela_logado = uic.loadUi("tela_logado.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_1.pushButton.clicked.connect(faz_login)
tela_logado.pushButton.clicked.connect(logout)
tela_1.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_1.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)


tela_1.show()
app.exec()
