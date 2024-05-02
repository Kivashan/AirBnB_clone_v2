#!/usr/bin/python3
"""Module that contains helper functions to parse arguments passed
in console.py function do_create"""


# split string containing parameters into a list of parameters
# example of string - "name='Chicago' id=1234"
# example of list of parameters - [name='Chicago', id=1234]
def to_list(line):
    """Splits a string containing parameters into a list of parameters

    Parameters:
        line - a string containing parameters

    Return:
        returns a list object cotaining all parameters(each list item
        is a string object).
    """
    parameter_list = line.split()
    return parameter_list


def type_conversion(string):
    """Converts the given string to str, int or float

    Parameters:
        string - A given string

    Return:
        Returns the converted string, either of type str, type float or
        type int or None if string is not one of the aforementioned types
    """
    if string.startswith('\"') and string.endswith('\"'):
        string = string.strip('\"')
        if '\"' in string:
            string = string.replace('\"', '\\\"')
        if '_' in string:
            string = string.replace('_', ' ')
    elif string.isdigit():
        string = int(string)
    elif '.' in string:
        string = float(string)
    else:
        return None

    return string


def to_dict(parameter_list):
    """Takes a list and converts it to a dict

    Parameters:
        Parameter_list - a list containing all a string format of key=value
        pairs

    Return:
        A dictionary containing key value pairs if parameter_list is not an
        empty list, otherwise returns an empty dictionary
    """
    dictionary = {}

    for parameter in parameter_list:
        if '=' in parameter:
            if parameter[0] != '=' and parameter[-1] != '=':
                args = parameter.split('=')
                args[1] = type_conversion(args[1])
                dictionary[args[0]] = args[1]

    return dictionary


def set_attr(obj, parameter_list):
    dictionary = to_dict(parameter_list)

    for key, value in dictionary.items():
        setattr(obj, key, value)

    return obj
