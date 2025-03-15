import random
from datetime import datetime, timedelta

class Tienda:
    def __init__(self):
        self.hora_actual = self.generar_hora_aleatoria()
        self.estado_tienda = self.verificar_horario_apertura(self.hora_actual)

    def generar_hora_aleatoria(self):
        segundos_aleatorios = random.randint(0, 86399)
        hora_base = datetime.combine(datetime.today(), datetime.min.time())
        hora_random = hora_base + timedelta(seconds=segundos_aleatorios)
        return hora_random.time()

    def verificar_horario_apertura(self, hora):
        apertura_mananera = datetime.strptime("06:00:00", "%H:%M:%S").time()
        cierre_mananero = datetime.strptime("12:00:00", "%H:%M:%S").time()
        apertura_tarde = datetime.strptime("14:00:00", "%H:%M:%S").time()
        cierre_tarde = datetime.strptime("18:00:00", "%H:%M:%S").time()

        if (apertura_mananera <= hora < cierre_mananero) or (apertura_tarde <= hora < cierre_tarde):
            return True
        else:
            return False

class Cliente:
    def __init__(self, es_empleado=False, tiene_membresia=False):
        self.es_empleado = es_empleado
        self.tiene_membresia = tiene_membresia

class ControlAcceso:
    def __init__(self, tienda):
        self.tienda = tienda

    def verificar_acceso(self, cliente):
        if cliente.es_empleado:
            return "Puedes ingresar!"
        elif self.tienda.estado_tienda and cliente.tiene_membresia:
            return f"Hora: {self.tienda.hora_actual} puedes pasar"
        else:
            return "No puedes pasar!"

class InterfazUsuario:
    def __init__(self):
        self.tienda = Tienda()
        self.control_acceso = ControlAcceso(self.tienda)

    def mostrar_menu(self):
        print("Bienvenido al sistema de Acceso Tienda")
        print("1. Resolver el ejercicio")
        print("2. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.resolver_ejercicio()
            elif opcion == '2':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def resolver_ejercicio(self):
        tipo_cliente = int(input("\n ¿Eres un empleado, o un cliente? \n 1. Empleado \n 2. Cliente \n Ingresa tu respuesta: "))
        if tipo_cliente == 1:
            cliente = Cliente(es_empleado=True)
        elif tipo_cliente == 2:
            tiene_membresia = input("Tienes una membresia? (s/n): ").strip().lower() == 's'
            cliente = Cliente(tiene_membresia=tiene_membresia)
        else:
            print("Opción no válida.")
            return

        resultado = self.control_acceso.verificar_acceso(cliente)
        print(resultado)

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()