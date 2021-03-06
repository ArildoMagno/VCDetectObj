# Remoto(Método mais simplificado):
##### Abra a versão online do código no colab, e execute as células do código.

**Acesso:** [CNN para detecção de objetos](https://colab.research.google.com/drive/1tbd_ZJIA7wQ-77wsnTldM0PjZ4fysFBx?usp=sharing)

# Localmente:

## Requisitos :

### Ambiente:
É necessário ter instalado a **versão 3.8.5 do Python ou superior** e do **pip 22.1.2**.

### Instação das bibliotecas necessárias:
Execute o comando abaixo no diretorio do projeto para instalar as bibliotecas necessárias via pip.
comando:
 
```sh 
 "$ pip3 install -r requirements.txt --no-deps".
```


### Execução:
* Coloque a imagem que deseja analisar no diretório /imagens.
* Altere o imagem_path no arquivo main.py para o caminho da imagem.
* Execute o arquivo main.py para realizar a análise.
* O resultado será salvo no diretório /results.

# Localmente via Docker:
Se preferir, pode utilizar o docker rodando os seguintes comandos:
```sh
$ docker build --rm -f Dockerfile -t ubuntu:visaocomp .
$ docker run --rm -it ubuntu:visaocomp
$ cd /home/usuario/trab
```
