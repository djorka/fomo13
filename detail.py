from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod


@view_function
def process_request(request, pnum=0):
    if pnum == 0:
        return HttpResponseRedirect('/catalog/index/')
    else:
        prod = cmod.Product.objects.get(id=pnum)
        category = prod.category_id
        cat = cmod.Category.objects.all()
        images = prod.image_urls()

    if prod in request.last_five:
        request.last_five.remove(prod)
        request.last_five.insert(0, prod)
    else:
        request.last_five.insert(0, prod)

    context = {
        'prod': prod,
        'category': category,
        'cat': cat,
        'images': images,
    }
    return request.dmp.render('detail.html', context)
