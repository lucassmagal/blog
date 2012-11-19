title: Começando a programar em Go
published: 2012-09-06
slug: comecando-programar-em-go

Com a greve das federais perto de terminar, é hora de voltar a fazer algo
produtivo, então resolvi aprender Go, uma linguagem de programação C-like
que uns caras do Google desenvolveram.

Não vou falar muito de história, diz a
[Wikipedia](http://en.wikipedia.org/wiki/Go_%28programming_language%29)
que a linguagem foi anunciada no final de 2009, dá uma olhada lá.
As características principais eram uma sintaxe que lembrava C (mas muito,
muito mais enxuta), suporte nativo à
programação concorrente e características de linguagens dinâmicas
(como inferência de tipos).

### Por que Go?

Acabei me interessando pela linguagem após ver diversos desenvolvedores
postando suas impressões. O primeiro que li,
[5 weeks of Go](http://blog.iandavis.com/2012/05/23/5-weeks-of-go/), já me deu uma
boa introdução das características da linguagem. Há alguns posts interessantes
[aqui também](http://areyoufuckingcoding.me/),
inclusive em um deles o autor argumenta se a linguagem é
realmente orientada a objetos ou não, mas isso fica pra outro dia.

### Sintaxe básica

Como eu disse acima, Go é C-like, mas alguns aspectos da linguagem certamente
o farão se lembrar de Pascal ou Python. Felizmente (ou não, depende do seu
gosto), Go simplificou a sintaxe ao máximo possível: não há ponto e vírgula,
por exemplo. Também não existe bloco while ou do-while, em Go só existe for:

<pre>
<code class="go">
// Direto do Effective Go
// http://golang.org/doc/effective_go.html#for

// Like a C for
for init; condition; post { }

// Like a C while
for condition { }

// Like a C for(;;)
for { }
</code>
</pre>

Outra simplificação: não há parênteses nos blocos, você escreve if condition
{ } ao invés de if(condition) { }. A propósito, em Go as chaves são
obrigatórias, mesmo que seu bloco só contenha um comando.

Declarar variáveis em Go permite algumas simplificações, tudo para evitar a
redundância. Os exemplos abaixo são equivalentes:

<pre><code class="go">
// Variáveis são declaradas usando a palavra reservada 'var'
// Em Go, os tipos são declarados após o nome das variáveis
var foo int
foo = 3

// Também dá pra encurtar, em uma única linha
var foo int = 3

// O jeito mais curto, no entanto, usa o operador :=
// O código abaixo é exatamente igual aos dois anteriores
// Go irá inferir o tipo a partir do valor atribuído
foo := 3
</code></pre>

Não vou me estender muito pois eu acabaria escrevendo demais =S
Eu resolvi praticar a linguagem resolvendo alguns problemas clássicos de
dojos, que podem ser encontrados [aqui](http://dojopuzzles.com/).

Para o próximo post vou resolver o problema do
[Caixa Eletrônico](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/), explicando
tudo passo-a-passo e aplicando o TDD. Já fiz uma
[versão preliminar](https://gist.github.com/3660567) que
funciona usando algumas coisas interessantes, como a lib testing e slices
(em Go, arrays estáticos e dinâmicos são tipos de dados distintos).
