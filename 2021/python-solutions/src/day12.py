# Advent of Code 2021
# Day 12: 

from collections import defaultdict

def build_graph(paths):
  graph = defaultdict(list)
  for node1, node2 in paths:
    graph[node1] += [node2]
    graph[node2] += [node1]
  return graph

def search(graph, part, seen=set(), cave='start'):
    if cave == 'end': 
      return 1
    if cave in seen:
        if cave == 'start': 
          return 0
        if cave.islower():
            if part == 1: 
              return 0
            else: part = 1

    return sum(search(graph, part, seen|{cave}, n)for n in graph[cave])

def part1(paths):
  graph = build_graph(paths)
  return search(graph, part=1)
  
def part2(paths):
  graph = build_graph(paths)
  return search(graph, part=2)

if __name__ == "__main__":
  with open('./input/day12.txt') as f:
    paths = [path.strip().split('-') for path in f.readlines()]

  print('---- Part One ----')
  print(part1(paths))
  print('---- Part Two ----')
  print(part2(paths))
