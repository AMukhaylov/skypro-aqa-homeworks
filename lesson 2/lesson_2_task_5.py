month = int(input("Введите месяц = "))

def month_to_season(month): 
    if 1 <= month <= 2 or month == 12:
        print("Месяц зимы")
    elif 3 <= month <= 5:
        print("Месяц весны")
    elif 6 <= month <= 8:
        print("Месяц лета")
    elif 9 <= month <= 11:
        print("Месец осени")
    else: 
        print("Нет такого месяца")

month_to_season(month)