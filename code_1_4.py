def anagram1(s,t):
    return sorted(s)==sorted(t)

def anagram2(s,t):
    if len(s)<>len(t):
        return False
    appears = [0]*256
    for c in s:
        appears[ord(c)]+=1
    for c in t:
        appears[ord(c)]-=1
        if appears[ord(c)]<0:
            return False # Found more of char c in t than in s.
    for i in appears:
        if i<>0:
            return False
    return True