max_value = 0
max_name = 0
count_of_airlines = int(input())
if 1 <= count_of_airlines <= 20:
    for airlines in range(1, count_of_airlines + 1):
        name = input()
        sum_count_passengers = 0
        count_of_flights = 0
        command = input()
        if 1 <= int(command) <= 360:
            while command != "Finish":
                count_of_passengers = int(command)
                sum_count_passengers += count_of_passengers
                count_of_flights += 1
                average_passengers = int(sum_count_passengers / count_of_flights)
                command = input()
            if average_passengers > max_value:
                max_value = average_passengers
                max_name = name
            print(f"{name}: {average_passengers} passengers.")
    print(f"{max_name} has most passengers per flight: {max_value}")
