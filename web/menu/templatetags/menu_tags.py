from django import template
from ..models import MenuItem, Menu

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    try:
        menu_items = MenuItem.objects.filter(menu__name=menu_name)
        menu_tree = {}
        active_item_id = None
        for item in menu_items:
            if item.get_absolute_url() == current_url:
                active_item_id = item.id

            menu_tree[item.id] = {'item': item, 'children': {}, 'is_active': False, 'is_expanded': False}

        if active_item_id:
            current_id = active_item_id
            while current_id:
                menu_tree[current_id]['is_active'] = True
                menu_tree[current_id]['is_expanded'] = True
                parent_id = menu_tree[current_id]['item'].parent_id
                if parent_id:
                    menu_tree[parent_id]['is_expanded'] = True
                current_id = parent_id

        for item in menu_items:
            if item.parent_id is None:
                continue
            parent = menu_tree[item.parent_id]
            parent['children'][item.id] = menu_tree[item.id]

        root_items = {id: node for id, node in menu_tree.items() if node['item'].parent_id is None}

        return {'menu_tree': root_items, 'current_url': current_url}

    except Menu.DoesNotExist:
        return {'menu_tree': {}, 'current_url': current_url}