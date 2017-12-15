from datetime import datetime


class NeredeNelerOluyorMiddleware(object):

    def __init__(self, get_response):
        print("__init__")
        self.get_response = get_response

    def __call__(self, request):
        print("###########################################################################")
        print("__call__ --> önce")
        request.saatkac = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = self.get_response(request)
        print(response.status_code)
        print("__call__ --> sonra")
        print("###########################################################################")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view --> " + view_func.__name__)

    def process_template_response(self, request, response):
        print("process_template_response")
        return response
