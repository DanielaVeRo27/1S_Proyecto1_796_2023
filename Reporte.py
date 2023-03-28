def Reporte1(Datos):
    html = open('Resultado_201902559'+'.html','w')
    html.write('<html>')
    html.write('    <head>')
    html.write('        <title>'+"Reporte de Errores"+'</title>')
    html.write('    </head>')
    html.write('    <body>')
    html.write('        <h3>--Errores Encontrados--</h3>')
    for i in Datos:
        try:
            html.write("   { ")
            html.write("       No.:"+str(i["No."])+'\n')
            html.write('<br>')
            html.write("       Descripcion-Token:"+'{'+'\n')
            html.write('<br>')
            html.write("           Lexema:"+str(i["Token"])+'\n')
            html.write('<br>')
            html.write("           Fila:"+str(i["fila"])+'\n')
            html.write('<br>')
            html.write("           Columna:"+str(i["columna"])+'\n')
            html.write('<br>')
            html.write("       }"+'\n')
            html.write('<br>')
            html.write("    },"+'\n')
            html.write('<br>')
            cont +=1
        except:
            print("Error en el reporte ")
            html.write('    </body>')
    html.write("}")
    
    html.write('</html>')
    html.close()

    """ for i in range(40,lineasT):
        #html.write('        <h3>'+texto[i]+'</h3>')
        html.write('        <p>'+texto[i]+'</p>')
    html.write('    </body>')"""
    