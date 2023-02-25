#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Open JSON files Book """
import json
import config
from posts_func import get_posts_all


def get_bookmarks(path=config.BOOKMARKS_PATH):
    """ Возвращает все закладки """
    with open(path, 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)
        return bookmarks


def get_bookmark_post_id():
    """ Отображения постов из закладок - не работает """
    all_bookmarks = get_bookmarks()
    all_posts = get_posts_all()

    # return [post for post in all_posts if post.get('pk') in all_bookmarks]
    post_ids = [bookmark["post_id"] for bookmark in all_bookmarks]
    posts_bookmarked = [post for post in all_posts if post["pk"] in post_ids]
    return posts_bookmarked


def save_bookmarks(bookmarks, path=config.BOOKMARKS_PATH):
    """ Save bookmarks """
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(bookmarks, file, indent=4, ensure_ascii=False)


def add_bookmarks(post_id):
    """ Добавляет закладку """
    bookmarks = get_bookmarks()  # Возвращает все закладки
    new_bookmarks = {"post_id": int(post_id), "pk": len(bookmarks) + 1}
    bookmarks.append(new_bookmarks)
    save_bookmarks(bookmarks)
    return bookmarks


def remove_bookmarks(post_id):
    """ Удаляет закладки """
    del_bookmarks = get_bookmarks(config.BOOKMARKS_PATH)
    # удаление элемента из словаря
    delete_bookmarks = [item for item in del_bookmarks if item["post_id"] != post_id]
    save_bookmarks(delete_bookmarks)
    return del_bookmarks
