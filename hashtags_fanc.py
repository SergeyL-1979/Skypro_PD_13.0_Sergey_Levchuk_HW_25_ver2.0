#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" HASH_TAG """

from posts_func import get_posts_all


def wrap_to_link(tag):
    """ tag """
    return f"<a href='/tag/{tag}'>#{tag}</a>"


def get_tags(content):
    """ get tag """
    words = []
    for word in content.split(" "):
        if word[0] == "#":
            words.append(wrap_to_link(word[1:]))
        else:
            words.append(word)
    return " ".join(words)


def link_content():
    """ link tag """
    all_tag = get_posts_all()
    hash_tag = []
    for link in all_tag:
        tag_link = link.get('content')
        hash_tag.append(tag_link)
    return str(hash_tag)
