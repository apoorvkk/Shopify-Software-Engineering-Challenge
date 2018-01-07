def parse_menus_data(menus_info={}):
	products = {}
	root_ids = []

	for product in menus_info['menus']:
		if not 'parent_id' in product:
			root_ids.append(product['id'])
		products[product['id']] = product
	return products, root_ids
