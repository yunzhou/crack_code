'''
You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
public static void merge(int[] a, int[] b, int n, int m) {
2 int k = m + n - 1; // Index of last location of array b
3 int i = n - 1; // Index of last element in array b
4 int j = m - 1; // Index of last element in array a
5
6 // Start comparing from the last element and merge a and b
7 while (i >= 0 && j >= 0) {
8 if (a[i] > b[j]) {
9 a[k--] = a[i--];
10 } else {
11 a[k--] = b[j--];
12 }
13 }
14 while (j >= 0) {
15 a[k--] = b[j--];
16 }
17 }
'''


def merge_two_sort_array(a, b, na, nb):
    k = na + nb - 1
    i = na - 1
    j = nb - 1
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[k] = a[i]
        else:
            a[k] = b[j]
        k -= 1
        j -= 1
    while j >= 0:
        a[k] = b[j]
        k -= 1
        j -= 1
