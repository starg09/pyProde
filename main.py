# coding=UTF-8
# pyProde v0.1


from utils import *
from prode import *
from fixture import *
import time, os
from colorama import init
init()
from colorama import Fore, Back, Style

def ordenar_fixture(lista_puntajes):
	"""Como ordenar_puntajes, pero para el fixture, por numero de partido.
	"""
	lista_ordenada = sorted(lista_puntajes, key=lambda x: (x['numero_partido']))
	return lista_ordenada

def preparar_archivos():
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

def menuprincipal():
	limpiar_pantalla()

def printlogo_mini():
	print Fore.GREEN + """
===============================================================================
   ÚÄ¿Â ÂÉÍ»ÂÄ¿ÚÄ¿ÚÂ¿ÚÄ¿
   ÃÄÙÀÂÙÌÍ¼ÃÂÙ³ ³ ³³Ã´ 
   Á   Á Ê  ÁÀÄÀÄÙÄÁÙÀÄÙ   
===============================================================================

""" + Fore.RESET

def menuJugador(nombre):
	salir = False
	OpcInv_Jugador = False
	while not(salir):
		limpiar_pantalla()
		printlogo_mini()
		print """
""" + Back.WHITE + Fore.BLACK + "  Menu de Jugador - " + nombre + "  " + Back.RESET + Fore.RESET + """

    1: Mi Prode
    2: Modificar Partido
    3: Ver tabla de posiciones
    0: Volver al men£ principal"""
		print ""
		if OpcInv_Jugador:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci¢n inv lida. Por favor, int‚ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci¢n elegida, y luego presione Enter: "))
			OpcInv_Jugador = False if opcion in [0,1,2,3,4,5] else True
			if opcion == 1:
				#TO-DO
				pass
			elif opcion == 2:
				#TO-DO
				pass
			elif opcion == 3:
				#TO-DO
				pass
			elif opcion == 4:
				#TO-DO
				pass
			elif opcion == 5:
				#TO-DO
				pass
			elif opcion == 0:
				salir = True
		except ValueError:
			OpcInv_Jugador = True

def loginJugador():
	#To-do. Por ahora manda un nombre debug para ver el menu.
	menuJugador("MISSINGNO")

def ListarFixture():
	limpiar_pantalla()
	ArchFixture = open("fixture.dat","rb")
	fixture, dummy = leer_desde_archivo(ArchFixture)
	ArchFixture.close()
	fixture = ordenar_fixture(fixture)
	print "\n  Lista de Partidos  \n"
	i = 1
	for item in fixture:
		print "  " + str(item["numero_partido"]) + ") " + str(item["local"]) + " - " + str(item ["visitante"]),
		if not(item["jugado"]):
			print " (" + str(item["goles_local"]) + "-" + str(item["goles_visitante"]) + ")"
		else:
			print ""
		i += 1
		if i%7==1 and i<len(fixture):
			cualquiera = raw_input("\n\n  Presione enter para la siguiente pagina")
			limpiar_pantalla()
			print "\n  Lista de Partidos  \n"
	terminar = raw_input("\n\n  Presione enter para volver al menu anterior...")
def CargarFixture():
	limpiar_pantalla()
	ArchUsuarios = open("usuarios.dat","rb")
	usuarios = []
	fin_lectura_usuarios = False
	while not(fin_lectura_usuarios):
		item, fin_lectura_usuarios = leer_desde_archivo(ArchUsuarios)
		if item:
			usuarios.append(item)
	ArchUsuarios.close()
	if len(usuarios)>0:
		print "\n  Ya se han creado usuarios, no se puede volver a cargar el fixture.\n"
		terminar = raw_input("  Presione enter para volver al menu anterior...")
	else:
		i = 1
		finarch = False
		ImpFixture = open("fxt_ca_2015.txt","rt")
		lista = importar_fixture(ImpFixture)
		ImpFixture.close()
		ArchFixture = open("fixture.dat","wb")
		guardar_en_archivo(ArchFixture, lista)
		ArchFixture.close()
		print "\n  Fixture cargado con ‚xito.\n"
		terminar = raw_input("  Presione enter para volver al menu anterior...")






def menuAdmin():
	salir = False
	OpcInv_Admin = False
	while not(salir):
		limpiar_pantalla()
		printlogo_mini()
		print """
""" + Back.WHITE + Fore.BLACK + """  Menu de Administrador  """ + Back.RESET + Fore.RESET + """

    1: Cargar fixture del torneo
    2: Agregar usuarios
    3: Listar usuarios
    4: Cargar resultado de un partido
    5: Listar partidos
    0: Volver al men£ principal"""
		print ""
		if OpcInv_Admin:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci¢n inv lida. Por favor, int‚ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci¢n elegida, y luego presione Enter: "))
			OpcInv_Admin = False if opcion in [0,1,2,3,4,5] else True
			if opcion == 1:
				CargarFixture()
			elif opcion == 2:
				#TO-DO
				pass
			elif opcion == 3:
				#TO-DO
				pass
			elif opcion == 4:
				#TO-DO
				pass
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
		print """
""" + Back.WHITE + Fore.BLACK + """  ­Bienvenido a pyProde!  
  Por favor, ingrese el n£mero correspondiente a la opci¢n deseada.  """ + Back.RESET + Fore.RESET + """

	1: Ingresar como Administrador
	2: Ingresar como Jugador
	0: Salir"""
		print ""
		if OpcInv_Main:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci¢n inv lida. Por favor, int‚ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci¢n elegida, y luego presione Enter: "))
			OpcInv_Main = False if opcion in [0,1,2] else True
			if opcion == 1:
				menuAdmin()
			elif opcion == 2:
				loginJugador()
			elif opcion == 0:
				print Back.GREEN + Fore.BLACK + """
               
    ­Adi¢s!    
               
""" + Back.RESET + Fore.RESET
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