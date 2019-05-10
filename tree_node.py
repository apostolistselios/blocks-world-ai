import copy


class TreeNode(object):
    """ Implements a TreeNode class used in the search algorithms."""

    def __init__(self, state, parent, move, h, g, f):
        self.state = state
        self.parent = parent
        self.move = move
        self.h = h
        self.g = g
        self.f = f
        self.children = []

    def find_children(self, method, goal):
        """ Finds the children of a TreeNode object. If the child
        has been already visited is not added to the object's children list.

        params: visited_nodes
        """
        moves = self.find_possible_moves()
        for state in moves:
            g = self.g + 1
            if method == 'astar':
                h = self.heuristic_1(state, goal)
                f = h + g
                self.children.append(
                    TreeNode(state[0], self, state[1], h=h, g=g, f=h))
            elif method == 'best':
                h = self.heuristic_1(state, goal)
                self.children.append(
                    TreeNode(state[0], self, state[1], h=h, g=g, f=h))
            else:
                self.children.append(
                    TreeNode(state[0], self, state[1], h=0, g=g, f=0))

    def find_possible_moves(self):
        """Finds and returns the possible moves in the current state."""

        clear_blocks = {key: value for key,
                        value in self.state.items() if value['CLEAR']}

        moves = []
        for block, value in clear_blocks.items():
            if value['ON'] != -1:
                # Move a clear Block on table.
                on = value['ON']
                temp_state = self.clear_on_table(block, on)
                moves.append(temp_state)

                for block_ in clear_blocks:
                    if block != block_:
                        # Move a clear Block on a clear Block.
                        temp_state = self.clear_on_clear(block, block_)
                        moves.append(temp_state)

            elif value['ONTABLE']:
                # Move a Block on table on a clear Block.
                for block_ in clear_blocks:
                    if block != block_:
                        temp_state = self.table_on_clear(block, block_)
                        moves.append(temp_state)

        del clear_blocks
        return moves

    def clear_on_table(self, block, on):
        """ Move a clear block on table. """

        copy_blocks = {key: self.state[key].copy() for key in self.state}

        copy_blocks[block]['ONTABLE'] = 1
        copy_blocks[block]['ON'] = -1
        copy_blocks[on]['CLEAR'] = 1
        move = (block, on, 'table')

        return copy_blocks, move

    def table_on_clear(self, block, block_):
        """Moves a block on table on a clear block."""

        copy_blocks = {key: self.state[key].copy() for key in self.state}

        copy_blocks[block]['ONTABLE'] = 0
        copy_blocks[block]['ON'] = block_
        copy_blocks[block_]['CLEAR'] = 0
        move = (block, 'table', block_)

        return copy_blocks, move

    def clear_on_clear(self, block, block_):
        """Moves a clear block on a clear block."""

        copy_blocks = {key: self.state[key].copy() for key in self.state}

        below_block = copy_blocks[block]['ON']

        copy_blocks[block]['ON'] = block_
        copy_blocks[below_block]['CLEAR'] = 1
        copy_blocks[block_]['CLEAR'] = 0
        move = (block, below_block, block_)

        return copy_blocks, move

    def heuristic_1(self, state, goal):
        """Score the nodes depending on how many blocks are on their goal position."""
        score = 0

        for block in self.state:
            if not self.state[block] == goal[block]:
                score += 1

        return score

    def is_goal(self, goal):
        """Checks if the currents state is equal to the goal."""
        return self.state == goal

    def get_moves_to_solution(self):
        """Returns a list with the moves you have to make in order to reach the solution."""

        temp_node = copy.copy(self)
        path = []
        while temp_node.parent is not None:
            if temp_node.move is not None:
                path.append(temp_node.move)
            temp_node = temp_node.parent

        return path

    def __repr__(self):
        """ Representation of TreeNode object. """

        return f'{self.state},G={self.g}'

    def __lt__(self, other):
        """ Larger than operation of TreeNode object. """

        return self.f < other.f

    def __eq__(self, other):
        """ Equal operation on TreeNode object. """

        if other is not None:
            return self.state == other.state


if __name__ == '__main__':
    pass
