import sqlite3 

from colorama import Fore, Style, init

init(autoreset=True)

conexion = sqlite3.connect("inventario.db") 

cursor = conexion.cursor() 

# CREA LA TABLA 'productos' EN CASO DE QUE NO EXISTA.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
''')

#GUARDA LOS CAMBIOS EN LA BASE DE DATOS LUEGO DE CREAR LA TABLA.
conexion.commit() 

#LLAMA A LA BASE DE DATOS E INSERTA LOS ARGUMENTOS QUE INGRESO EL USUARIO.
def registrarProducto(nombre, descripcion, cantidad, precio, categoria):

    try:
        cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("\n")
        print("Producto registrado con exito.")

#EN CASO DE ERROR, SE DESHACE EL REGISTRO, SE MUESTRA EL ERROR Y SE REGRESA AL MENU.
    except sqlite3.Error as e:
        conexion.rollback()
        print("\n")
        print("Error al registrar el producto:", e)

#MUESTRA TODOS LOS PRODUCTOS REGISTRADOS EN LA BASE DE DATOS.
def mostrarProductos():

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
       print("\n")
       print("No hay productos registrados.")
    else:
        for producto in productos:
            print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripcion: {producto[2]} - Cantidad: {producto[3]} - Precio: {producto[4]} - Categoria: {producto[5]}")
            
    return productos

#ACTUALIZA UN PRODUCTO EN LA BASE DE DATOS, RECIBE LA COLUMNA QUE SE DESEA ACTUALIZAR, EL NUEVO VALOR Y EL ID DEL PRODUCTO. 
def actualizarProducto(columna, nuevoValor, id_producto):
    
    cursor.execute(f"UPDATE productos SET {columna} = ? WHERE id = ?", (nuevoValor, id_producto))
    conexion.commit()

#ELIMINA UN PRODUCTO DE LA BASE DE DATOS, RECIBE EL ID DEL PRODUCTO.
def eliminarProducto(id_producto):
    
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()

#BUSCA UN PRODUCTO EN LA BASE DE DATOS, RECIBE EL ID DEL PRODUCTO.
def buscarProducto(id_producto):
    
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    
    producto = cursor.fetchone()

    if producto == None:
        print("\n")
        print("No existe un producto con ese ID.")
    
    else:
        print("\n")
        print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripcion: {producto[2]} - Cantidad: {producto[3]} - Precio: {producto[4]} - Categoria: {producto[5]}")

#REPORTA LOS PRODUCTOS QUE TIENEN UN STOCK MINIMO, RECIBE LA CANTIDAD MINIMA.
def reportarProducto(cantidadMinima):
    
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (cantidadMinima,))
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("\n")
        print("No hay productos con stock minimo.")
    else:
        for producto in productos:
            print("\n")
            print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripcion: {producto[2]} - Cantidad: {producto[3]} - Precio: {producto[4]} - Categoria: {producto[5]}")

#CREE UNA FUNCION QUE IMPRIMA EL MENU PRINCIPAL.
def menu():
    
    print ("\n")
    print (Fore.CYAN + "========== Menu Principal ==========")
    print ("Ingresa 1 para AGREGAR un producto.")
    print ("Ingresa 2 para MOSTRAR productos.")
    print ("Ingresa 3 para ACTUALIZAR un producto.")
    print ("Ingresa 4 para ELIMINAR un producto.")
    print ("Ingresa 5 para BUSCAR un producto.")
    print ("Ingresa 6 para REPORTAR productos por stock.")
    print ("Ingresa 7 para SALIR.")

#INICIA EL PROGRAMA.
print ("\n")
print (Fore.BLUE + "////////// Sistema de Gestion de Inventario //////////")

programa = True

while programa == True:
#IMPRIME EL MENU
    menu()
    
#PREVIAMENTE ERA INT(INPUT("OPCION: ")), PERO LO DEJE COMO STRING PARA QUE EN CASO DE QUE EL USUARIO INGRESE UNA LETRA, NO SE CIERRE EL PROGRAMA Y SE EJECUTE EL ELSE.
    print ("\n")
    opcion = input (Fore.YELLOW + "Opcion: ")

    if opcion == "1":
        
        print ("\n")
        nombre = input (Fore.YELLOW + "Ingresa el nombre del producto: ").capitalize().strip()
        descripcion = input (Fore.YELLOW + "Ingresa su descripcion: ").capitalize().strip()
        
#ESTE BUCLE CONTROLA QUE LA CANTIDAD SEA UN NUMERO ENTERO POSITIVO.
        controlCantidad = True
        while controlCantidad == True:
            
            try:
                cantidad = int (input (Fore.YELLOW + "Ingresa su cantidad: "))
                
                if cantidad < 0:
                    print ("\n")
                    print ("ERROR: La cantidad no puede ser negativa.")
                elif cantidad == 0:
                    print ("\n")
                    print ("ERROR: La cantidad no puede ser cero.")
                else:
                    break

            except ValueError:
                print ("\n")
                print ("ERROR: Debes ingresar un numero para la cantidad.")

#ESTE BUCLE CONTROLA QUE EL PRECIO SEA UN NUMERO DECIMAL POSITIVO.
        controlPrecio = True
        while controlPrecio == True:
            
            try:
                precio = float (input (Fore.YELLOW + "Ingresa su precio: $"))
                
                if precio < 0:
                    print ("\n")
                    print ("ERROR: El precio no puede ser negativo.")
                
                elif precio == 0:
                    print ("\n")
                    print ("ERROR: El precio no puede ser cero.")
                
                else:
                    break

            except ValueError:
                print ("\n")
                print ("ERROR: Debes ingresar un numero para el precio.")

        categoria = input (Fore.YELLOW + "Ingresa su categoria: ").capitalize().strip()
        
        registrarProducto(nombre, descripcion, cantidad, precio, categoria)

#MUESTRA TODOS LOS PRODUCTOS REGISTRADOS EN LA BASE DE DATOS.
    elif opcion == "2":
        print ("\n")
        mostrarProductos()

#ACTUALIZA UN PRODUCTO EN LA BASE DE DATOS, RECIBE LA COLUMNA QUE SE DESEA ACTUALIZAR, EL NUEVO VALOR Y EL ID DEL PRODUCTO.
    elif opcion == "3":
        print ("\n")  
        productos = mostrarProductos()
        
        print ("\n")
        idProducto = int(input(Fore.YELLOW + "Ingresa el ID del producto que queres actualizar: "))
        
        print ("\n")
        for producto in productos:
            if producto[0] == idProducto:
               nombreProducto = producto[1]
               print (f'¿Que dato de {nombreProducto} queres actualizar?')

#CREE UN SUBMENU PARA ACTUALIZAR LOS PRODUCTOS DE FORMA MAS VISUAL. ESTA PARTE DEL CODIGO SE LLEVA LOS ARGUMENTOS DE MANERA SENCILLA PARA INTERACTUAR CON LA FUNCION ACTUALIZAR PRODUCTO.   
        print ("\n")
        print ("Ingresa 1 para actualizar el nombre.")
        print ("Ingresa 2 para actualizar la descripcion.")
        print ("Ingresa 3 para actualizar la cantidad.")
        print ("Ingresa 4 para actualizar el precio.")
        print ("Ingresa 5 para actualizar la categoria.")
        
        print ("\n")
        actualizarDato = int(input(Fore.YELLOW + "Ingresa el dato que queres actualizar: "))

        if actualizarDato == 1:

            columna = "nombre"
            nuevoValor = input(Fore.YELLOW + "Ingresa el nuevo nombre: ").capitalize().strip()  
            print ("\n")
            print (f"Acabas de actualizar el nombre de {nombreProducto} a {nuevoValor}")  
            actualizarProducto(columna, nuevoValor, idProducto)

        elif actualizarDato == 2:

            columna = "descripcion"
            nuevoValor = input(Fore.YELLOW + "Ingresa la nueva descripcion: ").capitalize().strip() 
            print ("\n")
            print (f"Acabas de actualizar la descripcion de {nombreProducto} a {nuevoValor}")   
            actualizarProducto(columna, nuevoValor, idProducto)

        elif actualizarDato == 3:

            columna = "cantidad"
            nuevoValor = int(input(Fore.YELLOW + "Ingresa la nueva cantidad: "))    
            print ("\n")
            print (f"Acabas de actualizar la cantidad de {nombreProducto} a {nuevoValor}")   
            actualizarProducto(columna, nuevoValor, idProducto)

        elif actualizarDato == 4:

            columna = "precio"
            nuevoValor = float(input(Fore.YELLOW + "Ingresa el nuevo precio: "))    
            print ("\n")
            print (f"Acabas de actualizar el precio de {nombreProducto} a {nuevoValor}")   
            actualizarProducto(columna, nuevoValor, idProducto)

        elif actualizarDato == 5:

            columna = "categoria"
            nuevoValor = input(Fore.YELLOW + "Ingresa la nueva categoria: ").capitalize().strip() 
            print ("\n")
            print (f"Acabas de actualizar la categoria de {nombreProducto} a {nuevoValor}")   
            actualizarProducto(columna, nuevoValor, idProducto)
        
        else:
            print ("\n")
            print ("Opcion no valida. Intentalo de nuevo.")
               
#ELIMINA UN PRODUCTO DE LA BASE DE DATOS, RECIBE EL ID DEL PRODUCTO. REQUIERE UNA CONFIRMACION EN LA TERMINAL PREVIO A ELIMINAR EL PRODUCTO.
    elif opcion == "4":
        
        print ("\n")  
        productos = mostrarProductos()
        
        print ("\n")
        idProducto = int(input(Fore.YELLOW + "Ingresa el ID del producto que queres eliminar: "))
        
        nombreProducto = ""
        for producto in productos:
            if producto[0] == idProducto:
               nombreProducto = producto[1]
               
        if nombreProducto == "":
            print ("\n")
            print ("Producto no encontrado.")
            
        else:
            print ("\n")
            print (f'Estas a punto de ELIMINAR {nombreProducto}, esta accion es irreversible. ¿ESTAS SEGURO?')
        
            print ("\n")
            confirmacion = input(Fore.YELLOW + "Ingresa 'Y' para confirmar o 'N' para cancelar: ").upper()
        
            if confirmacion == "Y":
                eliminarProducto(idProducto)
                print ("\n")
                print (f"Acabas de eliminar {nombreProducto}.")
        
            else:
                print ("\n")
                print ("Operacion cancelada.")

#BUSCA UNICAMENTE UN PRODUCTO EN LA BASE DE DATOS, RECIBE EL ID DEL PRODUCTO.
    elif opcion == "5":
        
        print ("\n")
        idProducto = int(input(Fore.YELLOW + "Ingresa el ID del producto que queres buscar: "))
        
        buscarProducto(idProducto)
        
#CONTROL DE STOCK SEGUN LA CANTIDAD MINIMA.
    elif opcion == "6":
        
        print ("\n")
        cantidadMinima = int(input(Fore.YELLOW + "Ingresa la cantidad minima: "))
        reportarProducto(cantidadMinima)

#SALIR DEL PROGRAMA, CIERRA LA CONEXION A LA BASE DE DATOS Y SALE DEL CICLO WHILE.
    elif opcion == "7":
        
        print ("\n")
        print ("Saliendo del programa...")
        
        conexion.close()
        break
    
    else:
        print ("\n")
        print ("Opcion no valida. Intentalo de nuevo.")