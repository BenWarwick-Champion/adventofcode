# Advent of Code 2020
# Day 16: Ticket Translation


if __name__ == "__main__":
    with open("Data/day16.txt", "r") as f:
        data = f.readlines()

    rule_data = [line.strip() for line in data[:20]]
    my_ticket = [int(num) for num in data[22].split(',')]
    ticket_data = [line.strip() for line in data[25:]]
    # rule_data, my_ticket, tickets = data[:20], data[22], data[25:]

    restrictions = {}
    for line in rule_data:
        field, rules = line.split(': ')
        rules = rules.split(' or ')
        rules = [rule.split('-') for rule in rules]
        restrictions[field] = [[int(num) for num in rule] for rule in rules]
        # { 'departure location' : [[49, 920], [932, 950]] }

    tickets = []
    ticket_data = [line.split(',') for line in ticket_data]
    for line in ticket_data:
        tickets.append([int(num) for num in line])
        # [[337, 687, 607, ...], [896, 791, 715, ...], [...]]

    # Use: restrictions, my_ticket, tickets
    forbidden_numbers = set()
    lower_bound = min(restrictions[r][0][0] for r in restrictions)
    upper_bound = max(restrictions[r][1][1] for r in restrictions)
    mid_l_bound = max(restrictions[r][0][1] for r in restrictions)
    mid_u_bound = min(restrictions[r][1][0] for r in restrictions)
    for r in restrictions:
        for i in range(mid_l_bound+1, mid_u_bound-1):
            forbidden_numbers.add(i)

    invalid_values = []
    for ticket in tickets:
        for num in ticket:
            if num in forbidden_numbers or num < lower_bound or num > upper_bound:
                invalid_values.append(num)
            
    ticket_error_rate = sum(invalid_values)
    print("Part 1 solution:", ticket_error_rate) # 26009
