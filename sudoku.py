#!/usr/bin/python3

class sudokuCell:
    def __init__(self):
        self.val = None
        self.cands = set(range(1,10))

    def setValue(self, v):
        assert v in self.cands
        self.val = v
        self.cands = set([v])

    def removeCands(self, c):
        pass




if __name__ == '__main__':
    foo = sudokuCell()
    print(foo.cands)
    foo.setValue(4)
    print(foo.cands)

