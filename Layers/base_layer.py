class BaseLayer:
    def __init__(self, layer_file_path):
        # self.key_layer_name = key_layer_name
        self.layer_file_path = layer_file_path
        self.extension = str(self.layer_file_path).rpartition('.')[2]
