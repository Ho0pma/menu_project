**Цель проекта: **реализовать древовидное меню с помощью шаблонного тега draw_menu. 

**Запуск: **
1 вар: 
  - в корне проекта прописать docker-compose up --build. Автоматически создастся два меню для демонстрации.

2 вар:
- зайти в settigs и установить:
DATABASES = {
  'default': {
      . . .
      'HOST': 'localhost',
      . . .
  }
} 

- создать+запустить контейнер:
docker run -d \
  --name postgres_container \
  -e POSTGRES_DB=django_db \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -v django_db_volume:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:latest

- установить пакеты:
  pip install django
  pip install psycopg2-binary
  python -m pip install django-debug-toolbar

- запустить проект: python manage.py runserver

При втором варианте использования необходимо создать через меню самостоятельно через админку.
Код написан под следующие меню и элементы:
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

Если хочется создать свое меню:
  - Использовать тег в шаблоне: {% draw_menu 'your_menu_name' %}.
  - Предварительно, перед отрисовкой нужно создать меню и меню_итемы в админке, создать представления, шаблоны и маршруты.

