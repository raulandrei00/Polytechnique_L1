def hello_world():
    return 'Hello world!'

def check_day(n):
    if (n < 1 or n > 7):
        return None
    elif (n > 5):
        return 'rest!'
    else:
        return 'work!'

months = ['January' , 'February' , 'March' , 'April' , 'May', 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']
def name_of_month(m):
    m -= 1
    if (m < 0 or m > 11):
        return None
    else:
        return months[m]

def str_with_suffix(n):
    if (n % 10 == 1 and n % 100 != 11):
        return str(n) + "st"
    elif (n % 10 == 2 and n % 100 != 12):
        return str(n) + 'nd'
    elif (n % 10 == 3 and n % 100 != 13):
        return str(n) + 'rd'
    else:
        return str(n) + 'th'

def is_leap_year (y):
    if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
        return True
    else:
        return False


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def number_of_days (m , y):
    return days[m-1] + (m == 2 and is_leap_year(y))

def date_string (d , m , y):
    '''use prev functions to check existance of date then return it'''
    if (m < 1 or m > 12 or d < 1 or d > number_of_days(m , y)):
        return 'Nonexistent date'
    else:
        return 'The ' + str_with_suffix(d) + ' of ' + name_of_month(m) + ', ' + str(y)

def time_string (t):
    '''just decompose t from greatest unit of measurement to the smallest'''
    answer = str()
    if (t // (3600 * 24) > 0):
        answer += str(t // (3600 * 24)) + ' day'
        if (t // (3600 * 24) != 1):
            answer += 's'
        answer += ', ' 
        t -= (t // (3600 * 24)) * (3600 * 24)
    if (t // 3600 > 0):
        answer += str(t // 3600) + ' hour'
        if (t // 3600 != 1):
            answer += 's'
        answer += ', ' 
        t -= (t // 3600) * 3600
    if (t // 60 > 0):
        answer += str(t // 60) + ' minute'
        if (t // 60 != 1):
            answer += 's'
        answer += ', ' 
        t -= (t // 60) * 60
    answer += str(t) + " second"
    if (t != 1):
            answer += 's'
    return answer

#print(time_string(10000))

#print(date_string(29, 2, 2000))