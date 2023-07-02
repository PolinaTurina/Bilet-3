from django.urls import path
from .views import *

app_name = 'shop_app'

urlpatterns = [
    path('tovar/', tovar_list_view, name='tovar'),
]