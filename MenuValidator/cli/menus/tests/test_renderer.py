import unittest
import menus


class TestRenderAggregateMenusJson(unittest.TestCase):
    def test_correct_params(self):
        valid_menus = [{
            'root_id': 2,
            'children': [4, 6]
        }]
        invalid_menus = [{
            'root_id': 1,
            'children': [1, 3, 5]
        }]
        result = menus.render_aggregate_menus_json(valid_menus, invalid_menus)
        expected_result = (
            '{"valid_menus": [{"root_id": 2, "children": [4, 6]}], '
            '"invalid_menus": [{"root_id": 1, "children": [1, 3, 5]}]}'
            )

        self.assertEqual(expected_result, result)

    def test_correct_empty_valid_menus(self):
        valid_menus = []
        invalid_menus = [{
            'root_id': 1,
            'children': [1, 3, 5]
        }]
        result = menus.render_aggregate_menus_json(valid_menus, invalid_menus)
        expected_result = (
            '{"valid_menus": [], '
            '"invalid_menus": [{"root_id": 1, "children": [1, 3, 5]}]}'
            )

        self.assertEqual(expected_result, result)

    def test_correct_empty_invalid_menus(self):
        valid_menus = [{
            'root_id': 2,
            'children': [4, 6]
        }]
        invalid_menus = []
        result = menus.render_aggregate_menus_json(valid_menus, invalid_menus)
        expected_result = (
            '{"valid_menus": [{"root_id": 2, "children": [4, 6]}], '
            '"invalid_menus": []}'
            )

        self.assertEqual(expected_result, result)

    def test_both_empty_menus(self):
        result = menus.render_aggregate_menus_json([], [])
        expected_result = '{"valid_menus": [], "invalid_menus": []}'

        self.assertEqual(expected_result, result)

    def test_no_menus_supplied(self):
        result = menus.render_aggregate_menus_json()
        expected_result = '{"valid_menus": [], "invalid_menus": []}'

        self.assertEqual(expected_result, result)
