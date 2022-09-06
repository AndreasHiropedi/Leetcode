class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        
        for i in range(len(s)):
            if s[i] == '#' and stack1:
                stack1.pop()
                continue
            if s[i] != '#':
                stack1.append(s[i])
        
        for j in range(len(t)):
            if t[j] == '#' and stack2:
                stack2.pop()
                continue
            if t[j] != '#':
                stack2.append(t[j])
        
        if stack1 == stack2:
            return True
        
        return False
