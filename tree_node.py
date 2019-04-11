import copy


class TreeNode(object):
    def __init__(self, world, parent):
        self.world = world
        self.parent = parent
        self.h = 0
        self.g = 0
        self.f = 0
        self.children = []

    def find_children(self):
        children = self.world.get_possible_moves()

        for world in children:
            node = TreeNode(world=world, parent=self)
            flag, equal_parent = node.check_with_parents()
            if not flag:
                self.children.append(node)

        if equal_parent in children:
            print('Equal parent in children')
            exit(1)

        for child in self.children:
            child.g = child.parent.g + 1

    def check_with_parents(self):
        parent = copy.copy(self.parent)
        while parent != None:
            if parent.world.are_worlds_equal(self.world):
                return True, parent

            parent = parent.parent

        return False, parent

    def route_to_root(self):
        temp_node = copy.copy(self)
        solution_length = self.g
        print('Printing solution')

        while temp_node.parent != None:
            print(temp_node.world)
            temp_node = temp_node.parent

    def __repr__(self):
        return f'W:{self.world}, G:{self.g}'


if __name__ == '__main__':
    pass
