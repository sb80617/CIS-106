def tuition_owed(district, credit_hours2):
    if district == "O":
        credit = 550
    else:
        credit = 250
    tuition = credit * credit_hours2
    return tuition

def problem_5():
    total = 0 
    while True:
        consent = input("Do you want to run program?: ")
        if consent != "Yes" and consent != "yes":
            break
        student = input("Enter last name: ")
        credit_hours = int(input("Enter credit hours: "))
        district_code = input("Enter district code: ")
        owed = tuition_owed(district_code, credit_hours)
        total += owed
        print(f"Last name: {student}")
        print(f"owed amount: {owed}")
        print(f"total owed amount: {total}")
problem_5()

