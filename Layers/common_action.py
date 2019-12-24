import os
import re
import fmeobjects
from Layers.locators import PatternsDpt
from Layers.locators import WorkspacesPath


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


def tab_to_pl_sch_tab(prim_search_dict, target_dir):
    # Full path to Workspace
    workspace = WorkspacesPath.TAB_TO_PL_SCH_TAB
    # Set workspace parameter s by creating a dictionary of name value pairs
    parameters = dict()
    parameters['DestDataset_MAPINFO_4'] = target_dir

    counter = 0
    for layer_name, paths in prim_search_dict.items():
        for path in paths:
            parameters['SourceDataset_MAPINFO'] = path
            parameters['FEATURE_TYPES'] = os.path.basename(path).rstrip('.TAB')
            try:
                # initiate FMEWorkspaceRunner Class
                runner = fmeobjects.FMEWorkspaceRunner()
                # Run Workspace with parameters set in above dictionary
                runner.runWithParameters(workspace, parameters)
                counter += 1
            except fmeobjects.FMEException as ex:
                # Print out FME Exception if worskspace failed
                print(ex.message)
            else:
                # Tell user the workspace ran
                print('The Workspace: ' + workspace)
                print('...ran successfully')

            # get rid of FMEWorkspace runner so we don't leave an FME process running
            runner = None
    return f'Преобразовано в план-схему метры {counter} файлов .tab'


def from_tab_make_pls_mif(self):
    pass


def from_tab_make_shp(self):
    pass
