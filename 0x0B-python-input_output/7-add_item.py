#!/usr/bin/python3
""" this script will add arguments to a list and save them to a file """


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file


import sys


lst = []
lst.append(sys.argv[1:])
strlst = str(lst)

with open('add_item.json', 'a') as f:
    f.write(strlst)

