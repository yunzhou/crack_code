def get_ice_cream_flavor(m, n, a):
    print(a)
    complement_dict = {}
    for i, x in enumerate(a):
        comple = m - x
        if comple in complement_dict:
            return (i + 1, complement_dict[comple])
        else:
            complement_dict[x] = i + 1


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = get_ice_cream_flavor(m, n, a)
    print("{} {}".format(result[0], result[1]))