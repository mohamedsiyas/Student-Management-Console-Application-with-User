from authentication import signin

with open("students.txt", "r") as f:
    student_data = f.read().splitlines()

    print("Student ID\t Student Name\t Student Age\t Student Location")
    for data in student_data:
        student_info = data.split()
        print(f"{student_info[0]}\t\t\t\t{student_info[1]}\t\t\t{student_info[2]}\t\t\t\t{student_info[3]}")

num_students = len(student_data)
student_ages = [int(data.split()[2])for data in student_data]

print("No.of Students:", num_students)
print("Lowest Age of Student:", min(student_ages))
print("Highest Age of Student:", max(student_ages))
