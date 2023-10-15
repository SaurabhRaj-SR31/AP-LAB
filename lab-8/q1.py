import re

function_names = [name for name in dir(re) if callable(getattr(re, name))]


find_functions = [name for name in function_names if 'find' in name]

find_functions.sort()

print(find_functions)
