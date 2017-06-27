'''
Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array.
You may assume that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
'''


def binary_search(a, x):
    start = 0
    end = len(a)

    while start <= end:
        mid = int((start + end) / 2)
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1
'''
1 public static int search(int a[], int l, int u, int x) {
2 while (l <= u) {
3 int m = (l + u) / 2;
4 if (x == a[m]) {
5 return m;
6 } else if (a[l] <= a[m]) {
7 if (x > a[m]) {
8 l = m+1;
9 } else if (x >=a [l]) {
10 u = m-1;
11 } else {
12 l = m+1;
13 }
14 }
15 else if (x < a[m]) u = m-1;
16 else if (x <= a[u]) l = m+1;
17 else u = m - 1;
18 }
19 return -1;
20 }
'''
def binary_search_var1(a, x):
    start = 0
    end = len(a)

    while start <= end:
        mid = int((start + end) / 2)
        if a[mid] == x:
            return mid
        elif a[start] <= a[mid]:
            if x > a[mid]:
                start = mid + 1
            elif x > a[start]:
                end = mid - 1
            else:
                start = mid + 1
        elif x < a[mid]:
            end = mid - 1
        elif x <= a[end]:
            start = mid+1
        else:
            end = mid - 1

