#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import config
from posts_func import get_posts_all
from pprint import pprint


def wrap_to_link(tag):
    return f"<a href='/tag/{tag}'>#{tag}</a>"


def get_tags(content):

    words = []
    for word in content.split(" "):
        if word[0] == "#":
            words.append(wrap_to_link(word[1:]))
        else:
            words.append(word)
    return " ".join(words)


def link_content():
    all_tag = get_posts_all()
    hash_tag = []
    for link in all_tag:
        tag_link = link.get('content')
        hash_tag.append(tag_link)
    return str(hash_tag)


# d = link_content()
# pprint(get_tags(d))

# ==========================================================================
# def get_posts_by_tag(tag_name):
#     """Получение списка постов по тегу"""
#     tag_posts = []
#     posts = get_posts_all(config.POST_PATH)
#     tag = '#' + tag_name
#
#     for post in posts:
#         if tag in post['content']:
#             tag_posts.append(post)
#
#     return tag_posts
#
#
# def get_hashtags(post):
#     """Преобразование слов с хештегами в ссылки"""
#     # if '#' in post['content']:
#     #     words = post['content'].split(' ')
#     #     for index, word in enumerate(words):
#     #         if word.startswith('#'):
#     #             words[index] = f'<a href="/tag/{word[1:]}">{word}</a>'
#     #
#     #     post['content'] = ' '.join(words)
#     hashtags = []
#     for element in post.split(" "):
#         if element.startswith("#"):
#             hashtags.append(element[1:])
#     # print(hashtags)
#     return hashtags
#     # return post

# tagg = get_posts_by_tag('закат')
# # pprint(tagg[0])
# pprint(get_hashtags(tagg[0]['content']))
