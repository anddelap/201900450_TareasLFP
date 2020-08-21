from xml.dom import minidom
CarXML=minidom.parse("carros.xml")
todosCarros=CarXML.getElementsByTagName("carro")
print("---------------")
print("Lista de Carros")
print("---------------")
for carro in todosCarros:
    cid=carro.getAttribute("id")
    marca=carro.getElementsByTagName("marca")[0]
    modelo=carro.getElementsByTagName("modelo")[0]
    placa=carro.getElementsByTagName("placa")[0]
    serie=carro.getElementsByTagName("serie")[0]
    print("Carro %s:" % cid)
    print("Marca: %s" % marca.firstChild.data)
    print("Modelo: %s" % modelo.firstChild.data)
    print("Placa: %s" % placa.firstChild.data)
    print("Serie: %s" % serie.firstChild.data)
    print()


