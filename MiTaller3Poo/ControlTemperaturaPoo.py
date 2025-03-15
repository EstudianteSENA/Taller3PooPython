import random
import time

class SensorTemperatura:
    def leer_temperatura(self):
        # Simula la lectura de la temperatura de manera aleatoria
        return random.randint(1, 30)

class ControladorTemperatura:
    def procesar_temperatura(self, temperatura):
        if temperatura < 10:
            return "Calefactor activado"
        elif 10 <= temperatura <= 25:
            return "Sistema inactivo"
        else:
            return "Ventilador activado"

class Invernadero:
    def __init__(self):
        self.sensor = SensorTemperatura()
        self.controlador = ControladorTemperatura()

    def simular_control(self):
        for _ in range(3):  # Simula 3 lecturas de temperatura
            temperatura = self.sensor.leer_temperatura()
            estado = self.controlador.procesar_temperatura(temperatura)
            print(f"La temperatura es: {temperatura}°C... {estado}")
            time.sleep(5)  # Simula la lectura cada 5 segundos

class InterfazUsuario:
    def __init__(self):
        self.invernadero = Invernadero()

    def mostrar_menu(self):
        print("\n=== Bienvenido al programa de temperatura ===")
        print("1. Ejecutar programa")
        print("2. Cerrar programa")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            respuesta = input("¿Qué deseas hacer? (1-2): ").strip()

            if respuesta == '1':
                self.invernadero.simular_control()
            elif respuesta == '2':
                print("Gracias por usar!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()