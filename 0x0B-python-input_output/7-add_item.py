#!/usr/bin/python3
""" this script will add arguments to a list and save them to a file """


import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_json_file = __import__('6-load_from_json_file.py').load_from_json_file


try:
    lst = load_json_file('add_item.json')
except:
    lst = []

lst += argv[1:]
save_to_json_file(lst, 'add_item.json')
