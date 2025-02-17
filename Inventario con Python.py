import pandas as pd

def ingresar_producto(inventario):
    print("Ingresar producto")
    id_producto = input("Ingrese el ID del producto: ")
    
    if id_producto in inventario:
        print("Error: Ya existe un producto con este ID.")
        return
    
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo del producto: "))
    
    inventario[id_producto] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "stock_minimo": stock_minimo,
        "ventas": 0  # Contador de ventas inicializado en cero
    }
    print("Producto ingresado con éxito.")

def mostrar_todos(inventario):
    print("Lista de productos")
    for id_producto, datos in inventario.items():
        print(f"ID: {id_producto}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

def control_stock(inventario):
    print("Control de Stock")
    productos_bajo_stock = {id: prod for id, prod in inventario.items() if prod['cantidad'] <= prod['stock_minimo']}
    
    if productos_bajo_stock:
        for id_producto, datos in productos_bajo_stock.items():
            print(f"ID: {id_producto}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Stock mínimo: {datos['stock_minimo']}")
    else:
        print("No hay productos con stock bajo.")

def buscar_producto(inventario):
    print("Buscar producto")
    id_producto = input("Ingrese el ID del producto: ")
    producto = inventario.get(id_producto)
    
    if producto:
        print(f"Producto encontrado: {producto}")
    else:
        print("Producto no encontrado.")

def modificar_producto(inventario):
    print("Modificar producto")
    id_producto = input("Ingrese el ID del producto a modificar: ")
    
    if id_producto in inventario:
        print("Producto encontrado. Ingrese los nuevos datos.")
        nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
        descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ")
        cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
        precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
        
        if nombre:
            inventario[id_producto]['nombre'] = nombre
        if descripcion:
            inventario[id_producto]['descripcion'] = descripcion
        if cantidad:
            inventario[id_producto]['cantidad'] = int(cantidad)
        if precio:
            inventario[id_producto]['precio'] = float(precio)
        
        print("Producto modificado con éxito.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario):
    print("Eliminar producto")
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    
    if id_producto in inventario:
        del inventario[id_producto]
        print("Producto eliminado con éxito.")
    else:
        print("Producto no encontrado.")

def generar_reportes(inventario):
    print("Generación de Reportes")
    total_productos = len(inventario)
    productos_bajo_stock = sum(1 for datos in inventario.values() if datos['cantidad'] <= datos['stock_minimo'])
    mas_vendidos = sorted(inventario.values(), key=lambda x: x['ventas'], reverse=True)
    
    print(f"Total de productos en inventario: {total_productos}")
    print(f"Productos con stock bajo: {productos_bajo_stock}")
    
    if mas_vendidos:
        print(f"Producto más vendido: {mas_vendidos[0]['nombre']} con {mas_vendidos[0]['ventas']} ventas")
    else:
        print("No se han registrado ventas.")

def exportar_a_excel(inventario):
    print("Exportar a Excel")
    
    if not inventario:
        print("No hay datos en el inventario para exportar.")
        return
    
    df = pd.DataFrame.from_dict(inventario, orient='index')
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ") + ".xlsx"
    
    try:
        df.to_excel(nombre_archivo, index_label='ID Producto', engine='openpyxl')
        print(f"Datos exportados con éxito a {nombre_archivo}.")
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Ingresar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Mostrar todos los productos")
    print("6. Control de Stock")
    print("7. Generar Reportes")
    print("8. Exportar a Excel")
    print("9. Salir")

def main():
    inventario = {}
    opciones = {
        "1": ingresar_producto,
        "2": buscar_producto,
        "3": modificar_producto,
        "4": eliminar_producto,
        "5": mostrar_todos,
        "6": control_stock,
        "7": generar_reportes,
        "8": exportar_a_excel,
        "9": lambda: print("Saliendo del programa. ¡Adiós!")
    }
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        accion = opciones.get(opcion)
        
        if accion:
            accion(inventario)
        else:
            print("Opción no válida. Intente de nuevo.")
        
        if opcion == "9":
            break

if __name__ == "__main__":
    main()