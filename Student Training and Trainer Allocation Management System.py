class Trainer:
    def __init__(self, name, course, timings, duration):
        self.name = name
        self.course = course
        self.timings = timings
        self.duration = duration


class TrainingSystem:
    def __init__(self):
        self.trainers = [
            Trainer("Arun", "Python", ["9 AM - 11 AM", "2 PM - 4 PM"], 30),
            Trainer("Priya", "Data Science", ["9 AM - 11 AM", "11 AM - 1 PM"], 60),
            Trainer("Kumar", "SQL", ["11 AM - 1 PM", "2 PM - 4 PM"], 15),
            Trainer("Divya", "Machine Learning", ["2 PM - 4 PM"], 45),
            Trainer("Arun", "Machine Learning", ["9 AM - 11 AM"], 45),
            Trainer("Priya", "Python", ["11 AM - 1 PM"], 30)
        ]

        self.students = []

    def register_student(self):
        while True:
            print("\n========== STUDENT REGISTRATION ==========")

            student_name = input(
                "Enter student name (or type 'stop' to finish): "
            ).strip()

            if student_name.lower() == "stop":
                break

            if not student_name:
                print("Student name cannot be empty.")
                continue

            student_id = input("Enter student ID: ").strip()

            if not student_id:
                print("Student ID cannot be empty.")
                continue

            course = input(
                "Enter course (Python/Data Science/SQL/Machine Learning): "
            ).strip().lower()

            available_trainers = [
                trainer for trainer in self.trainers
                if trainer.course.lower() == course
            ]

            if not available_trainers:
                print("No trainers found for this course. Try again.")
                continue

            print("\nAvailable Trainers:")

            for i, trainer in enumerate(available_trainers, start=1):
                print(
                    f"{i}. {trainer.name} | "
                    f"Course: {trainer.course} | "
                    f"Timings: {', '.join(trainer.timings)} | "
                    f"Duration: {trainer.duration} days"
                )

            try:
                trainer_choice = int(
                    input("\nChoose trainer number: ")
                )

                if not 1 <= trainer_choice <= len(available_trainers):
                    print("Invalid trainer number.")
                    continue

            except ValueError:
                print("Enter a valid number.")
                continue

            selected_trainer = available_trainers[trainer_choice - 1]

            print("\nAvailable Timings:")

            for i, timing in enumerate(selected_trainer.timings, start=1):
                print(f"{i}. {timing}")

            try:
                time_choice = int(input("Choose timing number: "))

                if not 1 <= time_choice <= len(selected_trainer.timings):
                    print("Invalid timing number.")
                    continue

            except ValueError:
                print("Enter a valid number.")
                continue

            selected_time = selected_trainer.timings[time_choice - 1]

            student = {
                "Student ID": student_id,
                "Student Name": student_name,
                "Course": selected_trainer.course,
                "Trainer": selected_trainer.name,
                "Timing": selected_time,
                "Duration": f"{selected_trainer.duration} days"
            }

            self.students.append(student)

            print("\n========== ASSIGNMENT SUCCESSFUL ==========")

            for key, value in student.items():
                print(f"{key}: {value}")

            again = input(
                "\nRegister another student? (yes/no): "
            ).strip().lower()

            if again != "yes":
                break

    def show_all_students(self):
        print("\n========== ALL STUDENT ASSIGNMENTS ==========")

        if not self.students:
            print("No students registered.")
            return

        for student in self.students:
            print("-" * 45)

            for key, value in student.items():
                print(f"{key}: {value}")


if __name__ == "__main__":
    system = TrainingSystem()
    system.register_student()
    system.show_all_students()