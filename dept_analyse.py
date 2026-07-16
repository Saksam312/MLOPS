import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from employe2 import get_employee_data
from student2 import get_student_data


# ==========================================
# Taking Input From User
# ==========================================

employees = get_employee_data()

students = get_student_data()



# ==========================================
# 1. Department Salary Expense
# ==========================================

salary_expense = (
    employees
    .groupby("dept")["salary"]
    .sum()
    .reset_index()
)


salary_expense.rename(
    columns={
        "salary":"total_salary"
    },
    inplace=True
)



# ==========================================
# 2. Department Revenue
# ==========================================

student_revenue = (
    students
    .groupby("dept")["fee"]
    .sum()
    .reset_index()
)


student_revenue.rename(
    columns={
        "fee":"total_revenue"
    },
    inplace=True
)



# ==========================================
# 3. Employee Count
# ==========================================

employee_count = (
    employees
    .groupby("dept")
    .size()
    .reset_index(
        name="total_employees"
    )
)



# ==========================================
# 4. Student Count
# ==========================================

student_count = (
    students
    .groupby("dept")
    .size()
    .reset_index(
        name="total_students"
    )
)
import math

def employee_suggestion(row):

    if row["total_students"] <= row["total_capacity"]:
        return "No requirement"

    shortage = row["total_students"] - row["total_capacity"]

    extra = math.ceil(shortage / row["average_capacity"])

    return f"Add {extra} employee(s)"



# ==========================================
# 5. Mentor Capacity
# ==========================================

mentor_capacity = (
    employees
    .groupby("dept")
    ["mentor_capacity"]
    .sum()
    .reset_index()
)


mentor_capacity.rename(
    columns={
        "mentor_capacity":
        "total_capacity"
    },
    inplace=True
)



# ==========================================
# Merge All Department Data
# ==========================================

department = salary_expense.merge(
    student_revenue,
    on="dept",
    how="outer"
)


department = department.merge(
    employee_count,
    on="dept",
    how="outer"
)


department = department.merge(
    student_count,
    on="dept",
    how="outer"
)


department = department.merge(
    mentor_capacity,
    on="dept",
    how="outer"
)


department.fillna(
    0,
    inplace=True
)



# ==========================================
# Calculations
# ==========================================


# Profit / Loss

department["profit_loss"] = (
    department["total_revenue"]
    -
    department["total_salary"]
)



# Capacity Utilisation

department["capacity_utilisation_%"] = (

    department["total_students"]
    /
    department["total_capacity"]

) * 100



# Students per mentor

department["students_per_mentor"] = (

    department["total_students"]
    /
    department["total_employees"]

).round(2)



# ==========================================
# Employee Requirement
# ==========================================


def employee_suggestion(row):

    # One mentor can handle 30 students

    required = round(
        row["total_students"] / 30
    )


    extra = (
        required
        -
        row["total_employees"]
    )


    if extra > 0:

        return (
            "Add "
            + str(extra)
            + " employees"
        )

    else:

        return "No requirement"



department["suggestion"] = department.apply(
    employee_suggestion,
    axis=1
)



# ==========================================
# Display Result
# ==========================================


print("\n========== Department Report ==========\n")


print(
department[
[
"dept",
"total_revenue",
"total_salary",
"profit_loss",
"total_students",
"total_capacity",
"capacity_utilisation_%",
"students_per_mentor",
"suggestion"
]
]
)



# Save Report

department.to_csv(
"department_report.csv",
index=False
)



# =================================================
# GRAPH 1
# Capacity Utilisation
# =================================================


plt.figure(
    figsize=(10,5)
)


sns.barplot(
    data=department,
    x="dept",
    y="capacity_utilisation_%",
    hue="dept",
    palette="Blues",
    legend=False
)


plt.axhline(
    90,
    color="red",
    linestyle="--",
    label="90% Limit"
)


plt.title(
    "Department Capacity Utilisation"
)


plt.xlabel(
    "Department"
)


plt.ylabel(
    "Capacity Utilisation (%)"
)


plt.legend()

plt.xticks(
    rotation=45
)


plt.tight_layout()

plt.show()



# =================================================
# GRAPH 2
# Profit Loss
# =================================================


plt.figure(
    figsize=(10,5)
)


sns.barplot(
    data=department,
    x="dept",
    y="profit_loss",
    hue="dept",
    palette="RdYlGn",
    legend=False
)


plt.axhline(
    0,
    color="black"
)


plt.title(
    "Department Profit / Loss"
)


plt.xlabel(
    "Department"
)


plt.ylabel(
    "Profit / Loss Amount"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()

plt.show()



# =================================================
# GRAPH 3
# Employee Requirement
# =================================================


department["required_employees"] = (

department["total_students"]
/
30

).apply(
    lambda x: round(x)
)



employee_graph = department[
[
"dept",
"total_employees",
"required_employees"
]
]


employee_graph = employee_graph.melt(
    id_vars="dept",
    var_name="Employee Type",
    value_name="Number"
)



plt.figure(
    figsize=(10,5)
)


sns.barplot(
    data=employee_graph,
    x="dept",
    y="Number",
    hue="Employee Type"
)


plt.title(
    "Current Employees vs Required Employees"
)


plt.xlabel(
    "Department"
)


plt.ylabel(
    "Employees"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()

plt.show()