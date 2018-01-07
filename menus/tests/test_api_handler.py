import unittest
import menus

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

      self.assertEqual(products, {1: {'id': 1, 'data': 'Hello', 'child_ids': []}})
      self.assertEqual(root_ids, [1])

    def test_valid_existing_menu_info(self):
        menus_info = {
            "menus":[
                {
                  "id":1,
                  "data":"House",
                  "child_ids":[3]
                },
                {
                  "id":2,
                  "data":"Company",
                  "child_ids":[4]
                },
                {
                  "id":3,
                  "data":"Kitchen",
                  "parent_id":1,
                  "child_ids":[5]
                },
                {
                  "id":4,
                  "data":"Meeting Room",
                  "parent_id":2,
                  "child_ids":[6]
                },
                {
                  "id":5,
                  "data":"Sink",
                  "parent_id":3,
                  "child_ids":[1]
                },
                {
                  "id":6,
                  "data":"Chair",
                  "parent_id":4,
                  "child_ids":[]
                }
            ],
            "pagination":{
            "current_page":1,
            "per_page":5,
            "total":19
            }
        }
        products, root_ids = menus.parse_menus_data(menus_info)

        self.assertEqual(products, {1: {'id': 1, 'data': 'House', 'child_ids': [3]}, 2: {'id': 2, 'data': 'Company', 'child_ids': [4]}, 3: {'id': 3, 'data': 'Kitchen', 'parent_id': 1, 'child_ids': [5]}, 4: {'id': 4, 'data': 'Meeting Room', 'parent_id': 2, 'child_ids': [6]}, 5: {'id': 5, 'data': 'Sink', 'parent_id': 3, 'child_ids': [1]}, 6: {'id': 6, 'data': 'Chair', 'parent_id': 4, 'child_ids': []}})
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

# Add mocks
class TestFetchMenusData(unittest.TestCase):

	def test_many_pages(self):
		pass

	def test_empty_page(self):
		pass

	def test_one_page(self):
		pass

	def test_http_error(self):
		pass

class TestConstructMenusUrl(unittest.TestCase):

	def test_valid_page_and_id(self):
		pass

	def test_no_args_provided(self):
		pass

	def test_page_arg_provided_only(self):
		pass

	def test_id_arg_provided_only(self):
		pass

	def test_invalid_page(self):
		pass

	def test_invalid_id(self):



