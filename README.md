## Guia do Desenvolvedor

O guia do desenvolvedor disponível abaixo pode ser resumido como um documento que concentra todas as orientações sobre como o projeto está estruturado, quais os padrões de implementação e de estilização utilizados, como é possível contribuir com o repositório, entre muitas outras informações importantes que devem ser consultadas.

> [Guia do desenvolvedor](./guia-desenvolvedor.md)

<details open>
  <summary><h2>1. Execução com Docker</h3></summary>
  
  #### Crie a imagem da aplicação:
  
  ```
  docker build -t microblog-api .
  ```
  
  #### Execute a imagem da aplicação:
  
  ```
  docker run -p 8000:8000 microblog-api
  ```
  </details>

<details>
  <summary><h2>2. Execução com Python</h3></summary>
  
  #### Clone o repositório:
  
  ```
  git clone https://github.com/maaure/microblog.git
  ```
  
  #### Acesse o diretório gerado:
  
  ```
  cd microblog
  ```
  
  #### Crie um ambiente virtual:
  
  ```
  python -m venv venv
  ```
  
  #### Ative o ambiente virtual (Linux):
  
  ```
  . venv/bin/activate
  ```
  
  #### Ative o ambiente virtual (Windows):
  
  ```
  .\venv\Scripts\activate
  ```
  
  #### Instale as dependências:
  
  ```
  pip install -r requirements.txt
  ```
  
  #### Aplique as migrações:
  
  ```
  python manage.py migrate
  ```
  
  #### Execute a aplicação:
  
  ```
  python manage.py runserver
  ```
  
  #### Abra a aplicação no navegador:
  
  ```
  http://localhost:8000/api/doc/
  ```

</details>
