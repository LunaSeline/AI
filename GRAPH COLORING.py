def graph_colouring(graph, colours):
    n = len(graph)
    colouring = [-1] * n
    for i in range(n):
        available_colours = [True] * n
        for j in graph[i]:
            if colouring[j] != -1:
                available_colours[colouring[j]] = False
        for j in range(n):
            if available_colours[j]:
                colouring[i] = j
                break
    return colouring

if __name__ == "__main__":
    
    # Input from user
    graph = []
    
    n = int(input("Number of vertices: "))
    for i in range(n):
        graph.append(list(map(int, input("Vertices adjacent to vertex " + str(i) + ": ").split())))
    colours = list(map(str, input("Enter Colors: ").split()))
    
    # Function call
    colouring = graph_colouring(graph, colours)
    print("COLORING OF THE GRAPH:", colouring)