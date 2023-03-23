import math
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
            self.Resultado = 1/_num
        return self.Resultado
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
            self.Resultado == _num1**(1/_num2)
        elif _operador == '"Mod"':
            self.Resultado == _num1 % _num2
        elif _operador == '"Seno"':
            self._CorroborarOperadorV1(_operador,_num1)
        return self.Resultado



