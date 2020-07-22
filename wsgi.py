from webob import Request, Response

class WebFramework:

    def __init__(self):
        self.routes = {}
    
    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle(request)
        
        return response(environ, start_response)
    
    def client_error_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def handle(self, request):
        response = Response()
        handler = self.routes.get(request.path)
        if handler:
            handler(request, response)
            return response
        
        self.client_error_response(response)
        return response
