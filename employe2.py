import pandas as pd


def get_employee_data():

    employees = []

    n = int(input("Enter number of employees: "))

    for i in range(n):

        print("\nEmployee", i+1)

        name = input("Enter employee name: ")
        dept = input("Enter department: ")
        salary = float(input("Enter salary: "))
        capacity = int(input("Enter mentor capacity: "))

        employees.append(
            [
                name,
                dept,
                salary,
                capacity
            ]
        )


    employee_df = pd.DataFrame(
        employees,
        columns=[
            "employee_name",
            "dept",
            "salary",
            "mentor_capacity"
        ]
    )


    employee_df.to_csv(
        "employee_data.csv",
        index=False
    )


    return employee_df