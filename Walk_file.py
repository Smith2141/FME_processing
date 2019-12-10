import os

PATH = r'C:\Users\1\Desktop\This_a_dir'
#PATH = 'CeHeReIeSeTeMeAeS'

def possible_depth(base_path):
    base_path = os.path.normpath(base_path).replace('\\', '*')
    base_len = len(base_path.split('*'))
    return base_len

base_path_len = possible_depth(PATH)
for root, dirs, files in os.walk(PATH):
    if possible_depth(root) <= base_path_len+1 and '11' not in root:
        print(root)
