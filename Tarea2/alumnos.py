import csv
with open('alumnos.csv') as f:
    reader=csv.reader(f)
    for read in reader:
        print("Clave: {0}, Nombre: {1}, Apellido: {2}, Promedio: {3}".format(read[0],read[1],read[2],read[3]))
