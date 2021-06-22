from os import curdir, system
from re import X
from PyQt5 import uic,QtWidgets,QtGui
import mysql.connector


conexão=mysql.connector.connect(
    host='Localhost',
    user='root',
    password='jonas123',
    database='projeto_sco' 
)
id_global=str(0)
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
def chama_dados_conta():
    Perfil.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    DADOS_CONTA.show()


    global nome_aluno_str
    global e_mail_aluno_str
    global senha_usuario_str

    comandoSQL="SELECT id FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSQL)
    id_usuario=cursor.fetchall()
    id_user_str=str(id_usuario[0][0])


    comandoEMAIL="SELECT e_mail FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoEMAIL)
    e_mail_aluno=cursor.fetchall()
    e_mail_aluno_str=str(e_mail_aluno[0][0])


    comandoNOME="SELECT nome FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoNOME)
    nome_aluno=cursor.fetchall()
    nome_aluno_str=str(nome_aluno[0][0])


    comandoSENHA="SELECT senha FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSENHA)
    senha_usuario=cursor.fetchall()
    senha_usuario_str=str(senha_usuario[0][0])


    DADOS_CONTA.NomeUsuario.setText(nome_aluno_str)
    DADOS_CONTA.C_email.setText(e_mail_aluno_str)
    DADOS_CONTA.C_nome.setText(nome_aluno_str)
    DADOS_CONTA.C_senha.setText(senha_usuario_str)




    #BOTOES NA TELA DE DADOS DO USUARIO
    DADOS_CONTA.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    DADOS_CONTA.B_NovoObjetivo.clicked.connect(chama_cad_materia)
    DADOS_CONTA.B_Sair.clicked.connect(chama_login)

    DADOS_CONTA.B_editar.clicked.connect(chama_editar_usuario)    
#--------------------------------------------------------------------------------------------------------------
def chama_login():
    Perfil.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    LOGIN.show()





    LOGIN.C_usuario.setText("")
    LOGIN.C_senha.setText("")
#---------------------------------------------------------------------------------------------------------------
def chama_perfil(nome_usuario):
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    Perfil.show()



    global id_global
    comandoSQL="SELECT id FROM aluno WHERE nome='"+nome_usuario+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSQL)
    id_usuario=cursor.fetchall()

    id_global=str(id_usuario[0][0])



        

    Perfil.NomeUsuario_Meio.setText(nome_usuario)
    Perfil.NomeUsuario.setText(nome_usuario)

    #BOTOS NA TELA DO PERFIL
    Perfil.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    Perfil.B_NovoObjetivo.clicked.connect(chama_cad_materia)
    Perfil.B_Conf_Conta.clicked.connect(chama_dados_conta)
    Perfil.B_Sair.clicked.connect(chama_login)
#--------------------------------------------------------------------
def chama_cadastro():
    Perfil.close()
    LOGIN.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    CADASTRAR.show()

    #BOTOES NA TELA DE CADASTRO.
    CADASTRAR.B_Cadastrar.clicked.connect(cadastrando_usuario)

