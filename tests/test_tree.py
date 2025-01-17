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
                {"id": 1, "parent": "root"},
                {"id": 2, "parent": 1, "type": "test"},
                {"id": 3, "parent": 1, "type": "test"},
                {"id": 4, "parent": 2, "type": "test"},
                {"id": 5, "parent": 2, "type": "test"},
                {"id": 6, "parent": 2, "type": "test"},
                {"id": 7, "parent": 4, "type": None},
                {"id": 8, "parent": 4, "type": None},
            ],
        )

    def test_get_existing_item(self):
        self.assertEqual(self.ts.get_item(2), {"id": 2, "parent": 1, "type": "test"})

    def test_get_non_existing_item(self):
        self.assertIsNone(self.ts.get_item(-1))

    def test_get_all_parent(self):
        expected = [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
        self.assertListEqual(self.ts.get_all_parents(7), expected)

    def test_get_children(self):
        expected = [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
        self.assertListEqual(self.ts.get_children(4), expected)
if __name__ == "__main__":
    unittest.main()