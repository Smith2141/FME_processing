import os
import time

fme_file = r"C:\Users\1\FME_processing\2_mapinfo2mapinfo.fmw"
source_dir = r"C:\LAYER_T"
source_file = r"C:\LAYER_T\51_01_0000000.TAB"
dest_dir = r"C:\LAYER_T\RES"

# for root, dirs, files in os.walk(source_dir):
#     for f in files:
#         if f.endswith('.TAB'):
#             print(f)
#             os.system(f'fme.exe {fme_file} --SourceData {f} --DestinationData {dest_dir}')

os.system(f'fme.exe {fme_file} --SourceData {source_file} --DestinationData {dest_dir} --NAME {source_file}')
