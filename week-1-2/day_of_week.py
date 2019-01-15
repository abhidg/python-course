import datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']

print("This is a program that shows the weekday given a date")
print("Press Ctrl-C at any point to exit")

def weekday(d):
    return days[d.isoweekday() - 1]

def date_to_string(d):
    return d.strftime("%d %b %Y")

while True:
    date_entered = input("Enter date (YYYY-MM-DD) ")
    try:
        d = datetime.datetime.strptime(date_entered, '%Y-%m-%d').date()
    except ValueError:
        print("Could not understand date")
        continue
    today = datetime.datetime.now().date()

    # exercise
    print("It is a Sunday")
