from tree_node import TreeNode
from utils import BREADTH, DEPTH, BEST, ASTAR


def initialize_search(world, queue):
    root = TreeNode(world, None)

    queue.put(root)


def search(queue, method):
    while not queue.empty():
        current = queue.get()

        if current.world.is_world_the_goal():
            return current

        current.find_children()

        for child in current.children:
            queue.put(child)

    return None


if __name__ == '__main__':
    pass
