import json
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado


class ColeccionVehiculos:
    def __init__(self):
        self.vehiculos = []

    def insertarElemento(self, vehiculo, posicion):
        if posicion < 0 or posicion > len(self.vehiculos):
            raise ValueError("Posición no válida")
        self.vehiculos.insert(posicion, vehiculo)

    def agregarElemento(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.vehiculos):
            raise IndexError("Posición no válida")
        tipo_vehiculo = type(self.vehiculos[posicion]).__name__
        return tipo_vehiculo

    def modificarPrecioVenta(self, patente, nuevo_precio_base):
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.patente == patente:
                vehiculo.precio_base = nuevo_precio_base
                return vehiculo.calcular_importe_venta()
        return None

    def mostrarVehiculoMasEconomico(self):
        vehiculo_mas_economico = min(self.vehiculos, key=lambda v: v.calcular_importe_venta())
        return vehiculo_mas_economico.modelo, vehiculo_mas_economico.cantidad_puertas, vehiculo_mas_economico.calcular_importe_venta()

    def mostrarTodosLosVehiculos(self):
        for vehiculo in self.vehiculos:
            importe_venta = vehiculo.calcular_importe_venta()
            print(f"Modelo: {vehiculo.modelo}, Puertas: {vehiculo.cantidad_puertas}, Importe de Venta: {importe_venta}")

    def guardarEnArchivo(self, archivo):
        with open(archivo, "w") as f:
            vehiculos_json = []
            for vehiculo in self.vehiculos:
                vehiculo_data = {
                    "tipo": type(vehiculo).__name__,
                    "modelo": vehiculo.modelo,
                    "cantidad_puertas": vehiculo.cantidad_puertas,
                    "color": vehiculo.color,
                    "precio_base": vehiculo.precio_base
                }

                if isinstance(vehiculo, VehiculoNuevo):
                    vehiculo_data["version"] = vehiculo.version
                elif isinstance(vehiculo, VehiculoUsado):
                    vehiculo_data["marca"] = vehiculo.marca
                    vehiculo_data["patente"] = vehiculo.patente
                    vehiculo_data["anio"] = vehiculo.anio
                    vehiculo_data["kilometraje"] = vehiculo.kilometraje

                vehiculos_json.append(vehiculo_data)

            json.dump(vehiculos_json, f)

    @classmethod
    def cargarDesdeArchivo(cls, archivo):
        coleccion = cls()
        with open(archivo, "r") as f:
            vehiculos_json = json.load(f)
            for vehiculo_data in vehiculos_json:
                tipo_vehiculo = vehiculo_data["tipo"]
                if tipo_vehiculo == "VehiculoNuevo":
                    vehiculo = VehiculoNuevo(
                        vehiculo_data["modelo"],
                        vehiculo_data["cantidad_puertas"],
                        vehiculo_data["color"],
                        vehiculo_data["precio_base"],
                        vehiculo_data["version"]
                    )
                elif tipo_vehiculo == "VehiculoUsado":
                    vehiculo = VehiculoUsado(
                        vehiculo_data["modelo"],
                        vehiculo_data["cantidad_puertas"],
                        vehiculo_data["color"],
                        vehiculo_data["precio_base"],
                        vehiculo_data["marca"],
                        vehiculo_data["patente"],
                        vehiculo_data["anio"],
                        vehiculo_data["kilometraje"]
                    )
                else:
                    raise ValueError("Tipo de vehículo desconocido")

                coleccion.agregarElemento(vehiculo)

        return coleccion



