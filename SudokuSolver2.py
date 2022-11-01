import copy
from collections import deque

class SudokuSolver:
    def __init__(self):
        self.digits= set("123456789")
        # self.board=self.take_input()
        

    def take_input(self):
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
                print(arr[i][j], end=" ")
            print("")
        print("")

    def print_arr(self, arr):
        
        with open("out.txt", "a") as f:
            for i in range(9):
                for j in range(9):
                    f.write(str(arr[i][j]) + " ")
                f.write("\n")
            f.write("\n")

    def solve(self, arr):
        open("out.txt", "w").close()
        q = deque()
        ans = []
        q.append(arr)
        i = 0
        j = 0
        k = 0
        while(len(q) > 0):
            tmp = q.popleft()
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
                            q.append(tmp2)
                            ans = tmp2
                            self.print_arr(tmp2)
                    k_got=True
                else:
                    k+=1
        
        return ans

        

s = SudokuSolver()

arr = s.take_input()
s.print_terminal(s.solve(arr))


        

