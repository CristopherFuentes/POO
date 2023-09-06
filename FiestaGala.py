class FiestaGala:

    def __init__(self,costoFijoPersona,opcionSaludable):
        self.costoFijoPersona = costoFijoPersona
        self.opcionSaludable = opcionSaludable
#-----------------------------------------------------------

    def get_costoFijoPersonas(self):
        return self.costoFijoPersona
    
    def set_costoFijopersona(self,costoFijoPersona):
        self.costoFijoPersona = costoFijoPersona

#-----------------------------------------------

    def get_opcionSaludable(self):
        return self.opcionSaludable
    
    def set_opcionSaludable(self,opcionSaludable):
        self.opcionSaludable = opcionSaludable
