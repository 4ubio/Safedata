import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class SafeData:

    def __init__(self):
        self.articulo1=articulos.Articulos()

        #Informacion y creacion de la ventana
        self.ventana = tk.Tk()
        self.ventana.title("SafeData")
        self.ventana.resizable(0,0)

        #IMPORTANTE. aqui se agregan pestañas
        self.cuaderno = ttk.Notebook(self.ventana)       

        #Pestañas de la aplicacion 
        self.crear()
        self.consultar()
        self.listar()
        self.borrar()
        self.actualizar()

        #Grid a las pestañas
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)

        #IMPORTANTE
        self.ventana.mainloop()
    
    #Pestaña crear
    def crear(self):

        #Agregar la pestaña crear a la interface
        self.paginaCrear = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaCrear, text="Crear articulo")

        #Creacion del formulario
        self.form1=ttk.LabelFrame(self.paginaCrear, text="Ingresa los siguientes datos: ")        
        self.form1.grid(column=0, row=0, padx=0, pady=0)

        #Campo del nombre del articulo
        self.label1=ttk.Label(self.form1, text="Nombre del articulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombreCrear=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form1, textvariable=self.nombreCrear, width=58)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4)

        #Campo del precio del articulo
        self.label2=ttk.Label(self.form1, text="Precio del articulo:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.precioCrear=tk.IntVar()
        self.entryPrecio=ttk.Entry(self.form1, textvariable=self.precioCrear, width=58)
        self.entryPrecio.grid(column=1, row=1, padx=4, pady=4)

        #Campo de la descripcion del articulo
        self.label3=ttk.Label(self.form1, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.descripcionCrear=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form1, textvariable=self.descripcionCrear, width=58)
        self.entryDescripcion.grid(column=1, row=2, padx=4, pady=4)

        #Boton crear
        self.boton1=ttk.Button(self.form1, text="Crear", command=self.crearArticulo)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
    
    #funcion para crear articulos
    def crearArticulo(self):

        try:
            #Guardar lo obtenido en una tupla
            datos=(self.nombreCrear.get(), self.precioCrear.get(), self.descripcionCrear.get())

            if self.nombreCrear.get() == '' or self.precioCrear.get() == '' or self.descripcionCrear.get() == '':
                mb.showerror("Error", "Debes llenar todos los campos")
            else:
                #Mandar lo obtenido
                self.articulo1.crear(datos)

                #Mostrar mensaje de exito
                mb.showinfo("Información", "Los datos fueron cargados")

                #Volver a dejar los valores en blanco
                self.nombreCrear.set("")
                self.precioCrear.set("")
                self.descripcionCrear.set("")

        except:
            mb.showerror("Error", "Debes ingresar un número")
            self.nombreCrear.set("")
            self.precioCrear.set("")
            self.descripcionCrear.set("")

    def consultar(self):

        #Agregar la pestaña consultar a la interface
        self.paginaConsulta = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaConsulta, text="Consulta por ID")

        #Creacion del formulario
        self.form2=ttk.LabelFrame(self.paginaConsulta, text="Ingresa el ID del articulo")
        self.form2.grid(column=0, row=0, padx=0, pady=0)

        #Campo del ID del articulo
        self.label1=ttk.Label(self.form2, text="ID del articulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idConsulta=tk.IntVar()
        self.entryid=ttk.Entry(self.form2, textvariable=self.idConsulta, width=25)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.form2, text="Consultar", command=self.consultaArticulo)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

        #Mostrar datos

        #Creacion del formulario
        self.form3=ttk.LabelFrame(self.paginaConsulta, text="Tu producto")
        self.form3.grid(column=1, row=0, padx=0, pady=0)

        #Nombre     
        self.label2=ttk.Label(self.form3, text="Nombre del articulo:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombreConsulta=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form3, textvariable=self.nombreConsulta, state="readonly")
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4) 

        #Precio
        self.label3=ttk.Label(self.form3, text="Precio del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precioConsulta=tk.IntVar()
        self.entryPrecio=ttk.Entry(self.form3, textvariable=self.precioConsulta, state="readonly")
        self.entryPrecio.grid(column=1, row=2, padx=4, pady=4)

        #Descripcion
        self.label3=ttk.Label(self.form3, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.descripcionConsulta=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form3, textvariable=self.descripcionConsulta, state="readonly")
        self.entryDescripcion.grid(column=1, row=3, padx=4, pady=4)
    
    def consultaArticulo(self):

        try:
            #Obtenemos el ID
            datos=(self.idConsulta.get(), )

            if self.idConsulta.get() == '':
                mb.showerror("Error", "Debes ingresar un ID")
                self.idConsulta.set('')
                self.nombreConsulta.set('')
                self.precioConsulta.set('')
                self.descripcionConsulta.set('')

            else:
                #Ejecutamos la consulta con el ID, nos devolvera una tupla con los datos requeridos
                respuesta=self.articulo1.consulta(datos)

        except:
            mb.showerror("Error", "Debes ingresar un número o un ID")
            self.idConsulta.set('')
            self.nombreConsulta.set('')
            self.precioConsulta.set('')
            self.descripcionConsulta.set('')
        
        #Llenara los campos del articulo
        if len(respuesta)>0:
            self.nombreConsulta.set(respuesta[0][0])
            self.precioConsulta.set(respuesta[0][1])
            self.descripcionConsulta.set(respuesta[0][2])
        else:
            self.idConsulta.set('')
            self.nombreConsulta.set('')
            self.precioConsulta.set('')
            self.descripcionConsulta.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    
    def listar(self):

        #Agregar la pestaña listar a la interface
        self.paginaLista = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaLista, text="Listado completo")

        #Creacion del formulario
        self.form4=ttk.LabelFrame(self.paginaLista, text="Tus articulos guardados:")
        self.form4.grid(column=0, row=0, padx=5, pady=10)

        #Boton
        self.boton1=ttk.Button(self.form4, text="Actualizar", command=self.listarArticulos)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        #Area de listado
        self.scrolledtext1=st.ScrolledText(self.form4, width=95, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
    
    def listarArticulos(self):

        #Obtenemos datos de la consulta
        respuesta=self.articulo1.listar()
        self.scrolledtext1.delete("1.0", tk.END)

        #Con ayuda del ciclo for, imprimimos cada articulo guardado
        for Articulo in respuesta:
            self.scrolledtext1.insert(tk.END, "ID: " + str(Articulo[0]) +
                                              "\nNombre: " + Articulo[1] +
                                              "\nPrecio: " + str(Articulo[2]) +
                                              "\nDescripcion: " + str(Articulo[3])+"\n\n")
    
    def borrar(self):

        #Agregar la pestaña borrar a la interface
        self.paginaBorrar = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaBorrar, text="Borrar artículos")

        #Creacion del formulario
        self.form5=ttk.LabelFrame(self.paginaBorrar, text="Ingresa el ID del articulo a borrar")        
        self.form5.grid(column=0, row=0, padx=5, pady=10)

        #Campo de los datos
        self.label1=ttk.Label(self.form5, text="ID del articulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idBorrar=tk.IntVar()
        self.entryid=ttk.Entry(self.form5, textvariable=self.idBorrar, width=60)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        #Boton
        self.boton1=ttk.Button(self.form5, text="Borrar", command=self.borrarArticulo)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrarArticulo(self):
        
        try:
            #Obtenemos el id
            datos=(self.idBorrar.get(), )

            if self.idBorrar.get() == '':
                mb.showerror("Error", "Debes ingresar un ID")
            else:
                #Obtenemos datos de la consulta
                cantidad=self.articulo1.borrar(datos)
            
        except:
            mb.showerror("Error", "Debes ingresar un número")
            self.idBorrar.set('')

        #Mostramos mensaje en pantalla
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
            self.idBorrar.set('')
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def actualizar(self):

        #Agregar la pestaña actualizar a la interface
        self.paginaActualizar = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaActualizar, text="Actualizar artículo")

        #Creamos el formulario
        self.form6=ttk.LabelFrame(self.paginaActualizar, text="Ingresa el ID del articulo a modificar")
        self.form6.grid(column=0, row=0, padx=5, pady=10)

        #Campo del ID del producto
        self.label1=ttk.Label(self.form6, text="ID del articulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idActualizar=tk.IntVar()
        self.entryid=ttk.Entry(self.form6, textvariable=self.idActualizar, width=25)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.form6, text="Consultar", command=self.consultaActualizar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

        #Creamos el formulario
        self.form7=ttk.LabelFrame(self.paginaActualizar, text="Tu producto")
        self.form7.grid(column=1, row=0, padx=5, pady=10)

        #Nombre     
        self.label2=ttk.Label(self.form7, text="Nombre del articulo:")
        self.label2.grid(column=0, row=0, padx=4, pady=4)
        self.nombreActualizar=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form7, textvariable=self.nombreActualizar)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4) 

        #Precio
        self.label3=ttk.Label(self.form7, text="Precio del articulo:")
        self.label3.grid(column=0, row=1, padx=4, pady=4)
        self.precioActualizar=tk.IntVar()
        self.entryPrecio=ttk.Entry(self.form7, textvariable=self.precioActualizar)
        self.entryPrecio.grid(column=1, row=1, padx=4, pady=4)

        #Descripcion
        self.label3=ttk.Label(self.form7, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.descripcionActualizar=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form7, textvariable=self.descripcionActualizar)
        self.entryDescripcion.grid(column=1, row=2, padx=4, pady=4)

        self.boton2=ttk.Button(self.form7, text="Modificar", command=self.actualizarArticulo)
        self.boton2.grid(column=1, row=3, padx=4, pady=4)

    def actualizarArticulo(self):

        try:
            #Obtenemos los datos
            datos=(self.nombreActualizar.get(), self.precioActualizar.get(), self.descripcionActualizar.get(), self.idActualizar.get())
            
            if self.nombreActualizar.get() == '' or self.precioActualizar.get() == '' or self.descripcionActualizar.get() == '':
                mb.showerror("Error", "Debes llenar todos los campos.")
            else:
                cantidad=self.articulo1.modificacion(datos)

        except:
            mb.showerror("Error", "Posibles errores:\nPrimero debes ingresar el ID del articulo.\nDebes llenar todos los campos.\nEn el campo de precio, debes ingresar un numero.")
            self.nombreActualizar.set('')
            self.precioActualizar.set('')
            self.descripcionActualizar.set('')

        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
            self.idActualizar.set('')
            self.nombreActualizar.set('')
            self.precioActualizar.set('')
            self.descripcionActualizar.set('')
        else:
            mb.showerror("Error", "Posibles errores:\nNo se ha actualizado nada.")
    
    def consultaActualizar(self):

        try:
            #Obtenemos el ID
            datos=(self.idActualizar.get(), )

            if self.idActualizar.get() == '':
                mb.showerror("Error", "Debes ingresar un ID")
            else:
                #Ejecutamos la consulta con el ID, nos devolvera una tupla con los datos requeridos
                respuesta=self.articulo1.consulta(datos)

        except:
            mb.showerror("Error", "Debes ingresar un número o un ID")
            self.idActualizar.set('')
        
        #Llenara los campos del articulo
        if len(respuesta)>0:
            self.nombreActualizar.set(respuesta[0][0])
            self.precioActualizar.set(respuesta[0][1])
            self.descripcionActualizar.set(respuesta[0][2])
        else:
            self.idActualizar.set('')
            self.nombreActualizar.set('')
            self.precioActualizar.set('')
            self.descripcionActualizar.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")


userInterface = SafeData()