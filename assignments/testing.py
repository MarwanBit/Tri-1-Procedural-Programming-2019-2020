import datetime
import problem_set_1

def date_time(year,month,day):
    date_time_object = datetime.date(year,month,day)
    print(date_time_object.timetuple().tm_yday)

date_time(2003,4,8) 

data_set = {
    "08/04/2003":2015,"09/04/2002":2015,
    "08-04-2003":2015,"09-04-2002":2015,
    "08042003":2015, "080403":2015, 
    "08/04/03":2015,"08-04-03":2015
    }
for i in data_set.items():
    i = list(i)
    print(f"{i[0]} : {i[1]}")

print(problem_set_1.waterCloset('''This is the String I am testing 
			This is the third line.'''))

print('\n'*5)

def dhms(secs):

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
            if remaining_seconds > 3600:
                hours = remaining_seconds // 3600
                remaining_seconds = hours % 60
                if remaining_seconds > 59:
                    minutes = remaining_seconds // 60 
                    remaining_seconds = minutes % 60 
            unsanitized_tuple = (days,hours,minutes,remaining_seconds)
            return sanitize_tuple(list(unsanitized_tuple))
        
        
        


print(dhms(600))
print(dhms(645))
print(dhms(3601))
print(dhms(3661))
print(dhms(43534))
print(dhms(3600))
print(dhms(86400))
print(dhms(5184000))
print(dhms(46430863603483))
print('\n')