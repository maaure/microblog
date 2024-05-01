# Guia de Contribuição

Este guia padroniza e explica o que é necessário para contribuir com o repositório **pnp-frontend**, no que diz respeito ao trabalho em equipe por meio de _issues_, _branchs_, _commits_, _merge requests_ etc.

### **1. Issues**

**1.1.** Verifique as [_issues_ existentes](https://gitlab.ifrn.edu.br/pnp/pnp-frontend/-/issues) que estão sem atribuição. Caso haja, é possível atribuir-se a uma, informar o prazo que pretende finalizá-la e então começar a trabalhar nela.

**1.2.** Se não houver nenhuma _issue_ disponível, pode-se criar uma nomeando-a com o padrão a seguir:

Formato:

> [verbo de ação no infinitivo] [descrição específica]

Exemplo:

> Corrigir erro gramatical no título da página de listagem de programas

**1.3.** Sempre durante a criação de uma _issue_, descreva detalhadamente qual o objetivo dela, visando facilitar possíveis consultas e/ou contribuições posteriores.

Exemplo:

> O título da página de listagem de programas está como "Progamas", mas deve ser corrigido para "Programas".

**1.4.** Verifique as [labels disponíveis](https://gitlab.ifrn.edu.br/pnp/pnp-frontend/-/labels) e relacione-as semanticamente com sua _issue_, conforme a proposta desta.

Ao final desse tópico, é possível ter uma issue atribuída a si.

### 2. Branchs

**2.1.** Crie uma _branch_ a partir da issue, mantendo a recomendação do Git referente ao nome da _branch_ ser equivalente ao nome da _issue_.

> Por padrão, deve-se utilizar a branch "dev" como fonte para criar a nova branch. Essa prática ajuda a reduzir a quantidade de conflitos e a manter o fluxo de desenvolvimento ágil.

Exemplo de issue:

> Corrigir erro gramatical no título da página de listagem de programas

Exemplo de branch:

> 80-corrigir-erro-gramatical-no-titulo-da-pagina-de-listagem-de-programas

Ao final desse tópico, é possível ter uma _branch_ de trabalho para sua _issue_.

### 3. Commits

**3.1.** Registre cada alteração objetiva por meio de um _commit_, o qual deve seguir o guia de mensagens de _commits_ do [GOVBR](https://govbr-ds.gitlab.io/tools/govbr-ds-wiki/git-gitlab/guias/commit/). Leia-o atentamente a fim de entender sobre padronização e boas práticas de _commits_, assim como o uso de prefixos nas mensagens, como _feat_, _fix_, _docs_ etc. que também podem ser verificados no guia mencionado acima.

**3.2.** Ao realizar um _commit_, no final da mensagem insira uma **#** (_hashtag_) seguida do número da _issue_ do repositório **pnp-frontend** que este _commit_ está relacionado.

Formato:

> \[prefixo]: [mensagem]. (#[issue-frontend])

Exemplo:

> feat: adiciona icone da PNP como favicon. (#26)

**3.3.** Quando o _commit_ estiver relacionado a uma história de usuário (HU), insira outra **#** seguida do número da issue presente no repositório **pnp-doc** referente a essa HU, visando manter a organização dos repositórios e facilitar o rastreamento de _commits_.

Formato:

> \[prefixo]: [mensagem]. (#[issue-frontend]) (pnp-doc#[issue-hu])

Exemplo:

> fix: corrige gramatica do titulo da pagina de listagem de programas. (#80) (pnp-doc#39)

Em que **#80** é a referência para uma issue do repositório de desenvolvimento “pnp-frontend" e **pnp-doc#39** se refere ao nome do repositório de documentação seguida da issue da história de usuário que será referenciada.

Ao final desse tópico, é possível registrar _commits_ em sua _branch_ de trabalho.

### **4.** Merge Requests

**4.1.** Quando houver finalizado o que sua issue se propõe a realizar, solicite um _merge request_ (MR) para a _branch_ **dev**, se coloque como responsável (_Assignee_) e selecione um revisor para esse procedimento. Sua solicitação será analisada e poderá ser aceita ou rejeitada.

**4.2.** Os _merge requests_ não aprovados possuem comentários feitos pelo revisor acerca dos motivos pelos quais ele não foi aceito. Realize os ajustes necessários e informe ao revisor que deseja uma nova análise e aguarde a resposta.

Ao final desse tópico, é possível abrir _merge requests_ que visam contribuir com o projeto.
