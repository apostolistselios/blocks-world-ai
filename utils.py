import re
import argparse
from queue import Queue, LifoQueue, PriorityQueue

METHODS = {
    'breadth': Queue(),
    'depth': LifoQueue(),
    'best': PriorityQueue(),
    'astar': PriorityQueue()
}


def load_problem(input):
    """ Loads the problem from the input file. """

    data = []
    with open(input, 'r') as file:
        raw_data = file.readlines()

        for line in raw_data:
            data.append(line.strip('\n').replace(' ', '-'))

    return data


def get_initial_state(data):
    """ Extracts the initial state from the data of the input file. """

    flag = False
    initial_state = []

    for line in data:
        if re.match(r'\A\(:INIT', line, re.I) or flag:
            flag = True
            if re.match(r'\A\(:goal', line, re.I):
                break

            pattern = r'CLEAR-\w{1}\d?|ONTABLE-\w{1}\d?|ON-\w{1}\d?-\w{1}\d?'
            initial_state.extend(re.findall(pattern, line))

    return initial_state


def get_goal_state(data):
    """ Extracts the goal state from the data of the input file. """

    flag = False
    goal_state = []

    for line in data:
        if re.match(r'\A\(:goal', line, re.I) or flag:
            flag = True
            pattern = r'CLEAR-\w{1}\d?|ONTABLE-\w{1}\d?|ON-\w{1}\d?-\w{1}\d?'
            goal_state.extend(re.findall(pattern, line))

    return goal_state


def get_objects_from_file(data):
    """ Extracts how many and which block objects the problem needs. """
    flag = False
    objects = []
    for line in data:
        if re.match(r'\A\(:object', line, re.I) or flag:
            flag = True
            if re.match(r'\A\(:INIT', line, re.I):
                break

            objects.extend(re.findall(r'\w{1}\d?', line))

    return objects[7:]


def initialize_blocks(objects, state):
    """Initializes a dictionary with blocks based on the state passed in."""

    blocks = {id: {'CLEAR': 1, 'ON': -1, 'UNDER': -1, 'ONTABLE': 1}
              for id in objects}

    for state in state:
        if len(state.split('-')) < 3:
            position, block = state.split('-')
        else:
            position, block, on = state.split('-')

        if position == 'CLEAR':
            blocks[block][position] = 1

        elif position == 'ONTABLE':
            blocks[block][position] = 1

        else:
            blocks[on]['UNDER'] = block
            blocks[block][position] = on
            blocks[block]['ONTABLE'] = 0

            if blocks[on]['CLEAR']:
                blocks[on]['CLEAR'] = 0

    return blocks


def write_solution(file, solution_path):
    """Writes the solution to a file."""

    solution_path.reverse()
    with open(file, 'w') as file:
        for i, move in enumerate(solution_path):
            file.write(f'{i+1}. move {move}\n')


if __name__ == '__main__':
    pass
