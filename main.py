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

    world = WorldState(i_blocks, g_blocks)
    world.get_possible_moves()

    initialize_search(args.method, world, search_queue)
    solution_node = search(search_queue, args.method)
    print(f'Solution:{solution_node}')
    print('Took: ', time.time() - start)

    if solution_node != None:
        pass
        # solution_node.route_to_root()
    else:
        print('No solution')


if __name__ == '__main__':
    main()
