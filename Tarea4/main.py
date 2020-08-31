import dominate
from dominate.tags import *
import webbrowser
ListaReportados=[{'nombre': 'registro 1', 'edad': 5, 'activo': True, 'saldo': 100.0}, 
{'nombre': 'registro 2', 'edad': 10, 'activo': False, 'saldo': 200.0}, 
{'nombre': 'registro 3', 'edad': 15, 'activo': True, 'saldo': 30.05}, 
{'nombre': 'registro 4', 'edad': 20, 'activo': False, 'saldo': 2784.4}, 
{'nombre': 'registro 5', 'edad': 25, 'activo': True, 'saldo': 9874.2}, 
{'nombre': 'registro 6', 'edad': 30, 'activo': True, 'saldo': 2365.0}, 
{'nombre': 'registro 7', 'edad': 35, 'activo': False, 'saldo': 2.3}, 
{'nombre': 'registro 8', 'edad': 40, 'activo': False, 'saldo': 0}, 
{'nombre': 'registro 9', 'edad': 45, 'activo': True, 'saldo': 7795.0}, 
{'nombre': 'registro 10', 'edad': 50, 'activo': False, 'saldo': 6987.23}]

def Reporte():
    titulos=['Nombre','Edad','Activo','Saldo']
    doc = dominate.document(title='Reporte')
    with doc.head:
        meta(charset="UTF-8")
    with doc:
        with div(cls='Tabla'):
            h1('Reportes')
            with table():
                for titulo in titulos:
                    with tr():
                        td(titulo)
                        x=0
                        while x <= len(ListaReportados)-1:
                            titulo=titulo.lower()
                            valor=str(ListaReportados[x].get(str(titulo)))
                            td(valor)
                            x+=1
    d=str(doc)
    f = open('Reporte.html','wb')
    f.write(bytes(d,"ascii"))
    f.close()
    
    webbrowser.open_new_tab('Reporte.html')
Reporte()