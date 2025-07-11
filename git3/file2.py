[200~students = []

  def add_student():
      name = input("Enter student name: ")
      roll = input("Enter roll number: ")
      course = input("Enter course: ")
      students.append({"name": name, "roll": roll, "course": course})
      print("Student added successfully!")

  def view_students():
      if not students:
          print("No students found.")
      else:
          print("\nStudent List:")
          for i, s in enumerate(students, 1):
              print(f"{i}. Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")

  def delete_student():
      view_students()
      idx = int(input("Enter student number to delete: "))
      if 0 < idx <= len(students):
          removed = students.pop(idx - 1)
          print(f"Deleted {removed['name']}")
      else:
          print("Invalid number.")

  while True:
      print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
      choice = input("Choice: ")
      if choice == '1':
          add_student()
      elif choice == '2':
          view_students()
      elif choice == '3':
          delete_student()
      elif choice == '4':
          break
      else:
          print("Invalid choice.")
  
