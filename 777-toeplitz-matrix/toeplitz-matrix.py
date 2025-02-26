class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i=0
        j=len(matrix[0])-1
        while(i!=len(matrix)):
            tempi = i
            tempj = j
            val = matrix[i][j]
            tempj += 1
            tempi += 1
            while(tempj < len(matrix[0]) and tempi < len(matrix)):
                print(tempi,tempj)
                if matrix[tempi][tempj] != val:
                    return False
                tempj += 1
                tempi += 1
            if j!=0:
                j -= 1
            else:
                i += 1
        return True