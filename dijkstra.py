from dataclasses import dataclass
import typing
import math
import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

# Following description and example from
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

@dataclass
class Vertex:
    label: int
    distance: float = math.inf
    adjacent_vertices: typing.Optional[typing.List['Vertex']] = None
    edges: typing.Optional[typing.List['Edge']] = None

@dataclass
class Edge:
    start: Vertex
    end: Vertex
    weight: float


def get_test_data() -> typing.Tuple[typing.List[Vertex], typing.List[Edge]]:
    """ Get the vertices and edges for the graph below
          8    7
        1 -- 2 -- 3
     /4 |    |2\   |  \9
    0   |11/ 8  \4 |14  4
     \8 | /7 |6  \ |  /10
        7 -- 6 -- 5 
           1    2
    """
    vertices = []
    for i in range(9):
        vertices.append(Vertex(i))
    edges = []
    # This is a directed graph. Do we duplicate edges
    # or always check start & end? if we want it undirected?
    # assigning edges clockwise from 0
    edges.append(Edge(vertices[0], vertices[1], 4))
    edges.append(Edge(vertices[1], vertices[2], 8))
    edges.append(Edge(vertices[2], vertices[3], 7))
    edges.append(Edge(vertices[3], vertices[4], 9))
    edges.append(Edge(vertices[4], vertices[5], 10))
    edges.append(Edge(vertices[5], vertices[6], 2))
    edges.append(Edge(vertices[6], vertices[7], 1))
    edges.append(Edge(vertices[7], vertices[0], 8))
    # diagonals
    edges.append(Edge(vertices[1], vertices[7], 11))
    edges.append(Edge(vertices[7], vertices[8], 7))
    edges.append(Edge(vertices[2], vertices[8], 2))
    edges.append(Edge(vertices[2], vertices[5], 4))
    edges.append(Edge(vertices[3], vertices[5], 14))
    edges.append(Edge(vertices[8], vertices[6], 6))
    edges.append(Edge(vertices[8], vertices[6], 6))

    return vertices, edges


def get_shortest_paths(vertices, edges, starting_point) -> typing.List[Vertex]:
    """
    Implementation of Dijkstra's algorithm
    """
    shortest_path_set = []
    starting_point.distance = 0
    while vertices:
        log.info("Main loop: %d vertices to process", len(vertices))
        # Storing this in a heap would be more efficient
        next_vertex = sorted(vertices, key=lambda v: v.distance)[0]
        for edge in edges:
            # TODO: store in hashset index by vertex
            if edge.start == next_vertex:
                if (next_vertex.distance + edge.weight) < edge.end.distance:
                    edge.end.distance = next_vertex.distance + edge.weight            
            if edge.end == next_vertex:
                if (next_vertex.distance + edge.weight) < edge.start.distance:
                    edge.start.distance = next_vertex.distance + edge.weight
        shortest_path_set.append(next_vertex)
        vertices.pop(next_vertex)

    return shortest_path_set

def print_shortest_paths(shortest_paths, starting_point):
    log.info("Shortest path lengths from vertex %d" % starting_point.label)
    for path in shortest_paths:

if __name__ == '__main__':
    vertices, edges = get_test_data()
    shortest_paths = get_shortest_paths(vertices, edges, vertices[0])
    print_shortest_paths(shortest_paths, vertices[0])
