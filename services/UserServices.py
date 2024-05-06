from entities.enums.CustomerType import CustomerType
from services.ScreenNotification import ScreenNotification
from entities.User import User
from services.EmailNotification import EmailNotification


class UserServices:
    def __init__(self):
        self.users = [];



    def createUser(self):
        id = input("id: ");
        name = input("Nombre: ");
        identification = input("Identificación: ");
        address = input("Dirección: ");
        phoneNumber = input("Teléfono: ");
        email = input("Correo electrónico: ");

        if self.findById(id):
            print(f"El id ya está registrado.");
            return None

        customerType = input("Tipo de cliente 1 para Comprador Ocasional, 2 para Comprador Mayorista: ")
        if customerType == "1":
            customerType = CustomerType.OCASIONAL
        elif customerType == "2":
            customerType = CustomerType.MAYORISTA
        else:
            print("Opción inválida")
            return None

        new_user = User(id, name, identification, address, phoneNumber, email, customerType)
        self.users.append(new_user)

        self.registerUser(new_user);
        print("Usuario creado: ");
        print(new_user);
        return new_user

    def registerUser(self, user):
        print(f"Registrando usuario")
        if user.customerType == CustomerType.MAYORISTA:
            notification = EmailNotification();
            message = notification.sendNotification(user);
        else:
            notification = ScreenNotification();
            message = notification.sendNotification(user);

        self.users.append(user);
        return message


    def findById(self, id):
        for user in self.users:
            if user.id == id:
                return user;

        return None

    def upgradeUser(self, id, newUser):
        user = self.findById(id)
        if user:
            print(f"Actualizando la información del usuario {user.name}");
            user.name = newUser.get("name", user.name);
            user.identification = newUser.get("identification", user.identification);
            user.address = newUser.get("address", user.address);
            user.phoneNumber = newUser.get("phone", user.phoneNumber);
            user.email = newUser.get("email", user.email);
            user.customer_type = newUser.get("customerType", user.customerType);
            print(f"User updated: {user}");
        else:
            print("El usuario no fue encontrado");

    def deleteUser(self, id):
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                print(f"Usuario con id {id} eliminado.");
            else:
                return print("No se encontro el usuario");


