import os
import re
import shutil
from Layers.locators import PatternsDpt

# path_the_files_DPT = input('Укажите папку ДПТ: ')
path_the_files_DPT = r'C:\Users\1\FME_processing\test_fme'
# path_electronic_version_of_DPT = input('Где будем создавать электронку?: ')
path_electronic_version_of_DPT = r'C:\Users\1\FME_processing\test_electronic_version'

PRIMARY_SEARCH_DICTIONARY = {'GZPRO': [],
                             'VZIS': [],
                             'DEMONTAZH': []
                             }


def possible_depth(base_path):
    base_path = os.path.normpath(base_path).replace('\\', '*')
    base_len = len(base_path.split('*'))
    return base_len


dpt_path_len = possible_depth(path_the_files_DPT)
for root, dirs, files in os.walk(path_the_files_DPT):
    if possible_depth(root) <= dpt_path_len + 1 and not re.search(PatternsDpt.PATTERN_OLD_DIR, root):
        # print(root, '\n', files)
        for file in files:
            for layer_name, pattern in PatternsDpt.PATTERN_DICTIONARY.items():
                if re.search(pattern, file):
                    PRIMARY_SEARCH_DICTIONARY[layer_name].append(os.path.join(root, file))

print('-'*25, '\n', 'В указанной папке найдены слои:')
for layer_name, paths in PRIMARY_SEARCH_DICTIONARY.items():
    print(f'{layer_name} {len(paths)} шт.: ')
    i = 1
    for path in paths:
        print(f'слой {i}>> {path}')
        i += 1

if not os.path.isdir(path_electronic_version_of_DPT):
    os.mkdir(path_electronic_version_of_DPT)
counter_copied_files = 0
for layer_name, paths in PRIMARY_SEARCH_DICTIONARY.items():
    i = 0
    for path in paths:
        shutil.copy(path, path_electronic_version_of_DPT)
        i += 1
    # print(f'Скопировано {i} файлов')
    counter_copied_files += i
print(f'Всего скопировано {counter_copied_files} файлов')