#------------------------------------------------------------------------------------------------------------------
def chama_meus_objetivos():
    LOGIN.close()
    Perfil.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_MATERIA.close() 
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    materia=str("materia")
    assunto=str("assunto")
    objetivo=str("objetivo")
    chave=str("resultado_chave")

    ver_materia=verificando_duplicada(materia)
    if ver_materia>1:
        try:
            limpando_duplicadas(materia,recebendo_materia)
        except:
            print("erro")

    ver_assunto=verificando_duplicada(assunto)
    if ver_assunto>1:
        try:
            limpando_duplicadas(assunto,recebendo_assunto)
        except:
            print("erro")
    ver_objetivo=verificando_duplicada(objetivo)

    if ver_objetivo>1:
        try:
            limpando_duplicadas(objetivo,recebendo_objetivo)
        except:
            print("erro")

    ver_chave=verificando_duplicada(chave)
    if ver_chave>1:
        try:
            limpando_duplicadas(chave,recebendo_chave)
        except:
            print("erro")
    MEUS_OBJETIVOS.show()
    
    try:
        cursor=conexão.cursor()
        comando_sql="SELECT objetivo.nome, materia.nome,assunto.nome,resultado_chave.nome,aluno.id FROM objetivo JOIN aluno ON objetivo.id_aluno=aluno.id JOIN materia ON objetivo.id_materia=materia.id JOIN assunto ON objetivo.id_assunto=assunto.id JOIN resultado_chave ON objetivo.id_resultado_chave=resultado_chave.id WHERE aluno.id = '"+id_global+"' "
        cursor.execute(comando_sql)
        objetivos_lindos=cursor.fetchall()

    
        MEUS_OBJETIVOS.tabela_objetivos.setRowCount(len(objetivos_lindos))
        MEUS_OBJETIVOS.tabela_objetivos.setColumnCount(4)

        for linha in range(0,len(objetivos_lindos)):
            for coluna in range(0,4):
                MEUS_OBJETIVOS.tabela_objetivos.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(objetivos_lindos[linha][coluna])))
    except:
        print("erro")



    
    #BOTOS NA TELA MEUS OBJETIVOS
    MEUS_OBJETIVOS.B_NovoObjetivo.clicked.connect(chama_cad_materia)
    MEUS_OBJETIVOS.B_Conf_Conta.clicked.connect(chama_dados_conta)
    MEUS_OBJETIVOS.B_Sair.clicked.connect(chama_login)
    MEUS_OBJETIVOS.excluir.clicked.connect(excluir_linha)
    MEUS_OBJETIVOS.editar.clicked.connect(editar_linha)
#-----------------------------------------------------------------------------------------------------------------
def chama_cad_materia():
    LOGIN.close()
    Perfil.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.show()


    ICAD_MATERIA.C_materia.setText("")



    #BOTOES NA TELA CADASTRAR OBJETIVOS
    ICAD_MATERIA.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    ICAD_MATERIA.B_Conf_Conta.clicked.connect(chama_dados_conta)
    ICAD_MATERIA.B_Sair.clicked.connect(chama_login)
    ICAD_MATERIA.proximo.clicked.connect(chama_assunto)

#---------------------------------------------------------------------------------------
def chama_assunto():
    Perfil.close()
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    ICAD_ASSUNTO.show()
    global recebendo_materia





    ICAD_ASSUNTO.C_assunto.setText("")

    recebendo_materia=ICAD_MATERIA.C_materia.text()
    print(recebendo_materia)
    
    COMANDOSQL="INSERT INTO materia(nome,id_aluno) VALUES ('"+recebendo_materia+"', '"+id_global+"')"
    try:
        cursor=conexão.cursor()
        cursor.execute(COMANDOSQL) 
        conexão.commit()
        cursor.close()
        print("Inserido materia")
    except:
        print("erro")


    #BOTOES NA TELA CADASTRAR ASSUNTO
    ICAD_ASSUNTO.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    ICAD_ASSUNTO.B_Conf_Conta.clicked.connect(chama_dados_conta)
    ICAD_ASSUNTO.B_Sair.clicked.connect(chama_login)
    ICAD_ASSUNTO.proximo.clicked.connect(chama_objetivo)
