class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.lower()
        lenS, ans = len(s), []
        def dfs(i, res=''):
            if i < lenS:
                dfs(i+1, res + s[i])
                if s[i].islower(): 
                    dfs(i+1, res + s[i].upper())
            else: 
                ans.append(res)
        dfs(0)
        return ans
