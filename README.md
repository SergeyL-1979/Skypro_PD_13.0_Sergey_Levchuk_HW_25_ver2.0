# Skypro_PD_13.0_Sergey_Levchuk_HW_25_ver2.0

Перейдите в папку `/etc/systemd/system` и создайте файл `flask-app.service` с настройками для будущего демона Gunicorn:

```
    [Unit]
    Description=SkyPro_HW25
    After=network.target
    
    [Service]
    WorkingDirectory=/home/l2023/skypro_hw_25/
    ExecStart=/home/l2023/venv/bin/python -m flask run -h 0.0.0.0 -p 80
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
```
После добавления нового сервиса перенастройте Systemd и запустите сервис:

```shell
$ systemctl daemon-reload
$ systemctl start flask_app.service
```
Если при запуске сервиса будет ошибка, то вы не заметите этого. Проверить работу сервиса можно командой:
```shell
$ systemctl status flask_app
```

# DEPLOY APP

## Вот основные директивы, которые можно использовать в файле `Dockerfile`:

    FROM - образ, на основе которого будет создаваться наш образ;
    RUN - выполнить команду в окружении образа;
    COPY - скопировать файл в образ;
    WORKDIR - задать рабочую папку для образа;
    ENV - задать переменную окружения образа;
    CMD - задать основной процесс образа;

## Команды для сборки и запуска докер контейнера
    docker-compose up --build -d
    docker-compose logs
    docker exec -it backend-flask /bin/bash
