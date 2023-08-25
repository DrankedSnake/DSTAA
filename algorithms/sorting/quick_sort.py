from typing import List


def sort(sequence: List[int]) -> List[int]:
    if len(sequence) < 2:
        return sequence
    else:
        pivot = sequence[0]
        right = [item for item in sequence[1:] if item > pivot]
        left = [item for item in sequence[1:] if item <= pivot]

        return sort(left) + sort([pivot]) + sort(right)


print(sort([-100, 4, 23, 0, 345, -23, 2, 5, 8, 3]))
