import csv
import students

def csv_convert():
        print("CSV started successfully exported.")

        student = students.read()

        if student is None:
            print("No Student found.")
            return

        if len(student) == 0:
            print("Students not found.")
            return

        with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Student ID",
                "Student Name",
                "Student Age",
                "Student Course"
            ])

            for stu in student:
                writer.writerow([
                    stu["Student ID"],
                    stu["Student Name"],
                    stu["Student Age"],
                    stu["Student Course"]
                ])

        print("Student data successfully exported.")


if __name__ == "__main__":
        csv_convert()