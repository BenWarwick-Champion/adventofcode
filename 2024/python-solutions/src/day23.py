# Advent of Code 2023
# Day 23

from collections import defaultdict
from itertools import combinations
import networkx as nx

def parse(raw_data):
    G = nx.Graph()
    connections = raw_data.split('\n')
    conns = defaultdict(list)
    for connection in connections:
        a, b = connection.split('-')
        conns[a].append(b)
        conns[b].append(a)
        G.add_edge(a, b)
    return conns, G

def part_one(raw_data):
    conns, _ = parse(raw_data)
    triples = set()
    for triple in combinations(conns.keys(), 3):
        a, b, c = triple
        if a[0] != 't' and b[0] != 't' and c[0] != 't':
            continue
        if b in conns[a] and c in conns[b] and a in conns[c]:
            triples.add(triple)
    return len(triples)

def part_two(raw_data):
    _, G = parse(raw_data)
    max_clique = max(nx.find_cliques(G), key=len)
    return ','.join(sorted(max_clique))

if __name__ == "__main__":
    with open("input/day23.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 1215

    print('---- Part Two ----')
    print(part_two(raw_data)) # bm,by,dv,ep,ia,ja,jb,ks,lv,ol,oy,uz,yt
