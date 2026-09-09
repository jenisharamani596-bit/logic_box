students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add student")
    print("2. Display All student")
    print("3. Update student Information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            Course = input("Enter Course: ")

            student = {
                "name": name,
                "age": age,
                "course": Course
            }

            students.append(student)
            print("Student Added!!")

        case 2:
            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")

        case 3:
            name = input("Enter student name: ")

            for student in students:
                if student["name"] == name:
                    student["name"] = input("Enter New Name: ")
                    student["age"] = int(input("Enter New Age: "))
                    student["course"] = input("Enter New Course: ")

                    print("Student Information Updated!!")
                    break
            else:
                print("Student Not Found")

        case 4:
            name = input("Enter name to delete: ")

            for student in students:
                if student["name"] == name:
                    students.remove(student)
                    print("Student Deleted!!")
                    break
            else:
                print("Student Not Found")

        case 5:
            print("subject offered:")
            print("1.python")
            print("2.AI")
            print("3.ML")
            print("4.Data Science")

        case 6:
            print("Thank you for using Student Management System!")
            break

        case _:
            print("Invalid Choice!!")