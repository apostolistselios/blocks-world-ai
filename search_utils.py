import time
from tree_node import TreeNode


def initialize_search(method, i_blocks, queue):
    """Initializes the root of the Tree and the search queue based
    on the search method."""

    root = TreeNode(i_blocks, None, None, 0, 0, 0)

    if method == 'astar' or method == 'best':
        queue.put((0, root))
    else:
        queue.put(root)


def search(queue, method, goal):
    """Searches the tree for a solution based on the search method."""
    visited_set = set()

    start = time.time()
    while (not queue.empty()) and (time.time() - start <= 60):
        if method == 'astar' or method == 'best':
            curr_f, current = queue.get()
        else:
            current = queue.get()

        # print('Curr:', current)
        if current.is_goal(goal):
            return current

        if str(current.state) in visited_set:
            continue

        current.find_children(method, goal)
        visited_set.add(str(current.state))

        for child in current.children:
            if method == 'depth' or method == 'breadth':
                queue.put(child)
            elif method == 'astar' or method == 'best':
                queue.put((child.f, child))

    return None


if __name__ == '__main__':
    pass
