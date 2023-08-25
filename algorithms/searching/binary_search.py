from typing import List


numbers = [1, 3, 5, 7, 9, 12, 14, 16, 100]


def search(sequence: List[int], number: int) -> bool:
    low = 0
    height = len(sequence) - 1
    middle = 0
    iteration = 1

    while middle != height:
        middle = ((height + low) / 2).__ceil__()
        middle_number = sequence[middle]
        if middle_number == number:
            return True
        elif middle_number < number:
            low = middle
        elif middle_number > number:
            height = middle
        else:
            raise Exception("Error...")
        print(f"{iteration} iteration was made...")
        iteration += 1


print(search(numbers, 100))
