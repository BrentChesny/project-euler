def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def solve():
    weekday = 1
    count = 0

    for y in xrange(1900, 2001):
        for m in xrange(1, 13):
            for d in xrange(1, 32):
                if d > days_in_month(m, y):
                    break

                if y >= 1901 and d == 1 and weekday == 7:
                    count += 1

                weekday = 1 if weekday == 7 else weekday + 1

    return count

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
