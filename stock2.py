import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar los productos y sus cantidades
stock = {}

# Función para agregar un producto al stock
def agregar_producto():
    producto = entrada_producto.get().strip()
    cantidad = entrada_cantidad.get().strip()

    if producto and cantidad.isdigit():
        cantidad = int(cantidad)
        if producto in stock:
            stock[producto] += cantidad
        else:
            stock[producto] = cantidad
        messagebox.showinfo("Éxito", f"{cantidad} unidades de '{producto}' agregadas al stock.")
        actualizar_lista()
        limpiar_entradas()
    else:
        messagebox.showwarning("Error", "Ingrese un producto válido y una cantidad numérica.")

# Función para eliminar un producto del stock
def eliminar_producto():
    producto = entrada_producto.get().strip()
    
    if producto in stock:
        del stock[producto]
        messagebox.showinfo("Éxito", f"'{producto}' eliminado del stock.")
        actualizar_lista()
        limpiar_entradas()
    else:
        messagebox.showwarning("Error", "El producto no existe en el stock.")

# Función para modificar un producto en el stock
def modificar_producto():
    producto = entrada_producto.get().strip()
    cantidad = entrada_cantidad.get().strip()

    if producto in stock:
        if cantidad.isdigit():
            stock[producto] = int(cantidad)
            messagebox.showinfo("Éxito", f"'{producto}' actualizado a {cantidad} unidades.")
            actualizar_lista()
            limpiar_entradas()
        else:
            messagebox.showwarning("Error", "Ingrese una cantidad numérica válida.")
    else:
        messagebox.showwarning("Error", "El producto no existe en el stock para modificarlo.")

# Función para actualizar la lista de productos en la interfaz
def actualizar_lista():
    lista_productos.delete(0, tk.END)
    for producto, cantidad in stock.items():
        lista_productos.insert(tk.END, f"{producto}: {cantidad} unidades")

# Función para limpiar las entradas de texto
def limpiar_entradas():
    entrada_producto.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Stock - ABM")

# Widgets de la interfaz
tk.Label(ventana, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada_producto = tk.Entry(ventana)
entrada_producto.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.grid(row=1, column=1, padx=5, pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_producto)
boton_agregar.grid(row=2, column=0, padx=5, pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_producto)
boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

boton_modificar = tk.Button(ventana, text="Modificar", command=modificar_producto)
boton_modificar.grid(row=2, column=2, padx=5, pady=5)

lista_productos = tk.Listbox(ventana, width=50)
lista_productos.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
