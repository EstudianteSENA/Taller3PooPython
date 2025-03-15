import random

class SensorMovimiento:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer_sensor(self):
        # Simula la detección de movimiento de manera aleatoria
        return random.choice([True, False])

class SistemaAlarma:
    def __init__(self):
        self.activa = True  # Estado inicial de la alarma

    def activar(self):
        self.activa = True
        print("Alarma activada.")

    def desactivar(self):
        self.activa = False
        print("Alarma desactivada.")

    def esta_activa(self):
        return self.activa

class DeteccionIntrusos:
    def __init__(self):
        self.sensor1 = SensorMovimiento("Sensor 1")
        self.sensor2 = SensorMovimiento("Sensor 2")
        self.sensor3 = SensorMovimiento("Sensor 3")
        self.alarma = SistemaAlarma()
        self.es_noche = True  # Simula si es de noche o no

    def simular_deteccion(self):
        while True:
            # Leer los sensores
            sensor1 = self.sensor1.leer_sensor()
            sensor2 = self.sensor2.leer_sensor()
            sensor3 = self.sensor3.leer_sensor()

            print(f"\nLectura de sensores: Sensor 1: {sensor1}, Sensor 2: {sensor2}, Sensor 3: {sensor3}")

            # Procesar los datos de los sensores
            if self.es_noche and self.alarma.esta_activa():
                sensores_activados = sum([sensor1, sensor2, sensor3])
                if sensores_activados >= 2:
                    print("¡Alarma activada! Intruso detectado.")
                else:
                    print("Alarma desactivada. No se detectó intrusión.")
            else:
                print("Alarma desactivada. No es de noche o la alarma está desactivada.")

            continuar = input("¿Desea continuar simulando? (s/n): ")
            if continuar.lower() != 's':
                break

class InterfazUsuario:
    def __init__(self):
        self.sistema = DeteccionIntrusos()

    def mostrar_menu(self):
        print("\nBienvenido al Sistema de Detección de Intrusos")
        print("1. Activar/Desactivar la alarma")
        print("2. Simular detección de intrusos")
        print("3. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                if self.sistema.alarma.esta_activa():
                    self.sistema.alarma.desactivar()
                else:
                    self.sistema.alarma.activar()
            elif opcion == '2':
                self.sistema.simular_deteccion()
            elif opcion == '3':
                print("Gracias por usar el sistema de detección de intrusos. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()