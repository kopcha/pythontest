"""
Created on Mar 3, 2014

@author: xvok
"""

from my_functions.common import *
from my_functions.dict2xml import *


def main():
    products = {'AXE10507/229': 'R1A',
                'APT21009/229': 'R1A',
                'ANT24009/1': 'R1A',
                'ANT24808/25': 'R1A',
                'CRT240010/2': 'R1A',
                'CNT2401111': 'R3A',
                'CNT2412222': 'R2A',
                'CAAZ1071234': 'R7A',
                'CAAZ1074321': 'R6A',
                'CAAZA1072222': 'R5A',
                'CAAZA1073333': 'R7A',
                'CAA2045555': 'R8A',
                'CXA2526666': 'R1A',
                '7/CXC1465555': 'R8A',
                '4/CXC1465555': 'R8A'}
    print('Dictionary before sorting: {}'.format(products))
    sorted_dict = sort_dictionary_to_list(products)
    print('Dictionary after sorting: {}'.format(sorted_dict))
    release_products_in_prim(sorted_dict)

    xml = demo_dicttoxml()
    flush_to_file(file_path='/home/xvok/generated.xml', data=xml)

if __name__ == '__main__':
    main()
