from typing import List


def sum(sequence: List[int]) -> int:
    result = 0

    for item in sequence:
        result += item

    return result


numbers = [1, 2, 3, 4, 5, 6, 7]

# print(sum(numbers))


def recursive_sum(sequence: List[int]) -> int:
    result = sequence[0]
    if len(sequence) > 1:
        result += recursive_sum(sequence[1:])

    return result


print(recursive_sum(numbers))
