#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import config


def get_posts_all(path=config.POST_PATH):
    """ Функция загрузки данных из JSON """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def search_for_posts(query):
    """ Возвращает список постов по ключевому слову """
    content_search = []
    posts = get_posts_all()
    for post in posts:
        if query.lower() in post['content'].lower():
            content_search.append(post)
    return content_search


# def get_posts_by_user(user_name):
#     """ Возвращает посты определенного пользователя. Функция должна вызывать ошибку ValueError если такого
#     пользователя нет и пустой список, если у пользователя нет постов. """
#     poster_name = []
#     users_name = get_posts_all()
#     for user in users_name:
#         if user_name in user['poster_name']:
#             poster_name.append(user)
#     return poster_name
def get_posts_by_user(user_name):
    """ Возвращает посты определенного пользователя. Функция должна вызывать ошибку ValueError если такого
    пользователя нет и пустой список, если у пользователя нет постов. """
    poster_name = []
    is_user_exist = False
    users_name = get_posts_all()
    for user in users_name:
        if user_name in user['poster_name']:
            poster_name.append(user)
            is_user_exist = True
    if not is_user_exist:
        raise ValueError('Такого пользователя не существует')
    return poster_name


def get_post_by_pk(pk):
    """ Возвращает один пост по его идентификатору. """
    posts_pk = get_posts_all()
    for post in posts_pk:
        if post['pk'] == pk:
            return post


# ===== ЭТО ФУНКЦИИ СОХРАНЕНИЯ ПОСТОВ В JSON =====
def save_json_post(posts, path=config.POST_PATH):
    """ Сохранение данных в JSON """
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)


def add_content(post):
    """ Добавление данных в JSON """
    posts = get_posts_all()
    posts.append(post)
    save_json_post(posts)
