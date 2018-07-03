def find_elem(list_of_strings, name_string):
    # use the name_string to find the element in the list_of_strings
    # that matches the name_string
    # if there is a match, return that element
    # if there is no match, return an empty string
    for string in list_of_strings:
        if string === name_string:
            return string
        else:
            return ""


def find_elem_by(list_of_dictionaries, attribute, value):
    # iterate over each element of the list of dictionaries
    # use the given attribute and value to access the values from each dictionary
    # find the dictionary whose value matches that which is passed in
    # return the dictionary
    # if no match is found, return an empty dictionary
    for dict_elem in list_of_dictionaries:
        for key in dict_elem:
            if key == attribute:
                return dict_elem
            else:
                return {}


def filter_list(list_of_elements, callback_function):
    # should take in a list of elements and a callback that executes on each element
    # the callback is what determines whether that element should be returned from the filter_list function
    # the callback returns True or False
    # filter_list should return a new list of filtered elements
    return [element for element in list_of_elements if callback_function(element)]


def max(list_of_numbers):
    # returns the largest number in the list
    max = list_of_numbers[0]
    for num in list_of_numbers:
        if max < num:
            max = num
    return max

def max_by(list_of_dictionaries, attribute):
    # returns the dictionary with the attribute with the highest value
    max_elem = list_of_dictionaries[0]
    for dict_elem in list_of_dictionaries:
        if max_elem[attribute] < dict_elem[attribute]:
            max_elem = dict_elem
    return max_elem

def sort_strings(list_of_strings):
    # returns a list of strings in alphabetical order
    # remeber the 'a' has a lower value than 'b' or 'c'
    unsorted_list = list_of_strings
    sorted_list = []
    while unsorted_list:
        first_word = list_of_strings[0]
        for word in unsorted_list:
            if first_word > word:
                first_word = word
        sorted_list.append(first_word)
        unsorted_list.remove(first_word)
    return sorted_list
