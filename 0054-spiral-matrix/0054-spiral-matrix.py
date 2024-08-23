class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        
        up_b = 0
        right_b = n
        down_b = m
        left_b = -1
        
        UP, RIGHT, DOWN, LEFT = 1,2,3,4
        direc = RIGHT
        answer = []
        
        while len(answer) != m*n:
            if direc == RIGHT:
                while j < right_b:
                    answer.append(matrix[i][j])
                    j += 1
                right_b -= 1
                i, j = i + 1, j - 1
                direc = DOWN
                
            elif direc == DOWN:
                while i < down_b:
                    answer.append(matrix[i][j])
                    i += 1
                down_b -= 1
                i, j = i - 1, j - 1
                direc = LEFT
            
            elif direc == LEFT:
                while j > left_b:
                    answer.append(matrix[i][j])
                    j -= 1
                left_b += 1
                i, j = i - 1, j + 1
                direc = UP
                
            elif direc == UP:
                while i > up_b:
                    answer.append(matrix[i][j])
                    i -= 1
                up_b += 1
                i, j = i + 1, j + 1
                direc = RIGHT
                
        return answer