"""
Created on Apr 4, 2019

@author: Apostolis Tselios
"""

import os
import utils
import time
from search_utils import initialize_search, search
import sys


def main():
    start = time.time()
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) > 3:
        print('ERROR: TOO MANY ARGUMENTS!')
        sys.exit()
    else:
        method = sys.argv[1]
        input_file = sys.argv[2]

    search_queue = utils.METHODS[method]
    data = utils.load_problem(input_file)
    objects = utils.get_objects_from_file(data)
    initial_state = utils.get_initial_state(data)
    goal_state = utils.get_goal_state(data)

    print('OBJECTS:', objects)

    print('#################### INITIAL STATE ####################')
    print(initial_state)
    i_blocks = utils.initialize_blocks(objects, initial_state)
    for block, value in i_blocks.items():
        print(f'{block}:{value}')

    print('#################### GOAL STATE ####################')
    print(goal_state)
    g_blocks = utils.initialize_blocks(objects, goal_state)
    for block, value in g_blocks.items():
        print(f'{block}:{value}')

    initialize_search(method, i_blocks, search_queue)
    solution_node = search(search_queue, method, g_blocks)

    if solution_node != None:
        print('#################### SOLUTION ####################')
        print(solution_node)
        print('Took: ', time.time() - start)
        solution_path = solution_node.get_moves_to_solution()
        try:
            file_name = input_file.split('\\')[-1]
            output_file = './solutions/' + method + '-' + file_name
            utils.write_solution(output_file, solution_path)
        except FileNotFoundError:
            file_name = input_file.split('/')[-1]
            output_file = './solutions/' + method + '-' + file_name
            utils.write_solution(output_file, solution_path)
    else:
        print('############ ONE MINUTE PASSED AND NO SOLUTION WAS FOUND ############')


if __name__ == '__main__':
    main()
