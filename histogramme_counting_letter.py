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

    filter_dict = {}
    for val in sorted(file_tab):
        if val in filter_dict:
            filter_dict[val] += 1
        else:
            filter_dict[val] = 1
    for key, value in filter_dict.items():
        print(f'{key:4s} -> {value:3d}')

except IOError as err:
    print('Some error: ', strerror(err.errno))
