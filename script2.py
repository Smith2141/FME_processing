import os
from Layers.convertible_tab_layer import ConvertibleTabLayer
from Layers.common_action import create_primary_search_dictionary

# path_the_files_DPT = input('Укажите папку ДПТ: ')
# path_electronic_version_of_DPT = input('Где будем создавать электронку?: ')
path_the_files_DPT = os.path.join(os.getcwd(), r'test_fme')
path_electronic_version_of_DPT = os.path.join(os.getcwd(), r'test_electronic_version')

print('-' * 25, '\n', 'В указанной папке найдены слои:')
primary_search_dictionary = create_primary_search_dictionary(path_the_files_DPT)
for layer_name, paths in primary_search_dictionary.items():
    print(f'{layer_name} {len(paths)} шт.: ')
    i = 1
    for path in paths:
        print(f'слой {i}>> {path}')
        i += 1

if not os.path.isdir(path_electronic_version_of_DPT):
    os.mkdir(path_electronic_version_of_DPT)

counter = 0
for layer_name, paths in primary_search_dictionary.items():
    for p in paths:
        copying_layer = ConvertibleTabLayer(p)
        copying_layer.copy_tab_layer(path_electronic_version_of_DPT)
        counter += 1
print(f'Из рабочей директории скопировано {counter} слоёв .tab')
