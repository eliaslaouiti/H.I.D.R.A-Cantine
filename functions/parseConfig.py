# coding: utf-8
__author__ = 'Laouiti Elias Cédric'

COMMENT_CHAR = '#'
OPTION_CHAR = '='

def parse_config(filename):
    options = {}
    f = open(filename)
    for line in f:
        if COMMENT_CHAR in line:
            line, comment = line.split(COMMENT_CHAR, 1)
        if OPTION_CHAR in line:
            option, value = line.split(OPTION_CHAR, 1)
            option = option.strip()
            value = value.strip()
            options[option] = value
    f.close()
    return options
