# Tenemos que ver donde en si se alimenta la ruta y las lineas 
# Ver como funciona bien bien el codigo 
#------------------------------------------------------------------------------
ruta = "C:/Users/Luisa/Documents/Proyectos 2023/Doc3.txt"
archivo = open(ruta, 'r')
lineas = ''
for i in archivo.readlines():
    lineas += i

print(lineas)
#------------------------------------------------------------------------------
from Operaciones import OPERADORES



class Analizador:

    def __init__(self, entrada:str): 
            self.lineas = entrada
            self.pos = 0        # POSICION DE LOS CARACTERES DE ENTRADA 
            self.fila = 0       # FILA ACTUAL DE LA LINEA
            self.columna = 0    # COLUMNA ACTUAL  DEL CARACTER
            self.LErrores = []  # Donde se va a guardar 
            
    def _token(self, token:str, estado_actual:str, estado_sig:str):
            if self.lineas[self.pos] != " ":
                text = self._juntar(self.pos, len(token))   # Junta los caracteres 
                if self._analizar(token, text):        # analiza el token la entrada
                    self.pos += len(token)-1
                    self.columna += len(token)-1
                    return estado_sig
                else:
                     return 'ERROR'  # Eror en el orden?
            else:
                 return estado_actual

    def _juntar(self, pos:int, _count:int):
            try:
                tmp = ''
                for i in range ( pos, pos +_count):
                      tmp += self.lineas[i]
                return tmp
            except:
                  return None
                     
    def _analizar(self, token, texto):
        try:
            cont = 0
            token_tmp = ""
            for i in texto:   # i recorre los caractere del texto de entrada
                    # CUANDO LA LETRA HACE MATCH CON EL TEXTO EMTRA 
                if str(i) == str(token[cont]):
                    token_tmp += i 
                    cont += 1
                else: 
                    #print('ERROR1')     # ERROR de entrada o caracter no reconocido 
                    return False    
            print(f'**************** ENCONTRE -- {token_tmp}   *******************')
            return True

        except:
            print('ERROR2')
            return False
        
    def _digito(self, estado_sig):
        estado_actual = 'D0'
        numero= ""
        while self.lineas[self.pos] != "":
            
            # CAMBIO DE LINEA O DE FILA
            if self.lineas[self.pos] == '\n':
                self.fila += 1
                self.columna = 0
            
            # PARA SALIRSE 
            elif str(self.lineas[self.pos]) == '"':
                self.pos -=1
                return [estado_sig, numero]
            elif str(self.lineas[self.pos]) == ']':
                self.pos -=1
                return [estado_sig, numero]
            elif str(self.lineas[self.pos]) == '}':
                self.pos -=1
                return [estado_sig, numero]
            
            # PARA VER SI ES DECIMAL
            elif self.lineas[self.pos] == '.':
                token = "."
                if estado_actual == 'D2' or estado_actual == 'D0':
                     estado_actual = 'ERROR'
                elif self.lineas[self.pos] != ' ':
                     text = self._juntar(self.pos, len(token))
                     if self._analizar(token,text):
                          numero += text
                          estado_actual = 'D2'
                          self.pos += len(token)-1
                          self.columna += len(token)-1
                     else:
                          estado_actual = 'ERROR'

            # D0 -> [0-9] D0
            elif estado_actual =='D0' or estado_actual == 'D1':
                 if self.lineas != ' ':
                    estado_actual = 'ERRROR'
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                         token= i
                         text = self._juntar(self.pos, len(token)) 
                         if self._analizar(token,text):
                              numero += text
                              estado_actual = 'D1'
                              break
                         
            # D2 [0-9] D2
            elif estado_actual == 'D2':
                 if self.lineas[self.pos] != ' ':
                      estado_actual = 'ERRROR'
                      for i in ['0','1','2','3','4','5','6','7','8','9']:
                           text = self._juntar(self.pos, len(i))
                           if self._analizar(i, text):
                                numero += text
                                estado_actual = 'D2'
                                break
            # ERRORES 
            if estado_actual == 'ERROR':
                return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.pos < len(self.lineas) - 1:
                self.pos +=1
            else:
                break

    def _operaciones (self, estado_sig):
        estado_actual = 'S2'
        hijo_derecho =""
        hijo_izquierdo =""
        while self.lineas[self.pos] != "":
            if self.lineas[self.pos] == '\n':
                self.fila +=1
                self.columna=0

            # ----------------------
            # Estados

            

            # S2 → "Operacion" S3
            elif estado_actual == 'S2':
                 estado_actual = self._token('"Operacion"', 'S2', 'S3')
            
            # S3 → : S4
            elif estado_actual == 'S3':
                 estado_actual = self._token(':','S3','S4')

            # S4 → Operador S5
            elif estado_actual == 'S4':
                 operadores  = ['"Suma"', '"Resta"', '"Multiplicacion"', '"Division',
                                '"Potencia"', '"Raiz"', '"Inverso"', '"Mod"',
                                '"Seno"', '"Tangente"', '"Coseno"']
                 for i in operadores:
                    estado_actual = self._token(i,'S4', 'S5')
                    if estado_actual != 'ERROR':
                         operador = i 
                         break
            # S5 → "Valor1" S6
            elif estado_actual == 'S5':
                 estado_actual = self._token('"Valor1"', 'S5', 'S6')

            # S6 → : S7
            elif estado_actual == 'S6':
                 estado_actual = self._token(':', 'S6','S7')
            
            # S7 → DIGITO S10
            #    | [ S8
            elif estado_actual == 'S7':
                 estado_actual = self._token('[','S7','S8')
                 if estado_actual == 'ERROR':
                    estado_actual = 'S10'
                    a = self._digito('S10')
                    if "ERROR" == a[0]:
                         estado_actual = 'ERRROR'
                    elif a[0] == 'S10':
                        hijo_izquierdo = a[1]
                    
            # S8 → S2 S9
            elif estado_actual == 'S8':
                a =  self._operaciones('S9')
                estado_actual = a[0]
                hijo_izquierdo =a[1]

            # S9 → ] S10
            elif  estado_actual == 'S9':
                 estado_actual = self._token(']','S9','S10')
                
            # S10 → "Valor2" S11
            elif estado_actual == 'S10':
                 if (operador =='"Seno"') or (operador=='"Coseno"')or(operador=='"Tangente"')or ( operador=='"Inverso"'):
                      self.pos -=1
                      # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                      print("\t*****OPERACION ARITMETICA*****")
                      print('\t',operador ,'(',hijo_izquierdo ,')' )
                      print('\t*******************************\n')
                      ope = OPERADORES(operador,1)
                      result = ope._CorroborarOperadorV1(operador, int(hijo_izquierdo))
                      print( result)
                      #a[1]= result # Este lo agregue yo 
                      op = operador +'('+str(result) +')'
                      return ['S15', op]  
                 else:
                      estado_actual = self._token('"Valor2"','S10','S11')
            
            # S11 → : S12
            elif estado_actual == 'S11':
                 estado_actual = self._token(':','S11','S12')

            
            # S12 → DIGITO S15
            #  | [ S13
            elif estado_actual == "S12":
                estado_actual = self._token('[', 'S12', 'S13')
                if estado_actual == 'ERROR':
                    estado_actual = 'S15'
                    a = self._digito('S15')
                    if "ERROR" == a[0]:
                        estado_actual = 'ERROR'
                    elif 'S15' == a[0]:
                        hijo_derecho = a[1]
                        # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                        print("\t*****OPERACION ARITMETICA*****")
                        print('\t',hijo_izquierdo , operador, hijo_derecho)
                        print('\t*******************************\n')
                        op = hijo_izquierdo + operador + hijo_derecho
                        return [estado_sig, op]  

            # S13 → S2 S14
            elif estado_actual == 'S13':
                estado_actual = 'S14'
                a = self._operaciones('S14')
                hijo_derecho = a[1]
                if "ERROR" == a[0]:
                     estado_actual = 'ERROR'

            # S14 → ] S15
            elif estado_actual == 'S14':
                estado_actual = self._token(']', 'S14','S15')
                # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                print("\t*****OPERACION ARITMETICA*****")
                print('\t',hijo_izquierdo , operador, hijo_derecho)
                print('\t*******************************\n')
                op = hijo_izquierdo + operador + hijo_derecho
                return [estado_sig, op]  





            # ERRORES 
            if estado_actual == 'ERROR':
                print("********************************")
                print("\tERROR")
                print("********************************")
                # ERROR
                #self.guardarErrores(self.lineas[self.index], self.fila, self.columna)
                return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.pos < len(self.lineas) - 1:
                self.pos +=1
            else:
                break
    def _compile(self):
        global a
        estado_actual = 'S0'
        while self.lineas[self.pos] != "":
            if self.lineas[self.pos] == '\n':
                 self.fila +=1
                 self.columna =0

            # S0 → { S1
            elif estado_actual == 'S0':
                 estado_actual = self._token('{', 'S0','S1')
            # S1 → { S2
            elif estado_actual == 'S1':
                 estado_actual =self._token('{', 'S1','S2')
            # S2 "Operacion "S3
            elif estado_actual == 'S2':
                if self.lineas[self.pos] != " ":
                     print("Lineas Ver "+str(self.lineas))
                     a = self._operaciones('S15')
                     estado_actual = a[0]
                     print("\t*****RESULTADO*****")
                     print('\t',a[1])
                     print('\t*******************************\n')
            
            # S15 → } S16  
            elif estado_actual == 'S15':
                 estado_actual = self._token('}','S15','S16')
            
            # S16 → , 
            #   | } S17
            elif estado_actual == 'S16':
                if self.lineas != ' ':
                     estado_actual = self._token(',', 'S16','S1') 
            
            elif estado_actual == 'S17':
                 break
            
            # ERRORES 
            if estado_actual == 'ERROR':
                #print('\t AQUI OCURRIO UN ERROR')
                estado_actual = 'S0'
            
            #INCREMENTAR POSICION
            if self.pos < len(self.lineas) - 1:
                self.pos +=1
            else:
                break
 
a = Analizador(lineas)
a._compile()
        
                        

                    

                 