from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Load initial data'

    def handle(self, *args, **kwargs):
        main_menu = Menu.objects.create(name='main_menu')
        one = MenuItem.objects.create(menu=main_menu, name='one', named_url='menu:one')
        two = MenuItem.objects.create(menu=main_menu, name='two', parent=one, named_url='menu:two')
        three = MenuItem.objects.create(menu=main_menu, name='three', parent=two, named_url='menu:three')
        four = MenuItem.objects.create(menu=main_menu, name='four', named_url='menu:four')
        five = MenuItem.objects.create(menu=main_menu, name='five', parent=four, named_url='menu:five')

        second_menu = Menu.objects.create(name='second_menu')
        shelf_one = MenuItem.objects.create(menu=second_menu, name='Полка 1', named_url='menu:shelf_one')
        shelf_two = MenuItem.objects.create(menu=second_menu, name='Полка 2', named_url='menu:shelf_two')
        box_one = MenuItem.objects.create(menu=second_menu, name='Коробка 1', parent=shelf_one, named_url='menu:box_one')
        box_two = MenuItem.objects.create(menu=second_menu, name='Коробка 2', parent=shelf_one, named_url='menu:box_two')
        nails = MenuItem.objects.create(menu=second_menu, name='Гвозди', parent=box_one, named_url='menu:nails')
        screws = MenuItem.objects.create(menu=second_menu, name='Шурупы', parent=box_one, named_url='menu:screws')
        saw = MenuItem.objects.create(menu=second_menu, name='Пила', parent=shelf_two, named_url='menu:saw')
        axe = MenuItem.objects.create(menu=second_menu, name='Топор', parent=shelf_two, named_url='menu:axe')
        old_iron = MenuItem.objects.create(menu=second_menu, name='Старый утюг', parent=box_two, named_url='menu:old_iron')

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
