# coding=UTF-8
# pyProde v0.1


from utils import *
from prode import *
from fixture import *
import time, os
from colorama import init
init()
from colorama import Fore, Back, Style

def cargar_binario(nombre_archivo):
	archbin = open(nombre_archivo,"rb")
	datos, dummy = leer_desde_archivo(archbin)
	archbin.close()
	return datos

def guardar_binario(datos,nombre_archivo):
	archbin = open(nombre_archivo,"wb")
	guardar_en_archivo(archbin, datos)
	archbin.close()

def calcular_puntaje_jugador(jugador):
	puntaje = 0
	fixture = cargar_binario("fixture.dat")
	usuarios = cargar_binario("usuarios.dat")
	for item in usuarios:
		if item["nombre"] == jugador:
			datos_usuario = item
	fixture = ordenar_fixture(fixture)
	datos_usuario["prode"] = sorted(datos_usuario["prode"], key=lambda x: (x['numero_partido']))
	i = 1
	for item in fixture:
		if (datos_usuario["prode"][i-1]["ingresado"]):
			puntaje += calcular_puntaje(item, datos_usuario["prode"][i-1])
		i += 1
	return puntaje

def calcular_puntajes_de_todos(lista):
	for usuario in lista:
		usuario["puntaje"] = calcular_puntaje_jugador(usuario["nombre"])
	return lista

def ordenar_fixture(lista_puntajes):
	"""Como ordenar_puntajes, pero para el fixture, por numero de partido.
	"""
	lista_ordenada = sorted(lista_puntajes, key=lambda x: (x['numero_partido']))
	return lista_ordenada

def preparar_archivos():
	"""De no existir, crea los archivos donde se almacenan los datos de los usuarios, y el fixture.
	Se usa al comienzo del programa
	"""
	if not(os.path.isfile("usuarios.dat")):
		arch = open("usuarios.dat", "wb")
		arch.close()
	if not(os.path.isfile("fixture.dat")):
		arch = open("fixture.dat", "wb")
		arch.close()

def printlogo():
	logo = Style.BRIGHT + Fore.GREEN + """

===============================================================================

               _____               _      
              |  __ \\             | |     
   _ __  _   _| |__) | __ ___   __| | ___ 
  | \'_ \\| | | |  ___/ \'__/ _ \\ / _` |/ _ \\
  | |_) | |_| | |   | | | (_) | (_| |  __/
  | .__/ \\__, |_|   |_|  \\___/ \\__,_|\\___|
  | |     __/ |                           
  |_|    |___/                            


===============================================================================
""" + Fore.RESET + Style.RESET_ALL

	for linea in logo.split("\n"):
		print linea
		time.sleep(0.05)
	time.sleep(1)
	print Style.BRIGHT + "    Presiona Enter para continuar..." + Style.RESET_ALL,
	raw_input() #Seteo a una variable para que no salga en pantalla

def opcionsn(linea):
	s = "k"
	while s not in ["S","s","N","n"]:
		s = raw_input(linea + "[sS/nN]: ")
		if s not in ["S","s","N","n"]:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "\n  Opci�n invalida. Ingrese \"s/S\" para s�, o \"n/N\" para no. Luego presione Enter.\n" + Back.RESET + Fore.RESET + Style.RESET_ALL
	return True if s in ["S","s"] else False

def printlogo_mini():
	print Fore.GREEN + """
===============================================================================
   �Ŀ� ��ͻ�Ŀ�Ŀ�¿�Ŀ
   �������ͼ��ٳ � ��ô 
   �   � �  ������������   
===============================================================================

""" + Fore.RESET

