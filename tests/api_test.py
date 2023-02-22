import os.path
import pytest
import app
import config
import posts_func


class TestApi:
    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_all_posts(self):
        """ Проверяем, получени ли вообще адекватный список"""
        response = app.app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_all_content(self):
        """ Проверяем, правильные ли данные получены"""
        response = app.app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "Получен не список"
        # assert len(response.json) == 8, "Получено неверное количество элементов в списке"

    # Теперь тестируем один пост
    def test_single_post(self):
        """ Проверяем, что статус коды отдаются верно """
        response = app.app.test_client().get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200
        assert response.mimetype == "application/json", "Получен не JSON"
        assert type(response.json) == dict, "Получен не словарь"

    def test_check_keys(self):
        """ Проверяем, правильные ли ключи получены"""
        response = app.app.test_client().get('/api/posts/1', follow_redirects=True)
        first_keys = set(response.json.keys())
        assert self.post_keys == first_keys, "Полученные ключи не совпадают"

    # def test_all_posts_have_correct_keys(self):
    #     test_client = app.app.test_client()
    #     result = test_client.get("/api/posts/")
    #     list_of_posts = result.get_json(config.POST_PATH)
    #     for post in list_of_posts:
    #         assert post.keys() == self.post_keys, "Неправильные ключи у словаря"

    # def test_one_post(self):
    #     post = posts_func.get_post_by_pk(3)
    #     assert post["pk"] == 3, "возвращается неправильный пост"
