# import fme and shutil modules
from os import path

import fme
import shutil

# Filepath hardcoded to C:\TEMP
workspacePath = r'C:\LAYER_T'
# Filepath of source dataset using macroValues dictionary
sourceFile = fme.macroValues['SourceDataset_ESRISHAPE']

# Gets dataset name without extension with '_backup' appended
sourceName = path.splitext(path.basename(sourceFile))[0] + '_backup'

# Path of new zip with name
zipDir = '{}\\{}'.format(workspacePath, sourceName)

# Root directory of folder containing source dataset
sourcePath = path.dirname(sourceFile)

# If zip file with same name already exists, do not create, add message to log window
if path.exists(zipDir + '.zip'):  # Message to log window
    print(zipDir + '.zip already exists. Did not create zip.')
else:
    # Use shutil module to create zip file
    shutil.make_archive(zipDir, 'zip', sourcePath)
    print('Created backup of ' + path.basename(sourceFile))
    print('Path at ' + zipDir + '.zip')

# Debugging
# print(sourceName)
# print(zipDir)