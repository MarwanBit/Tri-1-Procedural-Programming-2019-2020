def user_input_integer():
    t = True
    while t:
        input_info = input("Type in an integer:")
        try:
            input_info = input_info.strip()
            input_info = int(input_info)
            string_output = "You entered....{}".format(input_info)
            print(string_output)
            return string_output
        except: 
            pass 

user_input_integer()
