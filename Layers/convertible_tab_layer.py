import os
import shutil
from .base_layer import BaseLayer
from Layers.locators import LayerExtension
import fmeobjects


class ConvertibleTabLayer(BaseLayer):
    def copy_tab_layer(self, destination_path):
        name_of_the_four_files = str(self.layer_file_path).rpartition('.')[0]
        for ext in LayerExtension.tab_layer_file_types:
            required_file_upper_case = f'{name_of_the_four_files}.{ext}'
            required_file_lower_case = f'{name_of_the_four_files}.{ext.lower()}'
            if os.path.exists(required_file_upper_case):
                shutil.copy(required_file_upper_case, destination_path)
            else:
                shutil.copy(required_file_lower_case, destination_path)
