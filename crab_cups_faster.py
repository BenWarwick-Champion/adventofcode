# Advent of Code 2020
# Day 23: Crab Cups (...but faster)

class Cup:
    def __init__(self, label) -> None:
        self.label = label
        self.next = None

    def __repr__(self) -> str:
        return f"Cup number: {self.label}"

class CrabGame:
    def __init__(self, cup_num, move_num, part2=False) -> None:
        self.cup_num = cup_num
        self.move_num = move_num
        self.cups = []
        self.lookup = dict()
        self.current = Cup(0)
        self.part2 = part2

    def init_cups(self) -> None:
        with open("Data/day23.txt", "r") as f:
            self.cups = [int(num) for num in list(f.readline().strip())]
        if self.part2:
            self.cups.extend(range(max(self.cups) + 1, self.cup_num + 1))

    def init_lookup(self) -> None:
        for i in range(1, self.cup_num + 1):
            self.lookup[i] = Cup(i)
        for i, _ in enumerate(self.cups):
            self.lookup[self.cups[i]].next = self.lookup[self.cups[(i+1)%len(self.cups)]]
        self.current = self.lookup[self.cups[0]]

    def play_game(self) -> None:
        for i in range(1, self.move_num + 1):
            select = self.current.next
            self.current.next = self.current.next.next.next.next # this is horrific

            dest = self.current.label
            while dest in [self.current.label, select.label, select.next.label, select.next.next.label]:
                if dest - 1 > 0:
                    dest = dest - 1
                else:
                    dest = self.cup_num

            next_cup = self.lookup[dest]
            select.next.next.next = next_cup.next
            next_cup.next = select
            self.current = self.current.next

    def print_result(self) -> None:
        if self.part2:
            result = self.lookup[1].next.label * self.lookup[1].next.next.label
            print(f"Part 2 solution: {result}")
        else:
            result = ''
            curr = self.lookup[1]
            for _ in self.lookup:
                result += str(curr.label)
                curr = curr.next
            a, b = result.split('1')
            print(f"Part 1 solution: {b + a}")


if __name__ == "__main__":
    part1 = CrabGame(9, 100)
    part1.init_cups()
    part1.init_lookup()
    part1.play_game()
    part1.print_result() # Part 1 solution: 47382659
    part2 = CrabGame(1_000_000, 10_000_000, part2=True)
    part2.init_cups()
    part2.init_lookup()
    part2.play_game()
    part2.print_result() # Part 2 solution: 42271866720
