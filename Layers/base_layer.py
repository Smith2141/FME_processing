class BaseLayer:
    def __init__(self, layer_name, layer_source_path, layer_final_path=None):
        self.layer_source_path = layer_source_path
        self.layer_name = layer_name

    def from_tab_make_pls_tab(self):
        pass

    def from_tab_make_pls_mif(self):
        pass

    def from_tab_make_shp(self):
        pass
