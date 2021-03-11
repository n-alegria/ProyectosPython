from .password import Password
from datetime import date, timedelta


class Listado():
    # Constructor ->
    def __init__(self):
        self.__listado = []
    # <- Fin constructor

    # Propiedades ->
    def get_listado(self):
        return self.__listado
    # <- Fin propiedades

    # Metodos ->
    # Imprime todos los objetos del listado
    def __str__(self):
        contador = 1
        if len(self.get_listado()) == 0:
            return '--> Lista vacia <--\n'
        else:
            cadena = 'Listado: \n\n'
            for password in self.__listado:
                cadena += f'{contador}) {password.__str__()}\n'
                contador += 1
            return cadena

    # Compara el objeto con el listado: True si esta en la lista / False si no se encuentra
    def __eq__(self, obj: Password):
        retorno = False
        for password in self.get_listado():
            if password == obj:
                retorno = True
                break
        return retorno

    # Agrega una contraseña
    def __add__(self, obj: Password):
        if self == obj:
            print('\n--> La contraseña ya se encuentra en la lista.\n')
        else:
            self.__listado.append(obj)
            print('\n--> Se agrego la contraseña a la lista.\n')
        return self

    # ELimina una contraseña
    def __sub__(self, pagina: str):
        if self == pagina:
            self.__listado.remove(pagina)
            print('\n--> Se elimino la contraseña de la lista.\n')
        else:
            print('\n--> La contraseña no se encuentra en la lista.\n')
        return self

    def listado_vencidas(self):
        self.setear_contrasenias_vencimiento()
        contador = 1
        cadena = 'Listado: \n\n'
        for password in self.__listado:
            if password.get_vencimiento():
                cadena += f'{contador}) {password.__str__()}\n'
                contador += 1
        return cadena

    # Si pasaron 26 semanas (6 meses) desde que se ingreso la contraseña, setea la variable en True
    def setear_contrasenias_vencimiento(self):
        for password in self.get_listado():
            fecha_vencimiento = password.get_fecha() + timedelta(weeks=26)
            if date.today() == fecha_vencimiento:
                password.set_vencimiento(True)
    # <- Fin metodos
