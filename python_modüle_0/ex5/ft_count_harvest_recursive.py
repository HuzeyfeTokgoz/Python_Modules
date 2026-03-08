def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def count_day(current_day):
        if current_day > day:
            print("Harvest time!")
            return
        print(f"Days {current_day}")
        count_day(current_day + 1)
    count_day(1)
