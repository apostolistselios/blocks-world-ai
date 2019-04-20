from tree_node import TreeNode


def initialize_search(world, queue):
    root = TreeNode(world, None)

    queue.put(root)


def search(queue, method):
    visited_nodes = []

    while not queue.empty():
        current = queue.get()

        if current.world.is_world_the_goal():
            return current

        visited_nodes.append(current)
        current.find_children(visited_nodes)

        for child in current.children:
            queue.put(child)

    return None


if __name__ == '__main__':
    pass
