

#data=employee.read()
#print(data)

#read - r
#write() - w
#read and write() - r+
#append - a

#file("file_name",mode)
#file.close()

#with open("File_name",'r') as db:

#   print(db.read())
#   db.close()


import csv
import employee


def csv_convert():
    print("CSV export started successfully.")

    employees = employee.read()

    if employees is None:
        print("No Employee found.")
        return

    if len(employees) == 0:
        print("Employees not found.")
        return

    with open("employee.csv", "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Employee ID",
            "Employee Name",
            "Employee Age",
            "Employee Department",
            "Employee Salary"
        ])

        for emp in employees:
            writer.writerow([
                emp["Employee ID"],
                emp["Employee Name"],
                emp["Employee Age"],
                emp["Employee Department"],
                emp["Employee Salary"]
            ])

    print("Employee data successfully exported.")


if __name__ == "__main__":
    csv_convert()