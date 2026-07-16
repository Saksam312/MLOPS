FILE_NAME = "management.json"

students = []
employees = []


import students
import employee


while True:

    print("\n========== MAIN MENU ==========")
    print("1. Student Management")
    print("2. Employee Management")
    print("3. Exit")

    choice = input("\nSelect Option: ")


    # ---------------- STUDENT MENU ----------------

    if choice == "1":

        while True:

            print("\n===== Student Management =====")
            print("1. Insert Student")
            print("2. Read Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back to Main Menu")


            ch = input("\nEnter your choice: ")


            if ch == "1":
                students.insert()

            elif ch == "2":
                students.read()

            elif ch == "3":
                students.update()

            elif ch == "4":
                students.delete()

            elif ch == "5":
                break

            else:
                print("\nInvalid choice.")



    # ---------------- EMPLOYEE MENU ----------------

    elif choice == "2":

        while True:

            print("\n===== Employee Management =====")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Back to Main Menu")


            ch = input("\nEnter your choice: ")


            if ch == "1":
                employee.insert()

            elif ch == "2":
                employee.read()

            elif ch == "3":
                employee.update()

            elif ch == "4":
                employee.delete()

            elif ch == "5":
                break

            else:
                print("\nInvalid choice.")



    # ---------------- EXIT ----------------

    elif choice == "3":

        print("\nExiting Program...")
        break


    else:

        print("\nInvalid choice.")