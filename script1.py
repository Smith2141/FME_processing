import os
import fmeobjects

# Full path to Workspace, example comes from the FME 2014 Training Full Dataset
# workspace = r"C:\Users\1\FME_processing\2_mapinfo2mapinfo.fmw"
workspace = os.path.join(os.getcwd(), r'fme_workspaces/2018mapinfo2mapinfo.fmw')
# source_dir = input('Укажите папку с файлами: ')
source_dir = os.path.join(os.getcwd(), 'test_fme')
target_dir = os.path.join(os.getcwd(), r'test_fme\RESULT')
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
