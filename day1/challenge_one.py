import csv
from typing import List

list_one: List[int] = []
list_two: List[int] = []


def read_input_lists() -> None:
    with open("day_one_input.csv") as input_file:
        input_reader = csv.reader(input_file, delimiter=' ', skipinitialspace=True)
        for row in input_reader:
            list_one.append(int(row[0]))
            list_two.append(int(row[1]))


def calculate_difference_between_lists() -> int:
    difference_between_lists: int = 0
    for x, value in enumerate(list_one):
        value_one: int = list_one[x]
        value_two: int = list_two[x]
        if value_one > value_two:
            difference_between_lists += value_one - value_two
        elif value_two > value_one:
            difference_between_lists += value_two - value_one
    return difference_between_lists


if __name__ == "__main__":
    read_input_lists()
    list_one.sort()
    list_two.sort()
    difference_between_lists: int = calculate_difference_between_lists()
    print(difference_between_lists)
