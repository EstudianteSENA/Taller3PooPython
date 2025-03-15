class Asiento:
    def __init__(self, identificador):
        self.identificador = identificador
        self.reservado = False

    def reservar(self):
        if not self.reservado:
            self.reservado = True
            return True
        return False

    def liberar(self):
        if self.reservado:
            self.reservado = False
            return True
        return False

    def __str__(self):
        estado = "Reservado" if self.reservado else "Disponible"
        return f"Asiento {self.identificador}: {estado}"

class Sala:
    def __init__(self, filas, asientos_por_fila):
        self.asientos = []
        for fila in filas:
            for numero in range(1, asientos_por_fila + 1):
                identificador = f"{fila}{numero}"
                self.asientos.append(Asiento(identificador))

    def mostrar_asientos(self):
        for asiento in self.asientos:
            print(asiento)

    def reservar_asiento(self, identificador):
        for asiento in self.asientos:
            if asiento.identificador == identificador:
                if asiento.reservar():
                    return True
                else:
                    return False
        return False

    def asientos_disponibles(self):
        return [asiento.identificador for asiento in self.asientos if not asiento.reservado]

class InterfazUsuario:
    def __init__(self):
        self.sala = Sala(['a', 'b', 'c', 'd'], 5)

    def mostrar_menu(self):
        print("\n=== Bienvenido al programa de reservas ===")
        print("1. Reservar asiento")
        print("2. Consultar asientos disponibles")
        print("3. Salir del programa")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            respuesta = input("¿Qué deseas hacer? (1-3): ").strip()

            if respuesta == '1':
                self.reservar_asiento()
            elif respuesta == '2':
                self.consultar_asientos()
            elif respuesta == '3':
                print("Gracias por usar el programa!")
                break
            else:
                print("Respuesta inválida!")

    def reservar_asiento(self):
        identificador = input("¿Qué asiento quieres reservar? (ejemplo: a1): ").strip().lower()
        if self.sala.reservar_asiento(identificador):
            print(f"Asiento {identificador} reservado con éxito.")
        else:
            print("Asiento no disponible o ya reservado.")

    def consultar_asientos(self):
        print("\nAsientos disponibles:")
        disponibles = self.sala.asientos_disponibles()
        if disponibles:
            print(", ".join(disponibles))
        else:
            print("No hay asientos disponibles.")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.iniciar()