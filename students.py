import json
import os

FILE_NAME = "students.json"

students = []


# Load data from JSON file
def load_data():

    global students

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            students = json.load(file)

    else:
        students = []



# Save data to JSON file
def save_data():

    with open(FILE_NAME, "w") as file:

        json.dump(
            students,
            file,
            indent=4
        )



# Insert student
def insert():

    load_data()

    n = int(input("\nEnter number of students to add: "))


    for i in range(n):

        print("\nEnter Student Details")

        sid = input("Enter Student ID: ")

        name = input("Enter Student Name: ")

        age = input("Enter Student Age: ")

        course = input(
            "Enter Student Course (CSE/ECE/EEE): "
        ).upper()

        fees = input(
            "Enter Student Fees: "
        )


        student = {

            "Student ID": sid,

            "Student Name": name,

            "Student Age": age,

            "Student Course": course,

            "Student Fees": fees

        }


        students.append(student)



    save_data()

    print("\nStudents added successfully.")

# Display students
def read():

    load_data()


    if len(students) == 0:

        print("\nNo students found.")

        return



    print("\n===== Student List =====")


    for s in students:


        print(
            "ID:",
            s["Student ID"],
            "| Name:",
            s["Student Name"],
            "| Age:",
            s["Student Age"],
            "| Course:",
            s["Student Course"],
            "| Fees:",
            s.get("Student Fees",0)
        )



    return students


# Update student
def update():

    load_data()


    sid = input(
        "\nEnter Student ID to update: "
    )


    for s in students:


        if s["Student ID"] == sid:


            s["Student Name"] = input(
                "Enter New Name: "
            )


            s["Student Age"] = input(
                "Enter New Age: "
            )


            s["Student Course"] = input(
                "Enter New Course: "
            ).upper()


            s["Student Fees"] = input(
                "Enter New Fees: "
            )


            save_data()


            print(
                "\nStudent updated successfully."
            )

            return



    print(
        "\nStudent not found."
    )



# Delete student
def delete():

    load_data()


    sid = input(
        "\nEnter Student ID to delete: "
    )


    for s in students:


        if s["Student ID"] == sid:


            students.remove(s)


            save_data()


            print(
                "\nStudent deleted successfully."
            )

            return



    print(
        "\nStudent not found."
    )



# Calculate fees according to course
def get_total_fees():


    load_data()


    fees = {

        "CSE": 0,

        "ECE": 0,

        "EEE": 0

    }

    course_map = {


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

    for s in students:


        course = s["Student Course"].upper()


        if course in course_map:


            amount = int(
                s.get("Student Fees",0)
            )


            fees[
                course_map[course]
            ] += amount



    return fees

# Exit program
def exit_program():

    print(
        "\nExiting Program..."
    )

    exit()