import copy
from collections import deque

class SudokuSolver:
    def __init__(self):
        self.digits= set("123456789")
        # self.board=self.take_input()
        

    def take_input(self):
        print("Please print the question below:: ")
        ans = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            line = input()
            for j, ch in enumerate(line):
                if ch in self.digits:
                    ans[i][j] = int(ch)
                else:
                    ans[i][j] = 0

        
        return ans

    def is_row_safe(self, i, arr):
        d = {}
        for n in arr[i]:
            d[n] = d.get(n, 0) + 1
        
        for k in d.keys():
            if(k!=0 and d[k] > 1):
                return False
        
        return True

    def is_column_safe(self, i, arr):
        d = {}
        
        for j in range(9):
            d[arr[j][i]] = d.get(arr[j][i], 0) + 1
        
        for k in d.keys():
            if(k!=0 and d[k] > 1):
                return False
        
        return True

    def is_box_safe(self, i, j, arr):
        rt_side = int(j/3)
        dn_side = int(i/3)

        st_col = 3*rt_side
        st_row = 3*dn_side

        nums = []
        for i in range(st_col, st_col+3):
            for j in range(st_row, st_row+3):
                nums.append(arr[j][i])
        
        d = {}
        for n in nums:
            d[n] = d.get(n, 0)+1
        
        for k in d.keys():
            if k != 0 and d[k] > 1:
                return False
        
        return True

    def is_safe(self, i, j, arr):
        return self.is_row_safe(i, arr) and self.is_column_safe(j, arr) and self.is_box_safe(i, j, arr)

    def is_completely_safe(self, arr):
        for i in range(9):
            for j in range(9):
                if not self.is_safe(i, j, arr):
                    return False
        
        return True

    def print_terminal(self, arr):
        print("")
        for i in range(9):
            for j in range(9):
                if arr[i][j] != 0:
                    print(arr[i][j], end=" ")
                else:
                    print(" ", end=" ")
                if j % 3 == 2:
                    print("|", end=" ")
            print("")
            if i % 3==2:
                print("-"*22)
            # print("")
        print("")

    def print_solutions(self, solutions):
        print(f"\nThe number of solutions is:: {len(solutions)}\nThe Solutions are::")
        for sol in solutions:
            s.print_terminal(sol)
            print("")

    def print_solutions_file(self, solutions):
        # print(f"\nThe number of solutions is:: {len(solutions)}\nThe Solutions are::")
        # for sol in solutions:
        #     s.print_terminal(sol)
        #     print("")
        pass

    def print_file(self, arr):
        
        with open("out.txt", "a") as f:
            for i in range(9):
                for j in range(9):
                    f.write(str(arr[i][j]) + " ")
                f.write("\n")
            f.write("\n")

    def solve_bab(self, arr):
        # open("out.txt", "w").close()
        q = deque()
        ans = []
        q.append(arr)
        i = 0
        j = 0
        k = 0

        last_standing = []
        while(len(q) > 0):
            tmp = q.popleft()
            # tmp = q.pop()
            k = 0
            k_got = False
            while k < 81 and (not k_got):
                i = int(k/9)
                j = k%9
                if(tmp[i][j]==0):
                    for p in range(1, 10):
                        tmp2 = copy.deepcopy(tmp)
                        tmp2[i][j] = p
                        if self.is_safe(i, j, tmp2):
                            if(k==80):
                                last_standing.append(tmp2)
                            q.append(tmp2)
                            ans = tmp2
                            # self.print_file(tmp2)
                    k_got=True
                else:
                    k+=1
        
        # for a in last_standing:
        #     self.print_terminal(a)

        return last_standing

    def solve_dfs(self, arr):
        pass
        
if __name__=="__main__":
    s = SudokuSolver()

    arr = s.take_input()
    solutions = s.solve_bab(arr)
    s.print_solutions(solutions)



        

