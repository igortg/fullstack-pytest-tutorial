import os
from roman7 import to_roman


def write_to_roman(text, output_filename):
    '''convert the given text numbers into roman and write it into a file'''
    converted = []
    for word in text.split():
        try:
            number = int(word)
        except ValueError:
            converted.append(word)
        else:
            converted.append(to_roman(number))
    if os.path.isfile(output_filename):
        raise IOError("File '{}' already exist".format(output_filename))
    with open(output_filename, 'w') as output_file:
        output_file.write(" ".join(converted))