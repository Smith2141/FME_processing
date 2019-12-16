import shutil
from .base_layer import BaseLayer


class ConvertibleTabLayer(BaseLayer, layer_final_path=None):
    def copy_tab_with_three_files(self, tab_path, file_extension_iter, destination_path):
        name_of_the_four_files = str(tab_path).rpartition('.')[0]
        counter_copied_files = 0
        for e in file_extension_iter:
            required_file_upper_case = f'{name_of_the_four_files}.{e}'
            required_file_lower_case = f'{name_of_the_four_files}.{e.lower()}'
            if os.path.exists(required_file_upper_case):
                shutil.copy(required_file_upper_case, destination_path)
                counter_copied_files += 1
            else:
                shutil.copy(required_file_lower_case, destination_path)
                counter_copied_files += 1
        print(f'Всего скопировано {counter_copied_files} файлов')

    def from_tab_make_pls_tab(self):
        pass

    def from_tab_make_pls_mif(self):
        pass

    def from_tab_make_shp(self):
        pass
