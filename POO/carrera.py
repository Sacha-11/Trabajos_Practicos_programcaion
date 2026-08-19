from Personaje import Personaje

menu = '''
1- Crear personaje
2- Corer carrera
3- salir '''

while  True:
    print(menu)
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre=input("ingrese el nombre: ")
        altura=float(input("Ingrese la altura del personaje: "))
        velocidad=int(input("Ingrese la velocidad: "))
        resistencia=int(input("Ingrese el valor de la resistencia: "))
        fuerza=int(input("Ingrese la fuerza del personaje: "))

        personaje1=Personaje(nombre,altura,velocidad,resistencia,fuerza)
        print(personaje1)

    elif opcion == 2:
        tiempo=personaje1.correr()
        print(nombre, "corrio", tiempo, "en segundos")

    elif tiempo < 200:
        vivo = False
        print (nombre, "a muerto")
    elif opcion == 3:
        break