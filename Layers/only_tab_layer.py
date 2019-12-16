import os
import shutil
from .base_layer import BaseLayer
from Layers.locators import LayerExtension


class ConvertibleTabLayer(BaseLayer):
    def copy_tab_with_three_files(self, destination_path):
        name_of_the_four_files = str(self.layer_file_path).rpartition('.')[0]
        counter_copied_files = 0
        for ext in LayerExtension.tab_layer_file_types:
            required_file_upper_case = f'{name_of_the_four_files}.{ext}'
            required_file_lower_case = f'{name_of_the_four_files}.{ext.lower()}'
            if os.path.exists(required_file_upper_case):
                shutil.copy(required_file_upper_case, destination_path)
                counter_copied_files += 1
            else:
                shutil.copy(required_file_lower_case, destination_path)
                counter_copied_files += 1
        assert counter_copied_files == 4
        print(f'Всего скопировано {counter_copied_files} файлов')

    def from_tab_make_pls_tab(self):
        pass

    def from_tab_make_pls_mif(self):
        pass

    def from_tab_make_shp(self):
        pass
