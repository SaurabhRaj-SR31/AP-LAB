class Vehicle:
    def __init__(self):
        self.owner_name = ""
        self.vehicle_id = ""
        self.manufacturer_name = ""

    def input_data(self):
        self.owner_name = input("Enter the vehicle owner's name: ")
        self.vehicle_id = input("Enter the vehicle identification number: ")
        self.manufacturer_name = input("Enter the manufacturer's name: ")

    def display_data(self):
        print("Vehicle Owner:", self.owner_name)
        print("Vehicle ID:", self.vehicle_id)
        print("Manufacturer:", self.manufacturer_name)


class Passenger(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_passengers = 0

    def input_data(self):
        super().input_data()
        self.num_passengers = int(input("Enter the number of passengers: "))

    def display_data(self):
        super().display_data()
        print("Number of Passengers:", self.num_passengers)


vehicle = Passenger()
vehicle.input_data()
print("\nVehicle Information:")
vehicle.display_data()
