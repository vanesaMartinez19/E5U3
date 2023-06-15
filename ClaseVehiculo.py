class Vehiculo:
    def __init__(self, modelo, cantidad_puertas, color, precio_base):
        self.modelo = modelo
        self.cantidad_puertas = cantidad_puertas
        self.color = color
        self.precio_base = precio_base

    def calcular_importe_venta(self):
        importe_venta = self.precio_base + (self.precio_base * 0.1)  # Gastos de patentamiento

        if self.version == "full":
            importe_venta += self.precio_base * 0.02

        return importe_venta