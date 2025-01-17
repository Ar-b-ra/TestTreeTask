class TreeStore:
    def __init__(self, items: list):
        self._item_types = {}
        self._parent_to_children = {"root": []}
        self._children_to_parent = {}
        self.__prepare_graph(items)

    def __prepare_graph(self, items):
        for item in items:
            self.add_item(item)

    def get_all(self) -> list:
        return [self.get_item(node_id) for node_id in self._children_to_parent]

    def get_item(self, node_id) -> dict | None:
        if node_id not in self._children_to_parent:
            return None
        result = {
            "id": node_id,
            "parent": self._children_to_parent[node_id],
        }
        if node_id in self._item_types:
            result["type"] = self._item_types[node_id]
        return result

    def add_item(self, new_item):
        self._parent_to_children.setdefault(new_item["parent"], [])
        self._parent_to_children[new_item["parent"]].append(new_item["id"])
        self._parent_to_children[new_item["id"]] = []
        self._children_to_parent[new_item["id"]] = new_item.get(
            "parent", "root"
        )  # Сохраняется порядок добавления
        if "type" in new_item:
            self._item_types[new_item["id"]] = new_item["type"]

    def get_children(self, node_id) -> list:
        return [
            self.get_item(child_id)
            for child_id in self._parent_to_children.get(node_id, [])
        ]

    def get_all_parents(self, node_id) -> list:
        result = []
        cur_node_id = node_id
        while (parent := self._children_to_parent.get(cur_node_id)) not in (
            "root",
            None,
        ):
            result.append(self.get_item(parent))
            cur_node_id = parent
        return result
