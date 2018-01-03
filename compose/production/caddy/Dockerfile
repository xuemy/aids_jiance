FROM abiosoft/caddy:0.10.6

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./compose/production/caddy/Caddyfile /etc/Caddyfile
