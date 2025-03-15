class Regla:
    def __init__(self, divisor, palabra):
        self.divisor = divisor
        self.palabra = palabra

    def aplicar(self, numero):
        if numero % self.divisor == 0:
            return self.palabra
        return ""

class Juego:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def aplicar_reglas(self, numero):
        resultado = ""
        for regla in self.reglas:
            resultado += regla.aplicar(numero)
        return resultado or str(numero)

class FizzBuzz:
    def __init__(self):
        self.juego = Juego()
        self.juego.agregar_regla(Regla(3, "Fizz"))
        self.juego.agregar_regla(Regla(5, "Buzz"))

    def ejecutar(self, inicio, fin):
        for numero in range(inicio, fin + 1):
            print(self.juego.aplicar_reglas(numero))

class InterfazUsuario:
    def __init__(self):
        self.fizzbuzz = FizzBuzz()

    def mostrar_menu(self):
        print("\n=== Bienvenido al programa de Fizz & Buzz ===")
        print("1. Ejecutar programa")
        print("2. Cerrar programa")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            respuesta = input("¿Qué deseas hacer? (1-2): ").strip()

            if respuesta == '1':
                self.fizzbuzz.ejecutar(1, 100)
            elif respuesta == '2':
                print("Gracias por usar!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()