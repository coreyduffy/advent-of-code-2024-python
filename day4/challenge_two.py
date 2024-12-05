from typing import List, Tuple


def get_wordsearch_rows() -> List[List[str]]:
    with open("day_four_input.txt") as input_file:
        return [list(row.strip()) for row in input_file.readlines()]


def is_x_mas(wordsearch_rows: List[List[str]], row_index: int, column_index: int, num_of_rows: int,
             num_of_columns: int) -> bool:
    if wordsearch_rows[row_index][column_index] != "A":
        return False

    diagonal_one = [(1, 1), (-1, -1)]
    diagonal_two = [(-1, 1), (1, -1)]

    return diagonal_is_mas(diagonal_one, wordsearch_rows, row_index, column_index, num_of_rows,
                           num_of_columns) and diagonal_is_mas(diagonal_two, wordsearch_rows, row_index, column_index,
                                                               num_of_rows, num_of_columns)


def diagonal_is_mas(diagonal_co_ords: List[Tuple[int, int]], wordsearch_rows: List[List[str]], row_index: int,
                    column_index: int, num_of_rows: int,
                    num_of_columns: int) -> bool:
    found_letter = None
    for co_ords in diagonal_co_ords:
        current_x = column_index + co_ords[0]
        current_y = row_index + co_ords[1]

        if current_x < 0 or current_x >= num_of_columns or current_y < 0 or current_y >= num_of_rows:
            return False

        letter_at_position = wordsearch_rows[current_y][current_x]
        if letter_at_position not in ["M", "S"]:
            return False

        if found_letter == "M" and letter_at_position != "S":
            return False

        if found_letter == "S" and letter_at_position != "M":
            return False

        if not found_letter:
            found_letter = letter_at_position

    return True


if __name__ == "__main__":
    wordsearch_rows: List[List[str]] = get_wordsearch_rows()
    num_of_rows: int = len(wordsearch_rows)
    num_of_columns: int = len(wordsearch_rows[0])
    num_of_x_mas_occurrences = 0
    for row_index in range(num_of_rows):
        for column_index in range(num_of_columns):
            if is_x_mas(wordsearch_rows, row_index, column_index, num_of_rows, num_of_columns):
                num_of_x_mas_occurrences += 1
    print(num_of_x_mas_occurrences)
