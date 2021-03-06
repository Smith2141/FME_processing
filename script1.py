import os
import fmeobjects

# Full path to Workspace, example comes from the FME 2014 Training Full Dataset
workspace = r"C:\Users\1\FME_processing\fme_workspaces\2018mapinfo2mapinfo.fmw"
# workspace = os.path.join(os.getcwd(), r'fme_workspaces\2018mapinfo2mapinfo.fmw')
# source_dir = input('Укажите папку с файлами: ')
source_dir = os.path.join(os.getcwd(), 'test_fme')
# target_dir = os.path.join(os.getcwd(), r'test_fme\RESULT')
target_dir = os.path.join(os.getcwd(), r'test_electronic_version')
list_processing_files = []
# Set workspace parameter s by creating a dictionary of name value pairs
parameters = dict()
# для версии 2018 синтаксис параметра папки назначения: 'DestDataset_MAPINFO_4'!!!
# parameters['DestDataset_MAPINFO_4'] = target_dir
parameters['DestDataset_MAPINFO_4'] = target_dir

for root, dirs, files in os.walk(source_dir):
    for f in files:
        if f.endswith('.TAB') or f.endswith('.tab'):
            f = f'{f.rpartition(".")[0]}.TAB'
            list_processing_files.append(os.path.join(root, f))
            # Use Try so we can get FME Exception

for tab_file in list_processing_files:
    parameters['SourceDataset_MAPINFO'] = tab_file
    parameters['FEATURE_TYPES'] = os.path.basename(tab_file).rstrip('.TAB')
    try:
        # initiate FMEWorkspaceRunner Class
        print(f'Обработка {tab_file}')
        print(parameters)
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

    #     "C:\Program Files\FME\fme.exe" C:\Users\1\FME_processing\fme_workspaces\2018mapinfo2mif.fmw
    #           --FEATURE_TYPES "Lake_27_3"
    #           --DestDataset_MIF "C:\Users\1\FME_processing\test_electronic_version"
    #
    #     "C:\Program Files\FME\fme.exe" C:\Users\1\FME_processing\fme_workspaces\2018mapinfo2mapinfo.fmw
    #           --SourceDataset_MAPINFO "C:\Users\1\FME_processing\test_fme\Lake_27_3.TAB"
    #           --FEATURE_TYPES "Lake_27_3"
    #           --DestDataset_MAPINFO_4 "C:\Users\1\FME_processing\test_electronic_version"
