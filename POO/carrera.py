from Personaje import personaje

menu = '''
1- Crear personaje
2- Corer carrera
3- salir '''

while  True:
    print(menu)
    opcion = int(input("Ingrese una opcion"))

    if opcion == 1:
        nombre=input("ingrese el nombre")
        altura=float(input("Ingrese la altura del personaje"))
        velocidad=int(input(""))
        resistencia=int(input("Ingrese el valor de la resistencia"))
        fuerza=int(input("Ingrese la fuerza del personaje"))

        personaje1=Personaje(nombre,altura,velocidad,resistencia,fuerza)
        print(personaje1)

    elif opcion == 2:
        tiempo=Personaje.correr()
        print("El personaje corrio", tiempo)

    elif opcion == 3:
        break