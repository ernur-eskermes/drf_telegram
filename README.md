<h2 align="center">Отправка уведомлений в telegram через drf</h2>

Настройка
------------
Переименуйте drf_telegram в src(по желанию)

Создайте папку conf и файл config.env рядом с папки src. Этот файл необходим для настройки проекта. 
Пример настроек:
```shell
SECRET_KEY=gb1jxml$f(m%2zja5cho+0
DEBUG=True
TG_BOT_TOKEN=17123123220:AAHZ-UJQWPzwYqMdTDuI93213212dsdew
```

Локальный запуск проекта
------------
```shell
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    python manage.py bot
```

Основные эндпойнты
------------
api/accounts/create/ - Создание пользователя

api/token/ - Создание jwt токена

api/tg_bot/chats/create/ - Создание чата. После создания возвращается токен, который нужно передать в бот

api/tg_bot/messages/create/ - Создание сообщения. Сообщение сразу же отправляется ботом пользователю
