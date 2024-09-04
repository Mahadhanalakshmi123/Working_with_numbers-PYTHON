def minimum_refueling_stops(X, fuel_levels):
    fuel_levels.sort(reverse=True)
    refuel_count = 0
    for i in range(len(fuel_levels)):
        refuel_count += fuel_levels[i] < X
        fuel_levels[i] = max(fuel_levels[i], X)
        if i < len(fuel_levels) - 1:
            fuel_levels[i + 1] += fuel_levels[i] - X
    return refuel_count

X = 10
N = 5
fuel_levels = [3, 5, 7, 8, 9]
print(minimum_refueling_stops(X, fuel_levels))