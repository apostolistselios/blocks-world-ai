from tree_node import TreeNode


def initialize_search(method, state, queue):
    root = TreeNode(state, None, 0, 0, 0)

    if method == 'astar' or method == 'best':
        queue.put((0, root))
    else:
        queue.put(root)


def search(queue, method):
    visited_set = set()

    while not queue.empty():
        if method == 'astar' or method == 'best':
            curr_f, current = queue.get()
        else:
            current = queue.get()

        # print('Curr:', current)
        if current.state.is_goal():
            return current

        if str(current.state.i_blocks) in visited_set:
            continue

        current.find_children(method)
        visited_set.add(str(current.state.i_blocks))

        for child in current.children:
            if method == 'depth' or method == 'breadth':
                queue.put(child)
            elif method == 'astar' or method == 'best':
                queue.put((child.f, child))

    return None


if __name__ == '__main__':
    pass
