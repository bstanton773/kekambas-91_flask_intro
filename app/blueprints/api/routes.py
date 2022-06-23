from . import bp as api
from flask import jsonify
from app.models import Post

@api.route('/')
def index():
    return 'Hello World'


@api.route('/posts')
def posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])