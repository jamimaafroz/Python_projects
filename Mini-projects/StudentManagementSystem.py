#Basic student MANAGEMENT SYSTEM.


class Student:
    def __init__(self, name, student_id, dept, section):
        self.name = name
        self.student_id = student_id
        self.dept = dept
        self.section = section
    
    def show_details(self):
        print(f"ID: {self.student_id}  Name: {self.name}  Dept: {self.dept}  Section: {self.section}")

class StudentManager:
    def __init__(self):
        self.student_list = [] 
    
    def add_student(self, student):
     for s in self.student_list:
        if s.student_id == student.student_id:
            print("Student ID already exists.")
            return
     self.student_list.append(student)
     print(f"Successfully Added {student.name} to the system.")
    
    def delete_student(self, target_id):
        for student in self.student_list:
            if student.student_id == target_id:
                self.student_list.remove(student)
                print(f"{student.name} removed successfully.")
                return
        print("Student not found.") 
   
    def show_all_students(self):
        print("\n--- All Students ---")
        if not self.student_list:
            print("No students in the list.")
            return
        for student in self.student_list:
            student.show_details()
    
    def search_student(self, target_id):
        print(f"\nSearch result for student {target_id}")
        for student in self.student_list:
            if student.student_id == target_id:
                print("Student Found!")
                student.show_details()
                return student
        print("Student not found.")
    
    def update_student(self,target_id):
        print(f"\nEpdating previous data for student {target_id}")
        for student in self.student_list:
            if student.student_id==target_id:
                student.name = input("Enter new name: ")
                student.dept = input("Enter new department: ")
                student.section = input("Enter new section: ")
                print("Student updated successfully.")
                return
        print("Student not found.")

manager = StudentManager()

while True:
    print("\n" + "="*30)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. update Student")
    print("6. Exit")

    choice = input("\nEnter choice (1-5): ")

    # Handle Add Student
    if choice == '1':
        print("\n--- Add New Student ---")
        name = input("Enter Name: ")
        student_id = input("Enter ID: ")
        dept = input("Enter Department: ")
        section = input("Enter Section: ")
        #create new student obeject to add with the previous
        new_student = Student(name, student_id, dept, section)
        manager.add_student(new_student)

    # Handle Show Students
    elif choice == '2':
        manager.show_all_students()

    # Handle Search Student
    elif choice == '3':
        target_id = input("\nEnter the ID of the student to search: ")
        manager.search_student(target_id)

    # Handle Delete Student
    elif choice == '4':
        target_id = input("\nEnter the ID of the student to delete: ")
        manager.delete_student(target_id)
    
    # Handle Update Student
    
    elif choice=='5':
        target_id = input("\nEnter the ID of the student to update data: ")
        manager.update_student(target_id)

    # Handle Exit
    elif choice == '6':
        print("\nExiting the program. Goodbye!")
        break 

    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")