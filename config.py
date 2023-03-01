#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" CONFIG """
import os.path
# basedir = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = os.path.abspath(path="data")
POST_PATH = os.path.join(BASE_DIR, "posts.json")
COMMENT_PATH = os.path.join(BASE_DIR, "comments.json")
BOOKMARKS_PATH = os.path.join(BASE_DIR, "bookmarks.json")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "images")

MAX_CONTENT_LENGTH = 2 * 1024 * 1024

JSON_AS_ASCII = False


# print(BASE_DIR)
