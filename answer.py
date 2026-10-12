import json


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


students = load_data("student.json")
teachers = load_data("teacher.json")
classes = load_data("classes.json")
subjects = load_data("subjects.json")


# ================= STUDENTS =================

def add_student():
    student = {
        "student_id": input("Enter student ID: "),
        "name": input("Enter full name: "),
        "age": input("Enter age: "),
        "gender": input("Enter gender: "),
        "class": input("Enter class: ")
    }

    students.append(student)
    save_data("student.json", students)

    print("Student added successfully.")


def view_student():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


def search_student():
    search = input("Enter student ID or name: ").lower()

    for student in students:
        if (student["student_id"].lower() == search
                or student["name"].lower() == search):
            print(student)
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_data("student.json", students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


# ================= TEACHERS =================

def add_teacher():
    teacher = {
        "teacher_id": input("Enter teacher ID: "),
        "name": input("Enter full name: "),
        "subject": input("Enter subject taught: "),
        "phone": input("Enter phone number: ")
    }

    teachers.append(teacher)
    save_data("teacher.json", teachers)

    print("Teacher added successfully.")


def view_teachers():
    if not teachers:
        print("No teachers found.")
        return

    for teacher in teachers:
        print(teacher)


# ================= CLASSES =================

def add_class():
    school_class = {
        "class_name": input("Enter class name: "),
        "arm": input("Enter arm: "),
        "teacher": input("Enter assigned teacher: ")
    }

    classes.append(school_class)
    save_data("classes.json", classes)

    print("Class added successfully.")


def view_class():
    if not classes:
        print("No classes found.")
        return

    for school_class in classes:
        print(school_class)


# ================= SUBJECTS =================

def add_subject():
    subject = {
        "subject_name": input("Enter subject name: "),
        "teacher": input("Enter assigned teacher: ")
    }

    subjects.append(subject)
    save_data("subjects.json", subjects)

    print("Subject added successfully.")


def view_subject():
    if not subjects:
        print("No subjects found.")
        return

    for subject in subjects:
        print(subject)


# ================= MAIN MENU =================

def main():
    while True:
        print("\n======== SCHOOL MANAGEMENT SYSTEM ========")
        print("1. Manage students")
        print("2. Manage teachers")
        print("3. Manage classes")
        print("4. Manage subjects")
        print("5. View statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # STUDENTS
        if choice == "1":
            print("\n1. Add student")
            print("2. View students")
            print("3. Search student")
            print("4. Delete student")

            option = input("Enter your choice: ")

            if option == "1":
                add_student()

            elif option == "2":
                view_student()

            elif option == "3":
                search_student()

            elif option == "4":
                delete_student()

            else:
                print("Invalid choice.")

        # TEACHERS
        elif choice == "2":
            print("\n1. Add teacher")
            print("2. View teachers")

            option = input("Enter your choice: ")

            if option == "1":
                add_teacher()

            elif option == "2":
                view_teachers()

            else:
                print("Invalid choice.")

        # CLASSES
        elif choice == "3":
            print("\n1. Add class")
            print("2. View classes")

            option = input("Enter your choice: ")

            if option == "1":
                add_class()

            elif option == "2":
                view_class()

            else:
                print("Invalid choice.")

        # SUBJECTS
        elif choice == "4":
            print("\n1. Add subject")
            print("2. View subjects")

            option = input("Enter your choice: ")

            if option == "1":
                add_subject()

            elif option == "2":
                view_subject()

            else:
                print("Invalid choice.")

        # STATISTICS
        elif choice == "5":
            print("\n========= STATISTICS =========")
            print("Total students:", len(students))
            print("Total teachers:", len(teachers))
            print("Total classes:", len(classes))
            print("Total subjects:", len(subjects))

        # EXIT
        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


main()



