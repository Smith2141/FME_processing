import os
import re


class WorkspacesPath:
    TAB_TO_PL_SCH_TAB = os.path.join(os.getcwd(), r'fme_workspaces/2018mapinfo2mapinfo.fmw')


class PatternsDpt:
    PATTERN_OLD_DIR = re.compile(r'([СC]тарое)', re.IGNORECASE)
    PATTERN_GZPRO_TAB = re.compile(r'(ГЗПРО|ГЗРО).*\.tab$', re.IGNORECASE)
    PATTERN_VZIS_TAB = re.compile(r'(ВЗИС).*\.tab$', re.IGNORECASE)
    PATTERN_DICTIONARY = {'ГЗПРО': PATTERN_GZPRO_TAB, 'ВЗИС': PATTERN_VZIS_TAB}


class LayerExtension:
    tab_layer_file_types = ('TAB', 'MAP', 'ID', 'DAT')
