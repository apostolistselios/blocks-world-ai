from data_structures import TreeNode, DoubleLinkedList


def initialize_search(world, list):
    root = TreeNode(world, None)
    # print('Root:', root)
    #root.h = heuristic(root.world)

    list.add_node_front(root)
    # print('list.head:', list.head.tree_node)


def search(list):
    step = 0
    while list.head != None:
        current = list.head
        print('Current:', current)

        if current.tree_node.world.is_world_the_goal():
            print(step)
            return current.tree_node

        temp_node = list.head
        list.head = list.head.next
        del temp_node

        if list.head == None:
            list.tail == None

        current.tree_node.find_children()

        for child in current.tree_node.children:
            if child != []:
                list.add_node_front(child)

        step += 1

    return None


if __name__ == '__main__':
    pass
