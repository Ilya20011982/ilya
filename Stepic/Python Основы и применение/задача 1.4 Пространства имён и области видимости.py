parents = {None: ['global']}
namespace = {None: None, 'global': set()}

def create(name, var):
    if var not in parents:
        parents[var] = [name]
        namespace[name] = set()
    else:
        parents[var] += [name]
        namespace[name] = set()
def add(name, var):
    namespace[name].add(var)
def get(name, var):
    if name == None:
        return None
    if var in namespace[name]:
        return name
    else:
        for i, j in parents.items():
            if name in j:
                name = i
                break
        return get(name, var)
for i in range(int(input())):
    com, name, var = input().split()
    if com == 'create':
        create(name, var)
    if com == 'add':
        add(name, var)
    if com == 'get':
        print(get(name, var))
