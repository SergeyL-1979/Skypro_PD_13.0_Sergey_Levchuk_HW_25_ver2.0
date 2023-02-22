#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import config
from pprint import pprint


def get_comments_all(path=config.COMMENT_PATH):
    """ Функция загрузки данных из JSON """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# def get_comments_by_post_id(post_id):
#     """ – возвращает комментарии определенного поста. Функция должна вызывать ошибку ValueError если такого
#     поста нет и пустой список, если у поста нет комментов. """
#     post_ids = []
#     comments_posts = get_comments_all(config.COMMENT_PATH)
#     for comment in comments_posts:
#         if post_id == comment['post_id']:
#             post_ids.append(comment)
#     return post_ids
def get_comments_by_post_id(post_id):
    """ – возвращает комментарии определенного поста. Функция должна вызывать ошибку ValueError если такого
    поста нет и пустой список, если у поста нет комментов. """
    post_ids = []
    is_comment_exist = False
    comments_posts = get_comments_all()
    for comment in comments_posts:
        if post_id == comment['post_id']:
            post_ids.append(comment)
            is_comment_exist = True
    if not is_comment_exist:
        raise ValueError('Такого комментария не существует')
    return post_ids


def save_json_comments(comments, path=config.COMMENT_PATH):
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(comments, file, indent=4, ensure_ascii=False)


def add_comment(post_id, username, comment):
    comments = get_comments_all(config.COMMENT_PATH)
    new_comment = {"post_id": int(post_id), "commenter_name": username, "comment": comment, "pk": len(comments) + 1}
    comments.append(new_comment)
    save_json_comments(comments)
