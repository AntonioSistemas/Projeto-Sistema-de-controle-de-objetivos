from PyQt5 import uic,QtWidgets,QtGui
import mysql.connector



#METODO CONEXÃO COM O BANCO
conexão=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='projeto_sco'
)

#METODOS PARA CHAMAR AS TELAS COM BOTOES. 
#*************************************************************************************
#------------------------------------------------------------------------------------------------------------------
def chama_meus_objetivos():
    PERFIL.close()
    MEUS_OBJETIVOS.show()
#-----------------------------------------------------------------------------------------------------------------
def chama_cad_objetivo():
    PERFIL.close()
    CADASTRAR_OBEJTIVOS.show()
#-----------------------------------------------------------------------------------------------------------
def chama_dados_conta():
    PERFIL.close()
    DADOS_CONTA.show()
#-------------------------------------------------------------------------------------------------------------
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

    nome = CADASTRAR.C_usuario.text()
    e_mail = CADASTRAR.C_email.text()
    senha = CADASTRAR.C_senha.text()
    c_senha = CADASTRAR.C_ConfirmarSenha.text()

    if (c_senha == senha):
        comandoSQL = " INSERT INTO usuário(nome, e_mail, senha)VALUES (%s,%s,%s )"
        valores=(nome,e_mail,senha)
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

    #BOTOES NA TELA DE CADASTRO.
    CADASTRAR.B_Cadastrar.clicked.connect(chama_cadastro)
#-----------------------------------------------------------






#IMPORTANDO TELAS. 
#*****************************************************************************************************

app=QtWidgets.QApplication([])
#BOTOES NA TELA DE LOGIN.
LOGIN = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\LOGIN.ui")
PERFIL = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\PERFIL.ui")
CADASTRAR = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR.ui")
CADASTRAR_OBEJTIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR_OBJETIVOS.ui")
MEUS_OBJETIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\MEUS_OBJETIVOS.ui")
DADOS_CONTA = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\DADOS_CONTA.ui")

LOGIN.B_Entrar.clicked.connect(chama_perfil)
LOGIN.B_Cadastrar.clicked.connect(chama_cadastro)


LOGIN.show()
app.exec()
#*******************************************************************************************************