from tkinter import *
import tkinter as tk
from tkinter import ttk     # Ver si realmente se usa esta libreria
from tkinter import filedialog 
import webbrowser as wb
from Analizador2 import Analizador
from Graficador import Grafica

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
    global mensaje
    mensaje.set("Nuevo Fichero")
    texto.delete(1.0, "end")
    pass
def Abrir():
    global RutaAreaText
    VentanaP.configure(background="SlateGray1")    
    RutaAreaText   = filedialog.askopenfilename(initialdir='.', 
        filetype=(("ficheros de texto","*.txt"),),                      # solo se miran archivos del tipo txt
        title="Abrir Fichero de texto") 
    
    if RutaAreaText !="":
        fichero = open(RutaAreaText, 'r')
        contenido= fichero.read()
        texto.delete(1.0,'end')
        texto.insert("insert", contenido)
        fichero.close()
        VentanaP.title(RutaAreaText + "- Mi editor")
    print(RutaAreaText)
    texto.insert(0,RutaAreaText)
    
    pass
def Guardar():
    mensaje.set("Guardar Archivo")
    if RutaAreaText != "":
        Contenido = texto.get(1.0, 'end-1c') # end-1c → es para que no me agregue una linea 
        fichero = open(RutaAreaText, 'w+')
        fichero.write(Contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        Guardar_Como()
def Guardar_Como():
    global RutaAreaText
    mensaje.set("Guardar fichero como")
    fichero = filedialog.asksaveasfile(title='Guardar archico como ', mode='w', defaultextension=".txt")
    if fichero is not None:
        RutaAreaText = fichero.name
        Contenido = texto.get(1.0,'end-1c')
        fichero = open(RutaAreaText, 'w+')
        fichero.write(Contenido)
        fichero.close ()
        mensaje.set("Fichero guardado correctamente")
    else :
        mensaje.set("Error no se guardo")
        RutaAreaText=""
def Analizar():
    archivo = open(RutaAreaText, 'r')
    lineas = ''
    for i in archivo.readlines():
        lineas += i
    
    a = Analizador(lineas)
    a._compile()
    Grafica()


    mensaje.set("Analizar Fichero ")
    #Analisis.compilar(RutaAreaText)
def Errores():
    mensaje.set("Buscando errores en el fichero")
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
    print("Manual Usuario")
    wb.open(r'.\Documentacion\ManualTecnico.pdf')
    pass
def M_Usuario():
    wb.open(r'.\Documentacion\Manualusuario.pdf')
    pass
def T_Ayuda():
    wb.open(r'.\Documentacion\TemasAyuda.pdf')

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