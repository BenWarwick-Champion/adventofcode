# Advent of Code
# Day 16

import sys
import math

def hex_to_bin(hex_str):
  return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


class Packet:
  def __init__(self, version: int, type: int, literal: str = '', subpackets: list = []):
    self.version = version
    self.type = type
    self.literal = literal
    self.subpackets = subpackets or []
  def eval(self) -> int:
    if self.type == 0:
      return sum(sub.eval() for sub in self.subpackets)
    elif self.type == 1:
      return math.prod(sub.eval() for sub in self.subpackets)
    elif self.type == 2:
      return min(sub.eval() for sub in self.subpackets)
    elif self.type == 3:
      return max(sub.eval() for sub in self.subpackets)
    elif self.type == 4:
      return int(self.literal, 2)
    elif self.type == 5:
      return int(self.subpackets[0].eval() > self.subpackets[1].eval())
    elif self.type == 6:
      return int(self.subpackets[0].eval() < self.subpackets[1].eval())
    elif self.type == 7:
      return int(self.subpackets[0].eval() == self.subpackets[1].eval())
    return sys.maxsize

  def sum_versions(self) -> int:
    return sum([self.version, *(sub.sum_versions() for sub in self.subpackets)])
    
  @staticmethod
  def parse(bits: str):
    version, bits = int(bits[:3], 2), bits[3:]
    type_id, bits = int(bits[:3], 2), bits[3:]
    if type_id == 4:

      literal = ''
      while bits[0] != '0':
        literal, bits = literal + bits[1:5], bits[5:]
      literal, bits = literal + bits[1:5], bits[5:]

      return Packet(version, type_id, literal, subpackets=[]), bits

    subpackets = []
    length_type_id, bits = bits[0], bits[1:]
    if length_type_id == '0':
      total_length, bits = int(bits[:15], 2), bits[15:]

      orig_length = len(bits)
      while (orig_length - len(bits)) < total_length:
        subpacket, bits = Packet.parse(bits)
        subpackets.append(subpacket)

      return Packet(version, type_id, subpackets=subpackets), bits

    count, bits = int(bits[:11], 2), bits[11:]
    for _ in range(count):
      subpacket, bits = Packet.parse(bits)
      subpackets.append(subpacket)

    return Packet(version, type_id, subpackets=subpackets), bits

if __name__ == '__main__':
  with open('input/day16.txt', 'r') as f:
    data = f.read().strip()

  packet = hex_to_bin(data)
  print('---- Part One ----')
  print(Packet.parse(packet)[0].sum_versions())
  print('---- Part Two ----')
  print(Packet.parse(packet)[0].eval())
