class Student:
  def __init__(self, name, 
               roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
  
  def sort_Students(students):
    sorted_students=sorted(student
                        ,key=lambda               student:student.cgpa,                       reverse=True) 
# Create a list of student objects
students = [
Student("Rahul", "A001", 3.8),
Student("Jeeva", "A002", 3.5),
Student("Prem", "A003", 3.9),
Student("Mohan", "A004", 3.7)
]

# Sort the list of students based on CGPA
Sorted_students=(students)
# Print the sorted list
for student in Sorted_students:
  print(f"Name: {student.name},Roll Number: {student.roll_number}, CGPA: {student.cgpa}")