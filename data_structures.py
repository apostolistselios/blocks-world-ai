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
        # print('tree.world', self.world)
        children = self.world.get_possible_moves()
        # print(children)
        for world in children:
            node = TreeNode(world=world, parent=self)
            # print('check with parents:', node.check_with_parents())
            if not node.check_with_parents():
                self.children.append(node)

        for child in self.children:
            child.g += 1

    def check_with_parents(self):
        parent = copy.copy(self.parent)
        while parent != None:
            if parent.world.are_worlds_equal(self.world):
                return True

            parent = parent.parent

        return False

    def route_to_root(self):
        temp_node = copy.copy(self)
        solution_length = self.g
        print('Printing solution')

        while temp_node.parent != None:
            print(temp_node.world)
            temp_node = temp_node.parent

    def __repr__(self):
        return f'{self.world}'


class ListNode(object):
    def __init__(self, tree_node, next):
        self.tree_node = tree_node
        self.next = next


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_front(self, tree_node):
        new_node = ListNode(tree_node, self.head)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node

    def add_node_back(self, tree_node):
        new_node = ListNode(tree_node, None)

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.tree_node)

            current_node = current_node.next


if __name__ == '__main__':
    pass
