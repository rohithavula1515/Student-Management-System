import os

FILE_NAME = "password.txt"

# Create Password
def create_password():
    while True:
        password = input("Create a Password: ")

        if len(password) < 8:
            print("❌ Password must contain at least 8 characters.")
            continue

        upper = False
        lower = False
        digit = False
        special = False

        for ch in password:
            if ch.isupper():
                upper = True
            elif ch.islower():
                lower = True
            elif ch.isdigit():
                digit = True
            elif ch in "@#$%^&*!":
                special = True

        if not upper:
            print("❌ Password must contain at least one uppercase letter.")
            continue

        if not lower:
            print("❌ Password must contain at least one lowercase letter.")
            continue

        if not digit:
            print("❌ Password must contain at least one digit.")
            continue

        if not special:
            print("❌ Password must contain at least one special character (@#$%^&*!).")
            continue

        with open(FILE_NAME, "w") as file:
            file.write(password)

        print("✅ Password created and saved successfully.")
        break


# Login
def login():
    with open(FILE_NAME, "r") as file:
        saved_password = file.read()

    attempts = 3

    while attempts > 0:
        password = input("Enter Password: ")

        if password == saved_password:
            print("✅ Login Successful")
            return True

        attempts -= 1
        print("❌ Incorrect Password")
        print("Remaining Attempts:", attempts)

    print("❌ Access Denied")
    return False


# Main Program
if not os.path.exists(FILE_NAME):
    print("No password found.")
    print("Create a new password.")
    create_password()

print("\n------ LOGIN ------")

