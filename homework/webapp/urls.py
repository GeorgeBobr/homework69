from django.urls import path

from webapp.views import index, add, subtract, multiply, divide

app_name = "webapp_api"

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]