def mpg(miles, gallon):
    mpgs = miles / gallon
    cost = gallon * 3
    return mpgs, cost
    

def problem_3():
     i = 0
     while True:
        consent = input("Do you want to run program?: ")
        if consent != "Yes" and consent != "yes":
            break
        destination = input("Enter desired destination: ")
        miles_traveled = int(input("Enter miles traveled: "))
        gallons_used = int(input("Enter gallons used: "))
        mpgs, cost = mpg(miles_traveled, gallons_used)
        i += 1

        print(f"Destination entered: {destination}")
        print(f"miles traveled: {miles_traveled}")
        print(f"gallons used: {gallons_used}")
        print(f"Cost of trip {cost}")
        print(f"Miles per gallon: {mpgs}")
        print(f"Trips entered: {i}")
problem_3()
