"""
Created on Apr 4, 2019

@author: Apostolis Tselios
"""

import os
import utils
from search_utils import initialize_search, search
from data_structures import DoubleLinkedList
from block import Block
from world import World


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    input_file = utils.parse_arguments()
    if input_file != None:
        data = utils.load_problem(input_file)
    else:
        data = utils.load_problem()

    objects = utils.get_objects_from_file(data)
    print('OBJECTS:', objects)
    blocks = [Block(id) for id in objects]

    initial_state = utils.get_initial_state(data)
    print('INIT:', initial_state)

    goal_state = utils.get_goal_state(data)
    print('GOAL:', goal_state)

    world = World(blocks, goal_state, initial_state)
    world.blocks = world.initialize_blocks(world.initial_state,  world.blocks)
    print('WORLD:', world)

    list = DoubleLinkedList()

    initialize_search(world, list)
    solution_node = search(list)
    print('solution:', solution_node)

    if solution_node != None:
        pass
    else:
        print('No solution')


if __name__ == '__main__':
    main()
