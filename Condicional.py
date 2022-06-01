#declaracion de variable
from ast import If
from gc import callbacks


calificacion = input("introduce tu calificacion de AZ-900 aqui:")

calificacion = int(calificacion)

#preguntar si la calificacion es menor a 700
if calificacion < 700 > 101:
    input("Debiste estudiar Más, te lo dijeeee") #si es menor a 700 usa esto
if calificacion > 700:
    input("Sabia que Podrias, ahora tu podras ayudarme a crear una familia para mi") # si pasaste este es el bueno


elif calificacion > 1000 :
    print ("MENTIRAAAA!! eso es imposible" )
else : #sino se cumple el IF anterior pasa a esta linea
    print("FELICIDADES MUCHACHO! pasa por tu Certificado")# se ejecuta si ninguno de los if se cumple

# verificado de mayoria de edad

edad = input("Introduce tu edad:")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Pasale Champion")
elif edad > 100 :
    print("Solo acompañado de tu abuelo")
elif edad < 0 :
    print("Chupa la Mamila pues")
else:
    print("Adonde tan callado?")

    # en PYTHON NO existe SWITCH CASE

    
