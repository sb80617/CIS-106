def pay_rate(job_code, work):
    if job_code == "L":
        pay_rate = 25
        
    elif job_code == "A":
            pay_rate = 30
     
    elif job_code == "J":
            pay_rate = 50
    
    if work > 40:
        overtime_hours = work - 40
        gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        gross_pay = work * pay_rate
    
    return pay_rate, gross_pay
            

def problem_4():
    grossest_pay = 0
    while True:
        consent = input("Do you want to run program?: ")
        if consent != "Yes" and consent != "yes":
            break
        last_name = input("Enter last name: ")
        job_code = input("Enter job code: ")
        hours_worked = int(input("How many hours worked: "))
        pay_rates, gross_pay = pay_rate(job_code, hours_worked) #please list overtime number i'm so tired of using google
        grossest_pay += gross_pay
        print(f"last name: {last_name}")
        print(f"hours worked: {hours_worked}")
        print(f"pay rate: {pay_rates}")
        print(f"gross pay: {gross_pay}")
        print(f"sum of pay {grossest_pay}")
problem_4()

