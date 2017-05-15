
def is_incidental(graph, v1, v2):
    return graph[v1][v2] == 1 and graph[v2][v1] == 1

def create_edge(graph, v1, v2):
    graph[v1][v2] = 1
    graph[v2][v1] = 1


def delete_edge(graph, v1, v2):
    graph[v1][v2] = 0
    graph[v2][v1] = 0

def count_edges(graph):
    edges = []

    for i in range(len(graph)):
        for w in range(len(graph)):
            if (w, i) not in edges \
                and (i, w) not in edges \
                and is_incidental(graph, i, w):

                edges.extend([(w, i), (i, w)])

    return len(edges) / 2


def count_incidental(graph, v):
    from functools import reduce
    return reduce(lambda a, b: a+b, graph[v])

def is_connected(graph):
    visited = [False for i in graph]

    s = []
    vc = 0
    s.append(0)
    visited[0] = True
    while len(s):
        v = s.pop()
        vc += 1
        for i in get_incidentals(graph, v):
            if visited[i] is False:
                visited[i] = True
                s.append(i)
    return vc == len(graph)


def is_euler_graph(graph):
    allEven = True
    for i in range(len(graph)):
        if count_incidental(graph,i) % 2:
            allEven = False
    
    return allEven and is_connected(graph)


def get_incidentals(graph, v):
    incidental = [i for i in range(len(graph)) if is_incidental(graph, v, i)]
    return incidental


def get_graphs():
    i = 10
    graphs = {}
    while i <= 15:
        graphs[i] = load_graphs("./instancje/{0}w.txt".format(i))
        i += 5
    return graphs

def load_graphs(filename):
    def prepare(x):
        x = x.replace("[", "").replace("]", "").split("\n")
        return list(map(lambda y: list(map(lambda k: int(k), filter(None, y.split(", ")))), x))

    file = open(filename, 'r')
    content = file.read()
    file.close()
    graphs = map(prepare ,content.split("\n\n\n"))
    graphs = list(graphs)[:-1]
    return graphs

def save_to_file(result, name="result.txt"):
    with open(name, "a") as file:
        file.write(result)
