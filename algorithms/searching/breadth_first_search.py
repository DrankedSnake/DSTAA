from collections import deque


ernest = {"product": "avocado", "friends": []}

samanta = {"product": "coal", "friends": [ernest]}
jane = {"product": "coal", "friends": [ernest]}
bob = {"product": "coal", "friends": [ernest]}

james = {"product": "coal", "friends": [samanta]}
marta = {"product": "cooper", "friends": [jane]}
john = {"product": "iron", "friends": [bob]}

me = {"friends": deque([james, marta, john, ernest])}


def find_mango_seller(sequence: deque):
    """
    Breadth first search of avocado seller with time complexity O(!n)
    """
    while sequence:
        person = sequence.popleft()

        if person["product"] == "avocado":
            return person
        else:
            sequence += person["friends"]


print(find_mango_seller(me["friends"]))
