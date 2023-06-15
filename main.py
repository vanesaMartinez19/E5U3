from ClaseColeccion import ColeccionVehiculos
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado

def print_hi(name):
    pass

if __name__ == '__main__':
    coleccion = ColeccionVehiculos.cargarDesdeArchivo("vehiculos.json")

    while True:
        print("\n=== MENÚ ===")
        print("1. Insertar un vehículo en la colección en una posición determinada.")
        print("2. Agregar un vehículo a la colección.")
        print("3. Dada una posición de la Lista, mostrar qué tipo de objeto se encuentra almacenado en dicha posición.")
        print("4. Dada la patente de un vehículo usado, modificar el precio base y mostrar el precio de venta.")
        print("5. Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
        print(
            "6. Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print("7. Almacenar los objetos de la colección en el archivo 'vehiculos.json'.")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            modelo = input("Ingrese el modelo del vehículo: ")
            cantidad_puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base de venta: "))
            version = input("Ingrese la versión del vehículo (base o full): ")
            vehiculo = VehiculoNuevo(modelo, cantidad_puertas, color, precio_base, version)
            posicion = int(input("Ingrese la posición donde desea insertar el vehículo: "))
            try:
                coleccion.insertarElemento(vehiculo, posicion)
                print("Vehículo insertado correctamente.")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif opcion == "2":
            modelo = input("Ingrese el modelo del vehículo: ")
            cantidad_puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base de venta: "))
            marca = input("Ingrese la marca del vehículo: ")
            patente = input("Ingrese la patente del vehículo usado: ")
            anio = int(input("Ingrese el año del vehículo usado: "))
            kilometraje = int(input("Ingrese el kilometraje del vehículo usado: "))
            vehiculo = VehiculoUsado(modelo, cantidad_puertas, color, precio_base, marca, patente, anio, kilometraje)
            coleccion.agregarElemento(vehiculo)
            print("Vehículo agregado correctamente.")

        elif opcion == "3":
            posicion = int(input("Ingrese la posición de la Lista: "))
            try:
                tipo_vehiculo = coleccion.mostrarElemento(posicion)
                print(f"En la posición {posicion} se encuentra un objeto de tipo {tipo_vehiculo}.")
            except IndexError as e:
                print(f"Error: {str(e)}")

        elif opcion == "4":
            patente = input("Ingrese la patente del vehículo usado: ")
            nuevo_precio_base = float(input("Ingrese el nuevo precio base: "))
            precio_venta = coleccion.modificarPrecioVenta(patente, nuevo_precio_base)
            if precio_venta is not None:
                print(f"El nuevo precio de venta del vehículo usado con patente {patente} es: {precio_venta}")
            else:
                print("No se encontró un vehículo usado con la patente ingresada.")

        elif opcion == "5":
            modelo, cantidad_puertas, importe_venta = coleccion.mostrarVehiculoMasEconomico()
            print(
                f"Vehículo más económico: Modelo: {modelo}, Puertas: {cantidad_puertas}, Importe de Venta: {importe_venta}")

        elif opcion == "6":
            coleccion.mostrarTodosLosVehiculos()

        elif opcion == "7":
            coleccion.guardarEnArchivo("vehiculos.json")
            print("Vehículos almacenados correctamente en el archivo 'vehiculos.json'.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente nuevamente.")
