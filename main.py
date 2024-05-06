from services.UserServices import UserServices


def printMenu():
    print("Menu");
    print("1. Crear nuevo usuario");
    print("2. Buscar usuario por id");
    print("3. Actualizar infromación de usuario");
    print("4. Eliminar usuario")
    print("5. Salir");


def main():
    userServices = UserServices()


    while True:
        printMenu();
        option = input("Ingrese la opción deseada: ");

        if option == "1":
            print("\nCrear nuevo Usuario:")
            newUser = userServices.createUser()
            if newUser:
                print("Usuario creado con éxito.")

        elif option == "2":
            id = input("\nIngrese el id del usuario para buscar: ")
            userFound = userServices.findById(id);
            if userFound:
                print("\nUsuario:")
                print(userFound)
            else:
                print("\nUsuario no encontrado.")

        elif option == "3":
            id = input("Ingrese el ID del usuario a actualizar: ")
            newUser = {}
            newUser["name"] = input("Nuevo nombre: ")
            newUser["identification"] = input("Nueva identificación: ")
            newUser["address"] = input("Nueva dirección: ")
            newUser["phone"] = input("Nuevo teléfono: ")
            newUser["email"] = input("Nuevo correo electrónico: ")
            newUser["customerType"] = input("Nuevo tipo de cliente"
                                            " (1 para Comprador Ocasional, 2 para Comprador Mayorista): ")

            userServices.upgradeUser(id, newUser)

        elif option == "4":
            id = input("Ingrese el id del usuario a eliminar: ")
            userServices.deleteUser(id)

        elif option == "5":
            print("Saliendo del programa")
            break



        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
