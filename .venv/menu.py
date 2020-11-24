from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *
from login import MenuLog
from algoritmoVoraz import algoritmoVoraz
s= algoritmoVoraz()
class Menu:
    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Menu')
        

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Menu')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

         # Documento Input
        Button(frame,  
                text ="Login (Algoritmo de encriptado)",  
                command = self.openNewWind).grid(row = 1, columnspan = 2, sticky = W + E)
            
        Button(frame,  
                text ="Organizar Horario (Algoritmo Voraz)",  
                command = self.openNewWind2).grid(row = 2, columnspan = 2, sticky = W + E)
        
        Button(frame,  
                text ="CERRAR",  
                command = self.quit).grid(row = 3, columnspan = 2, sticky = W + E)

 
    def quit(self):
        self.wind.destroy()

    def openNewWind(self):
        window = Tk()
        aplicacion = MenuLog(window)
        window.mainloop()

    def openNewWind2(self):
        s.sol()


    # sets the geometry of main  
    # root window 
     
   
    
    
    
    
    # a button widget which will open a  
    # new window on button click 
if __name__ == '__main__':
    window = Tk()
    application = Menu(window)
    window.mainloop()
