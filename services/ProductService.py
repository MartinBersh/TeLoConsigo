from entities.Producto import Product
from entities.Variacion import Variacion
from entities.enums.Categoria import Categoria


class ProductService:
    def __init__(self):
        self.productos = [];

    def crearProductoVariedad(self):

        id = input("ID producto: ")
        nombre = input("Nombre: ")
        sku = input("Sku:")
        descripcion = input("Descripcion del producto: ")
        precio = input("Precio:")
        existencia = input("Existe el producto:")
        imagenes = input("imagenes: ")
        fecha_creacion = input("Fecha creacion: ")
        fecha_actu = input("Fecha actu: ")
        talla = input("Inserte talla: ")
        color = input("Color del producto: ")

        categoriaprod = input("Ingrese 1 para accesorio electrónico. 2 Ropa. 3 computadores. 4 celulares: ")
        if categoriaprod == "1":
            categoria = Categoria.ACCESORIO_ELECTRONICO
        elif categoriaprod == "2":
            categoria = Categoria.ROPA
        elif categoriaprod == "3":
            categoria = Categoria.COMPUTADORES
        elif categoriaprod == "4":
            categoria = Categoria.CELULARES

        newProduct = Variacion(id, nombre, sku, descripcion, precio,categoria, existencia, imagenes, fecha_creacion,
                               fecha_actu, talla, color,)
        self.productos.append(newProduct);
        print(f"Producto creado: {newProduct}")

    def crearProductoNormal(self):
        id = input("ID producto: ")
        nombre = input("Nombre: ")
        sku = input("Sku:")
        descripcion = input("Descripcion del producto: ")
        precio = input("Precio:")
        existencia = input("Existe el producto:")
        imagenes = input("imagenes: ")
        fecha_creacion = input("Fecha creacion: ")
        fecha_actu = input("Fecha actu: ")

        categoria = input("Ingrese 1 para accesorio electrónico. 2 Ropa. 3 computadores. 4 celulares: ")
        if categoria == 1:
            categoria = Categoria.ACCESORIO_ELECTRONICO
        elif categoria == 2:
            categoria = Categoria.ROPA
        elif categoria == 3:
            categoria = Categoria.COMPUTADORES
        elif categoria == 4:
            categoria = Categoria.CELULARES

        newProduct = Product(id, nombre, sku, descripcion, precio, categoria, existencia, imagenes, fecha_creacion,
                               fecha_actu)
        self.productos.append(newProduct);
        print(f"Producto creado: {newProduct}")


    def findById(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto;
        return None

    def upgradeProduct(self, id):
        product = self.findById(id)
        if isinstance(product, Variacion):
            product.nombre = input("Nombre: ")
            product.sku = input("Sku:")
            product.descripcion = input("Descripcion del producto: ")
            product.precio = input("Precio:")
            product.existencia = input("Existe el producto:")
            product.imagenes = input("imagenes: ")
            product.fecha_creacion = input("Fecha creacion: ")
            product.fecha_actu = input("Fecha actu: ")
            product.talla = input("Inserte talla: ")
            product.color = input("Color del producto: ")

            categoria = input("Ingrese 1 para accesorio electrónico. 2 Ropa. 3 computadores. 4 celulares")
            if categoria == 1:
                product.categoria = Categoria.ACCESORIO_ELECTRONICO
            elif categoria == 2:
                product.categoria = Categoria.ROPA
            elif categoria == 3:
                product.categoria = Categoria.COMPUTADORES
            elif categoria == 4:
                product.categoria = Categoria.CELULARES

        else:
            product.nombre = input("Nombre: ")
            product.sku = input("Sku:")
            product.descripcion = input("Descripcion del producto: ")
            product.precio = input("Precio:")
            product.existencia = input("Existe el producto:")
            product.imagenes = input("imagenes: ")
            product.fecha_creacion = input("Fecha creacion: ")
            product.fecha_actu = input("Fecha actu: ")

            categoria = input("Ingrese 1 para accesorio electrónico. 2 Ropa. 3 computadores. 4 celulares")
            if categoria == 1:
              product.categoria = Categoria.ACCESORIO_ELECTRONICO
            elif categoria == 2:
              product.categoria = Categoria.ROPA
            elif categoria == 3:
              product.categoria = Categoria.COMPUTADORES
            elif categoria == 4:
              product.categoria = Categoria.CELULARES


    def deleteProduct(self, id):
        product = self.findById()
        self.productos.remove(product)



