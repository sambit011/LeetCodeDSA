class Solution:
    def romanToInt(self, s: str) -> int:
        #s = s[1:-1]
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        map2 = {'IV':-2, 'IX':-2, 'XL':-20, 'XC':-20,'CD':-200,'CM':-200}
        num = 0
        for i in range(len(s)):
            num+=map[s[i]]
            if i > 0 and s[i-1:i+1] in map2:
                num+=map2[s[i-1:i+1]]
        
        return num