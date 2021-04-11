import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

class SafeData:

    def __init__(self):

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
        self.nombre=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form1, textvariable=self.nombre, width=58)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4)

        #Campo del precio del articulo
        self.label2=ttk.Label(self.form1, text="Precio del articulo:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.form1, textvariable=self.precio, width=58)
        self.entryPrecio.grid(column=1, row=1, padx=4, pady=4)

        #Campo de la descripcion del articulo
        self.label3=ttk.Label(self.form1, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form1, textvariable=self.descripcion, width=58)
        self.entryDescripcion.grid(column=1, row=2, padx=4, pady=4)

        #Boton crear
        self.boton1=ttk.Button(self.form1, text="Crear")
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
    
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
        self.id=tk.StringVar()
        self.entryid=ttk.Entry(self.form2, textvariable=self.id, width=25)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.form2, text="Consultar")
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

        #Mostrar datos

        #Creacion del formulario
        self.form3=ttk.LabelFrame(self.paginaConsulta, text="Tu producto")
        self.form3.grid(column=1, row=0, padx=0, pady=0)

        #Nombre     
        self.label2=ttk.Label(self.form3, text="Nombre del articulo:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form3, textvariable=self.nombre, state="readonly")
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4) 

        #Precio
        self.label3=ttk.Label(self.form3, text="Precio del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.form3, textvariable=self.precio, state="readonly")
        self.entryPrecio.grid(column=1, row=2, padx=4, pady=4)

        #Descripcion
        self.label3=ttk.Label(self.form3, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form3, textvariable=self.descripcion, state="readonly")
        self.entryDescripcion.grid(column=1, row=3, padx=4, pady=4)
    
    def listar(self):

        #Agregar la pestaña listar a la interface
        self.paginaLista = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.paginaLista, text="Listado completo")

        #Creacion del formulario
        self.form4=ttk.LabelFrame(self.paginaLista, text="Tus articulos guardados:")
        self.form4.grid(column=0, row=0, padx=5, pady=10)

        #Boton
        self.boton1=ttk.Button(self.form4, text="Listar")
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        #Area de listado
        self.scrolledtext1=st.ScrolledText(self.form4, width=95, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
    
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
        self.id=tk.StringVar()
        self.entryid=ttk.Entry(self.form5, textvariable=self.id, width=60)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        #Boton
        self.boton1=ttk.Button(self.form5, text="Borrar")
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

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
        self.id=tk.StringVar()
        self.entryid=ttk.Entry(self.form6, textvariable=self.id, width=25)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.form6, text="Consultar")
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

        #Creamos el formulario
        self.form7=ttk.LabelFrame(self.paginaActualizar, text="Tu producto")
        self.form7.grid(column=1, row=0, padx=5, pady=10)

        #Nombre     
        self.label2=ttk.Label(self.form7, text="Nombre del articulo:")
        self.label2.grid(column=0, row=0, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entryNombre=ttk.Entry(self.form7, textvariable=self.nombre)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4) 

        #Precio
        self.label3=ttk.Label(self.form7, text="Precio del articulo:")
        self.label3.grid(column=0, row=1, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.form7, textvariable=self.precio)
        self.entryPrecio.grid(column=1, row=1, padx=4, pady=4)

        #Descripcion
        self.label3=ttk.Label(self.form7, text="Descripcion del articulo:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.form7, textvariable=self.descripcion)
        self.entryDescripcion.grid(column=1, row=2, padx=4, pady=4)

        self.boton2=ttk.Button(self.form7, text="Modificar")
        self.boton2.grid(column=1, row=3, padx=4, pady=4)

userInterface = SafeData()