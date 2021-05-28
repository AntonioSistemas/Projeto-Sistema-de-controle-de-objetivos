import mysql.connector


def criandobd():

        conexão=mysql.connector.connect(
                host='localhost',
                user='root',
                password='', 
        )

        mycursor = conexão.cursor()
        mycursor.execute("CREATE DATABASE mydatabase")

        print("concluido")


