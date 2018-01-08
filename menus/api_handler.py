import requests
from urllib.parse import urlencode


def parse_menus_data(menus_info={}):
    products = {}
    root_ids = []

    for product in menus_info['menus']:
        if not 'parent_id' in product:
            root_ids.append(product['id'])
        products[product['id']] = product
    return products, root_ids


def construct_menus_url(page=1, problem_id=1):
  page = int(page)
  problem_id = int(problem_id)
  return 'https://backend-challenge-summer-2018.herokuapp.com/challenges.json?' + urlencode({'page': page, 'id': problem_id})


def fetch_menus_data(problem_id=1):
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

        if menu_data['pagination']['per_page'] * menu_data['pagination']['current_page'] >= menu_data['pagination']['total']:
            nodes_left = False
        page += 1
    return menus_info
