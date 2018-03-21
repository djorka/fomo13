from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod
import math


@view_function
def process_request(request, prod_id: cmod.Product, cat_id=0):
    prod = prod_id
    img = prod.image_urls()
    category = cat_id
    cat = cmod.Category.objects.all()
    if prod in request.last_five:
        request.last_five.remove(prod)
    request.last_five.insert(0, prod)


    context = {
        'prod': prod,
        'img': img,
        'cat': cat,
    }
    return request.dmp.render('detail.html', context)
