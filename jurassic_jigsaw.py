# Advent of Code 2020
# Day 20: Jurassic Jigsaw

import numpy as np

def uid_edge(edge):
    r_edge = [x for x in reversed(edge)]
    uid = min(edge, r_edge)
    return uid


def find_edges(piece):
    edges = []
    top_edge = piece[0]
    bottom_edge = piece[-1]
    right_edge = [piece[i][-1] for i in range(len(piece))]
    left_edge = [piece[i][0] for i in range(len(piece))]

    edges.append(uid_edge(top_edge))
    edges.append(uid_edge(right_edge))
    edges.append(uid_edge(bottom_edge))
    edges.append(uid_edge(left_edge))
    return edges


if __name__ == "__main__":
    with open("Data/day20.txt", "r") as f:
        data = [l.strip() for l in f.readlines()]

    pieces = {}
    for ind, line in enumerate(data):
        if 'Tile' in line:
            #pieces[line[5:-1]] = np.array([list(l) for l in data[ind + 1:ind + 11]]).reshape(10, 10)
            pieces[line[5:-1]] = [list(l) for l in data[ind+1:ind+11]]

    edges = {}
    for piece in pieces:
        edges[piece] = find_edges(pieces[piece])

    # Create a unique id for every edge
    # add them all to a list of uids 
    uids = []
    for piece in edges:
        for i in range(4):
            uids.append(edges[piece][i]) # uid
    
    # All the outside edges of the puzzle should be unique
    # assuming 12x12 puzzle we expect 48 outside edges
    outside_edges = []
    for uid in uids:
        if uids.count(uid) == 1:
            outside_edges.append(uid)
    print("Outside edges:", len(outside_edges))

    corners = []
    for piece in edges:
        count = 0
        count = sum([1 for edge in outside_edges if edge in edges[piece]])
        if count > 1:
            corners.append(piece)

    print(corners)
    total = 1
    for corner in corners:
        total *= int(corner)
    print("Part 1 solution:", total)
