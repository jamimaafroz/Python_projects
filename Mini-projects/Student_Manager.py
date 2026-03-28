# Student manager system using a List of Dictionaries
import json
import numpy as np

student_list = []

def load_data():
    global student_list
    try:
        with open("students.json", "r") as file:
            student_list = json.load(file)
    except:
        student_list = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(student_list, file, indent=4)

def addStudent():
    studentInfo = {}
    print("\n--- Adding New Student ---")
    print("Type 'quit' as the key to finish adding this student.")
    
    while True:
        key = input("Enter Key (e.g., Name, ID, Marks): ")
        if key.lower() == 'quit':
            break
        
        if key.lower() == 'marks':
            # Convert marks input to list of integers
            try:
                value = list(map(int, input("Enter marks (space separated): ").split()))
            except ValueError:
                print("Invalid marks. Please enter numbers only.")
                continue
        else:
            value = input(f"Enter Student {key}: ")
            # Convert numeric strings to int if possible
            if value.isdigit():
                value = int(value)
        
        studentInfo[key] = value  # <-- Correct indentation here

    if studentInfo:
        print("\nStudent Added: ", studentInfo)
        student_list.append(studentInfo)
        save_data()
    else:
        print("No student data entered.")

def deleteStudent():
    if len(student_list) == 0:
        print("The database is currently empty. No students to delete.")
        return
    search_key = input("Enter the key to search by (e.g., Name, ID): ")
    search_value = input(f"Enter the {search_key} of the student you want to delete: ")
    if search_value.isdigit():
        search_value = int(search_value)
        
    student_found = False
    for i, student in enumerate(student_list):
        if search_key in student and student[search_key] == search_value:
            removed_student = student_list.pop(i)
            print(f"\nSuccess! Deleted student: {removed_student}")
            student_found = True
            break 
            
    if not student_found:
        print(f"\nCould not find any student with {search_key} '{search_value}'.")
    save_data()
def updateStudent():
    if len(student_list) == 0:
        print("The database is empty. No students to update.")
        return
    
    search_key = input("Enter the key to search by (e.g., Name, ID): ")
    search_value = input(f"Enter the {search_key} of the student you want to update: ")
    
    if search_value.isdigit():
        search_value = int(search_value)
    
    # Find student
    for student in student_list:
        if search_key in student and student[search_key] == search_value:
            print(f"\nFound student: {student}")
            print("Enter new values (leave blank to keep current value):")
            
            for key in student.keys():
                if key.lower() == "marks":
                    marks_input = input(f"{key} (current: {student[key]}): ")
                    if marks_input.strip():  # if not empty
                        try:
                            student[key] = list(map(int, marks_input.split()))
                        except ValueError:
                            print("Invalid marks input. Skipping update for marks.")
                else:
                    new_value = input(f"{key} (current: {student[key]}): ")
                    if new_value.strip():  # if not empty
                        student[key] = int(new_value) if new_value.isdigit() else new_value
            
            save_data()
            print("\nStudent updated successfully!")
            print(student)
            return
    
    print(f"\nCould not find any student with {search_key} '{search_value}'.")

def showStudents():
    print("\n--- All Students ---")
    if len(student_list) == 0:
        print("The database is currently empty.")
    else:
        for index, student in enumerate(student_list):
            print(f"Student {index + 1}: {student}")

def find_topper():
    if len(student_list) == 0:
        print("No students in the database.")
        return
    
    all_marks = []
    names = []
    
    for student in student_list:
        if "Marks" in student:
            all_marks.append(student["Marks"])
            names.append(student.get("Name","Unknown"))
        else:
            all_marks.append[0]
            names.append(student.get("Name","Unknown"))
    max_len = max(len(m) for m in all_marks)
    all_marks = [m+[0]*(max_len-len(m)) for m in all_marks]
    
    marks_array = np.array(all_marks)
    total_marks = marks_array.sum(axis=1)
    topper_indices = np.where(total_marks == total_marks.max())[0]
    
    print("\n--- Topper Student(s) ---")
    for i in topper_indices:
        print(f"Name: {names[i]},Marks:{marks_array[i]},Total:{total_marks[i]}")
        
# --- Main Program Loop ---

load_data()
while True:
    print("\n" + "="*30)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Find Topper")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ")

    if choice == '1':
        addStudent()
        
    elif choice == '2':
        showStudents()
        
    elif choice == '3':
        find_topper()
        
    elif choice == '4':
        deleteStudent()
        
    elif choice == '5':
        updateStudent()
        
    elif choice == '6':
        print("\nExiting Student Management System. Goodbye!")
        break  
        
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")