if login():
    print("\nWelcome to Student Management System")
    # Write your Student Management System menu here.

    students = {
        101: {
            "name": "Rohith",
            "age": 20,
            "branch": "CSE",
            "avg_cgpa":8.5,
            "phone_no":9347988787

        },

        102: {
            "name": "Rahul",
            "age": 21,
            "branch": "ECE",
            "avg_cgpa":8.3,
            "phone_no":9347988788

        },
        103: {
            "name": "Ravi",
            "age": 21,
            "branch": "CIVIL",
            "avg_cgpa":4.5,
            "phone_no":9347988788

        },
        104: {
            "name": "Raju",
            "age": 20,
            "branch": "MECHANICAL",
            "avg_cgpa":9.5,
            "phone_no":9347988788

        },
        105: {
            "name": "rakul",
            "age": 22,
            "branch": "EEE",
            "avg_cgpa":8.7,
            "phone_no":9347988788

        },
        106: {
            "name": "rani",
            "age": 29,
            "branch": "CSE",
            "avg_cgpa": 8.7,
            "phone_no": 9347988788

        },
        107: {
            "name": "ranganadh",
            "age": 23,
            "branch": "EEE",
            "avg_cgpa": 8.7,
            "phone_no": 9347988788

        }

    }
    #add student details----------------------------------
    def validate_phone():
        while True:
            phone = input("Enter Phone Number: ")

            if len(phone) != 10:
                print("Phone number must contain exactly 10 digits.")
                continue

            if not phone.isdigit():
                print("Phone number should contain only digits.")
                continue

            if phone[0] not in "6789":
                print("Phone number must start with 6, 7, 8, or 9.")
                continue

            print("Valid Phone Number")
            return phone


    def validate_age():
        while True:
            age = input("Enter Age: ")
            if not age.isdigit():
                print("Age should contain only numbers.")
                continue

            age = int(age)

            if age < 16 or age > 30:
                print("Age must be between 16 and 30.")
                continue

            print("Valid Age")
            return age


    def add_student():
        s_id=int(input("enter the student_id:"))
        if s_id in students:
            print("student is already present /add a new student details")
        else:
            name=input("enter the new_student Name: ")
            age=validate_age()
            branch=input("enter the new_student Branch name: ")
            avg_cgpa=float(input("enter the new_student Avg_CGPA:"))
            phone=validate_phone()


        students[s_id]={
                "name": name,
                "age": age,
                "branch": branch,
                "avg_cgpa": avg_cgpa,
                "phone_no": phone

        }
    # update dictionaries ------------------------------------------

    def update_student():
        s_id=int(input("enter the student_id to update the student_data:"))
        if s_id not in students:
            print("Invalid student_id:")
        while True:
            print("enter (1) to update his name::")
            print("enter (2) to update his age::")
            print("enter (3) to update his branch::")
            print("enter (4) to update his avg_cgpa::")
            print("enter (5) to update his phone_no::")
            print("enter (6) to update his exit::")
            ch1=int(input("enter your choice"))
            if ch1==1:
                new_name=input("enter the updated name of student:")
                students[s_id]["name"]=new_name
            elif ch1==2:
                new_age = int(input("enter the updated age of student:"))
                students[s_id]["age"] = new_age
            elif ch1==3:
                new_branch = input("enter the updated branch of student:")
                students[s_id]["branch"] = new_branch
            elif ch1==4:
                new_avg_cgpa = float(input("enter the updated name of student:"))
                students[s_id]["avg_cgpa"] = new_avg_cgpa
            elif ch1==5:
                new_phone_no = int(input("enter the updated phone_no of student:"))
                students[s_id]["phone_no"] = new_phone_no
            elif ch1==6:
                ch2=input("do you want to exit(yes/no)")
                if ch2=="yes":
                    break
    # display data --------------------------------------------------------
    def display_student():
        for sid, details in students.items():
            print("=" * 40)
            print(f"Student ID : {sid}")
            print(f"Name       : {details['name']}")
            print(f"Age        : {details['age']}")
            print(f"Branch     : {details['branch']}")
            print(f"phone_no   :{details['phone_no']}")
    def search_student():
        s_id=int(input("enter the valid student_id:"))
        if s_id in students:
            print("found")
        else:
            print("not found")
    def delete_student():
        s_id = int(input("enter the valid student_id:"))

        if s_id in students:
                ch2 = input("do you actually want to delete student details(yes/no)")
                if ch2=="yes":
                    students.pop(s_id)
                else:
                    pass
        else:
            print("enter the valid student_id:")
    def highest_cgpa():
        first=list(students.keys())[0]
        for k in students:
            if students[k]["avg_cgpa"]>students[first]["avg_cgpa"]:
                first=k
        print("highest cgpa student in class is",students[first]["name"])
    def lowest_cgpa():
        first = list(students.keys())[0]
        for k in students:
            if students[k]["avg_cgpa"] < students[first]["avg_cgpa"]:
                first = k
        print("lowest cgpa student in the class is",students[first]["name"])
    def strength():
        s=len(students)
        print(s)
    def passed_students():
        li=[]
        for k,v in students.items():
            if students[k]["avg_cgpa"]>=5.0:
                li.append(students[k]["name"])
        print("passed students in college are::",li)
        x=len(li)
        y=len(students)
        percent=(x/y)*100
        print("overall pass percentage==>",percent)
    def failed_students():
        li=[]
        for k,v in students.items():
            if students[k]["avg_cgpa"]<5.0:
                li.append(students[k]["name"])
        print("failed students in college are::",li)
        x=len(li)
        y=len(students)
        percent=(x/y)*100
        print("overall fail percentage==>",percent)
    def branch_name():
        while True:
            print("1.CSE students details:")
            print("2.ECE students details:")
            print("3.EEE students details:")
            print("4.MECHANUICAL students details:")
            print("5.CIVIL students details:")
            print("6.to exit()")
            ch=int(input("enter the your choice"))
            if ch==1:
                res={}
                for k,v in students.items():
                    if students[k]["branch"]=="CSE":
                        res["s_id"]=students[k]
                        res["student_name"]=students[k]["name"]
                print("CSE students details",res)
            elif ch == 2:
                res = {}
                for k, v in students.items():
                    if students[k]["branch"] == "ECE":
                        res["s_id"] = students[k]
                        res["student_name"] = students[k]["name"]
                print("ECE students details:", res)
            elif ch == 3:
                res = {}
                for k, v in students.items():
                    if students[k]["branch"] == "EEE":
                        res["s_id"] = students[k]
                        res["student_name"] = students[k]["name"]
                print("EEE students details:", res)
            elif ch == 4:
                res = {}
                for k, v in students.items():
                    if students[k]["branch"] == "MECHANICAL":
                        res["s_id"] = students[k]
                        res["student_name"] = students[k]["name"]
                print("MECHANICAL students details:", res)
            elif ch == 5:
                res = {}
                for k, v in students.items():
                    if students[k]["branch"] == "CIVIL":
                        res["s_id"] = k
                        res["student_name"] = students[k]["name"]
                print("CIVIL students details:", res)
            elif ch==6:
                break
            else:
                pass
# sort students data:-------------------------------------------------
    def sort_students():
        while True:
            print("1.to sort students by names:")
            print("2.sort students by id")
            print("3.sort students by age:")
            print("4.to exit")
            ch=int(input("enter your choice:"))
            if ch==1:
                for sid, details in sorted(students.items(), key=lambda x: x[1]["name"]):
                    print(sid, details)
            elif ch==2:
                for sid, details in sorted(students.items()):
                    print(sid, details)
            elif ch==3:
                for sid, details in sorted(students.items(), key=lambda x: x[1]["age"]):
                    print(sid, details)
            elif ch==4:
                break
            else:
                pass
#       ------------------------take input data---------------------------------

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6.highest cgpa student")
        print("7.lowest cgpa student")
        print("8.strength of class")
        print("9.passed_students")
        print("10.failed_students")
        print("11.branch_wise details:")
        print("12.sorted information")
        print("13. Exit")
        ch=int(input("enter your choice:"))
        if ch==1:
            add_student()
        elif ch==2:
            display_student()

        elif ch==3:
            search_student()
        elif ch==4:
            update_student()
        elif ch==5:
            delete_student()
        elif ch==6:
            highest_cgpa()
        elif ch==7:
            lowest_cgpa()
        elif ch==9:
            passed_students()
        elif ch==10:
            failed_students()
        elif ch==11:
            branch_name()
        elif ch==12:
            sort_students()
        elif ch==13:
            break
















