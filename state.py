import re
import copy


class WorldState(object):
    def __init__(self, i_blocks, g_blocks, prev_pos):
        self.i_blocks = i_blocks
        self.g_blocks = g_blocks
        self.prev_pos = prev_pos

    def get_possible_moves(self):
        clear_blocks = {key: value for key,
                        value in self.i_blocks.items() if value['CLEAR']}

        moves = []

        for block, value in clear_blocks.items():
            if value['ON'] != -1:
                # Move a clear Block on table.
                on = value['ON']
                temp_state = self.clear_on_table(block, on)
                moves.append(temp_state)

                for block_ in clear_blocks:
                    if block != block_:
                        # Move a clear Block on a clear Block.
                        temp_state = self.clear_on_clear(block, block_)
                        moves.append(temp_state)

            elif value['ONTABLE']:
                # Move a Block on table on a clear Block.
                for block_ in clear_blocks:
                    if block != block_:
                        temp_state = self.table_on_clear(block, block_)
                        moves.append(temp_state)

        return moves

    def clear_on_table(self, block, on):
        """ Move a clear block on table. """

        copy_blocks = {key: self.i_blocks[key].copy() for key in self.i_blocks}

        copy_blocks[block]['ONTABLE'] = 1
        copy_blocks[block]['ON'] = -1
        copy_blocks[on]['CLEAR'] = 1

        prev_pos = (block, on, 'table')
        return WorldState(copy_blocks, self.g_blocks, prev_pos)

    def table_on_clear(self, block, block_):
        """Moves a block on table on a clear block."""

        copy_blocks = {key: self.i_blocks[key].copy() for key in self.i_blocks}

        copy_blocks[block]['ONTABLE'] = 0
        copy_blocks[block]['ON'] = block_
        copy_blocks[block_]['CLEAR'] = 0

        prev_pos = (block, 'table', block_)
        return WorldState(copy_blocks, self.g_blocks, prev_pos)

    def clear_on_clear(self, block, block_):
        """Moves a clear block on a clear block."""

        copy_blocks = {key: self.i_blocks[key].copy() for key in self.i_blocks}

        below_block = copy_blocks[block]['ON']

        copy_blocks[block]['ON'] = block_
        copy_blocks[below_block]['CLEAR'] = 1
        copy_blocks[block_]['CLEAR'] = 0

        prev_pos = (block, below_block, block_)
        return WorldState(copy_blocks, self.g_blocks, prev_pos)

    def is_goal(self):
        return self.i_blocks == self.g_blocks

    def __repr__(self):
        return str(self.i_blocks)

    def __eq__(self, other):
        return self.i_blocks == other.i_blocks


if __name__ == '__main__':
    pass
