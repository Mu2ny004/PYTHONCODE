# Base Class
class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")


# Subclass: Teacher
class Teacher(Staff):
    def __init__(self, name, staff_id, department, subject, teaching_hours):
        super().__init__(name, staff_id, department)
        self.subject = subject
        self.teaching_hours = teaching_hours

    def display_details(self):
        super().display_details()
        print(f"Subject: {self.subject}")
        print(f"Teaching Hours: {self.teaching_hours}")
        print(f"Overload: {'Yes' if self.is_overloaded() else 'No'}")

    def is_overloaded(self):
        return self.teaching_hours > 20


# Subclass: Administrator
class Administrator(Staff):
    def __init__(self, name, staff_id, department, position, office_hours):
        super().__init__(name, staff_id, department)
        self.position = position
        self.office_hours = office_hours

    def display_details(self):
        super().display_details()
        print(f"Position: {self.position}")
        print(f"Office Hours: {self.office_hours}")
        print(f"Senior: {'Yes' if self.is_senior() else 'No'}")

    def is_senior(self):
        return self.office_hours > 40


# Example usage:
teacher = Teacher("Alice", "T123", "Math", "Algebra", 25)
admin = Administrator("Bob", "A456", "Admin", "Registrar", 45)

print("Teacher Details:")
teacher.display_details()

print("\nAdministrator Details:")
admin.display_details()
