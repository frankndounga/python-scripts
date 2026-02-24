#!/usr/bin/env python

from os import strerror

src_file = input('Enter the source file: ')
try:
    file = open(src_file, 'r')
    file_tab = []
    read = file.read(1).lower()
    while read != '':
        file_tab.append(read)
        read = file.read(1).lower()
    file.close()

    filter_dict = {}
    for val in sorted(file_tab):
        if val in filter_dict:
            filter_dict[val] += 1
        else:
            filter_dict[val] = 1
    str_file = ""
    for key, value in sorted(filter_dict.items(), key=lambda x: x[1], reverse=True):
        str_file += f'{key:4s} -> {value:3d}\n'
    print(str_file)
    output_file = open(src_file+'.hist', 'wt')
    output_file.write(str_file)
    output_file.close()

except IOError as err:
    print('Some error: ', strerror(err.errno))
