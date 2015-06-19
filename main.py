# coding=UTF-8
#pyProde v0.1


from utils import *
import time
from colorama import init
init()
from colorama import Fore, Back, Style


def printlogo():
	logo = Style.BRIGHT + Fore.GREEN
	logo = logo + """

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
"""
	logo = logo + Fore.RESET + Style.RESET_ALL

	for linea in logo.split("\n"):
		print linea
		time.sleep(0.05)
	time.sleep(1)
	print Style.BRIGHT + "    Presionea Enter para continuar..." + Style.RESET_ALL,
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

def menuprincipal():
	continuar = False
	OpcInv = False
	while not(continuar):
		limpiar_pantalla()
		printlogo_mini()
		print """
""" + Back.WHITE + Fore.BLACK + """  ­Bienvenido a pyProde!  
  Por favor, ingrese el n£mero correspondiente a la opci¢n deseada.  """ + Back.RESET + Fore.RESET + """

	1: Ingresar como Administrador
	2: Ingresar como Jugador
	0: Salir"""
		print ""
		if OpcInv:
			print Back.RED + Fore.WHITE + Style.BRIGHT + "  Error: Ha ingresado una opci¢n inv lida. Por favor, int‚ntelo de nuevo...  " + Back.RESET + Fore.RESET + Style.RESET_ALL
		else:
			print ""
		print ""
		try:
			opcion = int(raw_input("  Ingrese la opci¢n elegida, y luego presione Enter: "))
			OpcInv = False if opcion in [0,1,2] else True
			continuar = True if opcion in [0,1,2] else False
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
		except ValueError:
			OpcInv = True
				





#
#Comienza el programa
#

limpiar_pantalla()
printlogo()
menuprincipal()