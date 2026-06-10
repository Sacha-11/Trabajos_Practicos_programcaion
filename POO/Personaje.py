class Personaje:
    vivo =True #vivo

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad =velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza

    def correr (self):
        if True:
            distancia = 1000
            tiempo= distancia / self.velocidad
            return tiempo

        else:
            print ("El personaje no  puede correr ")
                
    def recuperarse (self):
        pass