'''
Write a method to sort an array of strings so that all the anagrams are next to each other.
'''


def sort_anagram(a):
    return sorted(a, key=lambda n: ''.join(sorted(n)))


if __name__ == '__main__':
    a = ['abc', 'cba', 'aa', 'db', 'bd', 'anagram', 'gramana', 'the', 'het']
    print(sort_anagram(a))
