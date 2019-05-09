import copy


class TreeNode(object):
    """ Implements a TreeNode class used in the search algorithms."""

    def __init__(self, state, parent, h, g, f):
        self.state = state
        self.parent = parent
        self.h = h
        self.g = g
        self.f = f
        self.children = []

    def find_children(self, method):
        """ Finds the children of a TreeNode object. If the child
        has been already visited is not added to the object's children list.

        params: visited_nodes
        """
        children = self.state.get_possible_moves()
        for state in children:
            g = self.g + 1
            if method == 'astar':
                h = self.heuristic_1(state)
                f = h + g
                self.children.append(TreeNode(state, self, h=h, g=g, f=f))
                continue
            elif method == 'best':
                h = self.heuristic_1(state)
                self.children.append(TreeNode(state, self, h=h, g=g, f=h))
                continue

            self.children.append(TreeNode(state, self, h=0, g=g, f=0))

    def heuristic_1(self, state):
        """Score the nodes depending on how many blocks are on their goal position."""
        score = 0

        for block in state.i_blocks:
            if not state.i_blocks[block] == state.g_blocks[block]:
                score += 1

        return score

    def get_path_to_root(self):
        temp_node = copy.copy(self)
        path = []
        while temp_node.parent is not None:
            if temp_node.state.prev_pos is not None:
                path.append(temp_node.state.prev_pos)
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
