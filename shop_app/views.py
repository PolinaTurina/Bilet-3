from django.shortcuts import render
from.models import *
from .forms import *
from django.db.models import Q 


def tovar_list_view(request, category_id=None):
    category = Category.objects.all()
    

    q=request.GET.get('q', '')
    if q:
        tovar = Tovar.objects.filter(Q(category__name__icontains=q))
    else:
        tovar = Tovar.objects.all()


    context = {'tovar_list': tovar, 'categories': category}
    return render(request, 'shop_app/tovar_list.html', context)


