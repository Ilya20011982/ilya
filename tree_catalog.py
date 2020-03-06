import os
import Graph


def my_catalog(arg):
    if not os.path.isdir(arg):
        return catalog.add_node(arg)
    else:
        catalog[arg] = set(os.listdir(arg))
        for j in set(os.listdir(arg)):
            my_catalog(j)


catalog = Graph.Graph()
tmp = os.listdir('C:/Users/кредит/Desktop/PYTHON')

# for i in tmp:
#     my_catalog(i)
   
print(catalog, tmp)







