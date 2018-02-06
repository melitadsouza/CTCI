def uniqueCharacters(s):
    
    if len(s) == 0:
        return
    chars = set()
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
            
    return True

#No data structures used. Complexity - O(nlogn) because the string is sorted first.

def uniqueCharacters2(s):
    s = sorted(s)
    if len(s) == 0:
        return
    strlength = len(s)
    for i in range(strlength-1):
        if s[i]==s[i+1]:
            return False
    return True

#No data structres used. Complexity - O(n^2)

def uniqueCharacters3(s):
   
    if len(s) == 0:
        return
    strlength = len(s)
    for i in range(strlength-1):
        for j in range(i+1,strlength-1):
            if s[i] == s[j]:
                return False
    return True
