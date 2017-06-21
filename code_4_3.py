'''
public static TreeNode addToTree(int arr[], int start, int end){
2 if (end < start) {
3 return null;
4 }
5 int mid = (start + end) / 2;
6 TreeNode n = new TreeNode(arr[mid]);
7 n.left = addToTree(arr, start, mid - 1);
8 n.right = addToTree(arr, mid + 1, end);
9 return n;
10 }
11
12 public static TreeNode createMinimalBST(int array[]) {
13 return addToTree(array, 0, array.length - 1);
14 }
'''
def addToTree(arr, s, e):
    if e<s:
        return None
    mid = int((s+e)/2)
    n = {"value":arr[mid]}
    n["left"] = addToTree(arr,s,mid-1)
    n["right"] = addToTree(arr, mid+1, e)
    return n

if __name__ == '__main__':
    a=range(1,10)
    root = addToTree(a,0,len(a)-1)
    print(root)