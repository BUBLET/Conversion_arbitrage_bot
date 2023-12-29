from math import log, exp


def find_negative_cycle(graph, distance, predecessor, src, curr_list):
    tot = 1.0
    v = src
    u = predecessor[src]
    visited = set([src])

    # Поиск отрицательного цикла и вычисление общего веса
    while u not in visited:
        print(curr_list[v], "-->", curr_list[u], exp(-graph[u][v]))
        tot *= exp(-graph[u][v])
        visited.add(u)
        v = u
        u = predecessor[u]
    tot *= exp(-graph[src][v])
    print(curr_list[v], "-->", curr_list[src], exp(-graph[u][v]))
    print("Total:", tot)
    print()

    # Если общий вес меньше 1, выводим сообщение об отсутствии арбитражных возможностей
    if tot < 1.0:
        print("No Arbitrage opportunities")


def bellman_ford(graph, edge_list, src, V):
    distance = [float("inf") for _ in range(V)]
    predecessor = [-1 for _ in range(V)]

    distance[src] = 0

    # Алгоритм Беллмана-Форда для поиска кратчайших путей
    for _ in range(V - 1):
        for edge in edge_list:
            u, v, weight = edge
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Проверка наличия отрицательного цикла
    for edge in edge_list:
        u, v, weight = edge
        if distance[u] + weight < distance[v]:
            distance[v] = distance[u] + weight
            predecessor[v] = u

    return distance, predecessor


def create_graph(no_of_vertices):
    try:
        with open('graph_edges.txt', 'r') as edges:
            graph = [[0 for _ in range(no_of_vertices)] for _ in range(no_of_vertices)]
            for x in range(no_of_vertices):
                graph[x][x] = 1
            edge_list = []
            for line in edges:
                x = line.split(' ')
                u = int(x[0])
                v = int(x[1])
                edge_list.append([u, v, -log(float(x[2].strip('\n')))])
                graph[u][v] = -log(float(x[2].strip('\n')))
        return graph, edge_list
    except FileNotFoundError:
        print("Error: File 'graph_edges.txt' not found.")
        return None, None
    except ValueError:
        print("Error: Invalid data format in 'graph_edges.txt'.")
        return None, None


def main():
    # Чтение списка валют из файла
    try:
        with open('currency_list.txt', 'r') as f:
            curr_list = f.read().splitlines()
    except FileNotFoundError:
        print("Error: File 'currency_list.txt' not found.")
        return

    print(curr_list)
    no_of_vertices = len(curr_list)
    graph, edge_list = create_graph(no_of_vertices)
    if graph is None or edge_list is None:
        return

    # Выполняем алгоритм для каждой валюты
    for currency in curr_list:
        src = curr_list.index(currency)
        dist, pred = bellman_ford(graph, edge_list, src, no_of_vertices)
        find_negative_cycle(graph, dist, pred, src, curr_list)


if __name__ == '__main__':
    main()