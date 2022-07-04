# Detecção de objetos

Abra a versão online do código no [colab](https://colab.research.google.com/drive/1tbd_ZJIA7wQ-77wsnTldM0PjZ4fysFBx?usp=sharing), e execute as células do código.

## Execução local

Execute os comandos abaixo em ordem para instalar as bibliotecas necessárias via pip.

Entre no diretorio models/research e execute o comando:

```sh
$ pip install .
```

Na raiz do projeto execute o comando:

```sh
$ pip install -r requirements.txt --no-deps
```

Ou se preferir, pode utilizar o docker rodando os seguintes comandos:

```sh
$ docker build --rm -f Dockerfile -t ubuntu:visaocomp .
$ docker run --rm -it ubuntu:visaocomp
$ cd /home/usuario/trab
```

## Execução:

- Coloque a imagem que deseja analisar no diretório `imagens`.

- Altere o imagem_path no arquivo `main.py` para o caminho da imagem.

- Execute o arquivo `main.py` para realizar a análise.

- O resultado será salvo no diretório `results`.
