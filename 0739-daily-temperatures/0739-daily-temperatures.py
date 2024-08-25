class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []
        answer = [0]*len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                popped = stk.pop()
                answer[popped[1]] = i - popped[1]
            
            stk.append((temp, i))
         
        return answer
        