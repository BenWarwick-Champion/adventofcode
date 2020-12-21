# Advent of Code 2020
# Day 21: Allergen Assessment


if __name__ == "__main__":
    with open("Data/day21.txt", "r") as f:
        foods = [line.strip() for line in f.readlines()]

    all_allergens = set()
    all_ingredients = set()
    all_ing = []
    d = {}
    for line in foods:
        ingredients, allergens = line.split('(contains ')
        allergens = allergens.strip(')').split(', ')
        ingredients = ingredients.split()
        [all_allergens.add(a) for a in allergens]
        [all_ingredients.add(i) for i in ingredients]
        all_ing.extend(ingredients)
        for allergen in allergens:
            if allergen not in d:
                d[allergen] = set(ingredients)
            else:
                # intersection_update
                d[allergen] &= set(ingredients)

    identified = set()
    while not all([False for allergen in d if len(d[allergen]) != 1]):
        for allergen in d:
            if len(d[allergen]) == 1:
                identified |= d[allergen]
            else:
                d[allergen] -= identified

    bad_ingredients = []
    for ing in d.values():
        bad_ingredients.extend(list(ing))

    allergenic_ingredients = 0
    for ing in all_ing:
        if ing in bad_ingredients:
            allergenic_ingredients += 1

    total_allergy_free = len(all_ing) - allergenic_ingredients

    print("Number of unique allergens:", len(all_allergens))
    print("Number of unique ingredients:", len(all_ingredients))
    print("Total number of ingredients:", len(all_ing))
    
    print("Part 1 solution:", total_allergy_free)

    ordered_keys = []
    for key in d.keys():
        ordered_keys.append(key)
    ordered_keys.sort()

    cdil = []
    for key in ordered_keys:
        cdil.extend(list(d[key]))

    print("Part 2 solution:", ",".join(cdil))