FROM ubuntu:latest

RUN apt update && \
    apt install -y sudo curl git-core gnupg wget nano zsh python3 python3-pip && \
    adduser --quiet --disabled-password \
    --shell /bin/zsh --home /home/usuario \
    --gecos "User" usuario && \
    echo "usuario:<a href="mailto://p@eml">p@eml</a>" | \
    chpasswd &&  usermod -aG sudo usuario

COPY . ./home/usuario/trab

RUN cd /home/usuario/trab/models/research && pip3 install .

RUN cd /home/usuario/trab && pip3 install -r requirements.txt --no-deps