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
        if re.match(r'\A\(:INIT', line) or flag:
            if re.match(r'\A\(:goal', line):
                break

            pattern = r'CLEAR-\w{1}|ONTABLE-\w{1}|ON-\w{1}-\w{1}'
            for match in re.findall(pattern, line):
                initial_state.append(match)

            flag = True

    return initial_state


def get_goal_state(data):
    """ Extracts the goal state from the data of the input file. """
    flag = False
    goal_state = []

    for line in data:
        if re.match(r'\A\(:goal', line) or flag:
            flag = True
            for match in re.findall(r'ON-\w{1}-\w{1}', line):
                goal_state.append(match)

    return goal_state


def get_objects_from_file(data):
    """ Extracts how many and which block objects the problem needs. """

    for i, line in enumerate(data):
        if re.match(r'\A\(:object', line):
            match = re.search(r'(?<=\(:objects)-(\w-)+', data[i])
            break

    return [block for block in match.group() if block != '-']


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
        for move in solution_path:
            file.write(f'move {move}\n')


if __name__ == '__main__':
    pass
