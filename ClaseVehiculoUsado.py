class VehiculoUsado(Vehiculo):
    def __init__(self, modelo, cantidad_puertas, color, precio_base, marca, patente, anio, kilometraje):
        super().__init__(modelo, cantidad_puertas, color, precio_base)
        self.marca = marca
        self.patente = patente
        self.anio = anio
        self.kilometraje = kilometraje

    def calcular_importe_venta(self):
        importe_venta = self.precio_base - (self.precio_base * (2023 - self.anio) * 0.01) # Descuento por antigüedad

        if self.kilometraje > 100000:
            importe_venta -= self.precio_base * 0.02 # Descuento por alto kilometraje

        return importe_venta