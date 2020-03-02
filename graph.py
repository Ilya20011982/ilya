class Graph:
    def __init__(self):
        self.data = {}

    def __repr__(self):
        return 'Graph: ' + str(self.data)

    def add_node(self, value):
        self.data[value] = set()

    def add_vertex(self, parent, child):
        if parent not in self.data:
            self.add_node(parent)
        if child not in self.data:
            self.add_node(child)
        self.data[parent].add(child)

    def all_children(self, node):
        res = set()
        new = self.data[node]
        while new.difference(res):
            res.update(new)
            prev = new
            new = set()
            for new_node in prev:
                new.update(self.data[new_node])
        return res


exceptions = Graph()
with open('Stepic/Python Основы и применение/212.txt') as f:
    for i in range(int(f.readline())):
        child, *parents = f.readline().split()
        exceptions.add_node(child)
        if len(parents) > 0:
            parents.pop(0)
        for parent in parents:
            exceptions.add_vertex(parent, child)


print(exceptions)
print(exceptions.all_children('ArithmeticError'))
