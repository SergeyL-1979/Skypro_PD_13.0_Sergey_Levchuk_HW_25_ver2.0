""" TEST """
import app


class TestApi:
    """ Класс тестирования API """
    post_keys = {
        "poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk"
    }

    def test_all_posts(self):
        """ Проверяем, получен ли вообще адекватный список"""
        response = app.app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_all_content(self):
        """ Проверяем, правильные ли данные получены"""
        response = app.app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "Получен не список"

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
