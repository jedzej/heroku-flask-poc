from wsgiref.simple_server import make_server


def application(env, start_response):
    """
    A basic WSGI application
    """

    http_status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    response_text = "Hello World"

    start_response(http_status, response_headers)
    return [response_text]

if __name__ == "__main__":
    make_server('', 8000, application).serve_forever()
