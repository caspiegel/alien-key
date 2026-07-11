FROM caddy:2-alpine

COPY Caddyfile /etc/caddy/Caddyfile
COPY index.html data.json /srv/

# Fail the build, not the deploy, if the Caddyfile is malformed.
RUN caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
