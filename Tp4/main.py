'''Práctico 1 – Sistema de Login y Registro
Desarrollar un sistema de usuarios utilizando Programación Orientada a Objetos.
El programa deberá tener una clase padre Usuario y dos clases hijas: Estudiante y Administrador.
La contraseña deberá estar encapsulada y solo podrá verificarse mediante un método. El sistema debe permitir registrar usuarios, iniciar sesión con usuario y contraseña y mostrar los datos correspondientes según el tipo de usuario.
Conceptos a utilizar: clases, objetos, __init__(), métodos, encapsulamiento, herencia y super().
'''
print("Sistema de login y registro")

def Menu():
    menu = ''' 
    ####################################
    #        # 1- Login                #
    #       # 2- Registro              #
    #        # 3- Salir                #
    ####################################'''

class Usuario():
    def __init__(self, nombre, apellido, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
    def verificar_contrasena(self, contrasena):
        return self.contrasena == contrasena


print("Fin")