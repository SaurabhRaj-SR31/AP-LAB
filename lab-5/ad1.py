class Employee:
    next_employee_id = 2912
    total_salary = 0
    employee_list = []

    def __init__(self, name, salary, department):
        self.id = Employee.next_employee_id
        Employee.next_employee_id += 1
        self.name = name
        self.salary = salary
        self.department = department
        Employee.total_salary += self.salary
        Employee.employee_list.append(self)

    def __del__(self):
        Employee.total_salary -= self.salary
        Employee.employee_list.remove(self)

    def display(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    @classmethod
    def compute_total_salary(cls):
        return cls.total_salary


def search_employee(employee_id):
    for emp in Employee.employee_list:
        if emp.id == employee_id:
            emp.display()
            break
    else:
        print(f"Employee with ID {employee_id} not found.")


if __name__ == "__main__":
    n = int(input("Enter the number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        department = input("Enter employee department: ")
        employee = Employee(name, salary, department)

    while True:
        print("\nOptions:")
        print("1. Search for an employee by ID")
        print("2. Compute total salary of all employees")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp_id = int(input("Enter the ID of the employee to search: "))
            search_employee(emp_id)
        elif choice == 2:
            total_salary = Employee.compute_total_salary()
            print(f"Total salary of all employees: {total_salary}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
