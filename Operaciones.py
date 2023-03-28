import math
from fractions import Fraction 
class OPERADORES:
    def __init__(self):
        self.Operador = ""
        self.Hijos = 0
        self.Valor1 = 0
        self.Valor2 = 0
        self.Resultado = 0
        pass
    
    
    def _CorroborarOperadorV1 (self, _operador, _num):
        if _operador == '"Seno"':
            print("Seno1: " +str(_num))
            self.Resultado = math.sin(math.radians( _num))
            
        elif _operador == '"Coseno"':
            print("Coseno 1", str(_num))
            self.Resultado = math.cos(math.radians(_num))
        elif _operador == '"Tangente"':
            print("Tangente 1", str(_num))
            self.Resultado = math.tan(math.radians(_num))
        elif _operador == '"Inverso"':
            self.Resultado = Fraction(1/_num)
        return round(self.Resultado,2)
    
    def _CorroborarOperadorV2(self, _operador, _num1, _num2 ):

        if _operador == '"Suma"':
            self.Resultado =  _num1+_num2
        elif _operador == '"Resta"':
            self.Resultado = _num1-_num2
        elif _operador == '"Multiplicacion"':
            self.Resultado = _num1 * _num2
        elif _operador  == '"Division"':
            self.Resultado = _num1/_num2
        elif _operador == '"Potencia"':
            self.Resultado = _num1**_num2
        elif _operador == '"Raiz"':
            print ("entro a raiz" + " num1: "+str(_num1),"  -- num2:  "+ str(_num2))
            aux = 1/_num2
            self.Resultado = _num1**(1/_num2)
            #print(str(self.Resultado)+ "resulttttttttttt")
        elif _operador == '"Mod"':
            self.Resultado = _num1 % _num2
        return round(self.Resultado,2)


class Colores:
    def __init__(self):
        self.Color = ""
        self.ColorFinal = ""
    def AsignarColor(self, _Color):
        if _Color == 'Amarillo' or _Color == 'Yellow' or _Color =='amarillo' or _Color=='yellow':
            self.ColorFinal = 'Yellow'
        elif _Color == "Rojo" or _Color == 'Red' or _Color == 'rojo' or _Color =='red':
            self.ColorFinal = 'Red'
        elif _Color == "Negro" or _Color =='negro' or _Color=='Black' or _Color == 'black':
            self.ColorFinal = 'Black'
        elif _Color == "Azul":
            self.ColorFinal = 'Blue'
        else:
            self.ColorFinal = 'Yellow'                        
        return self.ColorFinal

class Formas:

    def __init__(self):
        self.Forma = ""
        self.FormaCorrecta = ""

    def _VerificarForma(self, _Forma1):
        self.FormaCorrecta = 'circle'
        if _Forma1 == 'Rectangulo'or _Forma1 =='Caja':
            self.FormaCorrecta ='box'
        elif _Forma1 =='Poligono':
            self.FormaCorrecta = 'polygon'
        elif _Forma1 == 'Elipse' or _Forma1=='elipse':
            self.FormaCorrecta = 'ellipse'
        elif _Forma1 == 'Circulo' or _Forma1=='circulo' or _Forma1== 'Circle' or _Forma1=='circle':
            self.FormaCorrecta = 'circle'
        elif _Forma1 == 'huevo' or _Forma1=='Huevo':
            self.FormaCorrecta = 'egg'
        elif _Forma1 == 'pentagono' or _Forma1== 'Pentagono':
            self.FormaCorrecta = 'pentagon'
        elif _Forma1 =='Cuadrado':
            self.FormaCorrecta = 'square'
        return self.FormaCorrecta
