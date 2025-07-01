import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            dist = current_dist + weight
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                heapq.heappush(heap, (dist, neighbor))

    return distance