#--------------------------------------------------------------------------------
def chama_objetivo():
    Perfil.close()
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    ICAD_OBJETIVO.show()
    global recebendo_assunto

    ICAD_OBJETIVO.C_objetivo.setText("")

    recebendo_assunto=ICAD_ASSUNTO.C_assunto.text()
    global str_id_materia
    COMANDO_PEGAR_ID_MATERIA="SELECT id FROM materia WHERE id_aluno='"+id_global+"' AND nome='"+recebendo_materia+"' "
    cursor=conexão.cursor()
    cursor.execute(COMANDO_PEGAR_ID_MATERIA)
    id_materia=cursor.fetchall()
    str_id_materia=str(id_materia[0][0])


    COMANDOSQL="INSERT INTO assunto(nome,id_aluno,id_materia) VALUES ('"+recebendo_assunto+"', '"+id_global+"','"+str_id_materia+"')"
    try:
        cursor=conexão.cursor()
        cursor.execute(COMANDOSQL) 
        conexão.commit()
        cursor.close()
        print("Inserido assunto")
    except:
        print("erro")

    #BOTOES NA TELA DE CADASTRAR OBJETIVO
    ICAD_OBJETIVO.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    ICAD_OBJETIVO.B_Conf_Conta.clicked.connect(chama_dados_conta)
    ICAD_OBJETIVO.B_Sair.clicked.connect(chama_login)
    ICAD_OBJETIVO.proximo.clicked.connect(chama_chave)
#------------------------------------------------------------------------------------
def chama_chave():
    Perfil.close()
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    MENSAGEM_CAD.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    ICAD_CHAVE.show()

    ICAD_CHAVE.C_chave.setText("")

    global recebendo_objetivo
    recebendo_objetivo=ICAD_OBJETIVO.C_objetivo.text()
    COMANDO_PEGAR_ID_ASSUNTO="SELECT id FROM assunto WHERE id_aluno='"+id_global+"' AND nome='"+recebendo_assunto+"' "
    cursor=conexão.cursor()
    cursor.execute(COMANDO_PEGAR_ID_ASSUNTO)
    id_assunto=cursor.fetchall()
    str_id_assunto=str(id_assunto[0][0])

    COMANDOSQL="INSERT INTO objetivo(nome,id_aluno,id_materia,id_assunto) VALUES ('"+recebendo_objetivo+"', '"+id_global+"','"+str_id_materia+"','"+str_id_assunto+"')"
    try:
        cursor=conexão.cursor()
        cursor.execute(COMANDOSQL) 
        conexão.commit()
        cursor.close()
        print("Inserido objetivo")
    except:
        print("erro")


    #BOTOES NA TELA DE CADASTRAR CHAVE
    ICAD_CHAVE.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    ICAD_CHAVE.B_Conf_Conta.clicked.connect(chama_dados_conta)
    ICAD_CHAVE.B_Sair.clicked.connect(chama_login)
    ICAD_CHAVE.proximo.clicked.connect(mensagem)
#-----------------------------------------------------------------------------
def mensagem():
    Perfil.close()
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD_2.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    MENSAGEM_CAD.show()
    global recebendo_chave
    recebendo_chave=ICAD_CHAVE.C_chave.text()
    COMANDO_PEGAR_ID_OBJETIVO="SELECT id FROM objetivo WHERE id_aluno='"+id_global+"' AND nome='"+recebendo_objetivo+"' "
    cursor=conexão.cursor()
    cursor.execute(COMANDO_PEGAR_ID_OBJETIVO)
    id_objetivo=cursor.fetchall()
    str_id_objetivo=str(id_objetivo[0][0])


    COMANDOSQL="INSERT INTO resultado_chave(nome,id_aluno) VALUES ('"+recebendo_chave+"', '"+id_global+"')"
    try:
        cursor=conexão.cursor()
        cursor.execute(COMANDOSQL) 
        conexão.commit()
        cursor.close()
        print("Inserido resultado chave")
    except:
        print("erro")


    #BOTOES NA TELA DE MENSAGEM
    MENSAGEM_CAD.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    MENSAGEM_CAD.B_Conf_Conta.clicked.connect(chama_dados_conta)
    MENSAGEM_CAD.B_Sair.clicked.connect(chama_login)
    MENSAGEM_CAD.proximo.clicked.connect(concluindo)
