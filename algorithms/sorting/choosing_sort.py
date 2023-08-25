from typing import List
from copy import copy

numbers = [100, 23, -100, 34, 56, 78, 123, -23]


def find_biggest_index(sequence: List[int]) -> int:
    biggest = sequence[0]
    biggest_index = 0

    for index in range(1, len(sequence)):
        item = sequence[index]
        if item > biggest:
            biggest_index = index
            biggest = item

    return biggest_index


def sorting(sequence: List[int]) -> List[int]:
    """O(n^2)"""
    _sequence = copy(sequence)
    sorted_sequence = []

    while _sequence:
        sorted_sequence.append(_sequence.pop(find_biggest_index(_sequence)))

    return sorted_sequence


print(sorting(numbers))
