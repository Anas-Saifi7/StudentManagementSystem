class Student:
 def __init__(self, name, rollNo,  Id):
  self.name = name
  self.rollNo = rollNo
  self.Id = Id

 def __str__(self):
  return f"Name: {self.name}, Roll No: {self.rollNo}, Id:{self.Id}"

 class StudentManagementSystem:
   def __init__(self):
     self.students = []

def add_student(self, student):
  self.students.append(student)
  print(f"Student {student.name} added successfully.")

def remove_student(self, rollNo):
  if rollNo in self.rollNo:
    self.students.remove(student)
    print(f"Student with rollNumber {rollNo} removed successfully.")
  else:
    print(f"Student with rollNumber {rollNo} not found.")

  def search_student(self, rollNo):
    for student in self.students:
      if student.rollNo == rollNo:
        return student
      return None
 
  def display_students(self):
    if not self.students:
      print("No students found.")
    else:
      print("Student List:")
      for student in self.students:
        print(student)

def save_file(self, filename):
  with open(filename, 'w') as file:
      for student in self.students:
          file.write(f"{student.name},{student.rollNo},{student.Id}\n")
  print("Students saved to file successfully.")

def main():
  sms = StudentManagementSystem():
  while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Searach Student")
    print("4. Display All Students")
    print("5. Exit")
    choice = input( "Enter your choice (1-5):")
    if choice == '1':
       name = input( "Enter student name:")
       rollNo = input("Enter student roll number:")
       Id = input("Enter student Id:")
       student = Student(name, rollNo, Id)
       sms.add_student(student)
      
    elif choice == '2':
      rollNo = input("Enter student roll number to remove:")
      sms.remove_student(rollNo)
      
    elif choice == '3':
      rollNo = input("Enter student roll number to searach:")
      student = sms.search_student(rollNo)
      if student:
        print(student)
      else:
        print(f"Student with roll number {rollNo} not found.")

    elif choice == '4':
      sms.display_students()
    elif choice == '5':
      sms.save_file("students.txt")
      break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
      
      
        
 