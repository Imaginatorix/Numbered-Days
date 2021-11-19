import datetime

def doomday(y): # get doomsday of the year
    c = int(y % 100)
    a = (((5 * (int(y / 100) % 4)) % 7) + 2) % 7 # anchor
    return ((c + int(c / 4)) + a) % 7

def get_next(dname = 5, dnumber = 13): # Friday 13th
    date = datetime.datetime.now()
    y = date.year

    while True:
        if y == date.year:
            m = date.month
            if date.day > dnumber:
                m += 1
        else:
            m = 1

        if y % 4 == 0: # leap year
            doomsdays = [4, 29, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
        else:
            doomsdays = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]

        to_break = False
        month = 1 # I still need to change this, but it's a counter to know which month
        for day in doomsdays[m - 1:]:
            doom = doomday(y)

            doomsday = (doom + (dnumber - day)) % 7
            if doomsday == dname:
                print (datetime.datetime(y, month, dnumber))
                to_break = True
                break
           
            month += 1
               
        y += 1

        if to_break:
            break

if __name__ == "__main__":
    get_next()
