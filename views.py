#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request
from posts_func import get_posts_all, get_post_by_pk, search_for_posts, get_posts_by_user
from comment_func import get_comments_by_post_id, add_comment
from bookmarks_func import get_bookmarks, add_bookmarks, remove_bookmarks, get_bookmark_post_id
from hashtags_fanc import get_tags

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/')
def page_index():
    all_posts = get_posts_all()
    all_bookmarks = get_bookmarks()
    return render_template("index.html", posts=all_posts, all_bookmarks=all_bookmarks)


@main_bp.route('/post/<int:post_id>')
def page_post(post_id):
    user_post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_count = len(comments)

    if not user_post:
        return f"Post не найден {post_id}"
    return render_template("post.html", post=user_post,
                           comments=comments,
                           comments_count=comments_count,
                           user_post=get_tags(user_post['content']))


@main_bp.route('/post', methods=["POST"])
def save_comment_post():
    post_id = request.form.get("post_id")
    commenter_name = request.form.get("user")
    comment = request.form.get("comment")
    add_comment(post_id, commenter_name, comment)
    return redirect(request.referrer)


@main_bp.route('/users/<username>')
def posts_user(username):
    user_posts = get_posts_by_user(username)
    return render_template("user-feed.html", user_posts=user_posts)


@main_bp.route('/search/')
def search_post():
    posts_search = request.args.get('s').lower()
    posts = search_for_posts(posts_search)
    if not posts_search:
        return f''' <h2>NO SEARCH</h2>'''
    return render_template("search.html", posts=posts, posts_search=posts_search)


@main_bp.route('/bookmarks')
def all_bookmark():
    all_bookmarks = get_bookmarks()
    posts = get_bookmark_post_id()
    return render_template("bookmarks.html",
                           all_bookmarks=all_bookmarks,
                           posts=posts)


@main_bp.route('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    add_bookmarks(post_id)
    return redirect("/", code=302)


@main_bp.route('bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    remove_bookmarks(post_id)
    return redirect("/", code=302)


@main_bp.route('/tag/<tag_name>')
def get_by_tag(tag_name):
    content = search_for_posts(tag_name)
    return render_template("tag.html", by_tag=content)

