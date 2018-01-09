def dfs_find_products_in_menu_tree(root_id, products):
    stack = [(root_id, 0)]
    visited_product_ids = {}
    is_invalid_menu = False
    is_root_supposed_child = False

    while len(stack) > 0:
        item, curr_depth = stack.pop()

        if curr_depth > 4:
            is_invalid_menu = True

        curr_product_id = item
        curr_product = products[curr_product_id]
        visited_product_ids[curr_product_id] = True

        for child_id in curr_product['child_ids']:
            child_product = products[child_id]

            if child_id == root_id:
                is_root_supposed_child = True

            if ('parent_id' in child_product and
                    child_product['parent_id'] == curr_product_id and
                    child_id not in visited_product_ids):
                stack.append((child_id, curr_depth + 1))
            else:
                is_invalid_menu = True
                visited_product_ids[child_id] = True

    menu = {
        'root_id': root_id,
        'children': [product_id for product_id in visited_product_ids]
    }

    if not is_root_supposed_child:
        menu['children'].remove(root_id)

    return menu, is_invalid_menu


def validate_menus(root_ids, products):
    valid_menus = []
    invalid_menus = []
    for root_id in root_ids:
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(
            root_id, products)
        if is_invalid_menu:
            invalid_menus.append(menu)
        else:
            valid_menus.append(menu)
    return valid_menus, invalid_menus
