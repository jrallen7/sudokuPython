#!/usr/bin/python3

import argparse
from enum import Enum

class cellGroupType(Enum):
    ROW = 1
    COL = 2
    BOX = 3
    

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

class sudokuBoard:
    def __init__(self):
        self.cells = [sudokuCell() for foo in range(81)]
        
    def loadState(self, statestring):
        assert len(statestring) == 81
        for i,v in enumerate(statestring):
            pass
            
    def setCellValue(self,i,v):
        pass
        
    @staticmethod    
    def getCellGroupNumber(i, group):
        if group == cellGroupType.ROW:
            retval = i // 9
        elif group == cellGroupType.COL:
            retval = i % 9
        elif group == cellGroupType.BOX:
            retval = (i - (i%3))//3
        else:
            raise ValueError
        return retval
        

def runTests():
    print('run some tests here')
    foo = sudokuCell()
    print(foo.cands)
    foo.setValue(4)
    print(foo.cands)
    print()
    for i in range(81):
        print(sudokuBoard.getCellGroupNumber(i,cellGroupType.BOX), end='')
        if i%9 == 8:
            print()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve a sudoku problem')
    parser.add_argument('-t','--test', help='run some tests',action="store_true")
    args = parser.parse_args()
    
    if args.test:
        runTests()
        
    else:
        pass



