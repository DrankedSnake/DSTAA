from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node
    right: Node

    def to_puml(self) -> str:
        repr = ""
        repr += f"object {self.value}\n"

        if self.left:
            repr += f"{self.value}-down-> {self.left.value}\n"
            repr += f"{self.left.to_puml()}"
        if self.right:
            repr += f"{self.value}-down-> {self.right.value}\n"
            repr += f"{self.right.to_puml()}"
        
        return repr
