from django.http import HttpResponse  # Add this import at the top

class DisableFaviconMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/favicon.ico':
            return HttpResponse(status=204)

        response = self.get_response(request)
        return response
