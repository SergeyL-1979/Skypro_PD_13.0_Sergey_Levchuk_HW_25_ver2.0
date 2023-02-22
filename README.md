# Skypro_PD_13.0_Sergey_Levchuk_HW_25_ver2.0

Перейдите в папку `/etc/systemd/system` и создайте файл `flask-app.service` с настройками для будущего демона Gunicorn:

```shell
[Unit]
Description=SkyPro_HW25
After=network.target

[Service]
WorkingDirectory=/home/l2023/skypro_hw_25/

# Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
# ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
# ExecStart=gunicorn app:app -b 0.0.0.0:80 -w n

# ExecStart=gunicorn -b 0.0.0.0:80 server:process_http_request
ExecStart=/home/l2023/venv/bin/python -m flask run -h 0.0.0.0 -p 80
Restart=always

[Install]
WantedBy=multi-user.target
```
После добавления нового сервиса перенастройте Systemd и запустите сервис:

```shell
$ systemctl daemon-reload
$ systemctl start getip.service
```
Если при запуске сервиса будет ошибка, то вы не заметите этого. Проверить работу сервиса можно командой:
```shell
$ systemctl status getip
```



