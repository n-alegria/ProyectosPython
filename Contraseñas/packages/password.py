from datetime import date

class Password:
    # Constructor ->
    def __init__(self, pagina, contrasenia):
        self.__pagina = pagina
        self.__contrasenia = contrasenia
        self.__fecha_alta = date.today()
        self.__vencida = False
    # <- Fin constructor
        
    # Propiedades ->
    def set_pagina(self, pagina):
        self.__pagina = pagina
        
    def get_pagina(self):
        return self.__pagina
    
    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
        
    def get_contrasenia(self):
        return self.__contrasenia
        
    def get_fecha(self):
        return self.__fecha_alta
    
    def set_vencimiento(self, vencimiento):
        self.__vencida = vencimiento
    
    def get_vencimiento(self):
        return self.__vencida
    # <- Fin propiedades    
    
    # Metodos ->
    # Retorna un string con los valores del objeto
    def __str__(self):
        return (f'Pagina: {self.get_pagina()} - Contraseña: {self.get_contrasenia()} - Fecha de alta: {self.get_fecha().strftime("%d/%m/%y")}')
    
    # Igualdad entre objetos del tipo Password
    def __eq__(self, obj):
        return (self.get_pagina() == obj.get_pagina() and self.get_contrasenia() == obj.get_contrasenia())
    # <- Fin metodos