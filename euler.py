import graph_tools

def find_cycle(graph, v, cycle):
    for i in range(len(graph)):
        while graph[v][i]:
            graph_tools.delete_edge(graph, v, i)
            find_cycle(graph, i, cycle)
    cycle.append(v)

# void DFSEuler(int v)
# {
#   int i;

#   for(i = 0; i < n; i++)          // Przeglądamy sąsiadów
#     while(A[v][i])
#     {
#       A[v][i]--;                  // Usuwamy krawędź
#       A[i][v]--;
#       DFSEuler(i);                // Rekurencja
#     }
#   S[sptr++] = v;                  // Wierzchołek v umieszczamy na stosie
# }