# Woidyla family tree

import graphviz

woidyla = graphviz.Digraph("Woidylas", filename="woidyla_tree.gv")

woidyla.edge("Walter","Leslie")
woidyla.edge("Mary","Leslie")
woidyla.edge("Walter","Wendell")
woidyla.edge("Mary","Wendell")
woidyla.edge("Walter","Crystal")
woidyla.edge("Gloria","Crystal")
woidyla.edge("Walter","Suzann")
woidyla.edge("Gloria","Suzann")
woidyla.edge("Walter","Barbara")
woidyla.edge("Gloria","Barbara")
woidyla.edge("Walter","April")
woidyla.edge("Gloria","April")
woidyla.edge("Walter","Star")
woidyla.edge("Gloria","Star")
woidyla.edge("Crystal","Kasper")
woidyla.edge("Kevin","Kasper")
woidyla.edge("Crystal","Emilia")
woidyla.edge("Kevin","Emilia")
woidyla.edge("Leslie","Jesse")
woidyla.edge("Ron","Jesse")
woidyla.edge("Leslie","Dillon")
woidyla.edge("Ron","Dillon")
woidyla.edge("Jesse","Gavin")
woidyla.edge("Jesse","Addie")
woidyla.edge("Rachel","Gavin")
woidyla.edge("Rachel","Addie")
woidyla.edge("Wendell","Conrad")
woidyla.edge("Sheue","Conrad")
woidyla.edge("Wendell","Elle")
woidyla.edge("Rowena","Elle")

with woidyla.subgraph(name='cluster_0') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Wendell')
    c.node('Rowena')
    c.attr(label='Married')

with woidyla.subgraph(name='cluster_1') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Leslie')
    c.node('Don')
    c.attr(label='Married')

with woidyla.subgraph(name='cluster_2') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Jesse')
    c.node('Rachel')
    c.attr(label='Married')

with woidyla.subgraph(name='cluster_3') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Dillon')
    c.node('Cara')
    c.attr(label='Married')

with woidyla.subgraph(name='cluster_4') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Walter')
    c.node('Gloria')
    c.attr(label='Married')

with woidyla.subgraph(name='cluster_5') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.node('Kevin')
    c.node('Crystal')
    c.attr(label='Married')

woidyla.view()