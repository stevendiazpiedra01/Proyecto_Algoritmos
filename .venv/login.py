#Librerias para la interfaz grafica
from sqlite3.dbapi2 import Cursor
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *
#Libreria para la BD
import sqlite3
from .algoritmoDeEncriptacion import claseEncriptado

class Login:
    des = claseEncriptado()
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
        self.claves = Entry(frame)
        self.claves.focus()
        self.claves.grid(row = 2, column = 1)

        Button (text = "Login", command = self.login, width=25,padx=3,pady=3).grid(row =1 , column =1)
        


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
        clave = self.claves.get()
        query ='SELECT * from usuarios WHERE usuario = ? AND clave = ?'
        parametros = (usuario , clave)
        self.ejecutar_Query(query,parametros)

        if self.cursor.fetchall():
            showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
        else:
            showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")

if __name__ == '__main__':
    window = Tk()
    aplicacion = Login(window)
    window.mainloop()
