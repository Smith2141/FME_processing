import os
import re
from Layers.locators import PatternsDpt


def create_primary_search_dictionary(work_path, pattern=PatternsDpt):
    prim_search_dict = {'ГЗПРО': [],
                        'ВЗИС': [],
                        'ДЕМОНТАЖ': []
                        }
    base_path = os.path.normpath(work_path).replace('\\', '*')
    dpt_path_len = len(base_path.split('*'))
    for root, dirs, files in os.walk(work_path):
        root_path = os.path.normpath(root).replace('\\', '*')
        root_path_len = len(root_path.split('*'))
        if root_path_len <= dpt_path_len + 1 and not re.search(pattern.PATTERN_OLD_DIR, root):
            for file in files:
                for key_name, patt in pattern.PATTERN_DICTIONARY.items():
                    if re.search(patt, file):
                        prim_search_dict[key_name].append(os.path.join(root, file))
    return prim_search_dict
