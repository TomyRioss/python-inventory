# Lista de productos inicial
inventario = [
    {
        'nombre':'Manzana',
        'precio': 32.00,
        'detalles':'Manzana roja, común.'
    },
    {
        'nombre':'Manzana Premium',
        'precio':120.00,
        'detalles':'Manzana extra jugosa y de sabor más fuerte, más cara.'
    },
     {
        'nombre':'Cebollín',
        'precio':45,
        'detalles':'Cebollín pequeño individual.'
    }
]

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú interactivo de inventario:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    detalles = input("Ingrese los detalles del producto: ")
    producto = {
        'nombre': nombre,
        'precio': precio,
        'detalles': detalles
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

# Función para ver los productos
def ver_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Detalles: {producto['detalles']}")

# Bucle principal para el menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        ver_productos()
    elif opcion == '3':
        print("Saliendo del programa. ¡Adiós!")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
