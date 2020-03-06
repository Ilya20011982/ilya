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


if __name__ == '__main__':
    pass