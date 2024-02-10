<h1 align="center"> Product Code Bar </h1>
<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Dev-JoseRonaldo/product-code-bar?color=#F7DD43">

  <a href="https://github.com/Dev-JoseRonaldo/product-code-bar/blob/main/LICENSE">
    <img alt="Repository size" src="https://img.shields.io/github/repo-size/Dev-JoseRonaldo/product-code-bar">
  </a>
  
  <a href="https://github.com/Dev-JoseRonaldo/product-code-bar/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Dev-JoseRonaldo/product-code-bar">
  </a>
    
   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

   <a href="https://github.com/Dev-JoseRonaldo/boilerplate-next13-tailwind">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/Dev-JoseRonaldo/product-code-bar">
  </a>
</p>
<div align= 'center'>
 <img width=80% alt="Banner do projeto" src="https://res.cloudinary.com/devjoseronaldo/image/upload/v1707572878/code_bar_wmcozr.png">
</div>
<br/>

## 💻 Projeto

Este projeto visa a geração eficiente e precisa de códigos de barras exclusivos para produtos, a partir de identificadores únicos associados a cada item.  O sistema desenvolve códigos de barras que facilitam a rastreabilidade e gestão eficaz de produtos, proporcionando maior eficiência e organização no ambiente comercial.

<br>

## 🚀 Tecnologias

Foram usadas as seguintes tecnologias e bibliotecas para a realização do projeto:

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/8.0.x/)
- [Pylint](https://pypi.org/project/pylint/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Cerberus](https://docs.python-cerberus.org/)
- [pre-commit](https://pre-commit.com/)
- [python-barcode](https://pypi.org/project/python-barcode/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

<br>

## 👩🏽‍💻 Como usar ?

### Pré-requisitos

Antes de baixar o projeto você vai precisar ter instalado na sua máquina as seguintes ferramentas:

* [Git](https://git-scm.com)
* [Python](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)

### Em seguida:

```bash
# Clone o repositório
$ git clone git@github.com:Dev-JoseRonaldo/product-code-bar .git

# Acesse a pasta do projeto no terminal/cmd
$ cd product-code-bar 

# Abra essa pasta em seu editor de texto favorito
$ code .

# Instale as dependências presentes no arquivo requirements.txt
$ pip install -r requirements.txt

# Inicie o serrvidor:
# Execute o arquivo run.py que está na raiz do repositório

# O servidor inciará localmente na porta:3000 (http://localhost:3000/)
```

<br>

## 🧭 Rotas

#### ``[POST] /create_tag`` : Cria um código de barra para o código de produto especificado. 
Exemplo de corpo de requisição aceito:
```json
{
  "product_code": "9 789870 254652"
}
```

<br>

## ⚙️ Comandos úteis

`pytest -s -v`: Executa todos os testes

<br>

## 📝 Licença

  Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/Dev-JoseRonaldo/product-code-bar/blob/main/LICENSE) para mais detalhes.

---

Feito com ♥ by José Ronaldo :wave:
