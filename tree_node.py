import copy


class TreeNode(object):
    """ Implements a TreeNode class used in the search algorithms."""

    def __init__(self, world, parent):
        self.world = world
        self.parent = parent
        self.h = 0
        self.g = 0
        self.f = 0
        self.children = []

    def __repr__(self):
        """ Representation of TreeNode object. """

        return f'W:{self.world}, G:{self.g}'

    def __eq__(self, other):
        """ Equal operation on TreeNode object. """

        if other != None:
            return self.world == other.world

    def find_children(self, visited_nodes):
        """ Finds the children of a TreeNode object. If the child
        has been already visited is not added to the object's children list.

        params: visited_nodes
        """

        children = self.world.get_possible_moves()

        for world in children:
            node = TreeNode(world=world, parent=self)

            if not node in visited_nodes:
                self.children.append(node)

        for child in self.children:
            child.g = child.parent.g + 1

    def heuristic_1(self):
        """Score the nodes depending on how many blocks are on their goal position."""

        pass

    def route_to_root(self):
        temp_node = copy.copy(self)
        solution_length = self.g
        print('Printing solution')

        while temp_node.parent is not None:
            print(temp_node.world)
            temp_node = temp_node.parent


if __name__ == '__main__':
    pass
