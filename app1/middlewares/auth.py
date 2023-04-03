from django.shortcuts import redirect


def auth_middleware(get_response):

    def middleware(request):
        if request.path not in ['/login/','/register/']:
            if not request.session.get('user'):
                return redirect('/login/')

        response = get_response(request)
        return response
    return middleware