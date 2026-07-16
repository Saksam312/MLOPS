import employee
import students
import matplotlib.pyplot as plt



employee_expense = employee.get_salary_expense()

student_fees = students.get_total_fees()



courses = [
    "CSE",
    "ECE",
    "EEE"
]


salary_values=[]


for c in courses:

    salary_values.append(
        employee_expense[c]
    )



print("\nEmployee Salary Expense")

for c in courses:

    print(
        c,
        ":",
        employee_expense[c]
    )



print("\nStudent Fees Collection")

for c in courses:

    print(
        c,
        ":",
        student_fees[c]
    )



# Sorting according to course

sorted_salary = sorted(
    employee_expense.items(),
    key=lambda x:x[1],
    reverse=True
)


print("\nSorted Salary Expense")

for item in sorted_salary:

    print(item)



# Bar chart


colors=[
    "red",
    "blue",
    "green"
]


plt.bar(
    courses,
    salary_values,
    color=colors
)


plt.xlabel("Engineering Course")

plt.ylabel("Employee Salary Expense")

plt.title(
    "Employee Salary Expense Distribution"
)


plt.show()