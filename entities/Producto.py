class Product:

    def __init__(self, id, nombre, sku, descrpcion, precio, categoria,
                 existencia_disponible, lista_imagenes, fecha_creacion, fecha_actualizacion):
        self.id = id;
        self.nombre = nombre;
        self.sku = sku;
        self.descripcion = descrpcion;
        self.precio = precio;
        self.categoria = categoria;
        self.existencia_disponible = existencia_disponible;
        self.lista_imagenes = lista_imagenes;
        self.fecha_creacion = fecha_creacion;
        self.fecha_actualizacion = fecha_actualizacion;

    def __str__(self):
        return (f"ID: {self.id}\n Nombre: {self.nombre}\n Descripción: {self.descripcion}\n Precio: "
                f"{self.precio}\n Categoría: {self.categoria}\n Existencia Disponible: {self.existencia_disponible}\n"
                f" Lista de Imágenes: {self.lista_imagenes}\n Fecha de Creación: {self.fecha_creacion}\n "
                f"Fecha de Actualización: {self.fecha_actualizacion}");