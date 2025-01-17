import unittest
from tree_store import TreeStore


class TestTreeStore(unittest.TestCase):
    def setUp(self):
        items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None},
        ]
        self.ts = TreeStore(items)

    def test_get_all(self):
        self.assertListEqual(
            self.ts.get_all(),
            [
                {"id": 1, "parent": "root", "type": None},
                {"id": 2, "parent": 1, "type": "test"},
                {"id": 3, "parent": 1, "type": "test"},
                {"id": 4, "parent": 2, "type": "test"},
                {"id": 5, "parent": 2, "type": "test"},
                {"id": 6, "parent": 2, "type": "test"},
                {"id": 7, "parent": 4, "type": None},
                {"id": 8, "parent": 4, "type": None},
            ],
        )


if __name__ == "__main__":
    unittest.main()