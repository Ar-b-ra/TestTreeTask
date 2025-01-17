class TreeStore:
    def __init__(self, items: list):
        self._items = {}
        self._parent_to_children = {"root": []}
        self._children_to_parent = {}
        self.__prepare_graph(items)

    def __prepare_graph(self, items):
        for item in items:
            self.add_item(item)

    def get_all(self) -> list:
        return [self.get_item(node_id) for node_id in self._items]

    def get_item(self, node_id) -> dict | None:
        if node_id not in self._items:
            return None
        return {
            "id": node_id,
            "parent": self._children_to_parent[node_id],
            "type": self._items[node_id],
        }

    def add_item(self, new_item):
        self._parent_to_children.setdefault(new_item["parent"], [])
        self._parent_to_children[new_item["parent"]].append(new_item["id"])
        self._parent_to_children[new_item["id"]] = []
        self._children_to_parent[new_item["id"]] = new_item.get("parent", "root")
        self._items[new_item["id"]] = new_item.get("type")

    def get_children(self, node_id) -> list:
        return [
            self.get_item(child_id)
            for child_id in self._parent_to_children.get(node_id, [])
        ]

    def get_all_parents(self, node_id) -> list: ...
