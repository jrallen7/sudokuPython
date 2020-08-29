#!/usr/bin/python3

class sudokuCell:
    def __init__(self):
        self.val = None
        self.cands = set(range(1,10))

    def setValue(self, v):
        if self.val is None:
            self.val = v
            self.cands = set([v])
            retval = 1
        elif self.val == v:
            retval = 0
        else:
            raise ValueError
        return retval

    def removeCands(self, c):
        if c in self.cands:
            self.cands.remove(c)
            retval = 1
        else:
            retval = 0
        return retval

tests
    

if __name__ == '__main__':
    foo = sudokuCell()
    print(foo.cands)
    foo.setValue(4)
    print(foo.cands)