def tablaPosiciones(nombre):
	try:
		limpiar_pantalla()
		usuarios = cargar_binario("usuarios.dat")
		usuarios = calcular_puntajes_de_todos(usuarios)
		usuarios = ordenar_puntajes(usuarios)
		print "\n  Tabla de Posiciones\n"
		i = 1
		for item in usuarios:
			if item["nombre"] == nombre:
				print Fore.YELLOW + Style.BRIGHT + " ",
			else:
				print " ",
			print str(i) + ") " + item["nombre"] + ": " + str(item["puntaje"]) + " puntos",
			if item["nombre"] == nombre:
				print Fore.RESET + Style.RESET_ALL
			else:
				print ""
			i += 1
			if i%9==1 and i<len(usuarios):
				print "\n"
				cualquiera = raw_input("\n\n  Presione enter para la siguiente pagina")
				limpiar_pantalla()
				print "\n  Tabla de Posiciones\n"
		terminar = raw_input("\n\n  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def miProde(nombre):
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		usuarios = cargar_binario("usuarios.dat")
		for item in usuarios:
			if item["nombre"] == nombre:
				datos_usuario = item
		fixture = ordenar_fixture(fixture)
		datos_usuario["prode"] = sorted(datos_usuario["prode"], key=lambda x: (x['numero_partido']))
		print "\n  Mi Prode  \n"
		i = 1
		for item in fixture:
			print "  " + str(item["numero_partido"]) + ") " + str(item["local"]) + " - " + str(item ["visitante"]),
			if (datos_usuario["prode"][i-1]["ingresado"]):
				print " (" + str(datos_usuario["prode"][i-1]["goles_local"]) + "-" + str(datos_usuario["prode"][i-1]["goles_visitante"]) + ")",
			if (item["jugado"]):
				print " [" + str(item["goles_local"]) + "-" + str(item["goles_visitante"]) + "]",
				if not(datos_usuario["prode"][i-1]["ingresado"]):
					print "[0]"
				else:
					print "[" + str(calcular_puntaje(item, datos_usuario["prode"][i-1])) + "]"
			else:
				print ""
			i += 1
			if i%9==1 and i<len(fixture):
				cualquiera = raw_input("\n\n  Presione enter para la siguiente pagina")
				limpiar_pantalla()
				print "\n  Mi Prode  \n"
		terminar = raw_input("\n\n  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def AgregarPronostico(nombre):
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		usuarios = cargar_binario("usuarios.dat")
		for item in usuarios:
			if item["nombre"] == nombre:
				item["prode"] = sorted(item["prode"], key=lambda x: (x['numero_partido']))
				fixture = ordenar_fixture(fixture)
				ids_validos = []
				ids_jugados = []
				for item_fixture in fixture:
					ids_validos.append(item_fixture["numero_partido"])
					if (item_fixture["jugado"] == True):
						ids_jugados.append(item_fixture["numero_partido"]) 
				continuar_id = True
				while continuar_id:
					id_partido = -999
					while ((id_partido not in ids_validos) or (id_partido in ids_jugados)) and continuar_id:
						limpiar_pantalla()
						id_partido = leer_natural("  Inserte su numero de partido, del 1 al " + str(max(ids_validos)) + ": ")
						if id_partido not in ids_validos:
							continuar_id = opcionsn("  N�mero de partido fuera de rango. �Desea ingresar uno nuevamente?")
						if id_partido in ids_jugados:
							print "\n  Resultado cerrado, ya no se puede cargar.\n"
							continuar_id = opcionsn("  �Desea ingresar otro partido?")
					if (id_partido in ids_validos) and (id_partido not in ids_jugados):
						modificar_res = False
						while not(modificar_res):
							print "\n  Pronosticando partido " + str(id_partido) + ": " + fixture[id_partido-1]["local"] + " - " + fixture[id_partido-1]["visitante"] + "\n"
							gol_l = leer_natural(str(fixture[id_partido-1]["local"]) + ": ")
							gol_v = leer_natural(str(fixture[id_partido-1]["visitante"]) + ": ")
							modificar_res = opcionsn("  Usted ingres�:" + fixture[id_partido-1]["local"] + " " + str(gol_l) + " - " + fixture[id_partido-1]["visitante"] + " " + str(gol_v) + "\n  �Es esto correcto?")
						item["prode"][id_partido-1]["goles_local"] = gol_l
						item["prode"][id_partido-1]["goles_visitante"] = gol_v
						item["prode"][id_partido-1]["ingresado"] = True
						guardar_binario(usuarios,"usuarios.dat")
						print "\n  Resultado guardado con �xito."
						continuar_id = opcionsn("  �Desea agregar otro resultado?")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def MenuImportarProde(nombre):
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		usuarios = cargar_binario("usuarios.dat")
		for item in usuarios:
			if item["nombre"] == nombre:
				item["prode"] = sorted(item["prode"], key=lambda x: (x['numero_partido']))
				fixture = ordenar_fixture(fixture)
				nombre_archivo = raw_input("\n  [Para salir sin efectuar cambios, no mande nada]\n  [Formatos validos: *.csv - *.txt]\n\n  Ingrese el nombre del archivo a importar, y presione Enter: ")
				while (nombre_archivo) and(nombre_archivo.split(".")[-1] not in ["txt","csv"]):
					limpiar_pantalla()
					print "\n  ERROR: Formato no soportado.\n"
					nombre_archivo = raw_input("\n  [Para salir sin efectuar cambios, no mande nada]\n  [Formatos validos: *.csv - *.txt]\n\n  Ingrese el nombre del archivo a importar, y presione Enter: ")
				if nombre_archivo:
					if not(os.path.isfile(nombre_archivo)):
						limpiar_pantalla()
						print "\n  ERROR: Archivo no existente.\n"
						terminar = raw_input("\n\n  Presione Enter para volver al men� anterior...")
					else:
						ProdeAImportar = open(nombre_archivo,"rt")
						prode_importado = importar_prode(ProdeAImportar)
						ProdeAImportar.close()
						for partido in prode_importado:
							partido["ingresado"] = True
						item["prode"] = actualizar_prode(item["prode"], fixture, prode_importado)
						guardar_binario(usuarios,"usuarios.dat")
						limpiar_pantalla()
						print "\n  Prode importado con �xito.\n"
						terminar = raw_input("\n\n  Presione Enter para volver al men� anterior...")
				else:
					pass
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def menuJugador(nombre):
	salir = False
	OpcInv_Jugador = False
	while not(salir):
		limpiar_pantalla()
		printlogo_mini()
		print "\n" + Back.WHITE + Fore.BLACK + "  Menu de Jugador - " + nombre + "  " + Back.RESET + Fore.RESET + """

    1: Importar Prode
    2: Mi Prode
    3: Modificar Partido
    4: Ver tabla de posiciones
    0: Volver al men� principal"""
		print ""
		if OpcInv_Jugador:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci�n inv�lida. Por favor, int�ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci�n elegida, y luego presione Enter: "))
			OpcInv_Jugador = False if opcion in [0,1,2,3,4] else True
			if opcion == 1:
				MenuImportarProde(nombre)
			elif opcion == 2:
				miProde(nombre)
			elif opcion == 3:
				AgregarPronostico(nombre)
			elif opcion == 4:
				tablaPosiciones(nombre)
			elif opcion == 0:
				salir = True
		except ValueError:
			OpcInv_Jugador = True
def loginJugador():
	try:
		limpiar_pantalla()
		usuarios = cargar_binario("usuarios.dat")
		logeado = False
		if not(usuarios):
			dejar_login = True
			print "\n  Todavia no se ha creado ning�n usuario.\n"
			terminar = raw_input("  Presione Enter para volver al men� anterior...")
		else:
			dejar_login = False
		while not dejar_login:
			nick = raw_input("\n  Ingrese su nombre de usuario:")
			if not(nick.isalnum()):
				print "\n  ERROR: Solo se permiten caracteres alfanum�ricos.\n"
			else:
				for item in usuarios:
					if (item["nombre"] == nick.upper()):
						logeado = True
						dejar_login = True 
			if logeado:
				menuJugador(nick.upper())
			else:
				print "\n  ERROR: Usuario inexistente.\n"
				dejar_login = not(opcionsn("  �Desea ingresar otro usuario? "))
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")


def ListarFixture():
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		if not(fixture):
			print "\n  Error: Fixture no cargado.\n"
		else:
			fixture = ordenar_fixture(fixture)
			print "\n  Lista de Partidos  \n"
			i = 1
			for item in fixture:
				print "  " + str(item["numero_partido"]) + ") " + str(item["local"]) + " - " + str(item["visitante"]),
				if (item["jugado"]):
					print " (" + str(item["goles_local"]) + "-" + str(item["goles_visitante"]) + ")"
				else:
					print ""
				i += 1
				if i%9==1 and i<len(fixture):
					cualquiera = raw_input("\n\n  Presione enter para la siguiente pagina")
					limpiar_pantalla()
					print "\n  Lista de Partidos  \n"
		terminar = raw_input("\n\n  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def AgregarResultado():
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		if not(fixture):
			print "\n  Antes de agregar un resultado, debe cargarse el fixture.\n"
			terminar = raw_input("\n  Presione Enter para volver al men� anterior...")
		else:
			fixture = ordenar_fixture(fixture)
			ids_validos = []
			for item in fixture:
				ids_validos.append(item["numero_partido"])
			continuar_id = True
			while continuar_id:
				id_partido = -999
				while id_partido not in ids_validos and continuar_id:
					limpiar_pantalla()
					id_partido = leer_natural("  Inserte su numero de partido, del 1 al " + str(max(ids_validos)) + ": ")
					if id_partido not in ids_validos:
						continuar_id = opcionsn("  N�mero de partido fuera de rango. �Desea ingresar uno nuevamente?")
				if id_partido in ids_validos:
					modificar_res = False
					while not(modificar_res):
						print "\n  Modificando partido " + str(id_partido) + ": " + fixture[id_partido-1]["local"] + " - " + fixture[id_partido-1]["visitante"] + "\n"
						gol_l = leer_natural(str(fixture[id_partido-1]["local"]) + ": ")
						gol_v = leer_natural(str(fixture[id_partido-1]["visitante"]) + ": ")
						modificar_res = opcionsn("  Usted ingres�:" + fixture[id_partido-1]["local"] + " " + str(gol_l) + " - " + fixture[id_partido-1]["visitante"] + " " + str(gol_v) + "\n  �Es esto correcto?")
					fixture[id_partido-1]["goles_local"] = gol_l
					fixture[id_partido-1]["goles_visitante"] = gol_v
					fixture[id_partido-1]["jugado"] = True
					guardar_binario(fixture,"fixture.dat")
					print "\n  Resultado guardado con �xito."
					continuar_id = opcionsn("  �Desea agregar otro resultado?")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def ListarUsuarios():
	try:
		limpiar_pantalla()
		usuarios = cargar_binario("usuarios.dat")
		if not(usuarios):
			print "\n  No hay usuarios para listar.\n"
		else:
			usuarios_ordenados = sorted(usuarios, key=lambda x: (x['nombre']))
			print "\n  Lista de Usuarios  \n"
			i = 1
			for item in usuarios:
				print "  * " + item["nombre"]
				i += 1
				if i%8==1 and i<len(usuarios):
					cualquiera = raw_input("\n\n  Presione enter para la siguiente pagina")
					limpiar_pantalla()
					print "\n  Lista de Usuarios  \n"
		terminar = raw_input("\n  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def AgregarUsuario():
	try:
		limpiar_pantalla()
		fixture = cargar_binario("fixture.dat")
		if not(fixture):
			print "\n  Antes de crear usuarios, debe cargarse el fixture.\n"
		else:
			esalfan = False
			while not(esalfan):
				nombre_elegido = raw_input("\n  [Los nombres deben tener solo caracteres alfanum�ricos]\n  [La � no est� permitida]\n  Por favor, ingrese un nuevo nombre de usuario: ")
				esalfan = nombre_elegido.isalnum()
				if not(nombre_elegido.isalnum()):
					limpiar_pantalla()
					print Back.RED + Fore.WHITE + Style.BRIGHT + "\n  Error: Solo puede ingresar caracteres alfanum�ricos.\n" + Back.RESET + Fore.RESET + Style.RESET_ALL

			nombre_elegido = nombre_elegido.upper()
			usuarios = cargar_binario("usuarios.dat")
			NombreExistente = False
			if not(usuarios):
				usuarios = []
			for item in usuarios:
				if (item["nombre"] == nombre_elegido):
						NombreExistente = True
			if NombreExistente:
				print Back.RED + Fore.WHITE + Style.BRIGHT + "\n  Error: El usuario " + nombre_elegido + " ya existe en el sistema.\n" + Back.RESET + Fore.RESET + Style.RESET_ALL
			else:
				nuevo_usuario = {
					"nombre": nombre_elegido,
					"puntaje": 0,
					"prode": []
				}
				#To-do: Reemplazar por funciones de prode.py, usar csv de "0 a 0"
				ArchProde0a0 = open("prode_0_a_0.csv","rt")
				nuevo_usuario["prode"] = importar_prode(ArchProde0a0)
				ArchProde0a0.close()
				for partido in nuevo_usuario["prode"]:
					partido["ingresado"]= False #Cuesti�n est�tica, y a los partidos que no se haya ingresado pronostico se entregan 0 puntos.
				usuarios.append(nuevo_usuario)
				guardar_binario(usuarios,"usuarios.dat")
				print "\n  Usuario creado: " + nombre_elegido.upper()
		terminar = raw_input("  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")

def CargarFixture():
	try:
		limpiar_pantalla()
		usuarios = cargar_binario("usuarios.dat")
		if usuarios:
			print "\n  Ya se han creado usuarios, no se puede volver a cargar el fixture.\n"
		else:
			finarch = False
			ImpFixture = open("fxt_ca_2015.txt","rt")
			lista = importar_fixture(ImpFixture)
			ImpFixture.close()
			guardar_binario(lista,"fixture.dat")
			print "\n  Fixture cargado con �xito. " + str(len(lista)) + " partidos detectados.\n"
		terminar = raw_input("  Presione Enter para volver al men� anterior...")
	except IOError:
		terminar = raw_input("\n\n  ERROR: No se ha podido abrir el archivo.\n\n Presione Enter para volver al men� anterior...")
def menuAdmin():
	salir = False
	OpcInv_Admin = False
	while not(salir):
		limpiar_pantalla()
		printlogo_mini()
		print "\n" + Back.WHITE + Fore.BLACK + """  Menu de Administrador  """ + Back.RESET + Fore.RESET + """

    1: Cargar fixture del torneo
    2: Agregar usuarios
    3: Listar usuarios
    4: Cargar resultado de un partido
    5: Listar partidos
    0: Volver al men� principal"""
		print ""
		if OpcInv_Admin:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci�n inv�lida. Por favor, int�ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci�n elegida, y luego presione Enter: "))
			OpcInv_Admin = False if opcion in [0,1,2,3,4,5] else True
			if opcion == 1:
				CargarFixture()
			elif opcion == 2:
				AgregarUsuario()
			elif opcion == 3:
				ListarUsuarios()
			elif opcion == 4:
				AgregarResultado()
			elif opcion == 5:
				ListarFixture()
			elif opcion == 0:
				salir = True
		except ValueError:
			OpcInv_Admin = True


def menuprincipal():
	continuar = True
	OpcInv_Main = False
	while continuar:
		limpiar_pantalla()
		printlogo_mini()
		print "\n" + Back.WHITE + Fore.BLACK + """  �Bienvenido a pyProde!  
  Por favor, ingrese el n�mero correspondiente a la opci�n deseada.  """ + Back.RESET + Fore.RESET + """

	1: Ingresar como Administrador
	2: Ingresar como Jugador
	0: Salir"""
		print ""
		if OpcInv_Main:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci�n inv�lida. Por favor, int�ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci�n elegida, y luego presione Enter: "))
			OpcInv_Main = False if opcion in [0,1,2] else True
			if opcion == 1:
				menuAdmin()
			elif opcion == 2:
				loginJugador()
			elif opcion == 0:
				print Back.GREEN + Fore.BLACK + "\n               \n    �Adi�s!    \n               \n" + Back.RESET + Fore.RESET
				time.sleep(1.5)
				limpiar_pantalla()
				continuar = False
		except ValueError:
			OpcInv_Main = True
				

#
#Comienza el programa
#
limpiar_pantalla()
preparar_archivos()
printlogo()
menuprincipal()