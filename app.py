#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory
from views import main_bp
from api.views import api_blueprint


app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(api_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def page_error(e):
    """ Обработчик запросов к несуществующим страницам, например:
    /meow - верните в этом случае статус-код 404 """
    return render_template('error_page/404.html'), 404


@app.errorhandler(413)
def page_not_found(e):
    """ Обработчик ошибки загрузки файлов большого размера """
    return '''<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>
    <p>Повторите запрос! Вернитесь <a href="/" class="link">назад</a></p>''', 413


@app.errorhandler(500)
def internal_error(e):
    """ Обработчик ошибок, возникших на стороне сервера (ошибка 500, Internal Server Error)
    и верните в этом случае статус-код 500 """
    return render_template('error_page/500.html'), 500


if __name__ == "__main__":
    app.run(debug=True, port=5005)
