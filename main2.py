from services.ProductService import ProductService

def printMenu():
    print("Menu");
    print("1. Crear nuevo Producto");
    print("2. Buscar producto por id");
    print("3. Actualizar infromación de producto");
    print("4. Eliminar producto")
    print("5. Salir");


def main():
    productServices = ProductService()


    while True:
        printMenu();
        option = input("Ingrese la opción deseada: ");

        if option == "1":
            tipoProducto = input("Si el producto tiene variación ingrese 1. Si es producto normal ingrese 2\n")
            if tipoProducto == "1":
                productServices.crearProductoVariedad()
            elif tipoProducto == "2":
                productServices.crearProductoNormal()
            else:
                print("Opción invalida")

        elif option == "2":
            id = input("\nIngrese el id del producto para buscar: ")
            productFound = productServices.findById(id);
            if productFound:
                print("\nProducto:")
                print(productFound)
            else:
                print("\nProducto no encontrado.")

        elif option == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            productServices.upgradeProduct(id)

        elif option == "4":
            id = input("Ingrese el id del usuario a eliminar: ")
            productServices.deleteProduct(id)

        elif option == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
