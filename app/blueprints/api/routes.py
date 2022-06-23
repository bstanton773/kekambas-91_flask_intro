from . import bp as api

@api.route('/')
def index():
    return 'Hello World'