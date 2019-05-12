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
                h = self.heuristic(state[0], goal)
                f = h + g
                self.children.append(
                    TreeNode(state[0], self, state[1], h=h, g=g, f=f))
            elif method == 'best':
                h = self.heuristic(state[0], goal)
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
        copy_blocks[on]['UNDER'] = -1
        move = (block, on, 'table')

        return copy_blocks, move

    def table_on_clear(self, block, block_):
        """Moves a block on table on a clear block."""

        copy_blocks = {key: self.state[key].copy() for key in self.state}

        copy_blocks[block]['ONTABLE'] = 0
        copy_blocks[block]['ON'] = block_
        copy_blocks[block_]['UNDER'] = block
        copy_blocks[block_]['CLEAR'] = 0
        move = (block, 'table', block_)

        return copy_blocks, move

    def clear_on_clear(self, block, block_):
        """Moves a clear block on a clear block."""

        copy_blocks = {key: self.state[key].copy() for key in self.state}

        below_block = copy_blocks[block]['ON']

        copy_blocks[block]['ON'] = block_
        copy_blocks[below_block]['CLEAR'] = 1
        copy_blocks[below_block]['UNDER'] = -1
        copy_blocks[block_]['UNDER'] = block
        copy_blocks[block_]['CLEAR'] = 0
        move = (block, below_block, block_)

        return copy_blocks, move

    def heuristic(self, state, goal):
        """Score the nodes depending on how many blocks are on their goal position."""
        score = 0

        for block in state:
            if not state[block] == goal[block]:
                score += 1

            on = state[block]['ON']
            if on != -1:
                if state[on] != goal[on]:
                    score += 1

        return score

    # # IN PROGRESS
    # def heuristic_1(self, state, goal):
    #     """Score the nodes depending on how many blocks are on their goal position."""
    #     score = 0
    #     one_move = 0
    #     two_moves = 0
    #
    #     for block in state:
    #         # if not state[block] == goal[block]:
    #         #     score += 1
    #
    #         if state[block]['ONTABLE'] == 0 and goal[block]['ONTABLE'] == 1:
    #             # If the block is not on table and it should be.
    #             if not state[block]['CLEAR']:
    #                 # If the block is not clear it takes at least two moves to get ontable.
    #                 two_moves += 1
    #             else:
    #                 # If the block is clear it takes one moves to get ontable.
    #                 one_move += 1
    #         elif state[block]['ONTABLE'] == 1 and goal[block]['ONTABLE'] == 0:
    #             # If the block is on table but it shouldnt be.
    #             if not state[block]['CLEAR']:
    #                 # If the block is not clear it takes at least two moves to get on block it should be.
    #                 two_moves += 1
    #
    #                 goal_on = goal[block]['ON']
    #                 if not state[goal_on]['CLEAR']:
    #                     # If the block it should be on is not clear it takes at least two moves to get there.
    #                     two_moves += 1
    #
    #                 if state[block]['ON'] == goal[block]['ON']:
    #                     pass
    #
    #         if not state[block]['ON'] == goal[block]['ON']:
    #             # If its not on the block it should be.
    #             if state[block]['UNDER'] != -1 and state[block]['UNDER'] == -1:
    #                 score += 2
    #             else:
    #                 goal_on = goal[block]['ON']
    #                 if goal_on != -1:
    #                     if goal[goal_on]['UNDER'] != -1:
    #                         score += 2
    #                     else:
    #                         score += 1
    #         else:
    #             on = state[block]['ON']
    #             if on != -1 and not state[on]['ON'] == goal[on]['ON']:
    #                 # If the block that is on is not on the correct block.
    #                 score += 2
    #             elif on == -1 and not goal[block]['ONTABLE']:
    #                 score += 2
    #
    #     return score
    #
    # def heuristic_2(self, state, goal):
    #     score = 0
    #     one_move = 0
    #     two_moves = 0
    #
    #     for block in state:
    #         if not state[block] == goal[block]:
    #             # UNDER
    #             if not state[block]['UNDER'] == goal[block]['UNDER']:
    #                 under = state[block]['UNDER']
    #                 if under != -1:
    #                     # If the block is not under the block it should be.
    #                     if not state[under]['ON'] == goal[under]['ON']:
    #                         # If the block that is under is not on the block it should be.
    #                         score += 2
    #
    #                     under2 = state[under]['UNDER']
    #                     if under2 != -1:
    #                         if not state[under2]['ON'] == goal[under2]['ON']:
    #                             score += 4
    #
    #             elif state[block]['UNDER'] != -1:
    #                 # If the block is under the block it should be.
    #                 under = state[block]['UNDER']
    #                 if not state[under]['ON'] == goal[under]['ON']:
    #                     # If the block that is under is not on the block it should be.
    #                     score += 2
    #
    #                 under2 = state[under]['UNDER']
    #                 if under2 != -1:
    #                     if not state[under2]['ON'] == goal[under2]['ON']:
    #                         score += 4
    #
    #             # ON
    #             if not state[block]['ON'] == goal[block]['ON']:
    #                 on = state[block]['ON']
    #                 if on != -1:
    #                     if not state[on]['UNDER'] == goal[on]['UNDER']:
    #                         score += 2
    #
    #                     on2 = state[on]['ON']
    #                     if on2 != -1:
    #                         if not state[on2]['UNDER'] == goal[on2]['UNDER']:
    #                             score += 4
    #
    #             elif state[block]['ON'] != -1:
    #                 on = state[block]['ON']
    #                 if not state[on]['UNDER'] == goal[on]['UNDER']:
    #                     score += 2
    #
    #                 on2 = state[on]['ON']
    #                 if on2 != -1:
    #                     if not state[on2]['UNDER'] == goal[on2]['UNDER']:
    #                         score += 4
    #
    #     return score
    #
    # def heuristic_3(self, state, goal):
    #     score = 0
    #     one_move = 0
    #     two_moves = 0
    #
    #     for block in state:
    #         if not state[block] == goal[block]:
    #             flag = False
    #             if not state[block]['ON'] == goal[block]['ON']:
    #                 # If its not on the block it should be.
    #                 one_move += 1
    #             else:
    #                 on = state[block]['ON']
    #                 if on != -1 and not state[on]['ON'] == goal[block]['ON']:
    #                     flag = True
    #                     # If the block that is on is not on the correct block.
    #                     two_moves += 1
    #
    #             # if not flag:
    #             if not state[block]['UNDER'] == goal[block]['UNDER']:
    #                 if state[block]['UNDER'] != -1:
    #                     # If the block is not under the block it should be.
    #                     under = state[block]['UNDER']
    #                     if not state[under]['ON'] == goal[under]['ON']:
    #                         # If the block that is under is not on the block it should be.
    #                         score += 2
    #             elif state[block]['UNDER'] != -1:
    #                 # If the block is under the block it should be.
    #                 under = state[block]['UNDER']
    #                 if not state[under]['ON'] == goal[under]['ON']:
    #                     # If the block that is under is not on the block it should be.
    #                     score += 2
    #
    #     score = score + one_move * 2 + two_moves * 4
    #     return score

    def is_goal(self, goal):
        """Checks if the currents state is equal to the goal."""
        return self.state == goal

    def get_moves_to_solution(self):
        """Returns a list with the moves you have to make in order to reach the solution."""

        temp_node = copy.copy(self)
        path = []
        while temp_node.parent is not None:
            if temp_node.move is not None:
                path.append((temp_node.move, temp_node.h))
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
