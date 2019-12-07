# ============================================================================
#
#  Name     : RunWorkspace.py
#  
#  Purpose  : FMEPedia Sample of FMEWorkspaceRunner
#  
#  Author               Date            Changes made
#  ------------------   ------------    -------------------------------
#  Ken Bragg           July 15th, 2014   Original Definition


# Note: 
# The path to fmeobjects must by in your python path so you may need something like this:
# import sys 
# sys.path.append("C:\\apps\\FME2014\\fmeobjects\\python27")
import os
import time
import fmeobjects

# initiate FMEWorkspaceRunner Class
runner = fmeobjects.FMEWorkspaceRunner()

# Full path to Workspace, example comes from the FME 2014 Training Full Dataset
workspace = r"C:\Users\1\FME_processing\2_mapinfo2mapinfo.fmw"
source_dir = r"C:\LAYER_T"
dest_dir = r"C:\LAYER_T_RES"
list_tabs = []
# Set workspace parameter s by creating a dictionary of name value pairs
parameters = dict()
parameters['DestDataset_MAPINFO'] = dest_dir

for root, dirs, files in os.walk(source_dir):
    for f in files:
        if f.endswith('.TAB') or f.endswith('.tab'):
            print('*'*25, '\n', f)
            list_tabs.append(os.path.join(root, f))
            # Use Try so we can get FME Exception

for tab_item in list_tabs:
    parameters['SourceDataset_MAPINFO'] = tab_item
    try:
        runner = fmeobjects.FMEWorkspaceRunner()
        # Run Workspace with parameters set in above dictionary
        print(parameters)
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
        # time.sleep(3)

    # get rid of FMEWorkspace runner so we don't leave an FME process running
    runner = None
