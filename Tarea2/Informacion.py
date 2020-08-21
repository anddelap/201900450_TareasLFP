import json
i=1
with open("Informacion.json") as info:
    informacion=json.loads(info.read())
    for infos in informacion:
        print("Persona",i,":")
        print(infos['nombre'],infos['apellido'])
        print("Edad:",infos['edad'])
        print("Estudiante:",infos['estudiante'])            
        print("")
        i+=1
        
