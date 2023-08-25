# from tree.binary_search_tree.binary_search_tree_on_recursion.tree import Tree
from tree import Tree

if __name__ == "__main__":
    tree = Tree()
    # for item in range(1, 10):
    #     tree.add_node(item)
    tree.add_node(10)
    tree.add_node(5)
    tree.add_node(4)
    tree.add_node(6)
    tree.add_node(8)
    tree.add_node(12)
    tree.add_node(20)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(19)
    tree.add_node(11)
    tree.add_node(21)
    tree.add_node(9)
    tree.add_node(1)
    tree.to_puml()
    # print(tree.search(9))
