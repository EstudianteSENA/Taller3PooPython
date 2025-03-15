from cliente import cliente
from saludo import Saludo
# ++++ Codigo Principal +++

# creo el objeto cliente
objCliente = cliente()
objSaludo = Saludo()
# uso los metodos de los objetos
objCliente.tomar_datos()
aux_mensaje = objSaludo.hacer_saludo_formal()
objCliente.hacer_saludo(aux_mensaje)


# llamo a los metodos del objeto
