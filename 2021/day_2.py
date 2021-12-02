from typing import List

# Part I
with open("2021/inputs/day_2.txt") as f:
    commands: List[str] = f.readlines()

    forward_commands: List[int] = [int(c.split(" ")[1]) for c in commands if "forward" in c]
    down_commands: List[int] = [int(c.split(" ")[1]) for c in commands if "down" in c]
    up_commands: List[int] = [int(c.split(" ")[1]) for c in commands if "up" in c]

    x = sum(forward_commands)
    y = sum(down_commands) - sum(up_commands)

    print(f"X: {x}, Y: {y}")
    print(x*y)


# Part II
with open("2021/inputs/day_2.txt") as f:
    commands: List[str] = f.readlines()

    aim: int = 0
    x: int = 0
    y: int = 0

    for command in commands:
        units: int = int(command.split(" ")[1])

        if "up" in command:
            aim -= units
        elif "down" in command:
            aim += units
        elif "forward" in command:
            x += units
            y += aim * units
        else:
            pass

    print(f"X: {x}, Y: {y}")
    print(x*y)

