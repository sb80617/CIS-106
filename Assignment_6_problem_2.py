def batting_average(num_hit, num_bat):
    bat_average = num_hit / num_bat
    return bat_average
def problem_2():
    i = 0
    while True:
        consent = input("Do you want to run program?: ")
        if consent != "Yes" and consent != "yes":
            break
       
        last_name = input("Enter last name: ")
        number_hits = int(input("Enter number of hits: "))
        bats = int(input("Enter times at bat: "))
        bat_average = batting_average(number_hits, bats)
        i += 1
        print(f"Last name entered: {last_name}")
        print(f"Batting average: {bat_average}")
        print(f"Players entered: {i}")
problem_2()

