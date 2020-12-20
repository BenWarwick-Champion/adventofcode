# Advent of Code 2020
# Day 20: Jurassic Jigsaw

import numpy as np

def check_edges(puzzle, piece):
    # Need to do some madness to extract the edges of the puzzle
    # and the piece. Then need to see if any individual edge of the piece
    # matches any bit of the puzzle edges.
    # If it matches then need to smash the piece onto the puzzle in the
    # correct orientation. 
    pass


def uid_edge(edge):
    r_edge = [x for x in reversed(edge)]
    uid = min(edge, r_edge)
    return uid


def find_edges(piece):
    edges = []
    # Top, right, bottom, left
    top_edge = piece[0]
    bottom_edge = piece[-1]
    right_edge = []
    for i in range(len(piece)):
        right_edge.append(piece[i][-1])
    left_edge = []
    for i in range(len(piece)):
        left_edge.append(piece[i][0])

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
    # 144 pieces -> 576 edges

    # Each piece:
    # '1409':
    # [['.', '#', '#', '.'],
    #  ['#', '.', '#', '#']
    #  [...]] 

    edges = {}
    for piece in pieces:
        edges[piece] = find_edges(pieces[piece])
    print("Total edges:", len(edges))

    # edges:
    # '1409':
    # [ [], [], [], [] ]
    # Assume that every edge is unique.

    # Create a unique id for every edge
    # add them all to a list of uids 
    uids = []
    for piece in edges:
        for i in range(4):
            # edge1 = edges[piece][i]
            # edge2 = [x for x in reversed(edges[piece][i])]
            # uid = min(edge1, edge2)
            uids.append(edges[piece][i]) # uid
    # 576 edges in uids

    
    # All the outside edges of the puzzle should be totally unique
    # assuming 12x12 puzzle we could assume 48 outside edges
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

    # Notes for morning Ben:
    # You can't reference against edges because edges does not contain the UIDs
    # of the edges, they're all in random orders.
    # I think that the find_edges function should be written to incorportate the UIDs
    # of the corners. 

    print(corners)
    total = 1
    for corner in corners:
        total *= int(corner)

    print("Part 1 solution:", total)
