# Step 1: Create the StudentDatabase class
class StudentDatabase:
    student_list = []  # class attribute to store students

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)  # add Student object to student_list


# Step 2: Create the Student class
class Student:
    def __init__(self, student_id, name, department):
        # Step 3: Initialize attributes (private/protected)
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False  # default not enrolled

    # Step 4: Enroll Student
    def enroll_student(self):
        if self.__is_enrolled:
            print("Student is already enrolled!")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully!")

    # Step 5: Drop Student
    def drop_student(self):
        if not self.__is_enrolled:
            print("Student is not enrolled!")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully!")

    # Step 6: View Student Info
    def view_student_info(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {'Enrolled' if self.__is_enrolled else 'Not Enrolled'}")

    # Getter for private student_id (for searching only)
    def get_student_id(self):
        return self.__student_id


# Step 7: Manually adding students (No Menu for Adding)
# Creating Student Objects
s1 = Student(101, "John Doe", "CSE")
StudentDatabase.add_student(s1)

s2 = Student(102, "Jane Smith", "EEE")
StudentDatabase.add_student(s2)

s3 = Student(103, "Alice Johnson", "BBA")
StudentDatabase.add_student(s3)


# Step 8: Menu System
while True:
    print("\n===== Student Management Menu =====")
        
    options = [
        "2. Enroll Student",
        "3. Drop Student",
        "1. View All Students",
        "4. Exit"
    ]

    for option in options:
        print(option)
            
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- All Students ---")
        for student in StudentDatabase.student_list:
            student.view_student_info()
            print("-------------------------")

    elif choice == '2':
        try:
            sid = int(input("Enter Student ID to Enroll: "))
            found = False
            for student in StudentDatabase.student_list:
                if student.get_student_id() == sid:
                    student.enroll_student()
                    found = True
                    break
            if not found:
                print("Invalid Student ID!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == '3':
        try:
            sid = int(input("Enter Student ID to Drop: "))
            found = False
            for student in StudentDatabase.student_list:
                if student.get_student_id() == sid:
                    student.drop_student()
                    found = True
                    break
            if not found:
                print("Invalid Student ID!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == '4':
        print("Exiting the system...")
        break

    else:
        print("Invalid choice! Please enter between 1 to 4.")
