  # Base class: Person 
class Person:
    def __init__(self, person_id, name):
        # Common attributes shared by all people
        self.person_id = person_id
        self.name = name

    def display_info(self):
        print(f"ID: {self.person_id}, Name: {self.name}")
  
# Student inherits from Person
class Student(Person):
    def __init__(self, person_id, name, student_id):
        # Call parent
        super().__init__(person_id, name)
        self.student_id = student_id

    def display_info(self):
        # Override method to display student-specific details
        print(f"Student ID: {self.student_id}, Name: {self.name}")

# Staff inherits from Person
class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        print(
            f"Staff ID: {self.staff_id}, Name: {self.name}, Tax Number: {self.tax_num}"
        )
  
# General staff inherits from Staff
class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        print(
            f"General Staff | Name: {self.name}, Rate of Pay: ${self.rate_of_pay}/hour"
        )

# Academic staff inherits from Staff
class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def display_info(self):
        print(
            f"Academic Staff | Name: {self.name}, Publications: {self.publications}"
        )

# Main function
def main():

    # Create a Student object
    student = Student(1, "Ali", "S1001")
    student.display_info()

    print("-" * 50)

    # Create a General Staff object
    general_staff = General(2, "Alex", "ST2001", "TX12345", 30)
    general_staff.display_info()

    print("-" * 50)

    # Create an Academic Staff object
    academic_staff = Academic(3, "Dr John", "ST3001", "TX67890", 15)
    academic_staff.display_info()
  
if __name__ == "__main__":
    main()
