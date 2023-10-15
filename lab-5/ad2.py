class Owner:
    def __init__(self, name, address, profession, license_number):
        self.name = name
        self.address = address
        self.profession = profession
        self.license_number = license_number

    def displayOwner(self):
        print("Owner Details:")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Profession: {self.profession}")
        print(f"License Number: {self.license_number}")

class Car:
    def __init__(self, engine_number, reg_number, reg_date, color, owner, model):
        self.engine_number = engine_number
        self.reg_number = reg_number
        self.reg_date = reg_date
        self.color = color
        self.owner = owner
        self.model = model

    def displayCarDetails(self):
        print("Car Details:")
        print(f"Engine Number: {self.engine_number}")
        print(f"Registration Number: {self.reg_number}")
        print(f"Registration Date: {self.reg_date}")
        print(f"Color: {self.color}")
        self.owner.displayOwner()  # Display owner details using the Owner class method
        print(f"Model: {self.model}")

# Create owner objects
owner1 = Owner("John Doe", "123 Main St", "Engineer", "DL12345")
owner2 = Owner("Alice Smith", "456 Elm St", "Teacher", "DL67890")
owner3 = Owner("Bob Johnson", "789 Oak St", "Doctor", "DL54321")
owner4 = Owner("Mary Wilson", "101 Pine St", "Lawyer", "DL98765")
owner5 = Owner("David Lee", "202 Cedar St", "Artist", "DL24680")

# Create car objects with owners
car1 = Car("12345", "ABC123", "2023-01-15", "Red", owner1, "Sedan")
car2 = Car("67890", "XYZ456", "2023-02-20", "Blue", owner2, "SUV")
car3 = Car("54321", "PQR789", "2023-03-25", "Green", owner3, "Hatchback")
car4 = Car("98765", "LMN101", "2023-04-30", "Silver", owner4, "Convertible")
car5 = Car("24680", "UVW202", "2023-05-01", "Black", owner5, "Sports")

# Display car details
car1.displayCarDetails()
print("\n")
car2.displayCarDetails()
print("\n")
car3.displayCarDetails()
print("\n")
car4.displayCarDetails()
print("\n")
car5.displayCarDetails()
