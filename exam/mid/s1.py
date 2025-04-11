class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_all_students(cls):
        return cls.__student_list

    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Student is already enrolled!")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully!")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Student is not enrolled!")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully!")

    def view_student_info(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {'Enrolled' if self.__is_enrolled else 'Not Enrolled'}")

    # Getter for private ID (for searching purpose)
    def get_student_id(self):
        return self.__student_id


# Manually Adding Students
s1 = Student(101, "John Doe", "CSE")
s2 = Student(102, "Jane Smith", "EEE")
s3 = Student(103, "Alice Johnson", "BBA")

# Menu System
while True:
    print("\n===== Student Management Menu =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- All Students ---")
        for student in StudentDatabase.get_all_students():
            student.view_student_info()
            print("-------------------------")

    elif choice == '2':
        try:
            sid = int(input("Enter Student ID to Enroll: "))
            student = StudentDatabase.find_student_by_id(sid)
            if student:
                student.enroll_student()
            else:
                print("Invalid Student ID!")
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == '3':
        try:
            sid = int(input("Enter Student ID to Drop: "))
            student = StudentDatabase.find_student_by_id(sid)
            if student:
                student.drop_student()
            else:
                print("Invalid Student ID!")
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == '4':
        print("Exiting the system...")
        break

    else:
        print("Invalid choice! Please enter between 1 to 4.")
