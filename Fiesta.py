class Fiesta:

    def __init__(self,numeroPersonas):
        self.numeroPersonas = numeroPersonas
  

#------------------------------------------------------------

    def get_numeroPersonas(self):
        return self.numeroPersonas
    
    def set_numeroPersonas(self,numeroPersonas):
        self.numeroPersonas = numeroPersonas

#-----------------------------------------------------------





    def nropersonas(numeroPersonas):
        numeroPersonas = input(int("Ingrese Numero de Personas: "))
        while True:
            if numeroPersonas > 0:
                break
            else:
                numeroPersonas <= 0

    
    def bonoExtra(numeroPersonas):
        while True:
            if numeroPersonas > 12:
                print("Debe pagar un bono de 5000")
            else:
                break
        

    def costoComida(numeroPersonas):
        comida = numeroPersonas*3500
            

    def costoDecoracion(numeroPersonas):
        while True:
            if numeroPersonas > 20:
                print("El costo por personas sera de $22000")
            elif numeroPersonas:
                cdecoracion = numeroPersonas*16000
                print("El costo por persona sera de $16000")