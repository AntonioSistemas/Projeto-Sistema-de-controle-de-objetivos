import mysql.connector


conexão=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='projeto_sco'
)

def cadastrar_usuario(nome, e_mail, senha):
 
                comandoSQL = """ INSERT INTO usuário(nome, e_mail, senha) 
                                 VALUES (%s,%s,%s )"""
                valores=(nome,e_mail,senha)
                try:
                        cursor=conexão.cursor()
                        cursor.execute(comandoSQL,valores)
                        #mostrar mensagem de adicionado
                        conexão.commit()
                except:
                        print("houve erro na adição dos dados")
                        cursor.rollback()
                        cursor.close()


