from tkinter import *
import tkinter as tk
from tkinter import ttk     # Ver si realmente se usa esta libreria 

RutaAreaText =""

VentanaP = tk.Tk()
VentanaP.title("PROYECTO 1 (Scanner)")
VentanaP.geometry("745x478")
VentanaP.configure(background="MistyRose2")

MenuOpc = Menu(VentanaP)
VentanaP.config(menu=MenuOpc)
# Caja de texto Central 
texto = Text(VentanaP)
texto.place(x=10, y=10)
texto.config(padx=2, pady=3, bd=0, font=("Consolas", 12),background="thistle")
texto.pack(fill="both", expand=1)

def Nuevo():
    pass
def Abrir():
    pass
def Guardar():
    pass
def Guardar_Como():
    pass
def Analizar():
    pass
def Errores():
    pass

ArchivoOpc  = Menu(MenuOpc, tearoff=0)
ArchivoOpc.add_command(label="Nuevo", command=Nuevo)
ArchivoOpc.add_command(label="Abrir", command=Abrir)
ArchivoOpc.add_command(label="Guardar", command=Guardar)
ArchivoOpc.add_command(label="Guardar Como", command=Guardar_Como)
ArchivoOpc.add_command(label="Analizar", command=Analizar)
ArchivoOpc.add_command(label="Errores", command=Errores)
ArchivoOpc.add_separator()
ArchivoOpc.add_command(label="SALIR", command=VentanaP.quit)

def M_Tecnico():
    pass
def M_Usuario():
    pass
def T_Ayuda():
    pass

HelpOpc = Menu(MenuOpc, tearoff=0)
HelpOpc.add_command(label="Manual de Usuario", command=M_Usuario)
HelpOpc.add_command(label="Manual Tecnico", command=M_Tecnico)
HelpOpc.add_command(label="Temas de Ayuda ", command=T_Ayuda)

MenuOpc.add_cascade(label="Archivo", menu=ArchivoOpc)
MenuOpc.add_cascade(label="Ayuda", menu=HelpOpc)




# Monitor inferior 
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor ")
monitor = Label(VentanaP, textvar=mensaje, justify='left')
monitor.pack(side='left')
VentanaP.mainloop()