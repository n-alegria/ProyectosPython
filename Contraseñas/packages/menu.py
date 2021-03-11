from .listado import Listado
from .password import Password

class Menu():
    _opcion = None
    __listado = Listado()

    @classmethod
    def mensaje_bienvenida(cls):
        print("""\nBienvenido
            
    1) Agregar contraseña.
    2) Eliminar contraseña.
    3) Listar Contraseñas.
    4) Contraseñas vencidas.
    5) Salir.    
        """)
        
    @classmethod
    def seleccionar_opcion(cls):
        try:
            cls._opcion = int(input('Ingrese una opcion: '))
        except Exception as e:
            print(f'\n--> Error al ingresar una opcion ({e}) <--')
            print('--> Por favor, reintente.')
            
    @classmethod
    def agregar_contrasenia(cls):
        print('\n -> Agregar Contraseña <-\n')
        pagina = input('Ingrese el nombre de la pagina: ')
        contrasenia = input('Ingrese la contraseña: ')
        password = Password(pagina, contrasenia)
        cls.__listado += password
        
    @classmethod
    def eliminar_contrasenia(cls):
        print('\n -> Eliminar Contraseña <-\n')
        if len(cls.__listado.get_listado()) == 0:
            print('--> Lista vacia <--\n')
        else:
            print(cls.__listado)
            pagina = int(input('\nIngrese el numero de pagina que desea eliminar: '))
            cls.__listado -= cls.__listado.get_listado()[pagina-1]
            
    @classmethod
    def listar_contrasenias(cls):
        print('\n -> Listado de Contraseñas <-\n')
        print(cls.__listado)
        
    @classmethod
    def listar_vencidas(cls):
        print('\n -> Contraseñas Vencidas <-\n')
        print(cls.__listado.listado_vencidas())