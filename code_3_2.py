content = []
min_content = []
def push(x):
    content.append(x)
    if len(content) == 0:
        min_content.append(x)
    elif x <= get_min():
        min_content.append(x)


def pop():
    v = content.pop()
    if v == get_min():
        min_content.pop()
    return v


def get_min():
    if len(min_content) == 0:
        return None
    else:
        return min_content[-1]
