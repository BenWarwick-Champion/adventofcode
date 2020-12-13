# Advent of Code 2020
# Day 13: Shuttle Search

if __name__ == "__main__":
    with open("Data/day13.txt", "r") as f:
        timestamp = int(f.readline())
        data = f.readline()

    bus_data = data.split(',')
    buses = [int(num) for num in bus_data if num != 'x']

    bus_id, time = 0, 0
    min_wait = min(buses)
    for i in range(min(buses)):
        for bus in buses:
            wait = (timestamp + i) % bus
            if wait < min_wait:
                min_wait = wait
                time = i
                bus_id = bus

    print("Part 1 solution:", time * bus_id)

    e_timestamp = 0
    bus_list = []
    [bus_list.append([ind, int(num)]) for ind, num in enumerate(bus_data) if num != 'x']

    # bus_list:
    # [[0, 41], [35, 37], [41, 659], [49, 23], [54, 13], [60, 19], [70, 29], [72, 937], [89, 17]]
    # x % 41 = 0
    # x % 37 = 35
    # x % 659 = 41
    # etc 

    mod = 1
    for bus in bus_list:
        while (e_timestamp + bus[0]) % bus[1] != 0:
            e_timestamp += mod
        mod *= bus[1]

    # 756261495958122
    print("Part 2 solution:", e_timestamp)
    