import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox


class algoritmoVoraz:
    def wind1(self):
        self.ROOT = tk.Tk()
        self.ROOT.withdraw()
        # the input dialog
        self.USER_INP = simpledialog.askstring(title='Horario/Materias',
                                               prompt='¿Cuantas materias desea ingresar?')
        # check it out
        return(self.USER_INP)

    def wind2(self, n):
        self.ROOT = tk.Tk()
        self.ROOT.withdraw()
        # the input dialog
        self.USER_INP = simpledialog.askstring(title='Horario/Materias',
                                               prompt='Ingrese nombre de materia %d' % n)
        # check it out
        return(self.USER_INP)

    def wind3(self, n):
        self.ROOT = tk.Tk()
        self.ROOT.withdraw()
        # the input dialog
        self.USER_INP = simpledialog.askstring(title='Horario/Materias',
                                               prompt='Ingrese hora de Inicio %d:' % n)
        # check it out
        return(self.USER_INP)

    def wind4(self, n):
        self.ROOT = tk.Tk()
        self.ROOT.withdraw()
        # the input dialog
        self.USER_INP = simpledialog.askstring(title='Horario/Materias',
                                               prompt='Ingrese hora de Fin %d:' % n)
        # check it out
        return(self.USER_INP)

        # funcion para ordenar la lista de diccionarios
    def sortValuesByEndTime(n):
        return n['fin']

        # Algoritmo voraz para ordenar las materias, la
        # lista debe estar ordenada de menor a mayor
        # segun la hora de finalizacion
    def printMaxActivities(self,nombreMateria):
        n = len(nombreMateria)
        i = 0
		 # La primera actividad se selecciona
        messagebox.showinfo(
            'Su Horario es:', nombreMateria[i]['nombreMateria'])

       

        #print(nombreMateria[i]['nombreMateria'])

        # Se evaluan las demas actividades
        for j in range(n):

            # Si la materia inicia la hora igual o superior a la
            # hora fin de la anterior, se selecciona
            if nombreMateria[j]['inicio'] >= nombreMateria[i]['fin']:

                messagebox.showinfo('Materia: ',nombreMateria[j]['nombreMateria']),
                i = j

    def sol (self):
        nombreMateria = []
        
        numMaterias = self.wind1()

        for x in range(int(numMaterias)):

            nombreMateriaAux = self.wind2( x+1)
            inicioAux = self.wind3(x+1)
            finAux = self.wind4(x+1)
            # se ingresan los valores a un diccionario de datos dentro de una lista
            nombreMateria.append(
                {'inicio': inicioAux, 'fin': finAux, 'nombreMateria': nombreMateriaAux})

            self.printMaxActivities(nombreMateria)
