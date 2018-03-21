from catalog import models as cmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #   code to be executed for each request before the view (and later middleware) are caled
        recent_list = request.session.get('last_five', [])  # get 'last_five' from global variable, default it as a list if not there
        request.last_five = []  # declare new request variable and make it a list
        for p in recent_list:
            request.last_five.append(cmod.Product.objects.get(id=p))    # transfer recent list to new last_five variable

        response = self.get_response(request)
        #   code to be executed for each request/response after the view is called
        last_five_ids = []
        for r in request.last_five:
            last_five_ids.append(r.id)

        request.session['last_five'] = last_five_ids
        return response
