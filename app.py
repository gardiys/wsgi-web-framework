from wsgi import WebFramework

def application(environ, start_response):
    app = WebFramework()

    @app.route("/")
    def main_page(request, response):
        with open(r"views/index.html", "r") as f:
            response.text = f.read()

    @app.route("/info")
    def info_page(request, response):
        with open(r"views/info.html", "r") as f:
             response.text = f.read()

    return app(environ, start_response)
