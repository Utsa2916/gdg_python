class ScoreTracker:
    def __init__(self):
        print("Score traker created successfully")
        self.students = {}

    def add_student(self):
        """Add a new student with their exam scores."""
        name=input("Enter student name: ")
        c=int(input("Enter chemistry score: "))
        p=int(input("Enter physics score: "))
        m=int(input("Enter maths score: "))
        self.students[name] = [c,p,m]
        print(f"Added student: {name} with scores: {self.students[name]}")

    def update_scores(self):
        """Update the scores of an existing student."""
        name=input("Enter name of the students to be updated: ")
        
        if name in self.students:
            print("Enter new scores for chemistry, physics and maths")
            c=int(input("Enter chemistry score: "))
            p=int(input("Enter physics score: "))
            m=int(input("Enter maths score: "))
            self.students[name] = [c,p,m]
            print(f"Updated scores for {name}: {self.students[name]}")
        else:
            print(f"Student {name} not found.")

    def display_students(self):
        """Display all students and their scores."""
        if not self.students:
            print("No students found.")
            return
        for name in self.students:
            print(f"Student: {name}, Scores: {self.students[name]}")

    def calculate_statistics(self):
        """Calculate and display statistics for a given student."""
        name=input("Enter name of the students whose statistics to be calculated: ")
        if name in self.students:
            scores = self.students[name]
            average = sum(scores) / len(scores) if scores else 0
            highest = max(scores) if scores else 0
            lowest = min(scores) if scores else 0
            print(f"Statistics for {name}: Average: {average}, Highest: {highest}, Lowest: {lowest}")
        else:
            print(f"Student {name} not found.")

    def remove_student(self):
        """Remove a student from the system."""
        name=input("Enter name of the students to be removed: ")
        if name in self.students:
            del self.students[name]
            print(f"Removed student: {name}")
        else:
            print(f"Student {name} not found.")


def main():
    sst=None
    
    while True:
        print("\nMenu:")
        print("1. Create Student Score Tracker: ")
        print("2. Add New Student Record")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Display All Records")
        print("6. Calculate Statistics")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1': #create
            if sst is not None:
                print("Student Score Tracker has already been created")
            else:
                sst=ScoreTracker()
                print("Student Score Tracker created successfully")

            
        elif choice == '2': #add new
            sst.add_student()
            
        elif choice == '3':
            sst.update_scores()
        elif choice == '4':
            sst.remove_student()
        elif choice == '5':
            sst.display_students()
        elif choice == '6':
            sst.calculate_statistics()
        elif choice == '7':
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



























