# Diretórios e Arquivos

Este documento fornece tanto uma visão geral da estrutura de diretórios quanto uma descrição dos arquivos do projeto front-end da PNP.

## Visão geral do projeto

- 📂 frontend
  - [📂 .storybook](#storybook)
  - [📂 docker](#docker)
  - [📂 generators](#generators)
  - [📂 node_modules](#node_modules)
  - [📂 public](#public)
  - [📂 src](#src)
  - [📄 .env](#env)
  - [📄 .eslintrc.json](#eslintrc)
  - [📄 .prettierrc](#prettierrc)
  - [📄 docker-compose.yml](#docker-compose)
  - [📄 index.html](#index)
  - [📄 package.json](#package)
  - [📄 tsconfig.json](#tsconfig)
  - [📄 tsconfig.node.json](#tsconfig.node)
  - [📄 vite.config.ts](#vite)
  - [📄 yarn.lock](#yarn)

<br>

<a name="storybook"></a>
- 📂 **.storybook —** _Diretório que define a configuração do ambiente de documentação de componentes da aplicação._ 

<br>

<a name="docker"></a>
- 📂 **docker —** _Diretório que armazena configurações de criação de imagem docker da aplicação._

  - 📄 **.dockerignore —** _Arquivo que especifica quais arquivos e diretórios devem ser excluídos durante o processo de construção de uma imagem Docker._

  - 📄 **Dockerfile —** _Arquivo de Script com instruções utilizadas para criar uma imagem da aplicação._

<br>

<a name="generators"></a>
- 📂 **generators —** *Diretório que configura utilitários automatizados e personalizados para a aplicação.*

    - 📂 **templates —** *Diretório que armazena os templates base dos arquivos que serão gerados.*
        
        - 📄 **index.tsx.hbs —** *Arquivo modelo para gerar um arquivo "index.tsx" para um componente React.*
        
        - 📄 **stories.tsx.hbs —** *Arquivo modelo para gerar um arquivo de histórias (stories) para um componente React, geralmente usado em conjunto com ferramentas como o Storybook para documentar e visualizar componentes.*
        
    
    - 📄 **plopfile.js —** *Arquivo responsável pela geração automática de arquivos, podendo este ser um componente ou um storybook.*

<br>

<a name="node_modules"></a>
- 📂 **node_modules —** *Diretório que armazena as dependências do projeto.*

<br>

<a name="public"></a>
- 📂 **public —** *Diretório que armazena arquivos estáticos que não precisam passar por processamento durante a construção da aplicação.*

<br>

<a name="src"></a>
- 📂 **src** **—** *Diretório que armazena o código fonte do projeto. Para mais detalhes,[ clique aqui.](#visaoSRC)*

<br>

<a name="env"></a>
- 📄 **.env —** *Arquivo que armazena variáveis de ambiente da aplicação.*

<br>

<a name="eslintrc"></a>
- 📄 **.eslintrc.json —** *Arquivo usado para configurar as regras do ESLint no projeto.*

<br>

<a name="prettierrc"></a>
- 📄 **.prettierrc —** *Arquivo usado para configurar as opções do Prettier.*

<br>

<a name="docker-compose"></a>
- 📄 **docker-compose.yml —** *Arquivo usado para definir e configurar serviços, redes e volumes em um ambiente Docker.*

<br>

<a name="index"></a>
- 📄 **index.html —** *Arquivo responsável por carregar todos os recursos necessários para a aplicação.*

<br>

<a name="package"></a>
- 📄 **package.json —** *Arquivo que mantém as dependências do projeto e suas versões, scripts de construção e outras configurações importantes.*

<br>

<a name="tsconfig"></a>
- 📄 **tsconfig.json —** *Arquivo que define as configurações para o compilador TypeScript, especificando como o TypeScript deve transpilar o código TypeScript para JavaScript*.

<br>

<a name="tsconfig.node"></a>
- 📄 **tsconfig.node.json —** *Arquivo usado para configurar o ambiente Node.js em que o Typescript é executado.*

<br>

<a name="vite"></a>
- 📄 **vite.config.ts —** *Arquivo usado para configurar e personalizar as opções de construção do Vite.*

<br>

<a name="yarn"></a>
- 📄 **yarn.lock —** *Arquivo usado garantir que a instalação das dependências do projeto seja reproduzível e consistente em diferentes ambientes.*

<br>

<a name="visaoSRC"></a>
## Visão geral do diretório “src”

- 📂 src
  - [📂 assets](#assets)
  - [📂 components](#components)
  - [📂 features](#features)
  - [📂 hooks](#hooks)
  - [📂 interfaces](#interfaces)
  - [📂 pages](#pages)
  - [📂 routes](#routes)
  - [📂 services](#services)
  - [📂 states](#states)
  - [📂 utils](#utils)
  - [📄 App.tsx](#App)
  - [📄 declarations.d.ts](#declarations)
  - [📄 index.css](#index)
  - [📄 main.tsx](#main)
  - [📄 scaffold.tsx](#scaffold)
  - [📄 vite-env.d.ts](#vite-env)

<br>

<a name="assets"></a>
- 📂 **assets —** *Diretório responsável por armazenar arquivos estáticos que precisam ser processados ou importados pelo sistema de build do React.*
    
    - 📂 **cards —** *Diretório que armazena ícones dos cartões referentes às funcionalidades do sistema.*
    
    - 📂 **errors —** *Diretório que armazena ilustrações relacionadas a erros possíveis durante uso do sistema.* 
    
    - 📂 **logos —** *Diretório que armazena imagens de variações da logo da aplicação.*

<br>

<a name="components"></a>
- 📂 **components —** *Diretório que contém componentes globais, os quais podem ser acessados e utilizados em qualquer parte do projeto. Pode ser considerado como uma entidade compartilhada em toda a aplicação.*

    - 📂 **BrComponenteExemplo** — *Diretório de exemplo de um componente.*
        
        - 📄 **BrComponenteExemplo.stories.tsx** — *Arquivo de documentação do componente.*
        
        - 📄 **index.tsx** **—** *Arquivo de implementação da lógica interna do componente.*
        
        - 📄 **styles.css —** *Arquivo que define classes de estilização do componente.*
        
        - 📄 **subComponente.tsx —** *Arquivo opcional de implementação de um subcomponente local. Para cada subcomponente necessário, um arquivo deve ser criado.* 
    
    - 📄 **index.tsx —** *Arquivo barril que concentra todas as exportações globais, a fim de simplificar as importações dos mesmos em outros locais do projeto.*

<br>

<a name="features"></a>
- 📂 **features —** *Diretório que armazena as diferentes funcionalidades do projeto.*

    - 📂 **ExemploDeFuncionalidade —** *Diretório de exemplo da estrutura base de uma funcionalidade.*
        
        - 📂 **components —** *Diretório que armazena componentes específicos de uma funcionalidade.*
        
        - 📂 **forms —** *Diretório que armazena todos os arquivos de formulário que estão relacionados à funcionalidade.*
            
            - 📄 **delete.tsx —** *Arquivo de formulário de exclusão de uma entidade.*
            
            - 📄 **detail.tsx —** *Arquivo de visualização de uma entidade.*
            
            - 📄 **register.tsx —** *Arquivo de formulário de registro de uma entidade.*
            
            - 📄 **schema.ts —** *Arquivo de definição das validações dos formulário.*
            
            - 📄 **sections.ts —** *Arquivo de definição das seções e dos campos do formulário. Esse arquivo só é necessário quando se utiliza o componente BrFormGenerator para gerar algum dos formulários.*
            
            - 📄 **update.tsx —** *Arquivo de formulário de edição de uma entidade.*
            
        - 📂 **interfaces —** *Diretório que armazena interfaces locais da funcionalidade.*
            
            - 📂 **components —** *Diretório com interfaces locais dos componentes da funcionalidade.*
            
            - 📂 **filters —** *Diretório com interfaces locais dos filtros da funcionalidade.*
            
        
        - 📂 **pages —**  Diretório que armazena páginas específicas da funcionalidade.*
        
        - 📄 **index.tsx —** *Arquivo principal da funcionalidade.*
        
        - 📄 **styles.css —** *Arquivo de estilização da funcionalidade.*
        
    - 📂 **ExemploDeAgrupamentoDeFuncionalidades —** *Diretório exemplo de agrupamento de funcionalidades com algum grau de semelhança entre si.*
        
        - 📂 **ExemploDeFuncionalidade01**
        
        - 📂 **ExemploDeFuncionalidade02** 
        
        - 📂 **ExemploDeFuncionalidade03**
        
        - 📄 **index.ts —** *Arquivo que exporta todas as funcionalidades do agrupamento.*

<br>

<a name="hooks"></a>
- 📂 **hooks —** *Diretório que armazena hooks personalizados para a aplicação.*

    - 📄 **useAuth.ts —** *Arquivo usado para manipular os dados do usuário.*

    - 📄 **useCan.ts —** *Arquivo que gerência as permissões do usuário a depender de seu papel.*

<br>

<a name="interfaces"></a>
- 📂 **interfaces —** *Diretório armazena arquivos de definição de tipos (type definitions) ou interfaces TypeScript.* 

    - 📂 **components —** *Diretório que armazena arquivos de interfaces que definem a assinatura das props de cada componente global da aplicação.*

    - 📂 **filters —** *Diretório que armazena arquivos de interfaces contendo filtros genéricos (paginação, busca etc.) e específicos de todos os modelos da aplicação da PNP.*
        
        - 📂 **common —** *Diretório que armazena interfaces comuns que são usadas como base para outras interfaces de filtros.*
        
        - 📄 **exemploFilter.ts —** *Arquivo de exemplo de filtro.*
        
    - 📂 **models —** *Diretório que armazena arquivos de interfaces que definem a assinatura dos atributos de cada modelo da aplicação da PNP.*
        
        - 📂 **common —** *Diretório que armazena interfaces comuns que são usadas como base para outras interfaces de modelos da PNP.*
        
        - 📄 **iExemplo.ts —** *Arquivo de exemplo de interface de modelo.*
        
    - 📂 **services —** *Diretório que armazena arquivos de interfaces específicas que são necessárias para lidar com algumas comunicações  com a API.*
        
        - 📂 **common —** *Diretório que armazena interfaces comuns que são usadas como base para outras interfaces de serviços.*
        
        - 📄 **iExemploService.ts —** *Arquivo de exemplo de interface de serviço*.

<br>

<a name="pages"></a>
- 📂 **pages —** *Diretório que armazena páginas globais da aplicação.*

<br>

<a name="routes"></a>
- 📂 **routes —** *Diretório que contém as definições e configurações dos arquivos relacionados ao roteamento do front-end, gerenciando as diferentes rotas (URLs) do aplicativo e determinando qual componente deve ser renderizado em cada rota específica.*
    
    - 📄 **index.tsx —** *Arquivo responsável por gerenciar e controlar o acesso às rotas públicas e privadas da aplicação.*
    
    - 📄 **modelsRoutes.tsx —** *arquivo que define, agrupa e concentra as rotas de acordo com os modelos da aplicação em um único lugar, visando melhorar a organização, diminuir a repetição de código e facilitar eventuais alterações em rotas.*
    
    - 📄 **protected.tsx —** *Arquivo que define rotas protegidas que exigem autenticação.*
    
    - 📄 **public.tsx —** *Arquivo que define rotas públicas que não requerem autenticação.*

<br>

<a name="services"></a>
- 📂 **services —** *Diretório que contém arquivos relacionados a configuração e definição de serviços, a fim de lidar com a comunicação com APIs externas.*

    - 📂 **common —** *Diretório que define configurações que são comuns a todos os serviços da aplicação.*
        
        - 📄 **axiosInstance.ts —** *Arquivo de definição e configuração do cliente de requisições utilizado.*
        
        - 📄 **baseService.ts —** *Arquivo de Definição e configuração de classes e métodos HTTP comuns a todos os serviços (GET, POST, DELETE etc.).*
        
        - 📄 **headers.ts —** *Arquivo que define headers necessários para requisições com a API da PNP.*
        
    - 📂 **models —** *Diretório que contém arquivos que definem o endereço raiz de cada modelo nas rotas da API da PNP.*

<br>

<a name="states"></a>
- 📂 **states —** *Diretório que armazena e manipula estados que são persistidos em toda a aplicação.*
    - 📄 **userState.ts —** *Arquivo que persiste e manipula informações do usuário autenticado de forma global.*

<br>

<a name="utils"></a>
- 📂 **utils —** *Diretório que armazena arquivos de utilitários ou funções Javascript auxiliares e reutilizáveis.*

<br>

<a name="App"></a>
- 📄 **App.tsx —** *Arquivo que é usado para definir a estrutura global da aplicação.*

<br>

<a name="declarations"></a>
- 📄 **declarations.d.ts —** *Arquivo que define as tags do Web Components do GOV BR.*

<br>

<a name="index"></a>
- 📄 **index.css —** *Arquivo de estilização global da aplicação.*

<br>

<a name="main"></a>
- 📄 **main.tsx —** *Arquivo que serve como ponto de entrada da aplicação.*

<br>

<a name="scaffold"></a>
- 📄 **scaffold.tsx —** *Arquivo que mantém a estrutura básica que as páginas do projeto possuem.*
