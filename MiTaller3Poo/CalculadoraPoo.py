class Calculadora:
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            raise ValueError("No se puede dividir por cero.")
        return num1 / num2

class InterfazUsuario:
    def mostrar_menu(self):
        print("\n=== Bienvenido al programa de Calculadora ===")
        print("1. Ejecutar programa")
        print("2. Cerrar programa")

    def solicitar_numeros(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return num1, num2

    def solicitar_operador(self):
        operador = input("Ingrese el operador (+, -, *, /): ")
        return operador

    def mostrar_resultado(self, resultado):
        print(f"El resultado es: {resultado}")

    def preguntar_continuar(self):
        respuesta = input("¿Deseas realizar otra operación? (s/n): ").lower()
        return respuesta == 's'

class AplicacionCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()
        self.interfaz = InterfazUsuario()

    def ejecutar(self):
        while True:
            self.interfaz.mostrar_menu()
            opcion = input("Seleccione una opción (1-2): ").strip()

            if opcion == '1':
                num1, num2 = self.interfaz.solicitar_numeros()
                operador = self.interfaz.solicitar_operador()

                try:
                    if operador == "+":
                        resultado = self.calculadora.sumar(num1, num2)
                    elif operador == "-":
                        resultado = self.calculadora.restar(num1, num2)
                    elif operador == "*":
                        resultado = self.calculadora.multiplicar(num1, num2)
                    elif operador == "/":
                        resultado = self.calculadora.dividir(num1, num2)
                    else:
                        print("Operador no válido.")
                        continue

                    self.interfaz.mostrar_resultado(resultado)

                    if not self.interfaz.preguntar_continuar():
                        print("Gracias por usar la calculadora. ¡Hasta luego!")
                        break

                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '2':
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    app = AplicacionCalculadora()
    app.ejecutar()