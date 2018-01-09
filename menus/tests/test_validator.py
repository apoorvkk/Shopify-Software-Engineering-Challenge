import unittest
from unittest import mock

import menus
from menus.validator import dfs_find_products_in_menu_tree


@mock.patch('menus.validator.dfs_find_products_in_menu_tree')
class TestValidateMenus(unittest.TestCase):

    def test_calls_dfs_find_products_in_menu_tree(self, mock_dfs):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': []
            }
        }
        root_ids = [2]
        mock_dfs.return_value = ({}, True)
        menus.validate_menus(root_ids, products)
        mock_dfs.assert_called_with(2, products)

    def test_valid_menus_only(self, mock_dfs):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': []
            }
        }
        root_ids = [2]

        valid_menu = {
            'root_id': 2,
            'children': [4, 6]
        }
        mock_dfs.return_value = (valid_menu, False)
        expected_valid_menus = [{"root_id": 2, "children": [4, 6]}]
        valid_menus, invalid_menus = menus.validate_menus(root_ids, products)
        self.assertEqual(invalid_menus, [])
        self.assertEqual(valid_menus, expected_valid_menus)

    def test_invalid_menus_only(self, mock_dfs):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6, 2]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': []
            }
        }
        root_ids = [2]

        invalid_menu = {
            'root_id': 2,
            'children': [2, 4, 6]
        }
        mock_dfs.return_value = (invalid_menu, True)
        expected_valid_menus = [{"root_id": 2, "children": [2, 4, 6]}]
        valid_menus, invalid_menus = menus.validate_menus(root_ids, products)
        self.assertEqual(valid_menus, [])
        self.assertEqual(invalid_menus, expected_valid_menus)

    def test_both_valid_and_invalid_menus_only(self, mock_dfs):
        products = {
            1: {
                "id": 1,
                "data": "House",
                "child_ids": [3]
            },
            2: {
                "id": 2,
                "data": "Company",
                "child_ids": [4]
            },
            3: {
                "id": 3,
                "data": "Kitchen",
                "parent_id": 1,
                "child_ids": [5]
            },
            4: {
                "id": 4,
                "data": "Meeting Room",
                "parent_id": 2,
                "child_ids": [6]
            },
            5: {
                "id": 5,
                "data": "Sink",
                "parent_id": 3,
                "child_ids": [1]
            },
            6: {
                "id": 6,
                "data": "Chair",
                "parent_id": 4,
                "child_ids": []
            }
        }
        root_ids = [1, 2]

        returned_menus = [
            {
                'root_id': 1,
                'children': [1, 3, 5]
            },
            {
                'root_id': 2,
                'children': [4, 6]
            },
        ]
        mock_dfs.side_effect = [
            (returned_menus[0], True), (returned_menus[1], False)]
        expected_valid_menus = [{"root_id": 2, "children": [4, 6]}]
        expected_invalid_menus = [{"root_id": 1, "children": [1, 3, 5]}]
        valid_menus, invalid_menus = menus.validate_menus(root_ids, products)
        self.assertEqual(valid_menus, expected_valid_menus)
        self.assertEqual(invalid_menus, expected_invalid_menus)

    def test_invalid_root_ids(self, mock_dfs):
        mock_dfs.side_effect = KeyError
        with self.assertRaises(KeyError):
            menus.validate_menus([1, 1000], {})

    def test_no_root_ids(self, mock_dfs):
        valid_menus, invalid_menus = menus.validate_menus([], {})
        self.assertEqual(valid_menus, [])
        self.assertEqual(invalid_menus, [])


class TestDFSFindProductsInMenuTree(unittest.TestCase):
    def test_valid_tree(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': []
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [4, 6]
        }
        self.assertEqual(is_invalid_menu, False)
        self.assertEqual(menu, expected_menu)

    def test_invalid_acyclic_tree(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [8]
            },
            7: {
                'id': 7,
                'data': 'the bottom of the menu',
                        'child_ids': [8]
            },
            8: {
                'id': 8,
                'data': 'some data',
                        'parent_id': 7,
                        'child_ids': []
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [4, 8]
        }
        self.assertEqual(is_invalid_menu, True)
        self.assertEqual(menu, expected_menu)

    def test_valid_acyclic_tree_connected_to_invalid_tree(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [8]
            },
            7: {
                'id': 7,
                'data': 'the bottom of the menu',
                        'child_ids': [8]
            },
            8: {
                'id': 8,
                'data': 'some data',
                        'parent_id': 7,
                        'child_ids': []
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(7, products)

        expected_menu = {
            'root_id': 7,
            'children': [8]
        }
        self.assertEqual(is_invalid_menu, False)
        self.assertEqual(menu, expected_menu)

    def test_invalid_cyclic_tree_to_root(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': [2]
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [2, 4, 6]
        }
        self.assertEqual(is_invalid_menu, True)
        self.assertEqual(menu, expected_menu)

    def test_invalid_cyclic_tree_not_to_root(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': [4]
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [4, 6]
        }
        self.assertEqual(is_invalid_menu, True)
        self.assertEqual(menu, expected_menu)

    def test_just_valid_max_depth_tree(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': [7]
            },
            7: {
                'id': 7,
                'data': 'the bottom of the menu',
                        'parent_id': 6,
                        'child_ids': [5]
            },
            5: {
                'id': 5,
                'data': 'the bottom of the menu',
                        'parent_id': 7,
                        'child_ids': []
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [4, 6, 7, 5]
        }
        self.assertEqual(is_invalid_menu, False)
        self.assertEqual(menu, expected_menu)

    def test_invalid_max_depth_tree(self):
        products = {
            2: {
                'id': 2,
                'data': 'the top of the menu!',
                        'child_ids': [4]
            },
            4: {
                'id': 4,
                'data': 'the middle of the menu',
                        'parent_id': 2,
                        'child_ids': [6]
            },
            6: {
                'id': 6,
                'data': 'the bottom of the menu',
                        'parent_id': 4,
                        'child_ids': [7]
            },
            7: {
                'id': 7,
                'data': 'the bottom of the menu',
                        'parent_id': 6,
                        'child_ids': [5]
            },
            5: {
                'id': 5,
                'data': 'the bottom of the menu',
                        'parent_id': 7,
                        'child_ids': [10]
            },
            10: {
                'id': 10,
                'data': 'the bottom of the menu',
                        'parent_id': 5,
                        'child_ids': []
            }
        }
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(2, products)

        expected_menu = {
            'root_id': 2,
            'children': [4, 6, 7, 5, 10]
        }
        self.assertEqual(is_invalid_menu, True)
        self.assertEqual(menu, expected_menu)

    def test_invalid_root_id(self):
        with self.assertRaises(KeyError):
            dfs_find_products_in_menu_tree(2, {})
