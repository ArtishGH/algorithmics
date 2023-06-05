from collections import defaultdict

def create_bus_lines(n, roads):
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    bus_lines = []

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, line):
        visited[node] = True
        line.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, line)

    for city in range(1, n + 1):
        if not visited[city]:
            bus_line = []
            dfs(city, bus_line)

            if bus_line[0] in graph[bus_line[-1]]:
                idx = bus_line.index(bus_line[0], 1)
                bus_line = bus_line[:idx]

            bus_lines.append(bus_line)

    return bus_lines

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

lines = create_bus_lines(n, roads)

#output
print(len(lines))
for line in lines:
    print(len(line), *line)

# nie wiem czy kod jest dokończony, ale nie mam już siły na to patrzeć