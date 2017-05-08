#Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (i.e., "waterbottle" is a rotation of "erbottlewat").
def is_rotation(s1,s2):
    if len(s1)<>len(s2):
        return False
    return s2 in (s1+s1)
if __name__ == '__main__':
    print(is_rotation("waterbottle", "erbotdtlewat"))