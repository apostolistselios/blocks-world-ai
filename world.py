import re
import copy
from block import Block


class World(object):
    def __init__(self, blocks, goal_state, initial_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.blocks = blocks

    def __repr__(self):
        return repr(self.blocks)

    def get_block_index(self, id):
        for i, block in enumerate(self.blocks):
            if id == block.id:
                return i

    def initialize_blocks(self, state, blocks):
        for state in state:
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
            if block.on_block != None:
                # Move a clear Block on table.
                copy_blocks = [copy.copy(block) for block in self.blocks]

                pos1 = self.get_block_index(block.id)
                pos2 = self.get_block_index(block.on_block)

                copy_blocks[pos1].on_table = True
                copy_blocks[pos1].on_block = None
                copy_blocks[pos2].clear = True

                temp_world = World(copy_blocks, self.goal_state)
                moves.append(temp_world)

                for block_ in clear:
                    if block_.id != block.id:
                        # Move a clear Block on a clear Block.
                        copy_blocks = [copy.copy(block)
                                       for block in self.blocks]

                        pos1 = self.get_block_index(block.id)
                        pos2 = self.get_block_index(block.on_block)
                        pos3 = self.get_block_index(block_.id)

                        copy_blocks[pos1].on_block = block_.id
                        copy_blocks[pos2].clear = True
                        copy_blocks[pos3].clear = False

                        temp_world = World(copy_blocks, self.goal_state)
                        moves.append(temp_world)

            elif block.on_table:
                # Move a Block on table on a clear Block.
                for block_ in clear:
                    if block_.id != block.id:
                        copy_blocks = [copy.copy(block)
                                       for block in self.blocks]

                        pos1 = self.get_block_index(block.id)
                        pos2 = self.get_block_index(block_.id)

                        copy_blocks[pos1].on_table = False
                        copy_blocks[pos1].on_block = block_.id
                        copy_blocks[pos2].clear = False

                        temp_world = World(copy_blocks, self.goal_state)
                        moves.append(temp_world)

        return moves

    def are_worlds_equal(self, world):
        for block in self.blocks:
            for block_ in world.blocks:
                if block.id == block_.id:
                    if not (block.clear == block_.clear and block.on_table == block_.on_table and block.on_block == block_.on_block):
                        return False

        return True

    def is_world_the_goal(self):
        copy_blocks = [copy.copy(block) for block in self.blocks]
        goal_state_blocks = self.initialize_blocks(
            self.goal_state, copy_blocks)

        temp_world = World(goal_state_blocks, self.goal_state)

        if self.are_worlds_equal(temp_world):
            return True

        del temp_world
        return False


if __name__ == '__main__':
    pass
