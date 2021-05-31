from os import curdir
from PyQt5 import uic,QtWidgets,QtGui
import mysql.connector 


conexão=mysql.connector.connect(
    host='Localhost',
    user='root',
    password='',
    database='projeto_sco' 
)

#
#
#
#
#
#
#
#
#
#
#                                  METODOS PARA CHAMAR AS TELAS COM BOTOES. 
#*************************************************************************************
#------------------------------------------------------------------------------------------------------------------
def chama_meus_objetivos():
    PERFIL.close()
    MEUS_OBJETIVOS.show()
    
    
    
    #BOTOS NA TELA MEUS OBJETIVOS
    MEUS_OBJETIVOS.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    MEUS_OBJETIVOS.B_Conf_Conta.clicked.connect(chama_dados_conta)
    MEUS_OBJETIVOS.B_Sair.clicked.connect(chama_login)

#-----------------------------------------------------------------------------------------------------------------
def chama_cad_objetivo():
    PERFIL.close()
    CADASTRAR_OBEJTIVOS.show()

    #BOTOES NA TELA CADASTRAR OBJETIVOS
    CADASTRAR_OBEJTIVOS.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    CADASTRAR_OBEJTIVOS.B_Conf_Conta.clicked.connect(chama_dados_conta)
    CADASTRAR_OBEJTIVOS.B_Sair.clicked.connect(chama_login)

    #CADASTRAR_OBEJTIVOS.B_cadastrar.clicked.connect(chama_login)

#-----------------------------------------------------------------------------------------------------------
def chama_dados_conta():
    PERFIL.close()
    DADOS_CONTA.show()


    #BOTOES NA TELA DE DADOS DO USUARIO
    DADOS_CONTA.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    DADOS_CONTA.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    DADOS_CONTA.B_Sair.clicked.connect(chama_login)

    #DADOS_CONTA.B_editar_nome.clicked.connect()
    #DADOS_CONTA.B_excluir_nome.clicked.connect()
    #DADOS_CONTA.B_editar_senha.clicked.connect()
    #DADOS_CONTA.B_excluir_senha.clicked.connect()    
#--------------------------------------------------------------------------------------------------------------
def chama_login():
    PERFIL.close()
    CADASTRAR.close()
    LOGIN.show()
#---------------------------------------------------------------------------------------------------------------
def chama_perfil():
    LOGIN.close()
    PERFIL.show()

    #BOTOS NA TELA DO PERFIL
    PERFIL.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    PERFIL.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    PERFIL.B_Conf_Conta.clicked.connect(chama_dados_conta)
    PERFIL.B_Sair.clicked.connect(chama_login)
#--------------------------------------------------------------------

def chama_cadastro():
    LOGIN.close()
    CADASTRAR.show()
    #BOTOES NA TELA DE CADASTRO.
    CADASTRAR.B_Cadastrar.clicked.connect(cadastrando_usuario)
#-----------------------------------------------------------
#
#
#
#
#
#
#
#
#
#
#
#
#                                         METODOS CRUD USUARIO
#*****************************************************************************************************

def cadastrando_usuario ():
    nome = CADASTRAR.C_usuario.text()
    e_mail = CADASTRAR.C_email.text()
    senha = CADASTRAR.C_senha.text()
    c_senha = CADASTRAR.C_ConfirmarSenha.text()

    if (c_senha == senha):
        comandoSQL = " INSERT INTO aluno(nome, senha, e_mail)VALUES (%s,%s,%s )"
        valores=(nome,senha,e_mail)
        try:
            cursor=conexão.cursor()
            cursor.execute(comandoSQL,valores)
            conexão.commit()
            cursor.close()
            print('cadastrado')
        except:
            print("houve erro na adição dos dados")
    else:
        print ('As senhas digitadas são diferentes')


def autenticando_login ():
    usuario=LOGIN.C_usuario.text()
    senha=LOGIN.C_senha.text()
    comandoSQL="""  SELECT senha FROM  aluno WHERE  nome=(%s)"""
    valores=(usuario)
    
    try:
        cursor=conexão.cursor()
        cursor.execute(comandoSQL,valores)
        senha_bd=cursor.fetchone()

        if senha_bd==senha:
            LOGIN.close()
            PERFIL.show()
        
        
        else: print('um dos dados inseridos está invalido!')




    except:  
        print('erro') 

#                                         METODOS CRUD MATERIA
#***************************************************************************************************** 
# 
# 
#                                         METODOS CRUD RESULTADO_CHAVE
#*****************************************************************************************************


#                                         METODOS CRUD ASSUNTO
#*****************************************************************************************************




#                                         METODOS CRUD OBJETIVO
#*****************************************************************************************************

#
#
#
#
#
#
#
#
#
#
#

#                                      IMPORTANDO TELAS. 
#*****************************************************************************************************

app=QtWidgets.QApplication([])
#BOTOES NA TELA DE LOGIN.
LOGIN = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\LOGIN.ui")
PERFIL = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\PERFIL.ui")
CADASTRAR = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR.ui")
CADASTRAR_OBEJTIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR_OBJETIVOS.ui")
MEUS_OBJETIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\MEUS_OBJETIVOS.ui")
DADOS_CONTA = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\DADOS_CONTA.ui")

LOGIN.B_Entrar.clicked.connect(autenticando_login)
LOGIN.B_Cadastrar.clicked.connect(chama_cadastro)


LOGIN.show()
app.exec()
#*******************************************************************************************************