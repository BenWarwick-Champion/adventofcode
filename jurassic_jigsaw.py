# Advent of Code 2020
# Day 20: Jurassic Jigsaw

from pprint import pprint
from copy import deepcopy

def uid_edge(edge):
    r_edge = [x for x in reversed(edge)]
    uid = min(edge, r_edge)
    return uid

def find_edges(piece, unique=False):
    edges = []
    top_edge = piece[0]
    bottom_edge = piece[-1]
    right_edge = [piece[i][-1] for i in range(len(piece))]
    left_edge = [piece[i][0] for i in range(len(piece))]

    if unique:
        edges.append(uid_edge(top_edge))
        edges.append(uid_edge(right_edge))
        edges.append(uid_edge(bottom_edge))
        edges.append(uid_edge(left_edge))
    else:
        edges.append(top_edge)
        edges.append(right_edge)
        edges.append(bottom_edge)
        edges.append(left_edge)
    return edges

def flip(piece):
    flipped = []
    for line in piece[::-1]:
        flipped.append(line)
    return flipped

def rotate_right(piece):
    l = len(piece)-1
    r = 0
    while r < l:
        c = r
        lr = l - r
        while c < lr:
            lc = l - c
            mem = piece[r][c]
            piece[r][c] = piece[lc][r]
            piece[lc][r] = piece[lr][lc]
            piece[lr][lc] = piece[c][lr]
            piece[c][lr] = mem
            c += 1
        r += 1
    return piece

def rotate_left(piece):
    l = len(piece)-1
    r = 0
    while r < l:
        c = r
        lr = l - r
        while c < lr:
            lc = l - c
            mem = piece[r][c]
            piece[r][c] = piece[c][lr]
            piece[c][lr] = piece[lr][lc]
            piece[lr][lc] = piece[lc][r]
            piece[lc][r] = mem
            c += 1
        r += 1
    return piece

def trim(piece):
    trimmed = []
    for ind, line in enumerate(piece):
        if ind == 0 or ind == len(piece)-1:
            continue
        else:
            trimmed.append(line[1:-1])
    return trimmed

def complete_row(puzzle_row:list, r_pieces:set):
    while len(puzzle_row) < 12:
        curr = puzzle_row[-1]
        r_pieces.discard(curr)
        modified = False
        curr_edges = find_edges(pieces[curr])

        for piece in r_pieces:
            if modified:
                break
            chk_edges = find_edges(pieces[piece])
            for edge in chk_edges:
                # if the right edge of the current piece is the same as the searched piece
                # add that piece to the row (in the right orientation) 
                if curr_edges[1] == edge:
                    i = chk_edges.index(edge)
                    if i == 0:
                        pieces[piece] = flip(rotate_left(pieces[piece]))
                    elif i == 1:
                        pieces[piece] = flip(rotate_left(rotate_left(pieces[piece])))
                    elif i == 2:
                        pieces[piece] = rotate_right(pieces[piece])
                    else:
                        pass
                    puzzle_row.append(piece)
                    modified = True
                    break

            for edge in chk_edges:
                r_edge = [i for i in edge[::-1]]
                if curr_edges[1] == r_edge:
                    i = chk_edges.index(edge)
                    if i == 0:
                        pieces[piece] = rotate_left(pieces[piece])
                    elif i == 1:
                        pieces[piece] = rotate_left(rotate_left(pieces[piece]))
                    elif i == 2:
                        pieces[piece] = flip(rotate_right(pieces[piece]))
                    else:
                        pieces[piece] = flip(pieces[piece])
                    puzzle_row.append(piece)
                    modified = True
                    break
    return puzzle_row, r_pieces

def find_monsters(image, monster):
    m_height = len(monster)
    m_width = len(monster[0])
    h = len(image)
    w = len(image[0])
    monsters = 0

    for r in range(h - m_height):
        for c in range(w - m_width):
            count = 0
            for i in range(m_height):
                for j in range(m_width):
                    if monster[i][j] == image[r+i][c+j]:
                        count += 1
            if count == 15:
                monsters += 1
    return monsters


if __name__ == "__main__":
    with open("Data/day20.txt", "r") as f:
        data = [l.strip() for l in f.readlines()]

    pieces = {}
    for ind, line in enumerate(data):
        if 'Tile' in line:
            pieces[line[5:-1]] = [list(l) for l in data[ind+1:ind+11]]
    edges = {}
    unique_edges = {}
    for piece in pieces:
        edges[piece] = find_edges(pieces[piece])
        unique_edges[piece] = find_edges(pieces[piece], True)

    # Create a list of uids for every edge
    uids = []
    for piece in unique_edges:
        for i in range(4):
            uids.append(unique_edges[piece][i]) # uid
    
    # 12x12 expects 48 outside edges with no match
    outside_edges = []
    for uid in uids:
        if uids.count(uid) == 1:
            outside_edges.append(uid)
    print("Outside edges:", len(outside_edges))

    # Corner pieces have two outside edges
    corners = []
    d_corners = {}
    for piece in unique_edges:
        count = 0
        count = sum([1 for edge in outside_edges if edge in unique_edges[piece]])
        if count > 1:
            corners.append(piece)
            d_corners[piece] = [edge for edge in outside_edges if edge in unique_edges[piece]]

    print(corners) # '1283', '1511', '1619', '1901'
    total = 1
    for corner in corners:
        total *= int(corner)
    print("Part 1 solution:", total)

    r_pieces = set(pieces.keys()) # deepcopy(pieces)
    top_left_id = '1283'
    top_left = flip(rotate_left(pieces[top_left_id])) # get this by looking at the data
    pieces[top_left_id] = top_left
    initial_row = [top_left_id] # Just start with a top-left corner
    
    # Complete the first row
    puzzle_row, r_pieces = complete_row(initial_row, r_pieces)

    # Transpose the first row to the first column 
    # then use those pieces to complete each row
    puzzle = []
    for id in puzzle_row[::-1]:
        pieces[id] = rotate_left(pieces[id])
        row, r_pieces = complete_row([id], r_pieces)
        puzzle.append(row)

    # Time to assemble the image
    image = [['0']*96 for _ in range(96)] # 96 because 12 pieces * size(8) sub_images
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            sub_image = trim(pieces[puzzle[r][c]])
            for i in range(len(sub_image)):
                for j in range(len(sub_image[0])):
                    image[(r*8)+i][(c*8)+j] = sub_image[i][j]
    
    # Search the image for sea monsters
    # Assume the monsters don't overlap
    sea_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()[1:]

    monster = [list(line) for line in sea_monster]
    rough_sea = sum(sum(1 for c in r if c == '#') for r in image)
    monster_count = 0
    loops = 0
    while monster_count == 0:
        if loops == 4:
            image = flip(image)
        image = rotate_right(image)
        monster_count = find_monsters(image, monster)
        loops += 1

    part2 = rough_sea - monster_count*15
    print("Part 2 solution:", part2)
