""" VIEWS """
from flask import Blueprint, jsonify

from posts_func import get_posts_all, get_post_by_pk
from logs.logger import logger_api

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')


@api_blueprint.route('/posts/')
def posts_api():
    """ Возвращает полный список постов в виде JSON-списка """
    logger_api.info("Запрос /api/posts")
    posts = get_posts_all()
    return jsonify(posts), 200


@api_blueprint.route('/posts/<int:post_id>')
def single_post_api(post_id):
    """ Возвращает один пост в виде JSON-словаря """
    logger_api.info(f"Запрос /api/posts/{post_id}")
    post = get_post_by_pk(post_id)
    return jsonify(post), 200