#-------------------------------------------------------------------------------
def concluindo():
    Perfil.close()
    LOGIN.close()
    CADASTRAR.close()
    EDITAR_OBJETIVO.close()
    DADOS_CONTA.close()
    EDITAR_USER.close()
    ICAD_ASSUNTO.close()
    ICAD_OBJETIVO.close()
    ICAD_CHAVE.close()
    MENSAGEM_CAD.close()
    MEUS_OBJETIVOS.close()
    ICAD_MATERIA.close()
    MENSAGEM_CAD_2.show()

    global str_id_chave
    COMANDO_PEGAR_ID_CHAVE="SELECT id FROM resultado_chave WHERE id_aluno='"+id_global+"' AND nome='"+recebendo_chave+"' "
    cursor=conexão.cursor()
    cursor.execute(COMANDO_PEGAR_ID_CHAVE)
    id_chave=cursor.fetchall()
    str_id_chave=str(id_chave[0][0])

    COMANDO_ADD_CHAVE_OBJ="UPDATE objetivo SET id_resultado_chave='"+str_id_chave+"' WHERE id_aluno='"+id_global+"' AND nome='"+recebendo_objetivo+"'"
    cursor=conexão.cursor()
    cursor.execute(COMANDO_ADD_CHAVE_OBJ)
    conexão.commit()
    cursor.close()

    #BOTOES NA TELA DE MENSAGEM 2
    MENSAGEM_CAD_2.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    MENSAGEM_CAD_2.B_Conf_Conta.clicked.connect(chama_dados_conta)
    MENSAGEM_CAD_2.B_Sair.clicked.connect(chama_login)

def excluir_linha():
    linha=MEUS_OBJETIVOS.tabela_objetivos.currentRow()
    print(linha)
    MEUS_OBJETIVOS.tabela_objetivos.removeRow(linha)
    try:
        cursor=conexão.cursor()
        comandosql="SELECT id FROM objetivo"
        cursor.execute(comandosql)
        ids_lidos=cursor.fetchall()
        print(ids_lidos)
        valor_id=ids_lidos[linha][0]
        print(valor_id)
    except:
        print("erro")
    try:
        comandosql2="DELETE FROM objetivo WHERE id = '"+str(valor_id)+"'"
        cursor.execute(comandosql2)
    except:
        print("erro")

def editar_linha():
    MEUS_OBJETIVOS.close()
    EDITAR_OBJETIVO.show()   
    linha=MEUS_OBJETIVOS.tabela_objetivos.currentRow()
    global str_valor_id
    try:
        cursor=conexão.cursor()
        comandosql="SELECT id FROM objetivo"
        cursor.execute(comandosql)
        ids_lidos=cursor.fetchall()
        valor_id=ids_lidos[linha][0] 
        print(valor_id)       
    except:
        print("erro")
    try:
        str_valor_id=str(valor_id)
        cursor.execute("SELECT materia.nome, assunto.nome,objetivo.nome,resultado_chave.nome,aluno.id FROM objetivo JOIN aluno ON objetivo.id_aluno=aluno.id JOIN materia ON objetivo.id_materia=materia.id JOIN assunto ON objetivo.id_assunto=assunto.id JOIN resultado_chave ON objetivo.id_resultado_chave=resultado_chave.id WHERE objetivo.id = '"+str_valor_id+"' ")
        objetivos=cursor.fetchall()
        print(objetivos)
    except:
        print("erro")

    EDITAR_OBJETIVO.C_materia.setText(str(objetivos[0][0]))
    global xmateria
    xmateria=str(objetivos[0][0])
    EDITAR_OBJETIVO.C_assunto.setText(str(objetivos[0][1]))
    global xassunto
    xassunto=str(objetivos[0][1])
    EDITAR_OBJETIVO.C_Objetivo1.setText(str(objetivos[0][2]))
    global xobjetivo
    xobjetivo=str(objetivos[0][2])
    EDITAR_OBJETIVO.C_RC_A1.setText(str(objetivos[0][3]))
    global xchave
    xchave=str(objetivos[0][3])

    EDITAR_OBJETIVO.B_cadastrar.clicked.connect(salvando_edicao)
   
