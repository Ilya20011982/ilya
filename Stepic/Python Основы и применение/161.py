import sys
sys.stdin = open('161.txt')


parents = {}


n = int(input())
for i in range(n):
    name, *other = input().split()
    if len(other) > 0:
        other.pop(0)
    parents[name] = other


# def is_linked(child, parent):
#     if parent == child:
#         return True
#     if not child in parents:
#         return False
#     else:
#         for p in parents[child]:
#             if is_linked(p, parent):
#                 return True
#     return False


def is_linked(child, parent):
    queue = [child]
    checked = {child}
    while queue:
        if parent in queue:
            return True
        for x in parents[queue.pop(0)]:
            if x not in checked:
                queue.append(x)
                checked.add(x)
    return False


children = {}
for child in parents:
    for x in parents[child]:
        if x in children:
            children[x].add(child)
        else:
            children[x] = {child}

print(parents)
print(children)
