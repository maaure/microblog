<details open>
  <summary><h2>2.1. Execução com Docker</h3></summary>
  
  #### Crie a imagem da aplicação:
  
  ```
  docker build -t API .
  ```
  
  #### Execute a imagem da aplicação:
  
  ```
  docker run -p 8000:8000 API
  ```
  </details>

<details>
  <summary><h2>2.2. Execução com Python</h3></summary>
  
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
