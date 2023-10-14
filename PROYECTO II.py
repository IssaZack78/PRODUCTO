from tkinter import *
import tkinter as tk

root=Tk()
root.title("Posicionar")
root.geometry("400x400")

etiqueta1 = Label(root, text="Nombre")
etiqueta1.place(x=10,y=10)
entrada1 = Entry(root)
entrada1.place(x=170, y=10)

etiqueta2=Label(root, text="Codigo")
etiqueta2.place(x=10,y=40)
entrada2 = Entry(root)
entrada2.place(x=170,y=40)

etiqueta1 = Label(root, text="Precio")
etiqueta1.place(x=10,y=10)
entrada1 = Entry(root)
entrada1.place(x=170, y=10)

etiqueta2=Label(root, text="Proveedor")
etiqueta2.place(x=10,y=40)
entrada2 = Entry(root)
entrada2.place(x=170,y=40)

etiqueta1 = Label(root, text="Existencia")
etiqueta1.place(x=10,y=10)
entrada1 = Entry(root)
entrada1.place(x=170, y=10)

etiqueta2=Label(root, text="Estado")
etiqueta2.place(x=10,y=40)
entrada2 = Entry(root)
entrada2.place(x=170,y=40)

etiqueta1 = Label(root, text="Descuento")
etiqueta1.place(x=10,y=10)
entrada1 = Entry(root)
entrada1.place(x=170, y=10)

Boton=Button(root, text="Agregar Producto")
Boton.place(x=10,y=100)

Boton=Button(root, text="Buscar a un producto")
Boton.place(x=10,y=100)

Boton=Button(root, text="Modificar los datos de un producto")
Boton.place(x=10,y=100)

# Se crea el menú de la ventana
menu = tk.Menu()
# Se crean las opciones principales
menu_archivo = tk.Menu(menu, tearoff=0)

root.mainloop()
