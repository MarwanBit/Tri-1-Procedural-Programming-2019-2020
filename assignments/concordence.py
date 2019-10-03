from sys import argv 

def make_concordence_dictionary(file_name):
    '''Precondition: fileName is the name of an existing file
    Postcondition: returns dictionary with all distinc words in the file as keys and their 
    frequencies as values.'''
    word_dict_out = {}
    with open(file_name,'r') as fp:
        for line in fp:
            line = line.lower()
            words = line.split(" ")
            for word in words:
                word = word.strip("\n.;!:,?()\'")
                if word in word_dict_out:
                    word_dict_out[word] += 1 
                else: 
                    word_dict_out[word] = 1 
        return word_dict_out  

def create_alphabetical_file(input_dictionary, output_file_name):
    '''precondition: filename is the name of a possibly existing file,
    postcondition: puts dictionary entires into the file in the following format
    word\t\t\t freq where the words are in order'''
    with open(output_file_name,'w') as file_output:
        for item in sorted(input_dictionary.keys()):
            format_string = "{}\t\t\t{}\n".format(item,input_dictionary[item])
            file_output.write(format_string)
    file_output.close()

#*********************************************WIP NOT WORKING**************************************************
def return_frequency_intervals(input_list_of_tuples):
    '''precondition: a sorted concordence_dict alphanumerically
    postcondition: sorted in ascending alphanumberical order'''
    list_of_frequency_intervals = []
    sub_interval = []
    interval_same = True
    global_counter = 0
    while global_counter < len(input_list_of_tuples):
        while interval_same:
            for sub_tuple in input_list_of_tuples:
                if global_counter == 0:
                    sub_interval.append(sub_tuple)
                else:
                    if sub_tuple[1] == input_list_of_tuples[global_counter-1][1]:
                        sub_interval.append(input_list_of_tuples[global_counter])
                    elif sub_tuple[1] != input_list_of_tuples[global_counter-1][1]:
                        interval_same = False 
                global_counter += 1
        list_of_frequency_intervals.append(sub_interval)
        sub_interval = []
        interval_same = True
    return list_of_frequency_intervals
#****************************************************************************************************************

def sorting_concordence(input_dictionary):
    '''precondition: concordence dictionary is a concordence
    postcondition: sorted in ascending and alphanumerical order'''
    sorted_keys = sorted(input_dictionary.keys())
    sorted_values = [input_dictionary[i] for i in sorted(input_dictionary.keys())]
    input_list_of_tuples = zip(sorted_keys,sorted_values)
    alphanumberically_sorted_input_list_of_tuples = sorted(input_list_of_tuples,key = lambda x:x[0], reverse=False)
    alphanumerically_sorted_input_list_of_tuples = sorted(
        alphanumberically_sorted_input_list_of_tuples, 
        key= lambda x:x[1],
        reverse=True
        ) 
    list_of_keys = [i[1] for i in alphanumerically_sorted_input_list_of_tuples]
    return (alphanumerically_sorted_input_list_of_tuples, list_of_keys)


def run_file():
    file_name = argv[1]
    output_file_name = argv[2]
    create_alphabetical_file(make_concordence_dictionary(file_name),output_file_name + ".conc")
    sorted_dictionary = sorting_concordence(make_concordence_dictionary(file_name))
    print(sorted_dictionary[0])

    '''
    Check the following lines below out ....
    print(help(sort_alphanumerically))
    print(sort_alphanumerically.__doc__)
    '''


run_file()
