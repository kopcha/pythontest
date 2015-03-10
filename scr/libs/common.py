'''
Created on Mar 3, 2014

@author: xvok
'''
import re
def sayBye():
    print('Good Bye!')


def sort_dictionary_to_list(input_dict):
    result = []
    for level_no in range(len(LEVEL_PRIORITY)):
        print('Current product level number: {}'.format(level_no))
        for prod_no, r_state in input_dict.items():
            match = re.match('^\d*\/*([A-Z]{3,})\d+\/*', prod_no)
            if match:
                prod_abc_class = match.group(1)
                print('Retrieved product ABC class for {} {}: {}'.
                      format(prod_no, r_state, prod_abc_class))
                if prod_abc_class in LEVEL_PRIORITY[level_no]:
                    result.append((prod_no, r_state))
                else:
                    print('Product ABC class {} is not in the list!'.
                          format(prod_abc_class))
            else:
                print('Can not retrieve ABC class for {} {}'.
                      format(prod_no, r_state))
    return result

LEVEL_PRIORITY = {0: ['CAA', 'CXA', 'CXC', 'CAAZ', 'CAAZA'],
                  1: ['CNT', 'CNTU'],
                  2: ['CRT', 'CRTU'],
                  3: ['ANT'],
                  4: ['APT'],
                  5: ['AXE']}
