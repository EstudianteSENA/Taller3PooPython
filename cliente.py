# ****** Zona de Clase ******

#Se crea la clase
class cliente:
    #Se crea el metodo constructo de la clase
    def __init__(self):
        #Se crean los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
        
    # Crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre
        
    def set_apellido(self, dato_apellido):
        self.apellido_cliente = dato_apellido
    
    # Se crean metodos normales de la clase
    
    def tomar_datos(self):
        self.nombre_cliente = input("digite el nombre cliente: ")
        self.apellido_cliente = input("digite el apellido del cliente: ")
    
    def procesar_datos(self):
        aux = self.nombre_cliente + " " + self.apellido_cliente
        
    def mostrar_info_cliente(self):
        print(f"Nombre Cliente: {self.nombre_cliente} - Apellido Cliente: {self.apellido_cliente}")
        
    def hacer_saludo(self, datosaludo):
        print(f"{datosaludo} : {self.nombre_cliente} {self.apellido_cliente}")
