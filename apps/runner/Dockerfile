FROM alpine:3.20.0

ARG NAME_MAINTENER=Manuel
LABEL maintener=${NAME_MAINTENER}

RUN mkdir -p /data/in /data/out

WORKDIR /app

ENV NAME_TO_GREET=Dorian

COPY scripts/ .

ENTRYPOINT ["sh"]
CMD ["greetings.sh"]