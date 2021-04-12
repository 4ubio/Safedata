import mysql.connector

def database():

    #Creamos la base de datos
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="SafeData",
        port=3306
    )

    return database
