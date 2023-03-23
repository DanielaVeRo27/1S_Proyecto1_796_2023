import math
class OPERADORES:
    def __init__(self):
        self.Operador = ""
        self.Hijos = 0
        self.Valor1 = 0
        self.Valor2 = 0
        self.Resultado = 0
        pass
    
    def _CorroborarOperador(self, Valor1, Valor2):        
        if self.Hijos == 1:
            self._CorroborarOperadorV1(self.Operador, self.Valor1)
    def _CorroborarOperadorV1 (self, _operador, _num):
        if _operador == '"Seno"':
            print("Seno1: " +str(_num))
            self.Resultado = math.sin(_num)
        elif _operador == '"Coseno"':
            print("Coseno 1", str(_num))
        elif _operador == '"Tangente"':
            print("Tangente 1", str(_num))
            pass 
        return self.Resultado
def _CorroborarOperador2(self, _operador, _num1, _num2 ):

    if _operador == "Suma":

        pass



