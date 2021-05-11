FROM postgres:latest

RUN apt update \
&& apt install -y cron \
&& apt install -y python \
&& apt install -y python-pip \
&& pip install prometheus-client

COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron
RUN touch /var/log/cron.log

COPY docker-entrypoint.sh /
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

CMD ["postgres"]
