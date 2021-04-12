from db import database

class Articulos:

    #Creamos la conexion a la base de datos
    def conectar(self):
        conexion = database()
        return conexion
    
    def crear(self, datos):

        #Nos conectamos
        connect=self.conectar()

        #Creamos un cursos
        cursor=connect.cursor()

        #Escribimos el query
        sql="INSERT INTO Articulos(nombre, precio, descripcion) VALUES (%s,%s,%s)"

        #Ejecutamos el query
        cursor.execute(sql, datos)

        #Guardamos y cerramos
        connect.commit()
        connect.close()
    
    def consulta(self, datos):

        #Nos conectamos
        connect=self.conectar()

        #Creamos un cursos
        cursor=connect.cursor()

        #Escribimos el query
        sql="SELECT nombre, precio, descripcion FROM Articulos WHERE id=%s"

        #Ejecutamos el query
        cursor.execute(sql, datos)

        return cursor.fetchall()
    
    def listar(self):

        #Nos conectamos
        connect=self.conectar()

        #Creamos un cursos
        cursor=connect.cursor()

        #Escribimos el query
        sql="SELECT id, nombre, precio, descripcion FROM Articulos"

        #Ejecutamos el query
        cursor.execute(sql)

        return cursor.fetchall()
    
    def borrar(self, datos):

        #Nos conectamos
        connect=self.conectar()

        #Creamos un cursos
        cursor=connect.cursor()

        #Escribimos el query
        sql="DELETE FROM Articulos WHERE id=%s"

        #Ejecutamos el query
        cursor.execute(sql, datos)

        #Guardamos y cerramos
        connect.commit()
        connect.close()

        return cursor.rowcount
    
    def modificacion(self, datos):
        
        #Nos conectamos
        connect=self.conectar()

        #Creamos un cursos
        cursor=connect.cursor()

        #Escribimos el query
        sql="UPDATE Articulos SET nombre=%s, precio=%s, descripcion=%s WHERE id=%s"
        
        #Ejecutamos el query
        cursor.execute(sql, datos)

        #Guardamos y cerramos
        connect.commit()
        connect.close()

        return cursor.rowcount