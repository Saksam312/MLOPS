from day2 import employee

employee.employees


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        employee.insert()

    elif choice == "2":
        employee.read()

    elif choice == "3":
        employee.update()

    elif choice == "4":
        employee.delete()

    elif choice == "5":
        employee.exit_program()

    else:
        print("\nInvalid choice. Please try again.")