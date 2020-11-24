#Librerias para la interfaz grafica
from sqlite3.dbapi2 import Cursor
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#Libreria para la BD
import sqlite3
from algoritmoDeEncriptacion import claseEncriptado

des = claseEncriptado()
class Login:
    nombre_db = './db/loginDB.db'
    def __init__(self, window):
        
        # Initializations 
        self.wind = window
        self.wind.title('Login')

        # Creando contenedor
        frame = LabelFrame(self.wind, text = 'LOGIN')
        frame.grid(row = 0, column = 0, columnspan= 2, pady=3 )

        Label(frame,text = "Usuario:").grid(row = 1, column = 0)
        self.usuarios = Entry(frame)
        self.usuarios.focus()
        self.usuarios.grid(row = 1, column = 1)

        Label(frame,text = "Contraseña:").grid(row = 2, column = 0)
        self.claves = Entry(frame,show='*')
        self.claves.focus()
        self.claves.grid(row = 2, column = 1)

        Button (frame,text = "Login", command = self.login, width=25,padx=3,pady=3).grid(row =3, column =1)
        Button (frame,text = "Cerrar", command = self.quit, width=25,padx=3,pady=3).grid(row =4, column =1)
        

    def quit(self):
        self.wind.destroy()

    def ejecutar_Query(self, query, parametros = ()):#metodo para conectar a la BD
        with sqlite3.connect(self.nombre_db) as conn: #Guardando conexion en una variable
            self.cursor = conn.cursor() #Almacenando conexion/cursor en una variable, permite obtener la posicion en la BD
            #Cursor : instancia mediante la cual se puede invocar métodos que ejecutan declaraciones SQLite
            resultado = self.cursor.execute
            self.cursor.execute(query,parametros)
            conn.commit()
        return resultado

    def login(self):
        usuario = self.usuarios.get()

        clave = des.metodoEncriptacion(self.claves.get())
        query ='SELECT * from usuarios WHERE usuario = ? AND clave = ?'
        parametros = (usuario , clave)
        
        self.ejecutar_Query(query,parametros)

        if self.cursor.fetchall():
            messagebox.showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
            
        else:
            messagebox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
           

        

    
class Reg:

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Registro de Usuario')
        

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Registrar Nuevo Usuario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Nickname Input
        Label(frame, text = 'Nickname: ').grid(row = 1, column = 0)
        self.nickname = Entry(frame)
        self.nickname.focus()
        self.nickname.grid(row = 1, column = 1)

        # Contraseña 
        Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = Entry(frame,show="*")
        self.password.grid(row = 2, column = 1)
        
        # Confirmación Contraseña
        Label(frame, text = 'Confirmación: ').grid(row = 3, column = 0)
        self.passAux = Entry(frame, show="*")
        self.passAux.grid(row = 3, column = 1)

        # Button Add Product 
        ttk.Button(frame, text = 'Registrar', command = self.reg_usuario).grid(row = 4, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.messages = Label(self.wind,text = '', fg = 'red')
        self.messages.grid(row =6 , column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(self.wind,height = 6, columns = ('#0'))
        self.tree.grid(row = 5, column = 0, columnspan = 2)
    
        self.tree.heading('#0', text = 'NickName', anchor = CENTER)
        self.tree.heading('#1', text = 'Pass', anchor = CENTER)

        ttk.Button(self.wind,text = 'CERRAR', command = self.quit).grid(row = 7, columnspan = 2, sticky = W + E)

        self.consultar_Usuarios()

    def quit(self):
        self.wind.destroy()
    def validation(self):
        return len(self.nickname.get()) != 0 and len(self.password.get()) != 0 and len(self.passAux.get()) != 0 
    
    def run_query(self, query, parameters = ()):
        db_name = './db/loginDB.db' 
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def consultar_Usuarios(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM usuarios'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 3, text = row[1], values = (row[2]))
            
    def reg_user_aux(self, nick, passs):
        conAux = des.metodoEncriptacion(passs)
        query = 'INSERT INTO usuarios VALUES(NULL,?, ?)'
        parameters =  ( nick, conAux)
        self.run_query(query, parameters)

    def reg_usuario(self):
        if (self.validation()& (self.password.get() == self.passAux.get())):
            self.reg_user_aux(self.nickname.get(),self.password.get())
            self.messages['text'] = 'Usuario {} Agregado Satisfactoriamente'.format(self.nickname.get())
            messagebox.showinfo(title='Usuario Registrado', message='Usuario Registrado Correctamente.')
        else:
            messagebox.showwarning(title='Error', message='Error en el Registro, falta algun valor o las contraseñas no coinciden.')
        self.consultar_Usuarios()
    
    
       

class MenuLog:
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Menu')
        

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Menu')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

         # Documento Input
        Button(frame,  
                text ="Registro de Usuario",  
                command = self.openNewWindReg).grid(row = 1, columnspan = 2, sticky = W + E)
            
        Button(frame,  
                text ="Login",  
                command = self.openNewWindLog).grid(row = 2, columnspan = 2, sticky = W + E)
        
        Button(frame,  
                text ="CERRAR",  
                command = self.quit).grid(row = 3, columnspan = 2, sticky = W + E)

 
    def quit(self):
        self.wind.destroy()

    def openNewWindLog(self):
        window = Tk()
        aplicacion = Login(window)
        window.mainloop()

    def openNewWindReg(self):
        window = Tk()
        aplicacion = Reg(window)
        window.mainloop()
