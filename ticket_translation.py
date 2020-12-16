# Advent of Code 2020
# Day 16: Ticket Translation

import copy

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

    valid_tickets = []
    for ticket in tickets:
        is_valid = True
        for num in ticket:
            if num in invalid_values:
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)

    # fields holds a list of list
    fields = []
    for i in range(len(tickets[0])):
        fields.append([ticket[i] for ticket in valid_tickets])

    # remaining restrictions
    r_res = copy.deepcopy(restrictions)
    correct_field = {}
    for f in fields:
        for r in r_res:
            l_b = r_res[r][0][0]
            mlb = r_res[r][0][1]
            mub = r_res[r][1][0]
            u_b = r_res[r][1][1]

            if all((l_b <= n <= mlb or mub <= n <= u_b) for n in f):
                correct_field.setdefault(r, []).append(fields.index(f))

    # correct_field:
    # 'departure time' : [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18]
    # 'row' : [13, 15, 17]
    # 'seat' : [13, 17]
    # 'type' : [13]

    # c_f is correct_fields but with only 1 value
    c_f = dict()
    for f1 in correct_field:
        for f2 in correct_field:
            chk = set(correct_field[f1]).difference(set(correct_field[f2]))
            if len(chk) == 1:
                c_f[f1] = chk.pop()

    # Multiply the 6 departure values together
    total = 1
    for f in c_f:
        if 'departure' in f:
            total *= my_ticket[c_f[f]]

    print("Part 2 solution:", total) # 589685618167
