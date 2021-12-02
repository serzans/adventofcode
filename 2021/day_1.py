from typing import List

# PART I
clean_measurement = lambda m: int(m.strip())

def rolling_sum(l: List[int], window: int) -> List[int]:
    if len(l) < window:
        return []
    return [sum(l[i-(window-1):i+1]) for i in range(window-1, len(l))]

with open("2021/inputs/day_1.txt") as f:
    raw_measurements = f.readlines()
    measurements = list(map(clean_measurement, raw_measurements))

    num_increased = 0

    for i, measurement in enumerate(measurements):
        if i > 0:
            if measurement > measurements[i-1]:
                num_increased += 1

    print(num_increased)

# PART II
with open("2021/inputs/day_1.txt") as f:
    raw_measurements = f.readlines()
    measurements = list(map(clean_measurement, raw_measurements))

    window = 3
    rolling_measurements = rolling_sum(measurements, window)
    num_increased_rolling = 0

    for i, rolling_measurement in enumerate(rolling_measurements):
        if i > 0:
            if rolling_measurement > rolling_measurements[i-1]:
                num_increased_rolling += 1

    print(num_increased_rolling)
