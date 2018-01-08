import unittest
from unittest import mock
from unittest.mock import Mock
import json
import requests
import menus
from menus.api_handler import construct_menus_url


class TestParseMenusData(unittest.TestCase):

    def test_valid_empty_menu_info(self):
        menus_info = {
            'menus': []
        }
        products, root_ids = menus.parse_menus_data(menus_info)

        self.assertEqual(products, {})
        self.assertEqual(root_ids, [])

    def test_valid_one_product(self):
        menus_info = {
            'menus': [
                {
                    'id': 1,
                    'data': 'Hello',
                    'child_ids': []
                }
            ]
        }

        products, root_ids = menus.parse_menus_data(menus_info)

        self.assertEqual(
            products, {1: {'id': 1, 'data': 'Hello', 'child_ids': []}})
        self.assertEqual(root_ids, [1])

    def test_valid_existing_menu_info(self):
        menus_info = {
            "menus": [
                {
                    "id": 1,
                    "data": "House",
                    "child_ids": [3]
                },
                {
                    "id": 2,
                    "data": "Company",
                    "child_ids": [4]
                },
                {
                    "id": 3,
                    "data": "Kitchen",
                    "parent_id": 1,
                    "child_ids": [5]
                },
                {
                    "id": 4,
                    "data": "Meeting Room",
                    "parent_id": 2,
                    "child_ids": [6]
                },
                {
                    "id": 5,
                    "data": "Sink",
                    "parent_id": 3,
                    "child_ids": [1]
                },
                {
                    "id": 6,
                    "data": "Chair",
                    "parent_id": 4,
                    "child_ids": []
                }
            ],
            "pagination": {
                "current_page": 1,
                "per_page": 5,
                "total": 19
            }
        }
        products, root_ids = menus.parse_menus_data(menus_info)

        self.assertEqual(products, {
            1: {'id': 1, 'data': 'House', 'child_ids': [3]},
            2: {'id': 2, 'data': 'Company', 'child_ids': [4]},
            3: {'id': 3, 'data': 'Kitchen', 'parent_id': 1, 'child_ids': [5]},
            4: {'id': 4, 'data': 'Meeting Room', 'parent_id': 2,
                'child_ids': [6]},
            5: {'id': 5, 'data': 'Sink', 'parent_id': 3, 'child_ids': [1]},
            6: {'id': 6, 'data': 'Chair', 'parent_id': 4, 'child_ids': []}})
        self.assertEqual(root_ids, [1, 2])

    def test_invalid_empty_menu_info(self):
        menus_info = {}
        with self.assertRaises(KeyError):
            products, root_ids = menus.parse_menus_data(menus_info)

    def test_no_supplied_menu_info(self):
        with self.assertRaises(KeyError):
            products, root_ids = menus.parse_menus_data()

    def test_invalid_existing_menu_info_invalid_keys(self):
        menus_info = {
            'not a menu': 'random'
        }
        with self.assertRaises(KeyError):
            products, root_ids = menus.parse_menus_data(menus_info)

    def test_invalid_existing_menu_info_invalid_object(self):
        menus_info = ['not correctly formatted object']
        with self.assertRaises(TypeError):
            products, root_ids = menus.parse_menus_data(menus_info)


@mock.patch('requests.get')
class TestFetchMenusData(unittest.TestCase):

    def setUp(self):
        self.api_menu_data = []
        for i in range(1, 6):
            file = open(f'menus/tests/test_data/many_pages_{i}.json')
            self.api_menu_data.append(json.load(file))
            file.close()

        file = open('menus/tests/test_data/expected_many_pages.json')
        self.api_expected_menu_data = json.load(file)
        file.close()

    def test_no_problem_supplied(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.raise_for_status = Mock()
        mock_get.return_value.json.side_effect = self.api_menu_data
        menus_info = menus.fetch_menus_data()
        self.assertEqual(menus_info, self.api_expected_menu_data)

    def test_many_pages(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.raise_for_status = Mock()
        mock_get.return_value.json.side_effect = self.api_menu_data
        menus_info = menus.fetch_menus_data(problem_id=1)
        self.assertEqual(menus_info, self.api_expected_menu_data)

    def test_empty_page(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.raise_for_status = Mock()
        file = open('menus/tests/test_data/empty_page.json')
        mock_get.return_value.json.return_value = json.load(file)
        file.close()
        file = open('menus/tests/test_data/expected_empty_page.json')
        expected_empty_page = json.load(file)
        file.close()

        menus_info = menus.fetch_menus_data(problem_id=1)
        self.assertEqual(menus_info, expected_empty_page)

    def test_one_page(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.raise_for_status = Mock()
        file = open('menus/tests/test_data/one_page_only.json')
        mock_get.return_value.json.return_value = json.load(file)
        file.close()
        file = open('menus/tests/test_data/expected_one_page_only.json')
        expected_one_page_only = json.load(file)
        file.close()

        menus_info = menus.fetch_menus_data(problem_id=1)

        self.assertEqual(menus_info, expected_one_page_only)

    def test_http_error(self, mock_get):
        mock_get.return_value.raise_for_status.side_effect = \
            requests.exceptions.HTTPError("Not found.")
        with self.assertRaises(requests.exceptions.HTTPError):
            menus.fetch_menus_data()


class TestConstructMenusUrl(unittest.TestCase):
    def test_valid_page_and_id(self):
        url = construct_menus_url(2, 3)
        expected_url = ('https://backend-challenge-summer-2018'
                        '.herokuapp.com/challenges.json?page=2&id=3')
        self.assertEqual(url, expected_url)

    def test_no_args_provided(self):
        url = construct_menus_url()
        expected_url = ('https://backend-challenge-summer-2018'
                        '.herokuapp.com/challenges.json?page=1&id=1')
        self.assertEqual(url, expected_url)

    def test_page_arg_provided_only(self):
        url = construct_menus_url(page=1)
        expected_url = ('https://backend-challenge-summer-2018'
                        '.herokuapp.com/challenges.json?page=1&id=1')
        self.assertEqual(url, expected_url)

    def test_id_arg_provided_only(self):
        url = construct_menus_url(problem_id=1)
        expected_url = ('https://backend-challenge-summer-2018'
                        '.herokuapp.com/challenges.json?page=1&id=1')
        self.assertEqual(url, expected_url)

    def test_invalid_page(self):
        with self.assertRaises(ValueError):
            construct_menus_url(page='yolo', problem_id=1)

    def test_invalid_id(self):
        with self.assertRaises(ValueError):
            construct_menus_url(page=10, problem_id='yolo')
