import random
import time
import os
import csv
productos={}

def menuInicial():
    """Funcion que permite seleccionar una opcion de accion de sesion de usuario."""
    ok = True
    while ok:
        print("*****************************************")
        print("*      Sistema de Control de Stock      *")
        print("*****************************************")
        print("*                                       *")
        print("*        1. Iniciar Sesion              *")
        print("*        2. Salir                       *")
        print("*                                       *")
        print("*****************************************")
        
        try:
            opcion = int(input("Seleccionar una opción: "))
            if opcion >= 1 and opcion < 3:
                ok = False
                return opcion
            else:
                print("Por favor, elige una opción válida (1-2).")
        except ValueError:
            print("Error: Debes ingresar un número.")

    return -1

def menuPrincipal():
    """Funcion que permite seleccionar una opcion de accion relacionada a los vuelos segun el usuario ingresado."""
    ok=True
    while ok:
        print("*******************************************************************************************************")
        print("*                                          Menú Principal                                             *")
        print('*' * 103)                                                                               
        print("*  1. Total de facturación del mes, productos totales que se vendieron y el costo asociado            *")
        print("*  2. Total de facturación por tipo de producto, la cantidad vendida y el costo asociado              *")
        print("*  3. Seleccionar tipo de producto, detallado en la facturación y la cantidad vendida por dia de este *")
        print("*  4. Alta de producto *")
        print("*  5. Modificar stock *")
        print("*  6. Cerrar Sesión                                                                                   *")


        print("*******************************************************************************************************")

        #print("*  1. Consultar stock (precio - categoria - marca)                                                    *")
        #print("*  2. Alta - Baja - Modificación de productos                                                         *")
        #print("*  3. Registrar ventas                                                                                *")

        try:
            opcion = int(input("\nSeleccionar una opción: "))
            
            if opcion >= 1 and opcion <=6:
                ok = False
                return opcion
            else:
                print("Por favor, elige una opción válida (1-6)")
        except ValueError:
            print("Error: Debes ingresar un número.")

    return -1


def iniciarSesion(diccionario_usuarios, intentos): 
    """Funcion que permite a los usuarios existentes iniciar sesión en el sistema para acceder a sus reservas y realizar nuevas transacciones."""
    iniciarSesion = int(input("Ingrese su número de usuario: \n"))
    bandera = True

    while bandera:
        if iniciarSesion not in diccionario_usuarios:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Usuario no existente\n")
            intentos += 1
            
            iniciarSesion = int(input("Ingrese su número de usuario: \n"))
            if intentos == 3:
                intentos = 1
                print("Demasiados intentos fallidos.")
                bandera = False
        else:
            # Solicitar la contraseña
            contrasena = input("Ingrese su contraseña: \n")
            if diccionario_usuarios[iniciarSesion] ["contrasena"] == contrasena:
                os.system('cls' if os.name == 'nt' else 'clear')    
                print("Login exitoso")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear') 
                intentos = 0
                bandera = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Contraseña incorrecta\n")
                intentos += 1

                if intentos == 3:
                    intentos = 1
                    print("Demasiados intentos fallidos.")
                    bandera = False

    return intentos

