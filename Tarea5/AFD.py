cadena1 ="__servidor1" 
cadena2 ="3servidor"
def AFD(entrada):
    estado=0
    for  i in range(len(entrada)):
        if estado==0:
            if entrada[i] in ('_'):
                estado=1
                print(estado)
            elif entrada[i] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'):
                print('Lee letra')
                estado=2
            else:
                print('Cadena Incorrecta')
                return  
        elif estado==1:
            if entrada[i] in ('_'):
                estado=1
            elif entrada[i] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'):
                estado=3
            else:
                print('Cadena Incorrecta')
                return 
        elif estado==2:
            if entrada[i] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'):
                estado=2
            elif entrada[i] in ('1','2','3','4','5','6','7','8','9'):
                estado=4
            else:
                print('Cadena Incorrecta')
                return     
        elif estado==3:
            if entrada[i] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'):
                estado=3
            elif entrada[i] in ('1','2','3','4','5','6','7','8','9'):
                estado=4
            else:
                print('Cadena Incorrecta')
                return
    if estado==4:
        print('Cadena Correcta')
AFD(cadena1)
AFD(cadena2)        