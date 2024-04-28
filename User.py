class User:

    def __init__(self, id, name, identification, address, phoneNumber, email, customerType):
        self.id = id;
        self.name = name;
        self.identification = identification;
        self.address = address;
        self.phoneNumber = phoneNumber;
        self.email = email;
        self.customerType = customerType;

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Email: {self.email}, Dirección: {self.address}, Teléfono: {self.phoneNumber}, Tipo de Cliente: {self.customerType}"

