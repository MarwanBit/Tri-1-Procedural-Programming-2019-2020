import datetime

#################################################
#  Author: Marwan Bit
#  Date:   9/10/2019
#  PS1.py
#################################################

#If you get help on this assignment, you must report who you received 
#help from and on what you received help with.
#Fill out the comment box at the top under or suffer the pain of 
#death and endless heckling.

##put any imports at the top of this file (right here is fine)

##if you define any helper functions, put them here and give 
##them a docstring.

def meanie(theList):
    """Precondition: theList is a non-empty list of numbers
Postcondition: return the mean of the numbers."""
    return sum(theList)/len(theList)

def datePlus(theDate):
    """Precondition: theDate is a string containing a date.  
Postcondition: Return the sum of the year, month, and day.  You must accept any of the following formats of dates.  
You may assume that any year smaller than 15 is preceeded by 20 and any year larger than 15 is preceded by 19.
dd/mm/yyyy
dd-mm-yyyy
ddmmyyyy
ddmmyy
dd/mm/yy
dd-mm-yy
"""
    appended_string_list = []
    list_of_special_chars = ["/","-"]
    if list_of_special_chars[0] in theDate:
        appended_string_list = theDate.split(list_of_special_chars[0]) 
    elif list_of_special_chars[1] in theDate:
        appended_string_list = theDate.split(list_of_special_chars[1])
    else:
        appended_string_list.append(theDate[0:2])
        appended_string_list.append(theDate[2:4])
        appended_string_list.append(theDate[4:])

    sum = 0
    counter = 0
    for i in appended_string_list:
        if appended_string_list[counter] == appended_string_list[2]:
            if  len(i) == 2 and int(i) > 15:
                i = int(i)
                i += 1900 
            elif len(i) == 2 and int(i) < 15:
                i = int(i)
                i += 2000
        i = int(i)
        sum += i
        counter += 1
    return sum


#Challenge question:  Why did we nest the if statements this way?
#Can you develop a solid reason?  This is free code for the problems
#below.
###################FREE CODE######################################
def isLeap(year):
    """prec:  year is a modern year
postc: returns True if the year leaps.
"""
    out = False
    if year %4 == 0:
        out = not out
        if year % 100 == 0:
            out = not out
            if year % 400 == 0:
                out = not out
    return out
##############END FREE CODE######################################


