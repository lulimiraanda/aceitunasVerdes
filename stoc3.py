import tkinter as tk
from tkinter import messagebox

# Datos de inicio de sesión simulados
usuarios_validos = {
    "Roberta": "roberta2024",  # Usuario de ejemplo (nombre de usuario: contraseña)
}

# Diccionario para almacenar los productos y sus cantidades y precios
stock = {}

# Ventana de inicio de sesión
def ventana_inicio_sesion():
    ventana = tk.Tk()
    ventana.title("Inicio de Sesión")
    
    tk.Label(ventana, text="Sistema de Ingreso de Datos de Usuario").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
    tk.Label(ventana, text="Usuario").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(ventana, text="Contraseña").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entrada_contrasena = tk.Entry(ventana, show="*")
    entrada_contrasena.grid(row=2, column=1, padx=5, pady=5)
    
    def verificar_credenciales():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        
        if usuario in usuarios_validos and usuarios_validos[usuario] == contrasena:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            ventana.destroy()  # Cerrar la ventana de inicio de sesión
            ventana_control_stock()  # Abrir la ventana de control de stock
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    tk.Button(ventana, text="Iniciar sesión", command=verificar_credenciales).grid(row=3, column=0, columnspan=2, pady=10)
    
    ventana.mainloop()

# Ventana de control de stock
def ventana_control_stock():
    ventana = tk.Tk()
    ventana.title("Control de Stock")
    
    # Widgets de la interfaz
    tk.Label(ventana, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entrada_producto = tk.Entry(ventana)
    entrada_producto.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(ventana, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(ventana, text="Precio:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entrada_precio = tk.Entry(ventana)
    entrada_precio.grid(row=2, column=1, padx=5, pady=5)
    
    # Función para agregar un producto al stock
    def agregar_producto():
        producto = entrada_producto.get().strip()
        cantidad = entrada_cantidad.get().strip()
        precio = entrada_precio.get().strip()
        
        if producto and cantidad.isdigit() and precio.replace('.', '', 1).isdigit():
            cantidad = int(cantidad)
            precio = float(precio)
            if producto in stock:
                stock[producto]['cantidad'] += cantidad
                stock[producto]['precio'] = precio  # Actualizar el precio
            else:
                stock[producto] = {'cantidad': cantidad, 'precio': precio}
            messagebox.showinfo("Éxito", f"{cantidad} unidades de '{producto}' agregadas al stock con precio ${precio:.2f}.")
            actualizar_lista()
            limpiar_entradas()
        else:
            messagebox.showwarning("Error", "Ingrese un producto válido, una cantidad numérica y un precio numérico.")

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
        precio = entrada_precio.get().strip()
        
        if producto in stock:
            if cantidad.isdigit() and precio.replace('.', '', 1).isdigit():
                stock[producto]['cantidad'] = int(cantidad)
                stock[producto]['precio'] = float(precio)
                messagebox.showinfo("Éxito", f"'{producto}' actualizado a {cantidad} unidades con precio ${precio:.2f}.")
                actualizar_lista()
                limpiar_entradas()
            else:
                messagebox.showwarning("Error", "Ingrese una cantidad y un precio numéricos válidos.")
        else:
            messagebox.showwarning("Error", "El producto no existe en el stock para modificarlo.")
    
    # Función para actualizar la lista de productos en la interfaz
    def actualizar_lista():
        lista_productos.delete(0, tk.END)
        for producto, datos in stock.items():
            lista_productos.insert(tk.END, f"{producto}: {datos['cantidad']} unidades, Precio: ${datos['precio']:.2f}")
    
    # Función para limpiar las entradas de texto
    def limpiar_entradas():
        entrada_producto.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
    
    tk.Button(ventana, text="Agregar", command=agregar_producto).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(ventana, text="Eliminar", command=eliminar_producto).grid(row=3, column=1, padx=5, pady=5)
    tk.Button(ventana, text="Modificar", command=modificar_producto).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    lista_productos = tk.Listbox(ventana, width=50)
    lista_productos.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
    
    ventana.mainloop()

# Iniciar el programa con la ventana de inicio de sesión
ventana_inicio_sesion()
