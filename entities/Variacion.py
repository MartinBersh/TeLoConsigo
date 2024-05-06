from entities.Producto import Product


class Variacion(Product):
    def __init__(self, id, nombre, sku, descripcion, precio, categoria,
                 existencia_disponible, lista_imagenes, fecha_creacion, fecha_actualizacion,
                 talla, color):
        super().__init__(id, nombre,sku, descripcion, precio, categoria,
                         existencia_disponible, lista_imagenes, fecha_creacion, fecha_actualizacion)
        self.talla = talla;
        self.color = color;

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio: {self.precio}\n"
                f"Categoría: {self.categoria}\n"
                f"Existencia Disponible: {self.existencia_disponible}\n"
                f"Lista de Imágenes: {self.lista_imagenes}\n"
                f"Fecha de Creación: {self.fecha_creacion}\n"
                f"Fecha de Actualización: {self.fecha_actualizacion}\n"
                f"Talla: {self.talla}\n"
                f"Color: {self.color}\n"
                f"SKU: {self.sku}");
