from django.shortcuts import render
from.models import *


def tovar_list_view(request):
    tovar = Tovar.objects.all()
    context = {'tovar_list': tovar}
    return render(request, 'shop_app/tovar_list.html', context)
