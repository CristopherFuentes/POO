class Fiesta:

    def __init__(self,numeroPersonas,costoDecoracion,bonoExtra,costoComidaPersona,decora):
        self.numeroPersonas = numeroPersonas
        self.costoDecoracion = costoDecoracion
        self.bonoExtra = bonoExtra
        self.costoComidaPersona = costoComidaPersona
        self.decora = decora

#------------------------------------------------------------

    def get_numeroPersonas(self):
        return self.numeroPersonas
    
    def set_numeroPersonas(self,numeroPersonas):
        self.numeroPersonas = numeroPersonas

#-----------------------------------------------------------

    def get_costoDecoracion(self):
        return self.numeroPersonas
    
    def set_costoDecoracion(self,costoDecoracion):
        self.costoDecoracion = costoDecoracion
#-----------------------------------------------------------

    def get_bonoExtra(self):
        return self.bonoExtra
    
    def set_bonoExtra(self,bonoExtra):
        self.bonoExtra = bonoExtra

#--------------------------------------------------------

    def get_costoComidaPersona(self):
        return self.numeroPersonas
    
    def set_costoComidaPersona(self,costoComidaPersona):
        self.costoComidaPersona = costoComidaPersona

#----------------------------------------------------------

    def get_decora(self):
        return self.decora
    
    def set_decora(self,decora):
        self.decora = decora

#---------------------------------------------------------



    def Fiestaa(numeroPersonas):
        numeroPersonas = input(int("Ingrese Numero de Personas: "))
        while True:
            if numeroPersonas > 0:
                pass
            else:
                numeroPersonas <= 0