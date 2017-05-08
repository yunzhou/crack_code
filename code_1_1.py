'''
1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
'''
def isUniqueChars(s):
    appears = [False]*256
    for c in s:
        idx = ord(c)
        if appears[idx]:
            return False
        else:
            appears[idx]=True
    return True