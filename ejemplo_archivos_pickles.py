from utils import guardar_en_archivo, leer_desde_archivo


########### EJEMPLO 1 ##############
print '########### EJEMPLO 1 ##############'

# Guardo en el archivo
archivo = open('ejemplo.pkl', 'wb')

lista1 = [1, 2, 3]
lista2 = [4, 5]
diccionario = {'campo1': 1, 'campo2': 'dos'}

guardar_en_archivo(archivo, lista1)
guardar_en_archivo(archivo, None)
guardar_en_archivo(archivo, lista2)
guardar_en_archivo(archivo, 'Hola mundo')
guardar_en_archivo(archivo, diccionario)
guardar_en_archivo(archivo, 1)

archivo.close()


# Leo del archivo
arch = open('ejemplo.pkl', 'rb')

fin_de_archivo = False
while not fin_de_archivo:
	data, fin_de_archivo = leer_desde_archivo(arch)
	if not fin_de_archivo:
		print data

arch.close()


########### EJEMPLO 2 ##############
print '########### EJEMPLO 2 ##############'

# Guardo en el archivo
archivo = open('ejemplo_2.pkl', 'wb')
lista = [
	{'usuario': 'usuario1', 'puntaje': 5}, 
	{'usuario': 'usuario2', 'puntaje': 3}, 
	{'usuario': 'usuario3', 'puntaje': 1}, 
]

guardar_en_archivo(archivo, lista)
archivo.close()

# Leo del archivo
arch = open('ejemplo_2.pkl', 'rb')
data, fin_de_archivo = leer_desde_archivo(arch)
print data
arch.close()

