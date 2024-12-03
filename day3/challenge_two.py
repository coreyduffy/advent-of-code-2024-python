import re
from typing import List

# Check for do(), mul() and don't() commands.
# mul() commands should have 2 valid numbers as parameters, e.g. mul(20, 250), mul(1, 12345)
VALID_COMMAND_REGEX = "do\(\)|mul\(\d+,\d+\)|don't\(\)"


def get_data() -> str:
    with open("day_three_input.txt") as input_file:
        return input_file.read()


def get_sum_of_products_from_mul_commands(mul_commands: List[str]) -> int:
    result = 0
    enabled = True
    for mul_command in mul_commands:
        if mul_command == "do()":
            enabled = True
        elif mul_command == "don't()":
            enabled = False
        else:
            if enabled:
                values = re.findall("\d+", mul_command)
                if len(values) != 2:
                    raise ValueError("Issue determining which values to multiply")
                product = int(values[0]) * int(values[1])
                result += product
    return result


if __name__ == "__main__":
    data = get_data()
    mul_commands = re.findall(VALID_COMMAND_REGEX, data)
    result = get_sum_of_products_from_mul_commands(mul_commands)
    print(result)
