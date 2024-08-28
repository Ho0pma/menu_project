from django.urls import path
from . import views


app_name = 'menu'


urlpatterns = [
   path('', views.home, name='home'),
   path('one/', views.one, name='one'),
   path('two/', views.two, name='two'),
   path('three/', views.three, name='three'),
   path('four/', views.four, name='four'),
   path('five/', views.five, name='five'),

   path('shelf_one/', views.shelf_one, name='shelf_one'),
   path('shelf_two/', views.shelf_two, name='shelf_two'),
   path('box_one/', views.box_one, name='box_one'),
   path('box_two/', views.box_two, name='box_two'),
   path('nails/', views.nails, name='nails'),
   path('screws/', views.screws, name='screws'),
   path('saw/', views.saw, name='saw'),
   path('axe/', views.axe, name='axe'),
   path('old_iron/', views.old_iron, name='old_iron'),

]

