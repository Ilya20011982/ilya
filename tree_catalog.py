import os
import Graph


def my_catalog(arg):
    catalog.add_node(arg)
    if not os.path.isdir(arg):
        return
    else:
        for j in os.listdir(arg):
            catalog.add_vertex(arg, j)
            my_catalog(j)


catalog = Graph.Graph()
catalog.add_node(os.getcwd())
my_catalog(os.getcwd())

print(catalog)







