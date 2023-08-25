from typing import List


def sort(sequence: List[int]) -> None:
    """O(n^2)"""

    for index in range(1, len(sequence)):
        current_element = sequence[index]
        previous_index = index - 1

        while previous_index >= 0 and current_element < sequence[previous_index]:
            sequence[previous_index + 1] = sequence[previous_index]
            previous_index -= 1
            sequence[previous_index + 1] = current_element


numbers = [-5, 1, -100, 34, 45, 2]

sort(numbers)
print(numbers)
