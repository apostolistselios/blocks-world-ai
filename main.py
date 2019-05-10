"""
Created on Apr 4, 2019

@author: Apostolis Tselios
"""

import os
import utils
import time
from search_utils import initialize_search, search
from state import WorldState


def main():
    start = time.time()
    os.system('cls' if os.name == 'nt' else 'clear')

    args = utils.parse_arguments()

    search_queue = utils.METHODS[args.method]
    data = utils.load_problem(args.input)
    objects = utils.get_objects_from_file(data)
    initial_state = utils.get_initial_state(data)
    goal_state = utils.get_goal_state(data)

    print('OBJECTS:', objects)
    print('INIT:', initial_state)
    print('GOAL:', goal_state)

    i_blocks = utils.initialize_blocks(objects, initial_state)
    # print(i_blocks)
    g_blocks = utils.initialize_blocks(objects, goal_state)
    # print(g_blocks)

    initialize_search(args.method, i_blocks, search_queue)
    solution_node = search(search_queue, args.method, g_blocks)
    print(f'Solution:{solution_node}')
    print('Took: ', time.time() - start)

    if solution_node != None:
        solution_path = solution_node.get_moves_to_solution()
        try:
            output_file = f'./solutions/{args.method}-{args.input.lstrip("./prorblems/")}'
            utils.write_solution(output_file, solution_path)
        except FileNotFoundError:
            output_file = '.\solutions\\' + args.method + \
                '-' + args.input.lstrip(r".\prorblems\\")
            utils.write_solution(output_file, solution_path)
    else:
        print('No solution')


if __name__ == '__main__':
    main()
