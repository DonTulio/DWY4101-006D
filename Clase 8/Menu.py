class Menu:

    def __init__(self):
        self.opcion = 0
    
    def imprimir(self, texto):
        print(texto)
    
    def opciones(self):
        self.imprimir("Bienvenido al menú")
        self.imprimir("1.- Saludar")
        self.imprimir("2.- Salir....")
        self.opcion = input("Ingrese un valor ( 1 o 2 ) : ")
        self.evaluarOpciones()
        self.opciones()
    
    def evaluarOpciones(self):
        if self.opcion == "1":
            self.imprimir("Hola humano...")
        elif self.opcion == "2":
            exit()
        else:
            self.imprimir("Opción ingresada no es valida....")