class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]
        for i in range(numRows - 2):
            prevRow = triangle[-1]
            nextRow = [1] * (len(prevRow) + 1)
            for i in range(1, ((len(prevRow) // 2) + 1)):
                nextRow[i], nextRow[-(i + 1)] = (
                    prevRow[i] + prevRow[i - 1],
                    prevRow[i] + prevRow[i - 1],
                )

            triangle.append(nextRow)
        
        return triangle
