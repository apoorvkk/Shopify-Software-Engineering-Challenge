import unittest
from unittest.mock import Mock
from unittest import mock

import menus
from menus.validator import dfs_find_products_in_menu_tree

@mock.patch('menus.validator.dfs_find_products_in_menu_tree')
class TestValidateMenus(unittest.TestCase):
	def test_valid_menus_only(self, mock_dfs):
		pass

	def test_invalid_menus_only(self, mock_dfs):
		pass


	def test_both_valid_and_invalid_menus_only(self, mock_dfs):
		pass

	def test_invalid_root_ids(self, mock_dfs):
		pass

	def test_no_root_ids(self, mock_dfs):
		pass



class TestDFSFindProductsInMenuTree(unittest.TestCase):
	def test_valid_tree(self):
		# products = []
		# dfs_find_products_in_menu_tree(1, )
		pass

	def test_invalid_acyclic_tree(self):
		pass

	def test_invalid_cyclic_tree(self):
		pass

	def test_invalid_max_depth_tree(self):
		pass

	def test_invalid_root_id(self):
		pass

