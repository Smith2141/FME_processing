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

    def from_tab_make_pls_tab(self, source_dir, target_dir):
        list_processing_files = []
        # Set workspace parameter s by creating a dictionary of name value pairs
        parameters = dict()
        parameters['DestDataset_MAPINFO'] = target_dir
        parameters['FEATURE_TYPES'] = ""

        for root, dirs, files in os.walk(source_dir):
            for f in files:
                if f.endswith('.TAB') or f.endswith('.tab'):
                    list_processing_files.append(os.path.join(root, f))
                    # Use Try so we can get FME Exception

        for tab_file in list_processing_files:
            # parameters['SourceDataset_MAPINFO'] = tab_file
            parameters['SourceDataset_MAPINFO'] = tab_file
            try:
                # initiate FMEWorkspaceRunner Class
                runner = fmeobjects.FMEWorkspaceRunner()
                # Run Workspace with parameters set in above dictionary
                runner.runWithParameters(workspace, parameters)
                # Or use promtRun to prompt for published parameters
                # runner.promptRun(workspace)

            except fmeobjects.FMEException as ex:
                # Print out FME Exception if worskspace failed
                print(ex.message)

            else:
                # Tell user the workspace ran
                print('The Workspace: ' + workspace)
                print('...ran successfully')

            # get rid of FMEWorkspace runner so we don't leave an FME process running
            runner = None

    def from_tab_make_pls_mif(self):
        pass

    def from_tab_make_shp(self):
        pass
