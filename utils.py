import re
import argparse

BREADTH = 0
DEPTH = 1
BEST = 2
ASTAR = 3


def parse_arguments():
    """ Returns
    """

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--input', type=str,
                        help='Name of the input file.')
    # parser.add_argument('-o', '--output', type=str,
    #                     help='Name of the output file.')
    parser.add_argument('-m', '--method', type=str,
                        help='Searching method: 1)depth = depth first search, 2) breadth = breadth first search, 3)best = best first search, astar = astar algorithm')

    args = parser.parse_args()

    return args.input, args.method


def load_problem(input=r'.\problems\probBLOCKS-4-0.pddl.txt'):
    data = []
    with open(input, 'r') as file:
        raw_data = file.readlines()

        for line in raw_data:
            data.append(line.strip('\n').replace(' ', '-'))

    return data


def get_initial_state(data):
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
    flag = False
    goal_state = []

    for line in data:
        if re.match(r'\A\(:goal', line) or flag:
            flag = True
            for match in re.findall(r'ON-\w{1}-\w{1}', line):
                goal_state.append(match)

    return goal_state


def get_objects_from_file(data):
    for i, line in enumerate(data):
        if re.match(r'\A\(:object', line):
            match = re.search(r'(?<=\(:objects)-(\w-)+', data[i])
            break

    return [block for block in match.group() if block != '-']


if __name__ == '__main__':
    pass
