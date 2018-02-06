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
