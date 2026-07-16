import pandas as pd


def get_student_data():

    students = []

    n = int(input("Enter number of students: "))


    for i in range(n):

        print("\nStudent", i+1)

        name = input("Enter student name: ")
        course = input("Enter course: ")
        fee = float(input("Enter course fee: "))
        dept = input("Enter department: ")


        students.append(
            [
                name,
                course,
                fee,
                dept
            ]
        )


    student_df = pd.DataFrame(
        students,
        columns=[
            "name",
            "course",
            "fee",
            "dept"
        ]
    )


    student_df.to_csv(
        "student_data.csv",
        index=False
    )


    return student_df