from typing import List


# works but should be rewriten to be able get shortedst way instead of finish value calculated with shortest way
def find_lowest_costs(costs: dict, processed: List[str]):
    low_value, low_key = (
        float("inf"),
        None,
    )

    for key, value in costs.items():
        if value < low_value and key not in processed:
            low_value = value
            low_key = key

    return low_key


def search(costs: dict, graph: dict, parents: dict):
    processed = []
    node = find_lowest_costs(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_costs(costs, processed)


costs = {"a": 6, "b": 2, "finish": float("inf")}

parents = {
    "a": "start",
    "b": "start",
    "start": None,
}

graph = {
    "start": {"a": 6, "b": 2},
    "a": {"finish": 1},
    "b": {"a": 3, "finish": 5},
    "finish": {},
}

search(costs, graph, parents)
