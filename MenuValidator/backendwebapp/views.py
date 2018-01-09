from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
import cli.menus as menus


@api_view(['GET'])
def fetch_menus(request):
    problem_id = request.GET.get('problem-id', 1)
    menus_info = menus.fetch_menus_data(problem_id)
    products, root_ids = menus.parse_menus_data(menus_info)
    valid_menus, invalid_menus = menus.validate_menus(root_ids, products)
    return HttpResponse(menus.render_aggregate_menus_json(valid_menus, invalid_menus), content_type='application/json')


