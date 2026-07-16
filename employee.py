import json
import os

FILE_NAME = "employees.json"

employees = []


def load_data():
    global employees
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            employees = json.load(file)
    else:
        employees = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


def insert():
    load_data()

    n = int(input("\nEnter number of employees to add: "))

    for i in range(n):
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        age = input("Enter Employee Age: ")
        department = input("Enter Employee Department: ")
        salary = input("Enter Employee Salary: ")

        employees.append({
            "Employee ID": eid,
            "Employee Name": name,
            "Employee Age": age,
            "Employee Department": department,
            "Employee Salary": salary
        })

    save_data()
    print("\nEmployees added successfully.")


def read():
    load_data()

    if len(employees) == 0:
        print("\nNo employees found.")
        return []

    print("\nEmployee List")
    for e in employees:
        print(
            f"ID: {e['Employee ID']}, "
            f"Name: {e['Employee Name']}, "
            f"Age: {e['Employee Age']}, "
            f"Department: {e['Employee Department']}, "
            f"Salary: {e['Employee Salary']}"
        )

    return employees


def update():
    load_data()

    eid = input("\nEnter Employee ID to update: ")

    for e in employees:
        if e["Employee ID"] == eid:
            e["Employee Name"] = input("Enter New Name: ")
            e["Employee Age"] = input("Enter New Age: ")
            e["Employee Department"] = input("Enter New Department: ")
            e["Employee Salary"] = input("Enter New Salary: ")

            save_data()
            print("\nEmployee updated successfully.")
            return

    print("\nEmployee not found.")


def delete():
    load_data()

    eid = input("\nEnter Employee ID to delete: ")

    for e in employees:
        if e["Employee ID"] == eid:
            employees.remove(e)
            save_data()
            print("\nEmployee deleted successfully.")
            return

    print("\nEmployee not found.")


def exit_program():
    print("\nExiting Program...")
    exit()

def get_salary_expense():

    load_data()

    salary = {
        "CSE": 0,
        "ECE": 0,
        "EEE": 0
    }
    department_map = {
        "CS": "CSE",
        "CSE": "CSE",
        "COMPUTER SCIENCE ENGINEERING": "CSE",

        "EC": "ECE",
        "ECE": "ECE",
        "ELECTRONICS AND COMMUNICATION ENGINEERING": "ECE",

        "EE": "EEE",
        "EEE": "EEE",
        "ELECTRICAL AND ELECTRONICS ENGINEERING": "EEE"
    }

    for e in employees:

        dep = e["Employee Department"].upper()

        if dep in department_map:
            salary[
                department_map[dep]
            ] += int(e["Employee Salary"])

    return salary