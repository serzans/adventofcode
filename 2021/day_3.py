from typing import List
import copy

# Part I
with open("../2021/inputs/day_3.txt") as f:
    report_lines: List[str] = f.readlines()
    report_length = len(report_lines)
    num_bits:int = len(report_lines[0]) - 1

    average_report: List[int] = [0]*num_bits

    for report_line in report_lines:
        for i, bit in enumerate(report_line):
            if bit in "01":
                average_report[i] += int(bit)

    gamma_rate: int = int("0b" + "".join(["1" if a / report_length >= 0.5 else "0" for a in average_report]),2)
    epsilon_rate:int = int("0b" + "".join(["0" if a / report_length >= 0.5 else "1" for a in average_report]),2)

    print(gamma_rate*epsilon_rate)


# Part II
with open("../2021/inputs/day_3.txt") as f:
    oxygen_report_lines: List[str] = f.readlines()
    co2_report_lines: List[str] = copy.deepcopy(oxygen_report_lines)

    oxygen_report_length = len(oxygen_report_lines)
    co2_report_length = len(co2_report_lines)

    num_bits:int = len(oxygen_report_lines[0]) - 1

    average_oxygen_report: List[int] = [0]*num_bits
    average_co2_report: List[int] = [0]*num_bits

    for pos in range(num_bits):
        for report_line in oxygen_report_lines:
            average_oxygen_report[pos] += int(report_line[pos])
        average_oxygen_report[pos] = int((average_oxygen_report[pos] / oxygen_report_length) >= 0.5)

        oxygen_report_lines = list(filter(lambda x: int(x[pos]) == average_oxygen_report[pos], oxygen_report_lines))
        oxygen_report_length = len(oxygen_report_lines)

        if oxygen_report_length == 1:
            break

    oxygen_generator_rating = int("0b" + oxygen_report_lines[0],2)


    for pos in range(num_bits):
        for report_line in co2_report_lines:
            average_co2_report[pos] += int(report_line[pos])
        average_co2_report[pos] = int((average_co2_report[pos] / co2_report_length) < 0.5)

        co2_report_lines = list(filter(lambda x: int(x[pos]) == average_co2_report[pos], co2_report_lines))
        co2_report_length = len(co2_report_lines)

        if co2_report_length == 1:
            break

    co2_scrubber_rating = int("0b" + co2_report_lines[0],2)


    print(oxygen_generator_rating*co2_scrubber_rating)