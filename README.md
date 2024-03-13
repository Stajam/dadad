[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9FSFJhE3)
# Questão 1

Modifique o arquivo **templates/noticia.html** para exibir a imagem **spacex.webp** no local indicado. Crie a rota **/noticia** que renderize o arquivo em questão.

# Questão 2

Modifique o arquivo **templates/login.html** para incluir o arquivo css **signin.css** para estilizar a página. Crie uma rota chamada **/login** que renderize o arquivo em questão. 

# Questão 3
Crie uma rota chamada **/arearestrita** que receba como parâmetro um valor (lock ou unlock). E exiba a imagem correspondente do cadeado, de acordo com o valor do parâmetro recebido. Assim, quando o usuário acessar na URL no endereço de exemplo:

```html
http://seuprojeto.com/arearestrita/lock
```

sua página HTML deve exibir a imagem do cadeado fechado.

Já se o usuário digitar:
```html
http://seuprojeto.com/arearestrita/unlock
```

sua página HTML deve exibir a imagem do cadeado aberto.

# Questão 4

Crie uma rota chamada **/tema** que receba como parâmetro um valor de dark ou light e inclua, no arquivo tema.html, o css correspondente, de acordo com o parâmetro.  

Assim, quando o usuário digitar:
```html
http://seuprojeto.com/tema/dark
```
sua página HTML deve renderizar o arquivo **tema.html**, incluindo o arquivo **dark.css**.

Já se acessar pela URL:
```
http://seuprojeto.com/tema/light
```
sua página HTML deve renderizar o arquivo **tema.html** incluindo o arquivo **light.css**

# Questão 5

Crie uma rota chamada **/galeria** que receba como parâmetro um número inteiro, correspondente ao identificador de uma imagem (de 1 a 10, por exemplo). Baixe 10 imagens distintas na internet de uma mesma temática e renomei-as de 1 a 10 (ex: 1.jpg, 2.jpg, 3.jpg,…). Fique atento se todas possuem a mesma extensão (.jpg ou .png, por exemplo). 

Modifique o arquivo HTML chamado galeria.html que, para que de acordo com o parâmetro recebido, exiba na tela a imagem correspondente. Crie um arquivo css, também chamado galeria.css que defina as dimensões específicas das imagens para que todas sejam apresentadas no mesmo tamanho. 

Veja o exemplo de chamada da rota. Ao executar essa rota, deve ser exibida a imagem 1.jpg, por exemplo.

```html
http://seuprojeto.com/galeria/1
```

Já ao executar a rota abaixo, deve ser exibida a imagem 6.jpg.
```html
http://seuprojeto.com/galeria/6
```
