def add_node(v):
    if v in graph:
        print(v, "Node is already present in the graph")
    else:
        graph[v] = []


def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "node is not in the graph")
    elif v2 not in graph:
        print(v2, "node is not in the graph")
    else:
        # list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(v2)
        # graph[v2].append(list2)


graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("C", "B", 5)
add_edge("C", "A", 5)


print(graph)
