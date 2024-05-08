# Padrões de Implementação

Este guia estabelece diretrizes de nomenclatura e formatação para o desenvolvimento de componentes, interfaces de modelo, classes de serviço, além de outros elementos usados na implementação do front-end da Plataforma Nilo Peçanha.

O objetivo dessas diretrizes é promover uma padronização no código, facilitando a leitura, manutenção e colaboração entre os membros da equipe de desenvolvimento. Além disso, a consistência na nomenclatura e formatação ajuda a reduzir erros e garantir a qualidade do código produzido.

# Sumário

- [Nomenclatura](#nomenclatura)
  - [Componentes](#nomenclatura_componentes)
  - [Classes de Serviço](#classes_servico)
  - [Interfaces](#interfaces)
- [Formatação](#formatacao)
  - [Indentação e Alinhamento](#indentacao_alinhamento)
  - [Aspas](#aspas)
  - [Ponto e Vírgula](#ponto_virgula)
  - [Espaços](#espacos)
  - [Parênteses](#parenteses)
  - [Props](#props)
  - [Tags](#tags)
  - [Comprimento da Linha](#comprimento_linha)
  - [Funções](#funcoes)
  - [Componentes](#componentes)
  - [Variáveis e Parâmetros](#variaveis_parametros)

# Nomenclatura <a name="nomenclatura"></a>

## Componentes <a name="nomenclatura_componentes"></a>

- Utilize _`PascalCase`_ para nomear os componentes;
- Omita preposições nos nomes dos componentes. Por exemplo “Barra de Progresso”, deverá ser `BarraProgresso` ;
- Adicione o prefixo `Br` para os componentes. Por exemplo, `BrBarraProgresso` .
  - Observação: Não é necessário adicionar a preposição `Br` em componentes que só existem para compor outros componentes, ou seja, aqueles componentes que não são importados diretamente nas páginas.
- O arquivo em que o componente é implementado deve ser chamado `index.tsx` ;
- Nomeie o diretório do componente com o mesmo nome do componente.

## Classes de Serviço <a name="classes_servico"></a>

- Utilize `PascalCase` para nomear as classes de serviço.
- Nomeie o serviço adicionando o sufixo `Service` ao nome do recurso da _API_ que será consumido. Por exemplo, `InstituicaoService`, para o recurso "Instituição".

## Interfaces <a name="interfaces"></a>

- Modelo

  - Utilize _`PascalCase`_ para nomear as interfaces de modelo precedidos por um “i” minúsculo.
  - Nomeie a interface com o nome da entidade que está sendo definida pela interface. Por exemplo, ao se tratar da entidade Inconsistência de Ensino, use: `iInconsistenciaEnsino`.

- Props

  - Utilize o mesmo nome do componente sucedido de “Props”. Por exemplo `BrBarraProgressoProps`, para o componente `BrBarraProgresso`.
  - O arquivo em que as props são definidas deve ser nomeado com o prefixo “i” + o nome do componente. Por exemplo `BrBarraProgressoProps` deve ser salvo em um arquivo chamado `iBrBarraProgresso`.

- Filtros de Serviço

  - Nomeio o filtro adicionando o sufixo `Filter` ao nome do serviço que será filtrado. Por exemplo, `InstituicaoFilter`, para `InstituicaoService`.

- Interface de Serviço
  - Devem ser nomeadas utilizando o padrão `iNomeService`, onde "Nome" representa o recurso da API que será consumido. Por exemplo, se estamos lidando com o recurso "Instituição", a interface de serviço correspondente seria nomeada como `iInstituicaoService`.

# Formatação <a name="formatacao"></a>

## Indentação e Alinhamento <a name="indentacao_alinhamento"></a>

- Utilize _tabs_ em vez de espaços para a indentação.
- Configure o tamanho da tabulação como **4 espaços**.
- Todos elementos **JSX** de múltiplas linhas deve ter seu colchete de fechamento alinhado com o de abertura. Por exemplo:

```jsx
// ruim
<Componente
	parametro1="Parametro1"
	parametro2="Parametro2" />;

// ruim
<Componente
	parametro1="Parametro1"
	parametro2="Parametro2"
  	/>;

// bom
<Componente
	parametro1="Parametro1"
	parametro2="Parametro2"
/>;
```

## Aspas <a name="aspas"></a>

Utilize **aspas duplas** para strings, em vez de aspas simples.

```jsx
// ruim
<BrButton
	size='small'
/>;

// bom
<BrButton
	size="small"
/>;
```

## Ponto e Vírgula <a name="ponto_virgula"></a>

Sempre insira um ponto e vírgula no final de cada instrução. Por exemplo:

```jsx
const { user } = useStore();

useEffect(() => {
	loadTable();
}, []);
```

## Espaços <a name="espacos"></a>

- Sempre inclua um único espaço no fechamento de suas tags que não recebem `childrens`.

```jsx
// ruim
<Foo/>

// ruim
<Foo                 />

// ruim
<Foo
 />

// bom
<Foo />
```

- Inclua espaços quando as chaves envolverem uma variável. Por exemplo:

```jsx
// ruim
const {user} = useStore();

// bom
const { user } = useStore();
```

- Não deve-se usar espaços dentro das chaves de parâmetros de um componente. Por exemplo:

```jsx
// ruim
<BrTable
	data={ instituicoes }
	title="Instituições"
/>

// bom
<BrTable
	data={instituicoes}
	title="Instituições"
/>
```

## Parênteses <a name="parenteses"></a>

- Sempre inclua parênteses em torno do parâmetro de uma _`arrow function`_.

Exemplo:

```tsx
const minhaFuncao = (parametro) => {
	return parametro + 1;
};
```

## Props <a name="props"></a>

- Sempre use `camelCase` para nome de props.

```jsx
// ruim
<Componente
	UserName="hello"
	phone_number={12345678}
/>

// bom
<Componente
	userName="hello"
	phoneNumber={12345678}
/>
```

- Quando o valor Booleano for `true`, ele pode ser omitido.

```jsx
// ruim
<Component
	hidden={true}
/>

// bom
<Component
  	hidden
/>
```

- Sempre que puder, evite usar `index` como `key` de props. Opte por um `ID`.

```jsx
// ruim
{todos.map((todo, index) =>
	<Todo
		{...todo}
		key={index}
	/>
)}

// bom
{todos.map(todo => (
	<Todo
		{...todo}
		key={todo.id}
  	/>
))}
```

## Tags <a name="tags"></a>

- Sempre utilize tags **auto-fecháveis** para elementos que não possuem filhos.

```jsx
// ruim
<BrIcon icon="times"></BrIcon>

// bom
<BrIcon icon="times" />

// ruim
<img src="..."></img>

// bom
<img src="..."/>
```

- Quando o elemento **HTML** ou **JSX** tiver mais de uma propriedade, feche a tag em uma nova linha.

```jsx
// ruim
<BrButton
	secondary
	icon="times"
	circle />

// bom
<BrButton
	secondary
	icon="times"
	circle
/>
```

- Quando o elemento **HTML** ou **JSX** tiver mais de uma propriedade, alinhe-as horizontalmente.

```jsx
// ruim
<BrButton
	secondary
		icon="times"
		circle
/>

// bom
<BrButton
	secondary
	icon="times"
	circle
/>
```

## Comprimento da linha <a name="comprimento_linha"></a>

Recomenda-se que as linhas não ultrapassem em excesso `80` caracteres de comprimento.

## Funções <a name="funcoes"></a>

- Ao declarar funções sempre opte pela declaração tradicional de função usando a palavra reservada `function` .

```jsx
// ruim
const soma = (a: number, b: number): number => a + b;

// ruim
const soma = function(a: number, b: number): number => {
	return a + b;
}

// bom
function soma(a: number, b: number): number {
	return a + b;
}
```

> Apesar de mais compacta em alguns casos, a declaração de `arrow functions` (que utiliza a palavra `const` ao invés de `function`) pode dificultar a leitura do código em algumas situações. Recomenda-se usar _arrow functions_ somente como [funções callback](https://developer.mozilla.org/pt-BR/docs/Glossary/Callback_function).

- Ao definir uma função, especifique os **tipos dos parâmetros**.

```tsx
// ruim
function soma(a, b): number {
	return a + b;
}

// bom
function soma(a: number, b: number): number {
	return a + b;
}
```

- Sempre defina o **tipo de retorno** da função.

```jsx
// ruim
function soma(a: number, b: number){
	return a + b;
}

// bom
function soma(a: number, b: number): number {
	return a + b;
}

// ruim
function helloWorld() {
	console.log("Olá, Mundo!");
}

// bom
function helloWorld(): void {
	console.log("Olá, Mundo!");
}
```

## Componentes <a name="componentes"></a>

- Ao implementar um componente _React_, **exporte-o** **diretamente na assinatura** da função que o define.

```jsx
// ruim
function BrButton(props: BrButtonProps): JSX.Element { ... }

export default BrButton;

// bom
export default function BrButton(props: BrButtonProps): JSX.Element { ... }
```

- Defina os componentes como **funções**.
  - Por se tratar de funções, respeite as regras descritas na seção [funções](#funcoes). Use funções tradicionais e defina o tipo do retorno da função.

```jsx
// ruim
const BrButton = (props: BrButtonProps) => { ... }

export default BrButton;

// bom
export default function BrButton(props: BrButtonProps): JSX.Element { ... }
```

### Variáveis e Parâmetros <a name="variaveis_parametros"></a>

- Sempre defina o **tipo da variável** no momento da declaração.

```tsx
// ruim
let idade;
const nome;
const estado = "RN";

// bom
let idade: number;
const nome: string;
const estado: string = "RN";
```

- Prefira o uso de `const` para declarar variáveis que não terão seu valor reatribuído.

```tsx
const pi: number = 3.14;
```

- Use `let` apenas para variáveis cujo valor precisará ser reatribuído durante a execução do programa.

```tsx
let contador: number = 0;
```

- Evite declarar variáveis que não serão utilizadas no código.

```tsx
// Evite isso
let variavelNaoUtilizada: string;
```
