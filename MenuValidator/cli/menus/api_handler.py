import requests
from urllib.parse import urlencode


def parse_menus_data(menus_info={}):
    '''
    Takes in raw response data from Shopify's backend
    and then produces a dictionary where the product id is the
    key and the product object is value. Also identifies and
    keeps a list of root ids (nodes without parents).
    '''
    products = {}
    root_ids = []

    for product in menus_info['menus']:
        if 'parent_id' not in product:
            root_ids.append(product['id'])
        products[product['id']] = product
    return products, root_ids


def construct_menus_url(page=1, problem_id=1):
    page = int(page)
    problem_id = int(problem_id)
    url = (
        'https://backend-challenge-summer-2018.'
        'herokuapp.com/challenges.json?'
        )

    return url + urlencode({'page': page, 'id': problem_id})


def fetch_menus_data(problem_id=1):
    '''
    Based on the problem id provided, this function will
    make iterative requests to fetch all product data from
    the Shopify backend. This is done by making a request
    for each incremental page until there are no more products
    (or no more pages).
    '''
    page = 1
    nodes_left = True
    menus_info = {
        "menus": []
    }

    while nodes_left:
        response = requests.get(construct_menus_url(
            page, problem_id), headers={'Accept': 'application/json'})
        response.raise_for_status()
        menu_data = response.json()
        menus_info['menus'] += menu_data['menus']

        # Check if there are more products left on further pages.
        if (menu_data['pagination']['per_page'] *
                menu_data['pagination']['current_page']
                >= menu_data['pagination']['total']):
            nodes_left = False
        page += 1
    return menus_info
