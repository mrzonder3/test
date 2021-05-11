Реализовал 3 сервиса используя docker-compose:
* Postgres - база, [cron](cron) который запускает [скрипт](backup.py), который создает бэкап используя `pg_basebackup` и складывает в папку `/tmp/backup`, которая является внешним volume. Так же скрипт отправляет метрику `Backup has been created successfully` в prometheus используя pushgateway.
* Prometheus `http://localhost:9090/`
* Pushgateway `http://localhost:9091/`

Запуск `docker-compose up`
Бэкапы создаются каждую минуту в папке `backup`
