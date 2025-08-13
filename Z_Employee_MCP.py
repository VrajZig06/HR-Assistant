from fastmcp import FastMCP
import os
import csv
import random

MCPServer = FastMCP(
    name="Employee MCP Server"
)

@MCPServer.tool()
async def get_all_employee():
    """
    Retrieve all employee records from the data source.

    This asynchronous function fetches and returns all employee entries 
    from the Employee model or collection.

    Returns:
        list : A collection of Employee objects.
    """
    try:
        employees = []
        with open("EmployeData/employeeDetails.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append({
                    "emp_id": int(row["emp_id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": float(row["salary"])
                })
        return employees
    except FileNotFoundError:
        print("ERROR: File not found.")
        return []
    except Exception as e:
        print("ERROR:", e)
        return []

@MCPServer.tool
async def get_particular_employee(emp_id:int):
    """
    Retrieve details of a specific employee by their ID.

    This asynchronous function searches the Employee model or collection 
    for a record matching the given employee ID and returns the corresponding 
    employee details.

    Args:
        emp_id (int or str): The unique identifier of the employee.

    Returns:
        Employee: The Employee object if found, otherwise None.
    """

    try:
        Employee = []
        with open("EmployeData/employeeDetails.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Employee.append({
                    "emp_id": int(row["emp_id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": float(row["salary"])
                })

        EmpDetails = None
        for employee in Employee:
            if employee['emp_id'] == emp_id:
                EmpDetails = employee
                break
            else:
                EmpDetails = None

        if EmpDetails is not None:
            return EmpDetails
        else:
            return "Employee not found with this id"
    except Exception as e:
        print("ERROR : " ,e)

@MCPServer.tool()
async def get_total_numbers_of_employees() -> int:
    """
    Retrieve the total number of employees in the system.

    Returns:
        int: The total count of employees available in the Employee dataset.
    """

    try:
        Employee = []
        with open("EmployeData/employeeDetails.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Employee.append({
                    "emp_id": int(row["emp_id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": float(row["salary"])
                })
        total_employees = len(Employee)
        return total_employees
    except Exception as e:
        print("Error ",e)
    

@MCPServer.tool()
async def add_employee(name: str, department: str, salary: str):
    """
    Add a new employee to the employee records CSV file.

    Args:
        name (str): Employee's full name.
        department (str): Department where the employee works.
        salary (int): Employee's salary.

    Returns:
        str: Success message or False if an error occurs.
    """
    try:
        file_path = 'EmployeData/employeeDetails.csv'

        # Get existing employees
        emp_id = random.randint(100,1000000)
        
        # Ensure file exists
        if not os.path.isfile(file_path):
            # Create file with headers if it doesn't exist
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["emp_id","name" , "department", "salary"])

        # Append new employee
        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, name, department, salary])

            return f"Employee Created Succesfully with this {emp_id}"

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    MCPServer.run(transport='stdio')




