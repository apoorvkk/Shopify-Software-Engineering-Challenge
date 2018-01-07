import menus

if __name__ == '__main__':
	problem_id = input("Please enter a problem set id: ")
	menus_info = menus.fetch_menus_data(problem_id)
	products, root_ids = menus.parse_menus_data(menus_info)
	valid_menus, invalid_menus = menus.validate_menus(root_ids, products)
	print(menus.render_aggregate_menus_json(valid_menus, invalid_menus))
