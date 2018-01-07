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

def dfs_find_products_in_tree(root_id, products):
	stack = [root_id]
	curr_depth = 0
	visited_product_ids = {}
	is_invalid_menu = False

	while len(stack) > 0:
		item = stack.pop()
		if type(item) is dict:
			curr_depth = item['depth_level']
			if curr_depth > 4:
				is_invalid_menu = True
			continue

		curr_product_id = item
		curr_product = products[curr_product_id]
		visited_product_ids[curr_product_id] = True

		for child_id in curr_product['child_ids']:
			child_product = products[child_id]

			if 'parent_id' in child_product and child_product['parent_id'] == curr_product_id and child_id not in visited_product_ids:
				stack.append(child_id)
			else:
				is_invalid_menu = True
				visited_product_ids[child_id] = True
		stack.append({ 'depth_level': curr_depth+1 })

	menu = {
		'root_id': root_id,
		'children': [product_id for product_id in visited_product_ids]
	}

	if not is_invalid_menu and root_id in menu['children']:
		menu['children'].remove(root_id)

	return menu, is_invalid_menu

# Create dictionary out of response data and determine root nodes.
products = {}
root_ids = []

for product in menus_info['menus']:
	if not 'parent_id' in product:
		root_ids.append(product['id'])
	products[product['id']] = product

# Validate and aggregate the menus.
valid_menus = []
invalid_menus = []
for root_id in root_ids:
	menu, is_invalid_menu = dfs_find_products_in_tree(root_id, products)

	if is_invalid_menu:
		invalid_menus.append(menu)
	else:
		valid_menus.append(menu)

# Output the valid and invalid menus.
print(invalid_menus)
print('-' * 20)
print(valid_menus)
