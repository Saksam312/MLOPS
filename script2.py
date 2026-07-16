employee={}
employee["id"]=int(input("Enter id "))
employee["name"]=int(input("Entername "))
employee["department"]=int(input("Enter department "))
employee["salary"]=int(input("Enter salary "))

employees.append(employee)
case 1 :(
    print("\n Employees added successfully"))

case 2 :(
    print("\n Employee List"))

employees = []


def insert():
    n = int(input("\nEnter number of employees to add: "))
    for i in range(n):
        name = input(f"Enter employee {i + 1} name: ")
        employees.append(name)
    print("\nEmployees added successfully.")


def read():
    if len(employees) == 0:
        print("\nNo employees found.")
    else:
        print("\nEmployee List:")
        for i, emp in enumerate(employees, start=1):
            print(f"{i}. {emp}")


def update():
    old_name = input("\nEnter employee name to update: ")

    if old_name in employees:
        new_name = input("Enter new employee name: ")
        index = employees.index(old_name)
        employees[index] = new_name
        print("\nEmployee updated successfully.")
    else:
        print("\nEmployee not found.")


def delete():
    name = input("\nEnter employee name to delete: ")

    if name in employees:
        employees.remove(name)
        print("\nEmployee deleted successfully.")
    else:
        print("\nEmployee not found.")


def exit_program():
    print("\nExiting program...")
    exit()


while True:
    print("\n===== Employee Management =====")
    print("1. Insert")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            insert()

        case 2:
            read()

        case 3:
            update()

        case 4:
            delete()

        case 5:
            exit_program()

        case _:
            print("\nInvalid choice. Please try again.")

employees = []

while True:
    print("\n===== Employee Management =====")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    c = int(input("\nEnter your choice: "))

    match c:

        case 1:
            n = int(input("\nEnter number of employees to add: "))
            for i in range(n):
                name = input(f"\nEnter employee {i + 1} name: ")
                employees.append(name)
            print("Employees added successfully.")

        case 2:
            if len(employees) == 0:
                print("No employees found.")
            else:
                print("\nEmployee List:")
                for i, emp in enumerate(employees, start=1):
                    print(f"{i}. {emp}")

        case 3:
            old_name = input("\nEnter employee name to update: ")
            if old_name in employees:
                new_name = input("\nEnter new employee name: ")
                index = employees.index(old_name)
                employees[index] = new_name
                print("\nEmployee updated successfully.")
            else:
                print("\nEmployee not found.")

        case 4:
            name = input("\nEnter employee name to delete: ")
            if name in employees:
                employees.remove(name)
                print("\nEmployee deleted successfully.")
            else:
                print("\nEmployee not found.")

        case 5:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice. Please try again.")
