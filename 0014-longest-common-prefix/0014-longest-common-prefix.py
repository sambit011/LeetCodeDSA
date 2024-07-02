class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        pre = False
        s = strs[0]
        n = len(strs[1:])-1
        while s:
            i = 0
            for i, word in enumerate(strs[1:]):
                if not word.startswith(s):
                    break
                if i == n:
                    pre = True
            if pre:
                return s
            s = s[:-1]
        
        return ""