import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        combinations = [(2, "abc"), (3, "def"), (4, "ghi"), (5, "jkl"), (6, "mno"),
                       (7, "pqrs"), (8, "tuv"), (9, "wxyz")]
        combs = []
        for i in range (len(digits)):
            temp = []
            for (a,b) in combinations:
                if int(digits[i]) == a:
                    for letter in b:
                        temp.append(letter)
            combs.append(temp)
        
        if len(combs) == 1:
            return combs[0]
        
        products = list(itertools.product(*combs))
        items = []
        for item in products:
            items.append(list(item))
            
        final = []
        
        for l in items:
            word = ''.join(l)
            final.append(word)
            
        return final
