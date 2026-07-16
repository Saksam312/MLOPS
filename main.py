import students

while True:
    print("\n===== Student Management =====")
    print("1. Insert")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            students.insert()

        case 2:
            students.read()

        case 3:
            students.update()

        case 4:
            students.delete()

        case 5:
            students.exit_program()

        case _:
            print("\nInvalid choice.")