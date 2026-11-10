student = []
while True:
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter student name:")
        age = int(input("Enter student age:"))
        branch = input("Enter student branch:")
        student.append({"name": name, "age": age, "branch": branch})
        print("Student added successfully.")
    elif choice == 2:
       for s in student:
        print("Name:", s["name"], "| Age:", s["age"], "| Branch:", s["branch"])

    elif choice == 3:
        name = input("Enter student name to search:")
        found = False
        for s in student:
           if s["name"] == name:
                print("Student Found -> Name:", s["name"], "| Age:", s["age"], "| Branch:", s["branch"])
                found = True
                break
        if not found:
             print("Student not found.")
    elif choice == 4:
        name = input("Enter student name:")
        found = False
        for s in student:
            if s["name"] == name:
                student.remove(s)
                print("Student deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice. Please try again.")