"""
Created on Apr 4, 2019

@author: Apostolis Tselios
"""

import os
import utils
from queue import Queue, LifoQueue
from search_utils import initialize_search, search
from block import Block
from world import World


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    input_file, method = utils.parse_arguments()

    if method == None:
        print('Please specify a searching method: -m <method>.')
        exit(1)
    elif method == 'breadth':
        method = utils.BREADTH
        queue = Queue()
    elif method == 'depth':
        method = utils.DEPTH
        queue = LifoQueue()
    elif method == 'best':
        method = utils.BEST
    else:
        method = utils.ASTAR

    if input_file != None:
        data = utils.load_problem(input_file)
    else:
        data = utils.load_problem()

    objects = utils.get_objects_from_file(data)
    initial_state = utils.get_initial_state(data)
    goal_state = utils.get_goal_state(data)

    print('OBJECTS:', objects)
    print('INIT:', initial_state)
    print('GOAL:', goal_state)

    blocks = [Block(id) for id in objects]
    world = World(blocks, goal_state, initial_state)
    world.blocks = world.initialize_blocks(world.initial_state,  world.blocks)
    print('WORLD:', world)

    initialize_search(world, queue)
    solution_node = search(queue, method)
    print(f'Solution: {solution_node}')

    if solution_node != None:
        pass
        # solution_node.route_to_root()
    else:
        print('No solution')


if __name__ == '__main__':
    main()