def salvando_edicao():
    print(str_valor_id)
    materia=EDITAR_OBJETIVO.C_materia.text()
    assunto=EDITAR_OBJETIVO.C_assunto.text()
    objetivo=EDITAR_OBJETIVO.C_Objetivo1.text()
    resultado_chave=EDITAR_OBJETIVO.C_RC_A1.text()

    cursor=conexão.cursor()
    cursor.execute("UPDATE materia SET nome='"+materia+"' WHERE nome='"+xmateria +"' ")
    cursor.execute("UPDATE assunto SET nome='"+assunto+"' WHERE nome='"+xassunto +"' ")
    cursor.execute("UPDATE objetivo SET nome='"+objetivo+"' WHERE nome='"+xobjetivo +"' ")
    cursor.execute("UPDATE  resultado_chave SET nome='"+resultado_chave+"' WHERE nome='"+xchave +"' ")

    EDITAR_OBJETIVO.close()
    chama_meus_objetivos()

def limpando_duplicadas(tabela,descricao):
    try:
        cursor=conexão.cursor()
        cursor.execute("DELETE FROM '"+tabela+"' WHERE nome='"+descricao+"' ")
        cursor.close()
    except:
        print("Nao houve exclusao")
    try:
        cursor.execute("INSERT INTO '"+tabela+"'(nome,id_aluno) VALUES ('"+descricao+"','"+id_global+"')   ")
        cursor.commit()
        cursor.close
    except:
        print("erro")
def verificando_duplicada(tabela):
    try:
        cursor=conexão.cursor()
        cursor.execute("SELECT nome FROM "+tabela+" ")
        valores=cursor.fetchall()
    except:
        print("erro")
    try:  
        repetido=list(set(valores))
        reps=[]
        cont=0
        for i in repetido:
            if (valores.count(i) > 1 ):
                reps.append(i)
        teste=[]
        for linha in valores:
            for coluna in linha:
                teste.append(coluna)

        for i in teste:
            if i == str(reps[0][0]):
                cont=cont+1
    except:
        print("erro")
        cont=0
    return cont



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
    sero=0
    try:

        verificar_nome="SELECT nome FROM aluno WHERE nome='"+nome+"'"
        cursor=conexão.cursor()
        cursor.execute(verificar_nome)
        verificado=cursor.fetchall()
        str_ver=str(verificado[0][0])
    except:
        str_ver=str(sero)

    if str_ver==nome:
        CADASTRAR.aviso.setText("Nome inserido já existe")        
    else:
        if (c_senha == senha):
            comandoSQL = " INSERT INTO aluno(nome, senha, e_mail)VALUES (%s,%s,%s )"
            valores=(nome,senha,e_mail)
            try:
                cursor=conexão.cursor()
                cursor.execute(comandoSQL,valores) 
                conexão.commit()
                cursor.close()
                CADASTRAR.close()
                LOGIN.show()
                LOGIN.C_aviso.setText("Cadastrado")

            except:
                CADASTRAR.aviso.setText("erro na adição dos dados")
        else:
            CADASTRAR.aviso.setText("Senhas diferentes")

def autenticando_login ():
    usuario=LOGIN.C_usuario.text()
    senha=LOGIN.C_senha.text()
    comandoSQL="  SELECT senha FROM  aluno WHERE  nome= '"+ usuario +"'; "

    try:
        cursor=conexão.cursor()
        cursor.execute(comandoSQL)
        senha_bd=cursor.fetchall()

        if senha_bd[0][0]==senha:
            chama_perfil(usuario)

                    
        else: 
            LOGIN.C_aviso.setText("Dados de login incorretos!!!!")

    except:  
        LOGIN.C_aviso.setText("Dados de login invalidos!!")

