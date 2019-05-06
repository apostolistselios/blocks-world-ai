import re
import copy
from block import Block

# IDEAS!
# Could have a var object so i dont have to copy the list every time


# def __init__(self, blocks, goal_state, initial_state=None):
#     self.blocks = blocks
#     self.initial_state = initial_state
#     self.goal_state = goal_state
#     # self.goal_state = self.initialize_blocks(goal_state, blocks)
#     # if initial_state is not None:
#     #     self.blocks = self.initialize_blocks()
#     # else:
#     #     self.blocks = blocks

# def __init__(self, objects, i_state, g_state,):
#     self.objects = objects
#     self.i_state = i_state
#     self.g_state = g_state
#     self.blocks = self.__initialize_blocks()


class World(object):
    def __init__(self, blocks, goal_state, initial_state=None):
        self.blocks = blocks
        self.initial_state = initial_state
        self.goal_state = goal_state

    def __repr__(self):
        return repr(self.blocks)

    def __eq__(self, other):
        for sblock in self.blocks:
            for oblock in other.blocks:
                if sblock.id == oblock.id:
                    if not sblock == oblock:
                        return False

        return True

    def get_block_index(self, id):
        """Takes a block id as parameter and returns the position of
        that block in the blocks list."""

        for i, block in enumerate(self.blocks):
            if id == block.id:
                return i

    def initialize_blocks(self, state, blocks):
        for state in state:
            # print(state)
            if len(state.split('-')) < 3:
                position, block_id = state.split('-')
            else:
                position, block1_id, block2_id = state.split('-')

            for block in blocks:
                if position == 'CLEAR':
                    pos = self.get_block_index(block_id)
                    blocks[pos].clear = True
                elif position == 'ONTABLE':
                    pos = self.get_block_index(block_id)
                    blocks[pos].on_table = True
                else:
                    pos1 = self.get_block_index(block1_id)
                    pos2 = self.get_block_index(block2_id)

                    blocks[pos1].on_block = blocks[pos2].id
                    blocks[pos1].on_table = False

                    if blocks[pos2].clear:
                        blocks[pos2].clear = False

        return blocks

    def get_blocks_position_array(self):
        clear = [block for block in self.blocks if block.clear]
        on_block = [block for block in self.blocks if block.on_block != None]
        on_table = [block for block in self.blocks if block.on_table]

        return clear, on_block, on_table

    def get_possible_moves(self):
        clear, on_blocks, on_table = self.get_blocks_position_array()
        moves = []

        for block in clear:
            if block.on_block is not None:
                # Move a clear Block on table.
                temp_world = self.clear_on_table(block)
                moves.append(temp_world)

                for block_ in clear:
                    if block_.id is not block.id:
                        # Move a clear Block on a clear Block.
                        temp_world = self.clear_on_clear(block, block_)
                        moves.append(temp_world)

            elif block.on_table:
                # Move a Block on table on a clear Block.
                for block_ in clear:
                    if block_.id is not block.id:
                        temp_world = self.table_on_clear(block, block_)
                        moves.append(temp_world)

        return moves

    def clear_on_table(self, block):
        """Moves a clear block on table."""

        copy_blocks = [copy.copy(block) for block in self.blocks]

        pos1 = self.get_block_index(block.id)
        pos2 = self.get_block_index(block.on_block)

        copy_blocks[pos1].on_table = True
        copy_blocks[pos1].on_block = None
        copy_blocks[pos2].clear = True

        return World(copy_blocks, self.goal_state)

    def table_on_clear(self, block, block_):
        """Moves a block on table on a clear block."""

        copy_blocks = [copy.copy(block)
                       for block in self.blocks]

        pos1 = self.get_block_index(block.id)
        pos2 = self.get_block_index(block_.id)

        copy_blocks[pos1].on_table = False
        copy_blocks[pos1].on_block = block_.id
        copy_blocks[pos2].clear = False

        return World(copy_blocks, self.goal_state)

        return World(copy_blocks, self.goal_state)

    def clear_on_clear(self, block, block_):
        """Moves a clear block on a clear block."""

        copy_blocks = [copy.copy(block)
                       for block in self.blocks]

        pos1 = self.get_block_index(block.id)
        pos2 = self.get_block_index(block.on_block)
        pos3 = self.get_block_index(block_.id)

        copy_blocks[pos1].on_block = block_.id
        copy_blocks[pos2].clear = True
        copy_blocks[pos3].clear = False

        return World(copy_blocks, self.goal_state)

    def is_world_the_goal(self):
        # Could have a var object so i dont have to copy the list every time
        copy_blocks = [copy.copy(block) for block in self.blocks]
        goal_state_blocks = self.initialize_blocks(
            self.goal_state, copy_blocks)

        temp_world = World(goal_state_blocks, self.goal_state)

        if self == temp_world:
            return True

        del temp_world
        return False


if __name__ == '__main__':
    pass
