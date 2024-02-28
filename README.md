- - LP3 IFSP

repositorio para organizar os codigos da disciplina de Programação 

# instruções lab de informatica 

```Ao chegar no laboratorio

configurar o usuario local do git 

```bash 

git config --global user.name "Erick"
git config --global user.email "erickverissimodasilva144@gmail.com"

fazer o clone do seu repositorio do github 

```bash

git clone https://github.com/redrick12/lp3-ifsp

abrir o repo no vscoe 

```bash 
code lp3-ifsp 

criar um token para realizar o push
settings -> developer settings -> personal access tokens -> tokens (classic) 

generate new token, selecionar a opção Generate new token classic, marcar a opção scope repo 

Antes de sair do lab 
```bash 
git config --global --unset user.name 
git config --global --unset user.email

deletar o token no github
deslogar do github