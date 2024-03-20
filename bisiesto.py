year = int(input("Introduce the year which you want to know whether is leap-year:\n"))

match year:
    case year if ((year % 400 == 0) and (year%100 == 0)) or year%4 == 0:
        print(f"The {year} is leap-year")
    case _:
        print(f"The {year} is not leap-year")