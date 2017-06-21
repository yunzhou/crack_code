'''
9.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1
'''


def search(strings, s, first, last):
    while first <= last:
        while (first <= last and strings[last] == ""):
            last -= 1
        if (last < first):
            return -1
        mid = (last + first) >> 1
        while strings[mid] == "":
            mid += 1
        if strings[mid] == s:
            return mid
        elif strings[mid] < s:
            first = mid + 1
        else:
            last = mid - 1
    return -1
