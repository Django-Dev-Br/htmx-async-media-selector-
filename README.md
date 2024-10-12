# htmx-async-media-selector-
AsyncMediaSelector é um projeto web interativo desenvolvido com Django, HTMX e Bootstrap. Ele permite a seleção dinâmica de imagens por meio de requisições assíncronas, utilizando o poder do HTMX para realizar trocas de conteúdo diretamente no DOM, sem a necessidade de JavaScript explícito.


## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com PIP e venv**
- **o Django 5 requer Python 3.10 ou superior.**

- **No [repositório 001](https://github.com/Django-Dev-Br/001-django4-basic-project) há explicações sobre PIP e venv**

  Se necessário, confira o vídeo abaixo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):
 [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)


### Passos a passo para Executar em 6 etapas simples

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Django-Dev-Br/001-django5-basic-project.git
    ```

2. **Crie  um ambiente virtual no diretório root**:

   **Windows**
    ```bash
     python -m venv myvenv 
    ```
      **Linux**
     ```bash
     python3 -m venv myvenv  
    ```

3. **Ative o ambiente virtual criado**:

   **Windows**
    ```bash
    myvenv\Scripts\activate  
    ```

     **Linux**
    ```bash
    source myvenv/bin/activate  
    ```
    
4. **Acesse a pasta do projeto Django**:
    ```bash
    cd 001-django4-basic-project
    ```
    
5. **Instale o Django**:

   Fazer a instalação após a ativação da virtual env fará com que a instalação seja feita nessa pasta ao invés do computador. Isso significa que o pacote Django não estará disponivel para todos os usuários do computador, mas apenas para o contexto no qual essa venv esteja ativada. Veremos sua ativação logo abaixo.

    **Instalação manualmente via gerenciador de dependências PIP**
    ```bash
    pip install django
    ```
    - use, preferencialmente, a versão 5.1. Para tanto, execute o comando:

     ```bash
    pip install  "django>=5.1,<=5.2"
    ```

    ----- **OU** -----

    **Instalação via arquivo requirements**
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo requirements.txt é um arquivo de texto que contém uma lista de pacotes a ser instalado em uma venv. É uma boa prática de programação do ecossistema Python.

6. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Acesse no seu navegador o endereço a seguir:

http://127.0.0.1:8000/


### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevSecOps Full-stack com Python, Django, Bootstrap, Git Workflow e VPS Linux. 

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

### Junte-se a nós! 
E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
