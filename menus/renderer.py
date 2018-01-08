import json

def render_aggregate_menus_json(valid_menus=[], invalid_menus=[]):
	return json.dumps({
		'valid_menus': valid_menus,
		'invalid_menus': invalid_menus
	})
