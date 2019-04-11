
class Block(object):
    def __init__(self, id, clear=True, on_table=False, on_block=None):
        self.id = id
        self.clear = clear
        self.on_table = on_table
        self.on_block = on_block

    def __str__(self):
        return f'Block: {self.id}'

    def __repr__(self):
        return f'(Block {self.id}:{self.clear}, {self.on_table}, {self.on_block})'