def escribir_csv_productos():
    with open("inventario.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        # Cabeceras
        writer.writerow(["ID", "Nombre", "Categoría", "Precio", "Stock"])
        # Escribe cada producto
        for producto_id, datos in productos.items():
            writer.writerow([producto_id, datos["nombre"], datos["categoria"], datos["precio"], datos["stock"]])

def agregar_producto():
    """Función para agregar un producto al inventario y registrarlo en el CSV."""
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            stock_inicial = int(input("Ingrese el stock inicial del producto: "))
            break
        except ValueError:
            print("Error: Asegúrate de ingresar un número para el precio y el stock.")
    
    producto_id = len(productos) + 1  
    productos[producto_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock_inicial
    }
    
    print(f"\nProducto '{nombre}' agregado exitosamente con ID {producto_id}.\n")
    escribir_csv_productos()

def ver_productos():
    """Función para mostrar todos los productos en el inventario."""
    if productos:
        print("\nProductos en inventario:\n")
        for producto_id, datos in productos.items():
            print(f"ID: {producto_id} | Nombre: {datos['nombre']} | Categoría: {datos['categoria']} | Precio: ${datos['precio']} | Stock: {datos['stock']}")
    else:
        print("No hay productos en el inventario.\n")

def modificar_stock_producto():
    """Función para modificar el stock de un producto existente."""
    try:
        producto_id = int(input("Ingrese el ID del producto cuyo stock desea modificar: "))
        if producto_id in productos:
            cantidad = int(input("Ingrese la cantidad para agregar o reducir (número positivo para agregar, negativo para reducir): "))
            productos[producto_id]["stock"] += cantidad
            # Evita que el stock sea negativo
            if productos[producto_id]["stock"] < 0:
                productos[producto_id]["stock"] = 0
            print(f"\nEl stock del producto '{productos[producto_id]['nombre']}' ha sido actualizado. Nuevo stock: {productos[producto_id]['stock']}\n")
            escribir_csv_productos()  
        else:
            print("El ID ingresado no existe en el inventario.\n")
    except ValueError:
        print("Error: Asegúrate de ingresar un número válido para el ID y la cantidad.\n")

#Se carga Stock con la cantidad de productos random de 15-100 por producto
def generarRandStock():
    lista=[]
    for i in range(5):
        num = random.randint(15,150)
        lista.append(num)
    return lista

def generarPreciosTotales(lista):
    listaTotPdv=[]
    precTotInstImp = 0
    precTotInstNac = 0
    precTotOrtodon = 0
    precTotBandeja = 0
    precTotCajaAcr = 0

    for i in range(30):

        precTotInstImp += lista[i][0]
        precTotInstNac += lista[i][1]
        precTotOrtodon += lista[i][2]
        precTotBandeja += lista[i][3]
        precTotCajaAcr += lista[i][4]
        
    listaTotPdv.append(precTotInstImp)
    listaTotPdv.append(precTotInstNac)
    listaTotPdv.append(precTotOrtodon)
    listaTotPdv.append(precTotBandeja)
    listaTotPdv.append(precTotCajaAcr)

    return listaTotPdv

def generarCostosTotales(lista):
    listaTotCost=[]
    costTotInstImp = 500000
    costTotInstNac = 95000
    costTotOrtodon = 40000
    costTotBandeja = 60000
    costTotCajaAcr = 150000

    for i in range(30):

        costTotInstImp += lista[i][0]
        costTotInstNac += lista[i][1]
        costTotOrtodon += lista[i][2]
        costTotBandeja += lista[i][3]
        costTotCajaAcr += lista[i][4]
    
    listaTotCost.append(costTotInstImp)
    listaTotCost.append(costTotInstNac)
    listaTotCost.append(costTotOrtodon)
    listaTotCost.append(costTotBandeja)
    listaTotCost.append(costTotCajaAcr)
    

    return listaTotCost
        
def menu_1(listaIngresos,ventas,listaCostos):
    print("\n******************************************************************\n")

    pdvTotal=0
    costUniTot = 0

    for i in range(5):
        pdvTotal += listaIngresos[i]

    for i in range(5):
        costUniTot += listaCostos[i]

    print(f"\n* El total Facturado del mes (Precio de venta) en cuestión es: ${pdvTotal}")
    print(f"* La Cantidad de productos vendidos es: {ventas} Unidades")
    print(f"* El costo asociado de productos vendidos(Costo unitario + Costo Stock): ${costUniTot}\n")
    
    print("\n******************************************************************\n")

def menu_2(listaIngresosPP,listaVentas5Prod,listaCostosPP):
    print("\n******************************************************************\n")

    print(f"\nFacturación mensual de Instrumental Importado: ${listaIngresosPP[0]}")
    print(f"Facturación mensual de Instrumental Nacional: ${listaIngresosPP[1]}")
    print(f"Facturación mensual de Ortodoncia: ${listaIngresosPP[2]}")
    print(f"Facturación mensual de Bandejas de Acero Inoxidable: ${listaIngresosPP[3]}")
    print(f"Facturación mensual de Cajas de Acero Inoxidable: ${listaIngresosPP[4]}\n")

    print(f"\nCantidad Vendida de Instrumental Importado: {listaVentas5Prod[0]} Unidades")
    print(f"Cantidad Vendida Instrumental Nacional: {listaVentas5Prod[1]} Unidades")
    print(f"Cantidad Vendida de Ortodoncia: {listaVentas5Prod[2]} Unidades")
    print(f"Cantidad Vendida de Bandejas de Acero Inoxidable: {listaVentas5Prod[3]} Unidades")
    print(f"Cantidad Vendida de Cajas de Acero Inoxidable: {listaVentas5Prod[4]} Unidades\n")
    
    print(f"\nCosto asociado Instrumental Importado: ${listaCostosPP[0]}")
    print(f"Costo asociado Instrumental Nacional: ${listaCostosPP[1]}")
    print(f"Costo asociado Ortodoncia: ${listaCostosPP[2]}")
    print(f"Costo asociado Bandejas de Acero Inoxidable: ${listaCostosPP[3]}")
    print(f"Costo asociado Cajas de Acero Inoxidable: ${listaCostosPP[4]}\n")

    print("\n******************************************************************\n")

def menu_3(ListaXDiaPdvTot,CantidadTotProd):
    print("\n******************************************************************\n")

    ok=True
    #Se selecciona un producto
    while ok:
        print("\n**Productos a disposición:**")
        print("\n\t1. Instrumental Importado")
        print("\t2. Instrumental Nacional")
        print("\t3. Ortodoncia")
        print("\t4. Bandejas de Acero Inoxidable")
        print("\t5. Cajas de Acero Inoxidable\n")
        print("\tIngrese otro numero para regresar al Menú Principal\n")
        
        producto = int(input("Seleccionar un tipo de producto: "))
        
        if producto >= 1 and producto < 6:
           
            for i in range(30):
                #Se crea una lista para armar la matriz
                listaCantVendXdiaXproducto=[]

                for r in range(0,len(CantidadTotProd),5):
                    #Se crea una lista auxiliar pora generar las sublistas por dia
                    listaCantAux = []
            
                    #Se agregan los elementos a la sublista
                    listaCantAux.append(CantidadTotProd[r])
                    listaCantAux.append(CantidadTotProd[r+1])
                    listaCantAux.append(CantidadTotProd[r+2])
                    listaCantAux.append(CantidadTotProd[r+3])
                    listaCantAux.append(CantidadTotProd[r+4])

                    listaCantVendXdiaXproducto.append(listaCantAux)
            #Muestro La facturación y la cantidad vendida por dia del producto que se elija
                if producto == 1:    
                    print(f"\nDia {i+1}: Facuturación de Instrumental Importado: {ListaXDiaPdvTot[i][0]}")
                    print(f"\tCantidad de Instruemntal Importado Vendido: {listaCantVendXdiaXproducto[i][0]}")
                elif producto == 2:
                    print(f"\nDia {i+1}: Facuturación de Instrumental Nacional: {ListaXDiaPdvTot[i][1]}")
                    print(f"\tCantidad Instrumental Nacional Vendido: {listaCantVendXdiaXproducto[i][1]}")
                elif producto == 3:
                    print(f"\nDia {i+1}: Facuturación de Ortodoncia: {ListaXDiaPdvTot[i][2]}")
                    print(f"\tCantidad de Ortodoncia Vendida: {listaCantVendXdiaXproducto[i][2]}")
                elif producto == 4:    
                    print(f"\nDia {i+1}: Facuturación de Bandejas de Acero Inoxidable: {ListaXDiaPdvTot[i][3]}")
                    print(f"\tCantidad de Bandejas de Acero Inoxidable Vendida: {listaCantVendXdiaXproducto[i][3]}")
                else:  
                    print(f"\nDia {i+1}: Facuturación de Cajas de Acero Inoxidable: {ListaXDiaPdvTot[i][4]}")
                    print(f"\tCantidad de Cajas de Acero Inoxidable Vendida: {listaCantVendXdiaXproducto[i][4]}")
        else:
             print(f"No hay tipo de producto {producto}")
             ok=False

    print("\n******************************************************************\n")

def main():
    diccionario_usuarios = {0000:
                            {"nombre y apellido": "Administrador",
                             "contrasena": "admin"}
                            }

    salir = True
    salir2 = True

    while salir:
        seleccion = menuInicial()

        if seleccion == 1:
            intentos = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            intentos = iniciarSesion(diccionario_usuarios, intentos)        

            salir2 = True

            while salir2:
                    
                if intentos == 1:
                    intentos = 0
                    seleccion = 4
                else:
                    seleccion = menuPrincipal()

                    if seleccion == 1:
                        menu_1(generarPreciosTotales(ListaXDiaPdvTot), ventasTot, generarCostosTotales(ListaXDiaCostTot))
                    elif seleccion == 2:
                        menu_2(generarPreciosTotales(ListaXDiaPdvTot), totalVentas, generarCostosTotales(ListaXDiaCostTot))
                    elif seleccion == 3:
                        menu_3(ListaXDiaPdvTot, CantidadTotProd)
                    elif seleccion == 6:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Sesión cerrada.")                        
                        salir2 = False
                    elif seleccion == 4:
                        agregar_producto()
                    elif seleccion==5:
                        modificar_stock_producto()  
        else:
            print("\n   ¡Gracias por utilizar nuestro Sistema!")
            print("\n\t\t***** ADIOS *****\n")
            salir = False



#******** Programa Principal ********

lista=generarRandStock()

#Asignación de stock por producto
instImpStock=lista[0]
instNacStock=lista[1]
ortodonciaStock=lista[2]
bandejaStock=lista[3]
cajaStock=lista[4]

#Creacion de listas diversas 
CantVenPP = []
CantidadTotProd=[]

#Generacion de variables para saber la cantidad total de producto vendido, por producto
ventasDeInstImp= 0
ventasDeInstNac= 0
ventasDeOrtodoncia= 0
ventasDeBandeja= 0
ventasDeCaja= 0

#Precio de venta productos 
pdvInstImp = int(11000)
pdvInstNac = int(6000)
pdvOrtodoncia = int(6000)
pdvBandeja = int(5000)
pdvCaja = int(6200)

ventasTotXDia=[]
ventasTot=0
ingresoVentTotDia=0


#Iteración Mensual
for i in range(30):
    #Cantidad de ventas diarias aleatoreas por producto
    instImpVend=random.randint(0,2)
    instNacVend=random.randint(0,5)
    ortodonciaVend=random.randint(0,3)
    bandejaVend=random.randint(0,4)
    cajaVend=random.randint(0,4)

#Cargamos lista total de cantidad de productos 
    CantidadTotProd.append(instImpVend)
    CantidadTotProd.append(instNacVend)
    CantidadTotProd.append(ortodonciaVend)
    CantidadTotProd.append(bandejaVend)
    CantidadTotProd.append(cajaVend)

#Cantidad de productos totales vendidos
    ventasTot+=(instImpVend+instNacVend+ortodonciaVend+bandejaVend+cajaVend)

    #Cantidad vendida por producto
    ventasDeInstImp+= instImpVend
    ventasDeInstNac+= instNacVend
    ventasDeOrtodoncia+= ortodonciaVend
    ventasDeBandeja+= bandejaVend
    ventasDeCaja= cajaVend

    #Descuento de Stock de cada producto
    instImpStock-= instImpVend
    instNacStock-= instNacVend
    ortodonciaStock-= ortodonciaVend
    bandejaStock-= bandejaVend
    cajaStock-= cajaVend

#Se crea lista con los 5 valores totales mensuales de los productos
totalVentas=[]

#Se agregan los valores a la lista
totalVentas.append(ventasDeInstImp)
totalVentas.append(ventasDeInstNac)
totalVentas.append(ventasDeOrtodoncia)
totalVentas.append(ventasDeBandeja)
totalVentas.append(ventasDeCaja)

#Se generan listas tipo Matices para costos y precios diarios 
ListaXDiaCostTot=[]
ListaXDiaPdvTot=[]

for i in range(0,len(CantidadTotProd),5):
    #Se crean sublistas que simulan los datos diarios dentro (xdia) de una lista total
    listaAuxCosto = []
    listaAuxPrecio = []

    #Se cargan los costos diarios por producto
    costDiaInstImp = CantidadTotProd[i] * 45000
    costDiaInstNac = CantidadTotProd[i+1] * 6000
    costDiaOrtodoncia = CantidadTotProd[i+2] * 3500
    costDiaBandeja = CantidadTotProd[i+3] * 4000
    costDiaCaja = CantidadTotProd[i+4] * 5000

    #Se cargan los precios de venta diarios por producto
    pdvDiaInstImp = CantidadTotProd[i]*(pdvInstImp)
    pdvDiaInstNac = CantidadTotProd[i+1]*(pdvInstNac)
    pdvDiaOrtodoncia = CantidadTotProd[i+2]*(pdvOrtodoncia)
    pdvDiaBandeja = CantidadTotProd[i+3]*(pdvBandeja)
    pdvDiaCaja = CantidadTotProd[i+4]*(pdvCaja)


    #Se carga la lista auxiliar de costo para dividir en sublistas los dias
    listaAuxCosto.append(costDiaInstImp)
    listaAuxCosto.append(costDiaInstNac)
    listaAuxCosto.append(costDiaOrtodoncia)
    listaAuxCosto.append(costDiaBandeja)
    listaAuxCosto.append(costDiaCaja)

    #Se carga la lista auxiliar de Precio de Venta para dividir en sublistas los dias
    listaAuxPrecio.append(pdvDiaInstImp)
    listaAuxPrecio.append(pdvDiaInstNac)
    listaAuxPrecio.append(pdvDiaOrtodoncia)
    listaAuxPrecio.append(pdvDiaBandeja)
    listaAuxPrecio.append(pdvDiaCaja)

    #Se completan las listas totales por dia, por producto de precio y costo
    ListaXDiaCostTot.append(listaAuxCosto)
    ListaXDiaPdvTot.append(listaAuxPrecio)


main()