
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department


def search_employee_by_id(employee_list, target_id):
    for emp in employee_list:
        if emp.emp_id == target_id:
            return emp
    return None


n = int(input("Enter the number of employees: "))
employee_records = []

for i in range(n):
    print(f"Enter details for Employee {i+1}:")
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Employee Salary: "))
    emp_department = input("Enter Employee Department: ")

    emp = Employee(emp_id, emp_name, emp_salary, emp_department)
    employee_records.append(emp)

search_id = input("Enter Employee ID to search: ")
found_employee = search_employee_by_id(employee_records, search_id)

if found_employee:
    print("Employee Found:")
    print("ID:", found_employee.emp_id)
    print("Name:", found_employee.emp_name)
    print("Salary:", found_employee.emp_salary)
    print("Department:", found_employee.emp_department)
else:
    print("Employee not found.")
