from graphviz import Digraph


ColorNodo =" Red"
dot = Digraph(name='Probando el texto', node_attr={'shape': 'circle'},format='svg')
dot.attr('node', shape ='circle')
dot.attr('node', style='filled', shape ='circle', fillcolor="Yellow")
dot.attr('node', shape = 'record')
def Atrib_Grafica(ColorN, ColorL, forma):
    global dot, ColorNodo   
    ColorNodo = ColorN
    print(ColorN+"ENTRO AL METODO ")
    #dot = Digraph(name='Probando el texto', node_attr={'shape': 'circle'},format='svg')
    
    dot.attr('node', shape =forma)
    dot.attr('node', style='filled', shape ='box', fillcolor =ColorN)
    dot.attr('node', shape = 'record')


def GeneraNodo(Nodo1a,Nodo1b,Nodo1C,Nodo2a,Nodo2b,Nodo3a,Nodo3b):
    dot.node(Nodo1a,"{" + Nodo1b + "|{"+str(Nodo1C)+"}}")    
    dot.node(Nodo2a,str(Nodo2b))
    dot.node(Nodo3a,str(Nodo3b))


def GeneraRelacion(NodoA,NodoB):
    dot.edge(NodoA,NodoB)


def Grafica():
    dot.render('test-output/round-table.gv', view=True)
#GeneraNodo('a','b','c')