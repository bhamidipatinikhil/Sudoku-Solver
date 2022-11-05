from SudokuSolver2 import *
import random

class ImpossibleGeneration(Exception):
    # def __init__(self, msg):
    #     super.__init__(msg)
    pass


class SudokuGenerator:
    def __init__(self):
        self.ss = SudokuSolver()
        self.digits = [(i+1) for i in range(9)]
        pass

    def generate_simple_block(self, arr, st_r, st_c):
        l = list(range(1, 10))
        random.shuffle(l)
        k = 0
        for i in range(3):
            for j in range(3):
                arr[st_r+i][st_c+j] = l[k]
                k+=1

    def sets_generator(self, arr, st_r, st_c):
        lsetr = [set() for i in range(3)]
        lsetc = [set() for i in range(3)]
        setb = set()

        for j in range(3):
            for i in range(9):
                num = arr[st_r][i]
                if(num!=0):
                    lsetr[j].add(num)
        for j in range(3):
            for i in range(9):
                num = arr[j][st_c]
                if(num!=0):
                    lsetc[j].add(num)
        for i in range(3):
            for j in range(3):
                num = arr[st_r+i][st_c+j]
                if(num!= 0):
                    setb.add(num)
        
        return lsetr, lsetc, setb

    def generate_complex_block(self, arr, st_r, st_c):
        
        lsetr, lsetc, setb = self.sets_generator(arr, st_r, st_c)

        for i in range(3): 
            for j in range(3):
                candidates = [n for n in self.digits if ((n not in lsetr[i]) and (n not in lsetc[j]) and (n not in setb))]
                if(len(candidates)==0):
                    raise ImpossibleGeneration
                random.shuffle(candidates)
                chosen = candidates[0]

                arr[st_r+i][st_c+j] = chosen
                self.ss.print_terminal(arr)
                lsetr[i].add(chosen)
                lsetc[j].add(chosen)
                setb.add(chosen)
                

    def generate_sudoku(self):
        arr = [[0 for i in range(9)] for j in range(9)]

        self.generate_simple_block(arr, 0, 0)
        self.generate_simple_block(arr, 3, 3)
        self.generate_simple_block(arr, 6, 6)
        self.ss.print_terminal(arr)

        st_rows = [0, 0, 3, 3, 6, 6]
        st_cols = [3, 6, 0, 6, 0, 3]

        for i, j in zip(st_rows, st_cols):
            self.generate_complex_block(arr, i, j)
        
        return arr


if __name__=="__main__":
    try:
        ss = SudokuSolver()
        sg = SudokuGenerator()
        arr = sg.generate_sudoku()
        ss.print_terminal(arr)
        # ss.print_solutions(ss.solve_bab(sg.generate_sudoku()))
    except ImpossibleGeneration as e:
        print("Generation impossible")