def chama_editar_usuario():
    DADOS_CONTA.close()
    EDITAR_USER.show()

    global edit_nome, edit_e_mail, edit_senha, edit_c_senha


    EDITAR_USER.C_usuario.setText(nome_aluno_str)
    EDITAR_USER.C_email.setText(e_mail_aluno_str)
    EDITAR_USER.C_senha.setText(senha_usuario_str)
    EDITAR_USER.C_ConfirmarSenha.setText(senha_usuario_str)


    EDITAR_USER.Editar_nome.clicked.connect(editar_nome_user)
    EDITAR_USER.Editar_email.clicked.connect(editar_email_user)
    EDITAR_USER.Editar_senha.clicked.connect(editar_senha_user)
    EDITAR_USER.Excluir_usuario.clicked.connect(excluir_user)
    EDITAR_USER.voltar.clicked.connect(chama_dados_conta)

def editar_nome_user():

    edit_nome = EDITAR_USER.C_usuario.text()

    print(edit_nome)

    comandoSQL = " UPDATE aluno SET nome = %s WHERE id = %s"
    valores=(edit_nome,id_global)
    try: 
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL,valores)
        conexão.commit()
        cursor.close()
        EDITAR_USER.aviso.setText("Atualizado")
    except:
        EDITAR_USER.aviso.setText("erro ao atualizar dados")

def editar_email_user():

    edit_e_mail = EDITAR_USER.C_email.text()

    print(edit_e_mail)

    comandoSQL = " UPDATE aluno SET e_mail = %s WHERE id = %s"
    valores=(edit_e_mail,id_global)
    try: 
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL,valores)
        conexão.commit()
        cursor.close()
        EDITAR_USER.aviso.setText("Atualizado")
    except:
        EDITAR_USER.aviso.setText("erro ao atualizar dados")

def editar_senha_user():
    edit_senha = EDITAR_USER.C_senha.text()
    edit_c_senha = EDITAR_USER.C_ConfirmarSenha.text()
    
    if edit_c_senha==edit_senha:

        comandoSQL = " UPDATE aluno SET senha = %s WHERE id = %s"
        valores=(edit_senha,id_global)
        try: 
            cursor=conexão.cursor()  
            cursor.execute(comandoSQL,valores)
            conexão.commit()
            cursor.close()
            EDITAR_USER.aviso.setText("Atualizado")
        except:
            EDITAR_USER.aviso.setText("erro ao atualizar dados")
    else:
        EDITAR_USER.aviso.setText("Senhas são diferentes")

def excluir_user():

    comandoSQL = " DELETE FROM aluno WHERE id = '"+id_global+"'"
    try:
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL)
        conexão.commit()
        cursor.close()
        EDITAR_USER.close()
        LOGIN.show()
        LOGIN.C_aviso.setText("Usuario excluido")
    except:
        EDITAR_USER.aviso.setText("erro ao excluir usuario")



#
#
#
#
#
#
#                                      IMPORTANDO TELAS. 
#*****************************************************************************************************

app=QtWidgets.QApplication([])
LOGIN = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/LOGIN.ui")
Perfil = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/Perfil.ui")
CADASTRAR = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/CADASTRAR.ui")
EDITAR_OBJETIVO = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/EDITAR_OBJETIVO.ui")
MEUS_OBJETIVOS = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/MEUS_OBJETIVOS.ui")
DADOS_CONTA = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/DADOS_CONTA.ui")
EDITAR_USER = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/EDITAR_USER.ui")
ICAD_MATERIA = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/CAD_MATERIA.ui")
ICAD_ASSUNTO = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/CAD_ASSUNTO.ui")
ICAD_OBJETIVO = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/CAD_OBJETIVO.ui")
ICAD_CHAVE = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/CAD_CHAVE.ui")
MENSAGEM_CAD = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/MENSAGEM_CAD.ui")
MENSAGEM_CAD_2 = uic.loadUi ("/home/sthefany/Documentos/projetosco/TELAS.PY/MENSAGEM_CAD_2.ui")

#BOTOES NA TELA DE LOGIN
LOGIN.B_Entrar.clicked.connect(autenticando_login)
LOGIN.B_Cadastrar.clicked.connect(chama_cadastro)


LOGIN.show()
app.exec()
#*******************************************************************************************************def chama_assunto():