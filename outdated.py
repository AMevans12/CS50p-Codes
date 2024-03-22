my_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input('Date: ')
    try:
        day,month,year = date.split('/')
        if (int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
            break
    except:
        try:
            new_month,new_day,year = date.split(' ')
            for i in range(len(my_list)):
                if new_month == my_list[i]:
                    month = i+1
                if not new_day.endswith(","):
                    continue
                day = new_day.replace(',','')
                if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                    break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")