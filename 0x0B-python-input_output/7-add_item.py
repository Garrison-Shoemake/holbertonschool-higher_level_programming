#!/usr/bin/python3
""" This file loads, adds, and saves files """
import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_json_file = __import__('6-load_from_json_file.py').load_from_json_file


try:
    lst = load_json_file('add_item.json')
except:
    lst = []

lst += argv[1:]
save_to_json_file(lst, 'add_item.json')
