"""
Created on Apr 4, 2019

@author: Apostolis Tselios
"""

import os
import utils
import time
import sys
from tree_node import TreeNode


def search(queue, method, initial, goal):
    """Searches the tree for a solution based on the search method."""
    start = time.time()
    root = TreeNode(initial, None, None, 0, 0, 0)

    if method == 'astar' or method == 'best':
        queue.put((0, root))
    else:
        queue.put(root)

    visited_set = set()
    start = time.time()
    while (not queue.empty()) and (time.time() - start <= 60):
        # While the queue is not empty and a minutes hasn't passed.
        if method == 'astar' or method == 'best':
            curr_f, current = queue.get()
        else:
            current = queue.get()

        if current.is_goal(goal):
            return current

        if str(current.state) in visited_set:
            # If this state has been visited before don't add to the children
            # and continue with the next child.
            continue

        current.find_children(method, goal)
        visited_set.add(str(current.state))

        for child in current.children:
            if method == 'depth' or method == 'breadth':
                queue.put(child)
            elif method == 'astar' or method == 'best':
                queue.put((child.f, child))

    return None


def main():
    start = time.time()  # Start time.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal.

    # Handles the arguments.
    if len(sys.argv) > 3:
        print('ERROR: TOO MANY ARGUMENTS!')
        sys.exit()
    else:
        method = sys.argv[1]
        input_file = sys.argv[2]

    # Initializes the type of queue based on the search method.
    search_queue = utils.METHODS[method]

    # Parses the data and gets the objects (blocks), initial state and the goal state.
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

    solution_node = search(search_queue, method, i_blocks, g_blocks)

    if solution_node != None:
        # If a solution is found.
        print('#################### SOLUTION ####################')
        print(solution_node)

        # Calculates the time it took to find the solution.
        print('Took: ', time.time() - start)

        solution_path = solution_node.get_moves_to_solution()

        # Handling the backslashes in order to run cross platform.
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
        sys.exit()


if __name__ == '__main__':
    main()
