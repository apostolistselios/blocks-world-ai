
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

    def __eq__(self, other):
        return self.id == other.id and self.clear == other.clear and self.on_table == other.on_table and self.on_block == other.on_block


if __name__ == '__main__':
    b1 = Block('A', clear=False)
    b2 = Block('B')
    b3 = Block('A', clear=False)
    b4 = Block('C')
    b5 = Block('B')

    print(id(b2), id(b5))
    blocks = [b1, b2, b3]

    print(b5 in blocks)
