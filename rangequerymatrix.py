class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.empty = False
        self.length = len(matrix)
        self.bredth = None
        if self.length == 0 or self.length == 1 and self.bredth == 0:
            self.empty = True
        elif self.length == 1 and len(matrix[0]) == 0:
            self.empty = True
        else:
            self.bredth = len(matrix[0])
        self.opt = None
        if not self.empty:
            self.opt = [[0]*(1+self.bredth) for _ in range(0, self.length+1)]
            for i in range(1, self.length+1):
                for j in range(1, self.bredth+1):
                    self.opt[i][j] = self.opt[i-1][j]+self.opt[i][j-1]-self.opt[i-1][j-1]+matrix[i-1][j-1]
        # for o in self.opt:
        #     print(o)



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.empty:
            return 0
        return self.opt[row2+1][col2+1] - self.opt[row2+1][col1] - self.opt[row1][col2+1] + self.opt[row1][col1]

matrix = [[]]
obj = NumMatrix(matrix)
print(obj.sumRegion(0,0,0,0))