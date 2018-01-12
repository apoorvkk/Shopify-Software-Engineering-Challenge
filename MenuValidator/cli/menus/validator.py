def dfs_find_products_in_menu_tree(root_id, products):
    '''
    A depth first search has been applied on the given
    supposed tree so that we can:
    - Check for cyclic references.
    - Check for tree's depth being greater than 4.
    - Identify and collect all products in the graph.
    '''
    stack = [(root_id, 0)]
    visited_product_ids = {}
    is_invalid_menu = False

    # Identifies if a node in the tree has a child reference to root.
    # If a node in the tree refers to the root node as a child,
    # then there must be a cylic reference and root node should be in
    # children array.
    # If no node in the tree refers to the root node as a child,
    # then the children array should not include the root node at all.
    is_root_supposed_child = False

    while len(stack) > 0:
        curr_product_id, curr_depth = stack.pop()
        curr_product = products[curr_product_id]
        visited_product_ids[curr_product_id] = True

        if curr_depth > 4:
            is_invalid_menu = True

        for child_id in curr_product['child_ids']:
            child_product = products[child_id]

            # There is a cylic reference if child_id = root_id.
            # Root must be inside children array.
            if child_id == root_id:
                is_root_supposed_child = True

            # Check if child node has not been visited and
            # if the child node has a direct parent reference
            # to the current node of interest. If not,
            # the current node is making a false child claim
            # and hence, it is either child referring to a node
            # in this tree/menu (which makes a cycle) OR a node in
            # another tree/menu (which would be invalid because each
            # root id should manage a unqiue menu and 2 or more parents
            # cannot claim the same child).
            if ('parent_id' in child_product and
                    child_product['parent_id'] == curr_product_id and
                    child_id not in visited_product_ids):
                stack.append((child_id, curr_depth + 1))
            else:
                is_invalid_menu = True
                visited_product_ids[child_id] = True

    # If there was never a child reference to the root
    # (making menu invalid as root node cannot be a
    # child of another node), we must remove the root
    # from the children array as this contains ALL
    # visited nodes (including root).
    if not is_root_supposed_child:
        visited_product_ids.pop(root_id)

    # Collect all visited nodes into children array and state the root.
    menu = {
        'root_id': root_id,
        'children': [product_id for product_id in visited_product_ids]
    }

    return menu, is_invalid_menu


def validate_menus(root_ids, products):
    '''
    This function will run the validator (dfs search) on
    each menu (or supposed tree) to identify and collect
    valid and invalid menus. Each root_id should be responsible
    for a unique tree (if we have only valid menus) so this
    function iterates through each root_id and runs the
    validation check against the supposed tree/menu.
    '''

    valid_menus, invalid_menus = [], []

    for root_id in root_ids:
        menu, is_invalid_menu = dfs_find_products_in_menu_tree(
            root_id, products)
        if is_invalid_menu:
            invalid_menus.append(menu)
        else:
            valid_menus.append(menu)
    return valid_menus, invalid_menus
