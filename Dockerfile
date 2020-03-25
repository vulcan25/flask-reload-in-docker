from python:alpine
RUN apk add zsh git vim
RUN pip install -U pip && pip install flask gunicorn
WORKDIR /code
COPY ./code /code
CMD /bin/zsh
