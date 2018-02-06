def checkPermutation(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) != len(p):
            return False
        
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count = 1
                
        for char in p:
            if char in count:
                count[char] -= 1
            else:
                count = 1
        
        for k in count:
            if count[k] != 0:
                return False
        return True
