import random
import time

class Sensor:
    def __init__(self, nombre, rango_min, rango_max):
        self.nombre = nombre
        self.rango_min = rango_min
        self.rango_max = rango_max

    def leer_estado(self):
        # Simula la lectura del sensor dentro de un rango específico
        return random.randint(self.rango_min, self.rango_max)

class AireAcondicionado:
    def __init__(self):
        self.sensor_temperatura = Sensor("Temperatura", 1, 70)  # Rango de temperatura: 1°C a 70°C
        self.sensor_humedad = Sensor("Humedad", 1, 70)  # Rango de humedad: 1% a 70%
        self.encendido = False

    def verificar_condiciones(self):
        temperatura = self.sensor_temperatura.leer_estado()
        humedad = self.sensor_humedad.leer_estado()

        print(f"La temperatura actual es {temperatura}°C, y la humedad es {humedad}%.")

        if (temperatura > 28 and humedad > 60) or temperatura > 30:
            self.encendido = True
            print("El aire acondicionado está encendido!")
        else:
            self.encendido = False
            print("El aire acondicionado está apagado!")

class InterfazUsuario:
    def __init__(self):
        self.aire_acondicionado = AireAcondicionado()

    def mostrar_menu(self):
        print("Bienvenido al sistema de Control de Aire Acondicionado")
        print("1. Resolver el ejercicio")
        print("2. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.aire_acondicionado.verificar_condiciones()
            elif opcion == '2':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()