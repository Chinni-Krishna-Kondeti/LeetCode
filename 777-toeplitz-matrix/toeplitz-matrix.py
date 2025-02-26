class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i=0
        j=m-1
        while i!=n:
            val = matrix[i][j]
            tempj = j+1
            tempi = i+1
            while tempj < m and tempi < n:
                if matrix[tempi][tempj] != val:
                    return False
                tempj += 1
                tempi += 1
            if j!=0:
                j -= 1
            else:
                i += 1
        return True