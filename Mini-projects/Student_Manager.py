# Student manager system using a List of Dictionaries
import json


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
        json.dump(student_list, file)


def addStudent():
    studentInfo = {}
    print("\n--- Adding New Student ---")
    print("Type 'quit' as the key to finish adding this student.")
    
    while True:
        key = input("Enter Key (e.g., Name, ID, Marks): ")
        if key.lower() == 'quit':
            break
            
        value = input(f"Enter Student {key}: ")
        
        if value.isdigit():
            value = int(value)
            
        studentInfo[key] = value
        
    print("\nStudent Added: ", studentInfo)
    student_list.append(studentInfo)
    save_data()

def showStudents():
    print("\n--- All Students ---")
    if len(student_list) == 0:
        print("The database is currently empty.")
    else:
        for index, student in enumerate(student_list):
            print(f"Student {index + 1}: {student}")


# --- Main Program Loop ---

load_data()
while True:
    print("\n" + "="*30)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student (Coming Soon)")
    print("4. Delete Student (Coming Soon)")
    print("5. Update Student (Coming Soon)")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ")

    if choice == '1':
        addStudent()
        
    elif choice == '2':
        showStudents()
        
    elif choice == '3':
        print("\nFeature not yet implemented!")
        
    elif choice == '4':
        print("\nFeature not yet implemented!")
        
    elif choice == '5':
        print("\nFeature not yet implemented!")
        
    elif choice == '6':
        print("\nExiting Student Management System. Goodbye!")
        break  
        
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")