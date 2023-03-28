# Tenemos que ver donde en si se alimenta la ruta y las lineas 
# Ver como funciona bien bien el codigo 
# "C:/Users/Luisa/Documents/Proyectos 2023/Doc.txt"
#------------------------------------------------------------------------------
from Graficador import GeneraNodo,GeneraRelacion,Grafica,Atrib_Grafica

"""ruta = "C:/Users/Luisa/Documents/Proyectos 2023/Doc4.txt"
archivo = open(ruta, 'r')
lineas = ''
for i in archivo.readlines():
    lineas += i

print(lineas)"""
#------------------------------------------------------------------------------
from Operaciones import OPERADORES, Colores, Formas
from Reporte import Reporte1

Colors = Colores()
ope = OPERADORES()
Formitas = Formas ()
global OperacionT
OperacionT = "X"
OperacionTA = "S"
Valor2An = False
Valor1An = False
HijoPen2 = False
HijoPen1 = False
Poper = 0
Palabras = ""
Color_Nodo = ""
Color_Letra = ""
Forma_Nodo = ""


class Analizador:
    
    def __init__(self, entrada:str): 
            self.lineas = entrada
            self.pos = 0        # POSICION DE LOS CARACTERES DE ENTRADA 
            self.fila = 0       # FILA ACTUAL DE LA LINEA
            self.columna = 0    # COLUMNA ACTUAL  DEL CARACTER
            self.LErrores = []  # Donde se va a guardar 
            self.contE= 0
            
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
            #print(f'**************** ENCONTRE -- {token_tmp}   *******************')
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
        global BLuis,Valor1An,Valor2An,HijoPen1,HijoPen2,Poper
        global OperacionT,OperacionTA, estado_anterior
        BLuis = "X"
        estado_anterior = "S2"  
        estado_Auxiliar = False
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
                 if estado_actual == 'Error':
                     estado_anterior = 'S3'
            
            # S3 → : S4
            elif estado_actual == 'S3':
                 estado_actual = self._token(':','S3','S4')

            # S4 → Operador S5
            elif estado_actual == 'S4':
                 
                 operadores  = ['"Suma"', '"Resta"', '"Multiplicacion"', '"Division"',
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
                if estado_actual == 'ERROR':
                    print("AQUI FUE EL ERROR")
                    estado_anterior = 'S5'
                
                

            # S6 → : S7
            elif estado_actual == 'S6':
                 estado_actual = self._token(':', 'S6','S7')
            
            # S7 → DIGITO S10
            #    | [ S8
            elif estado_actual == 'S7':
                 estado_actual = self._token('[','S7','S8')
                 if estado_actual == 'ERROR':
                    #print("S7 Valor1 sin anidado "+estado_actual)
                    estado_actual = 'S10'                    
                    a = self._digito('S10')
                    if "ERROR" == a[0]:
                         estado_Auxiliar = False
                         estado_actual = 'ERRROR'
                    elif a[0] == 'S10':
                        hijo_izquierdo = a[1]                       
                        #print("Dato sin E "+estado_actual)     
                 else:
                    print("S7 Valor1 con anidado "+estado_actual)
                 if estado_actual == 'S8':
                    Valor1An = True
                   
                    
            # S8 → S2 S9
            elif estado_actual == 'S8':
                #print("S8 Aqui entra ? "+estado_actual)
                a =  self._operaciones('S9')                
                estado_actual = a[0]
                hijo_izquierdo =a[1]
                #print(str(hijo_izquierdo))
                estado_Auxiliar = True

            # S9 → ] S10
            elif  estado_actual == 'S9':
                 estado_actual = self._token(']','S9','S10')
                 if estado_actual == 'ERROR':
                      pass
                
            # S10 → "Valor2" S11
            elif estado_actual == 'S10':
                 estado_actual1 = self._token('}','S10','S16')
                 if estado_actual1 == 'ERROR':
                    #print("S10 No es el fin " + str(estado_actual1))
                    estado_actual1 = 'S9'                    
                 if (operador =='"Seno"') or (operador=='"Coseno"')or(operador=='"Tangente"')or ( operador=='"Inverso"'):
                      #print(self.lineas[self.pos])
                      self.pos -= 1
                      if estado_actual1 == 'S16':
                         self.pos += 1
                      # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                      print("\t*****OPERACION TRIGONOMETRICA*****")
                      print(self.lineas[self.pos])
                      BLuis = self.lineas[self.pos]
                      print('\t',operador ,'(',hijo_izquierdo ,')' )
                      print('\t*******************************\n')                      
                      result = ope._CorroborarOperadorV1(operador, int(hijo_izquierdo))
                      #print("Entro NIDO2 "+ str(Valor1An) + " " + str(Valor2An) + " " + str( HijoPen1) + " "+ str(HijoPen2)  )
                      #print("Resultado de Operacion = "+str(result)+ "  "+ str(int(hijo_izquierdo)))
                      Operacion = str(operador) + str(Poper)+"padre1"
                      OperacionA = str(operador)
                      #Hijo2 = str(float(hijo_derecho))+"-"+str(Poper)
                      Hijo1 = str(int(hijo_izquierdo)) + "-"+str(Poper)  
                      Hijo1a = str(int(hijo_izquierdo)) #Nombre del hijo 1
                      if Valor1An:
                         Operacion = str(operador) + str(Poper)+ "hijo21"
                         OperacionA = str(operador) + " + " + str(result)
                         OperacionT = Operacion
                         OperacionTA = OperacionA
                         HijoPen1 = True
                         Valor1An = False  
                      Padre = str(result)                      
                      Poper +=1 
                      #print("Padre "+str(Padre))
                      #print("Hijo1 "+ Hijo1+estado_actual1)
                      
                      GeneraNodo(Operacion,OperacionA,Padre,Hijo1,Hijo1a,Hijo1,Hijo1a)
                      GeneraRelacion(Operacion,Hijo1)
                      #GeneraRelacion(Operacion,Hijo2)
                      #print("Entro NIDO2 "+ str(Valor1An) + " " + str(Valor2An) + " " + str( HijoPen1) + " "+ str(HijoPen2)  )


                      #a[1]= result # Este lo agregue yo 
                      op = operador +'('+str(result) +')'
                      estado_Auxiliar = False
                      return [estado_actual1, result]  
                 else:
                      estado_actual = self._token('"Valor2"','S10','S11')
            
            # S11 → : S12
            elif estado_actual == 'S11':
                 #print("Entro a S11")
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

                        resultado = ope._CorroborarOperadorV2(operador,float(hijo_izquierdo),float(hijo_derecho))
                        Operacion = str(operador) + str(Poper)+"padre1"
                        OperacionA = str(operador)
                        Hijo1 = str(float(hijo_izquierdo)) + "-"+str(Poper)  
                        Hijo2 = str(float(hijo_derecho))+"-"+str(Poper)
                        Hijo1a = str(float(hijo_izquierdo))
                        Hijo2a = str(float(hijo_derecho))

                        if Valor2An:
                            Operacion = str(operador) + str(Poper) + "hijo1"
                            OperacionA = str(operador) + " + " + str(resultado)
                            OperacionT = Operacion
                            OperacionTA = OperacionA
                            HijoPen2 = True
                            Valor2An = False
                        if HijoPen1:
                           Hijo1 = OperacionT    
                           Hijo1a = OperacionTA
                           HijoPen1 = False        

                        if Valor1An:
                            Operacion = str(operador) + str(Poper)+"hijo1"
                            OperacionA = str(operador) + " + " + str(resultado)
                            OperacionT = Operacion
                            OperacionTA = OperacionA
                            HijoPen1 = True
                            Valor1An = False   
                        Padre = str(resultado)
                        
                        Poper +=1 
                        GeneraNodo(Operacion,OperacionA,Padre,Hijo1,Hijo1a,Hijo2,Hijo2a)                        
                        GeneraRelacion(Operacion,Hijo1)
                        GeneraRelacion(Operacion,Hijo2)
                        
                        op = resultado
                        #op = hijo_izquierdo + operador + hijo_derecho
                        return [estado_sig, op]  
                else:
                   #print("S12 Valor2 con anidado "+estado_actual)
                   Valor2An = True

            # S13 → S2 S14
            elif estado_actual == 'S13':
                estado_actual = 'S14'
                #print("Entro a S13")
                a = self._operaciones('S14')
                hijo_derecho = a[1]
                if "ERROR" == a[0]:
                     estado_actual = 'ERROR'

            # S14 → ] S15
            elif estado_actual == 'S14':
                print("Entro a S14") 
                estado_actual = self._token(']', 'S14','S15')
                # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                print("\t*****OPERACION ARITMETICA*****")
                print('\t',hijo_izquierdo , operador, hijo_derecho)
                print('\t*******************************\n')
                resultado = ope._CorroborarOperadorV2(operador,float(hijo_izquierdo),float(hijo_derecho))
                op = resultado
                Operacion = str(operador) + str(Poper)+"padre"
                OperacionA = str(operador)
                Hijo2 = str(float(hijo_derecho))
                Hijo2a = str(float(hijo_derecho))
                Hijo1 = str(float(hijo_izquierdo))  
                Hijo1a = str(float(hijo_izquierdo))  
                if Valor2An:
                    Operacion = str(operador) + str(Poper)+"hijo"
                    OperacionA = str(operador)
                    Valor2An = False
                if HijoPen2:
                    Hijo2 = OperacionT    
                    Hijo2a = OperacionTA
                    HijoPen2 = False
                if HijoPen1:
                    Hijo1 = OperacionT    
                    Hijo1a = OperacionTA
                    HijoPen1 = False
                Padre = str(resultado)
                GeneraNodo(Operacion,OperacionA,Padre,Hijo1,Hijo1a,Hijo2,Hijo2a)  
                GeneraRelacion(Operacion,Hijo2)
                GeneraRelacion(Operacion,Hijo1)
                OperacionT = str(operador) + "hijo"
                print("Entro ANIDADO"+ str(Valor1An) + " " + str(Valor2An) + " " + str( HijoPen1) + " "+ str(HijoPen2)  )
              
                
                return [estado_sig, op]  





            # ERRORES 
            if estado_actual == 'ERROR':
               """ print("********************************")
                print("\tERROR")
                print("********************************")"""
                # ERROR
               self.contE +=1
               self.guardarErrores(self.contE,self.lineas[self.pos], self.fila, self.pos)
               print(estado_anterior)
               estado_actual = estado_anterior
               return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.pos < len(self.lineas) - 1:
                self.pos +=1
            else:
                break

    
    def _compile(self):              
        global Valor2An, Palabras
        global OperacionT, Color_Nodo, Color_Letra,Forma_Nodo
        estado_actual = 'S0'
        estado_anterior ='S0'
        while self.lineas[self.pos] != "":
            if self.lineas[self.pos] == '\n':
                 self.fila +=1
                 self.columna =0

            # S0 → { S1
            elif estado_actual == 'S0':
                 estado_actual = self._token('{', 'S0','S1')
                 estado_anterior = 'S0'
            # S1 → { S2
            elif estado_actual == 'S1':
                 estado_actual =self._token('{', 'S1','S2')
                 if estado_actual == 'ERROR':
                     print("ERROR EN 'S1'")
                     estado_anterior = 'S1'
                     estado_actual = self._token('{', 'S1','S2')
                     print( self.lineas[self.pos])
                     print(estado_actual)
                 
            # S2 "Operacion "S3
            elif estado_actual == 'S2':
                if self.lineas[self.pos] != " ":
                     #print("Lineas Ver "+str(self.lineas))
                     a = self._operaciones('S15')
                     estado_actual = a[0]
                     if estado_actual != 'ERROR':
                        print("\t*****RESULTADO*****")
                        print('\t',a[1])
                        print('\t*******************************\n')
                     if estado_actual == 'ERROR':
                         estado_anterior = 'S2'
            
            # S15 → } S16  
            elif estado_actual == 'S15':
                 
                 estado_actual = self._token('}','S15','S16')
                 if estado_actual == 'ERROR':
                     estado_actual = self._token(']','S15','S15')
            # S16 → , 
            #   | "Texto" S18
            elif estado_actual == 'S16':
                if self.lineas != ' ':                     
                              
                     estado_actual = self._token(',', 'S16','S1') 
                     #print(estado_actual)
                if estado_actual == 'ERROR':                
                    estado_anterior == 'S16'
                    estado_actual =  self._token('"Texto"','S16','S18')
                    estado_actual=='S18'

            # S18 → : S19
            elif estado_actual == 'S18':
                estado_actual =  self._token(':"','S18','S19')
            
            # S19 → " S20
            elif estado_actual== 'S19':
                if self.lineas[self.pos] != '"':
                    Palabras += self.lineas[self.pos]
                    estado_actual = 'S19'
                else:
                    estado_actual = self._token('"','S19', 'S20')
            
            # S20 → "Color-Fondo-Nodo"  S21
            elif estado_actual == 'S20':
                estado_actual = self._token('"Color-Fondo-Nodo"','S20', 'S21')
            
            # S21 → :" S22
            elif estado_actual == 'S21':
                estado_actual = self._token(':"', 'S21', 'S22')

            # S22 → Letras S22
            #  | " S23
            elif estado_actual== 'S22':
                if self.lineas[self.pos] != '"':
                    Color_Nodo += self.lineas[self.pos]
                    estado_actual = 'S22'
                else:
                    estado_actual = self._token('"','S22', 'S23')
            
            # S23 → "Color-Fuente-Nodo" S24
            elif estado_actual == 'S23':                
                estado_actual = self._token('"Color-Fuente-Nodo"', 'S23','S24')
            
            # S24 → :" S25
            elif estado_actual == 'S24':
                estado_actual = self._token(':"', 'S24', 'S25')
            
            # S25 → Letras S25
            #  | " S26
            elif estado_actual== 'S25':
                if self.lineas[self.pos] != '"':
                    Color_Letra += self.lineas[self.pos]
                    estado_actual = 'S25'
                else:
                    estado_actual = self._token('"','S25', 'S26')
            
            # S26 → "Forma-Nodo" S27
            elif estado_actual == 'S26':
                estado_actual = self._token ('"Forma-Nodo"', 'S26','S27')

            # S27 → :" S28
            elif estado_actual == 'S27':
                estado_actual = self._token(':"', 'S27', 'S28')
            
            # S28 → Letras S28
            #  | " S29
            elif estado_actual == 'S28':
                if self.lineas[self.pos] != '"':
                    Forma_Nodo += self.lineas[self.pos]
                    estado_actual = 'S28'
                else:
                    estado_actual = self._token('"','S28', 'S17')




            # S17 final
            elif estado_actual == 'S17':
                 #Grafica()
                 print("Saliendo")
                 print("El texto es: ",Palabras + '\n'+ ' El Color del Nodo es : '+  Color_Nodo, '\n' + ' El color de la letra es: ' + Color_Letra, '\n'+'Forma_Nodo: ' + Forma_Nodo )
                 ColorNodo = Colors.AsignarColor(Color_Nodo)
                 ColorLetra = Colors.AsignarColor(Color_Letra)
                 FormaNodo = Formitas._VerificarForma(Forma_Nodo)
                 Atrib_Grafica(ColorNodo, ColorLetra, FormaNodo)
                 print()
                 self.Reporte()
                 break
            
            # ERRORES 
            if estado_actual == 'ERROR':
                print('\t AQUI OCURRIO UN ERROR     ', end="    ")
                print(self.lineas[self.pos])
                estado_actual = estado_anterior
                self.contE +=1
                self.guardarErrores(self.contE,self.lineas[self.pos], self.fila, self.pos)
                
            #INCREMENTAR POSICION
            if self.pos < len(self.lineas) - 1:
                self.pos +=1
            else:
                break
    def guardarErrores(self, No_E, token, fila, columna):
        global Report
        self.LErrores.append({"No.":No_E,"Token":token,"fila": fila, "columna":columna})
        #for i in se
        Report = open("ERRORESA.json",'w')
        Report.write("{     "+'\n')
        cont = 0
        Reporte1(self.LErrores)
        for i in self.LErrores:
            try:
                Report.write("   { ")
                Report.write("       No.:"+str(i["No."])+'\n')
                Report.write("       Descripcion-Token:"+'{'+'\n')
                Report.write("           Lexema:"+str(i["Token"])+'\n')
                Report.write("           Fila:"+str(i["fila"])+'\n')
                Report.write("           Columna:"+str(i["columna"])+'\n')
                Report.write("       }"+'\n')
                Report.write("    },"+'\n')
                cont +=1
            except:
                print("Error en el reporte ")
        Report.write("}")
        
        
    def Reporte(self):
        Report.close()
        pass



    def _LlenarGrafica(TextoPalaba, ColorN, ColorL, Forma ):
        print("El texto es: ",TextoPalaba + '\n'+ ' El Color del Nodo es : '+  ColorN, '\n' + ' El color de la letra es: ' + Color_Letra, 'Forma_Nodo: ' + Forma_Nodo )
"""a = Analizador(lineas)
a._compile()
Grafica()"""
        
                      