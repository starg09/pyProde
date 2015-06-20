#Prueba con interfaz incorporada en Python, TKinter

from Tkinter import *

def definir_imagen(archivo):
	image = Image.open(archivo)
	return ImageTk.PhotoImage(image)


def menuinicial(ventana):
	for widget in ventana.winfo_children():
		widget.destroy()
	ventana.title("pyProde - Menu Principal")
	frame_main = Frame(ventana)
	frame_main.pack()
	botadmin = Button(frame_main, text="Menu de Administrador", command=menuinicial, width=30)
	botjugador = Button(frame_main, text="Menu de Jugador", command=menuinicial, width=30)
	botsalir = Button(frame_main, text="Salir del Programa", command=menuinicial, width=30)
	botadmin.pack()
	botjugador.pack()
	botsalir.pack()
	ventana.mainloop()

def intro(ventana):
	ventana.title("pyProde - Bienvenido")
	frame_intro = Frame(ventana)
	frame_intro.pack()
	photo = PhotoImage(file="logo.gif")
	logo = Label(frame_intro, image=photo, pady=10)
	logo.photo = photo
	logo.pack()
	entrar = Button(frame_intro, text="Haz click aqui para empezar", command=menuinicial(ventana), width=30)
	entrar.pack()
	ventana.mainloop()



#Comienzo del programa

ventana = Tk()
intro(ventana)