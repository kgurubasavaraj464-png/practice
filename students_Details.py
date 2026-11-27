import sys

def student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city
    }

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python student.py name usn college city")
        sys.exit(1)

    name = sys.argv[1]
    usn = sys.argv[2]
    college = sys.argv[3]
    city = sys.argv[4]

    student = student_details(name, usn, college, city)

    print("Student Details")
    print("Name:", student["name"])
    print("USN:", student["usn"])
    print("College:", student["college"])
    print("City:", student["city"])