def dayInYear(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the ordinal position of the day in the year
    (Feb 15 is the 44th day of year 2000).
    Hint:  The list method sum is your friend. Learn about it."""
    date_time_object = datetime.date(year,month,day)
    day_in_year = date_time_object.timetuple().tm_yday
    return day_in_year


def daysLeftInYear(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the number of days left in the year
    (Feb 15 is the 44th day of year 2000)."""
    days_left_in_year = 0
    date_time_object = datetime.date(year,month,day)
    day_in_year = date_time_object.timetuple().tm_yday
    if isLeap(year):
        days_left_in_year = 366 - day_in_year
    else:
        days_left_in_year = 365 - day_in_year
    return days_left_in_year

def daysToGraduation(month, day, year=2019):
    """prec:  year/month/ is a valid date before graduation
    postc: returns the number of days until graduation
    """
    graduation_date = datetime.date(2021,5,25)
    input_date = datetime.date(year,month,day)
    days_till_graduation = graduation_date - input_date
    return days_till_graduation

def dhms(secs):
    """prec:  secs is a nonnegative integer
    postc: return a STRING of the form d:hh:mm:ss, where
    d is the number of days, h is the number of hours, m is the number of minutes, and s is the number of seconds, h < 24, 0 <= m, s, < 60.
    Give h, m, s a two character width, padding with zeroes as needed.
    """
    def sanitize_tuple(dhms_list):
        k = 0
        for i in dhms_list:
            if len(str(i)) == 1:        
                replaced_item =  str(dhms_list.pop(k)) + ":"
                dhms_list.insert(k,"0" + replaced_item)
            elif type(i) is not str:
                replaced_item = str(dhms_list.pop(k)) + ":"
                dhms_list.insert(k,replaced_item)
            k += 1
            
        dhms_string = ""
        dhms_string = dhms_string.join(dhms_list)
        dhms_string = dhms_string[0:len(dhms_string)-1]
        return dhms_string

    if secs > 59 and secs < 3600:
        minutes = secs // 60
        remaining_seconds = secs % 60 
        unsanitized_tuple = ("00:","00:",minutes,remaining_seconds)
        return sanitize_tuple(list(unsanitized_tuple))
    elif secs >= 3600 and secs < 86400:
        if secs == 3600:
            return "00:01:00:00"
        hours = secs // 3600
        remaining_seconds = secs % 3600
        if remaining_seconds > 59:
            minutes = remaining_seconds // 60
            remaining_seconds = minutes % 60
            unsanitized_tuple = ("00:",hours,minutes,remaining_seconds)
            return sanitize_tuple(list(unsanitized_tuple))
        else:
            unsanitized_tuple = ("00:",hours,"00:",remaining_seconds)
            return sanitize_tuple(list(unsanitized_tuple))
    elif secs >= 86400:
        if secs == 86400:
            return "01:00:00:00"
        else:
            hours = 0
            minutes = 0
            days = secs // 86400
            remaining_seconds = secs % 86400
            if remaining_seconds >= 3600:
                hours = remaining_seconds // 3600
                remaining_seconds = remaining_seconds % 3600
                if remaining_seconds > 59:
                    minutes = remaining_seconds // 60 
                    remaining_seconds = remaining_seconds % 60 
            unsanitized_tuple = (days,hours,minutes,remaining_seconds)
            return sanitize_tuple(list(unsanitized_tuple))
        

def waterCloset(theString):
    """precondition: thesString is a string.
postcondition: a tuple (c, w, l) where c is the number of characters in 
theString, w is the number of words, and l is the number of lines in the string"""
    #Number of characters excludes zero's
    list_of_words = theString.split(" ")
    number_of_words = len(list_of_words)
    character_string = theString.replace(" ", "")
    number_of_characters = len(character_string)
    number_of_lines = theString.count('\n') + 1
    information_tuple = (number_of_characters, number_of_words, number_of_lines)
    return information_tuple

def mathCase(x):
    """precondition: x is a number
postcondition: If x > 4, f(x) = x - 4, if x < -5, f(x) = x + 5,
otherwise, f(x) = 0.""" 
    if x > 4:
        return x-4 
    elif x < -5:
        return x+5 
    else:
        return 0
def closeEnough(a,b):
    return abs(a-b)<1e-6

def runTest(function, value, expected):
    if function(value) == expected:
        print("PASS for case %s" % value)
    else:
        print("FAIL because f(%s) != %s" %(value, expected))
def runTestFloat(function, value, expected):
    if closeEnough(function(expected), value):
        print("PASS for case %s" % value)
    else:
        print("FAIL because f(%s) != %s" %(value, expected))
 
   
if __name__ == "__main__":
    ##put test code here 
    ##Writing good test code helps your grade! And it prevents
    ## you from making stupid mistakes.  
    ##the samples show you what to do.
    ##
    value = [1,2,4,8,-15]
    expected = 0
    runTest(meanie, value, expected)
    value = [1,2,3,4,5,6]
    expected = 3.5
    runTest(meanie, value, expected)
    ##
    print(daysLeftInYear(2019,9,20) == 102)
    print(daysLeftInYear(2019,9,21) == 101)
    print(daysLeftInYear(2019,3,11) == 295)
    print(daysLeftInYear(2019,4,9) == 266)
    ##
    print(dayInYear(2019,9,20) == 263)
    print(dayInYear(2019,9,21) == 264)
    print(dayInYear(2019,3,11) == 70)
    print(dayInYear(2019,4,9) == 99)
    ##
    ##
    print(datePlus("01/01/1970") == 1972)
    print(datePlus("08/12/1995") == 2015)
    print(datePlus("08/12/95") == 2015)
    print(datePlus("08/12/14") == 2034)
    print(datePlus('081214') == 2034)
    print(datePlus('08-12-95') == 2015)
    ##
    print(daysToGraduation(9,20))