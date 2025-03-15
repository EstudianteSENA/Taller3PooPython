import time

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer_estado(self):
        # Simula la lectura del sensor preguntando al usuario
        estado = input(f"¿{self.nombre}? (s/n): ").strip().lower() == 's'
        return estado

class ControlLuces:
    def __init__(self):
        self.sensor_noche = Sensor("Es de noche")
        self.sensor_movimiento = Sensor("Hay movimiento en la habitación")
        self.luces_encendidas = False

    def encender_luces(self):
        self.luces_encendidas = True
        print("Las luces están encendidas.")

    def apagar_luces(self):
        self.luces_encendidas = False
        print("Las luces están apagadas.")

    def verificar_condiciones(self):
        es_noche = self.sensor_noche.leer_estado()
        hay_movimiento = self.sensor_movimiento.leer_estado()

        if es_noche and hay_movimiento:
            self.encender_luces()
        else:
            self.apagar_luces()

class InterfazUsuario:
    def __init__(self):
        self.control_luces = ControlLuces()

    def mostrar_menu(self):
        print("Bienvenido al sistema de Control de Luces Automático")
        print("1. Resolver el ejercicio")
        print("2. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.control_luces.verificar_condiciones()
                time.sleep(3)  # Esperar 3 segundos antes de continuar
            elif opcion == '2':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()