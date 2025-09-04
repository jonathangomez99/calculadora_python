def suma (a, b):
	"""
 	Realiza la suma de los argumentos.
  	
  	Args:
   		a, b (int o float): Los números a sumar. No importa el orden.
	
 	Returns:
 		(float): El resultado de la suma de los argumentos.
 	"""
	return float(a + b)

def resta (a, b):
	"""
 	Realiza la resta del argumento 'b' al argumento 'a'.
  	
	Args:
   		a, b (int o float): Los números a restar. El orden importa, se resta 'b' a 'a'.
	
 	Returns:
 		(float): El resultado de restar 'b' a 'a'.
  	"""
	return float(a - b)

def multiplicacion (a, b):
	"""
 	Realiza el producto de los argumentos.
  	
   	Args:
   		a, b (int o float): Los números a multiplicar. No importa el orden.
	
 	Returns:
 		(float): El resultado del producto de los argumentos.
  	"""
	return float(a * b)

def division (a, b):
	"""
 	Realiza la división del argumento 'a' por el argumento 'b'.
  	
   	Args:
   		a (int o float): Dividendo.
		b (int o float): Divisor.
 	El orden importa. Se divide a 'a' por 'b'.
	La división por 0 no está definida dentro de los números reales, por lo que intentarlo arrojará un error.
  	
  	Returns:
  		(float): El cociente de la división de 'a' por 'b'.
   	"""
	if b == 0:
		raise ValueError ("No se pude dividir entre 0")
	return float(a / b)
