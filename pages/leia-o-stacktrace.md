title: Leia o stacktrace
slug: leia-o-stacktrace
published: 2012-11-21

Uma das coisas que mais observava na época em que era monitor de programação
era que a maioria das pessoas, simplesmente, não liam os erros e warnings que
seus compiladores e interpretadores indicavam.. Muitas vezes diziam "o código
não está compilando, não consigo entender porquê" e quando eu verificava
eram erros de sintaxe, claramente indicados na primeira tentativa de compilação.
É interessante notar que esse comportamento ocorre, também,
*repetidas vezes* em fóruns e listas de discussão. Simplesmente jogam o
código com um "deu errado" e esperam que alguém resolva o problema, sem
ao menos terem usado o Google antes ou, obviamente, terem se dado ao trabalho
de ler o bendito stacktrace ou os reports de compilação.

Beleza, mas o que é, afinal, o stacktrace? A [Wikipedia](http://en.wikipedia.org/wiki/Stack_trace)
consegue explicar bem didaticamente, mas basicamente é um relatório da execução
do seu programa no momento do erro, e dá uma ajuda enorme na hora de entender
porquê o seu programa travou durante a execução. O Django, por exemplo, eu
posso ver todas as últimas chamadas a métodos até a ocorrência do erro,
inclusive seus argumentos. Em Python há o
[Traceback](http://docs.python.org/2/library/traceback.html), que me permite
manipular o stacktrace de um erro de diversas formas.

Claro, tirando algumas prováveis exceções (ainda não conheci nenhuma),
stacktraces são [feias de doer](http://www.urubatan.com.br/mensagens-de-erro-sao-feias-mas-nao-mentem-nem-mordem/).
Além disso, pra entender o que está ocorrendo é necessário o mínimo de conhecimento
na linguagem. Mas tranquilo, sempre tem [gente bacana](http://macoli.wordpress.com/2010/02/20/noobs-e-stacktraces/)
ensinando como interpretar esses reports *from hell*, e alguns frameworks
também ajudam bastante, como o Django. A partir daí, é ler e praticar mesmo.

Por que falo isso? Pra mim, é fundamental saber interpretar os errors e
warnings de um sistema, um dos passos pra se tornar *ninja* em uma linguagem,
e em programação em geral.

A propósito, stack traces só ajudam a encontrar bugs em tempo de execução...
mas na hora da compilação não tem segredo, é a mesma regra: leia e procure
entender. A documentação da linguagem provavelmente já documenta o que significa
cada erro e ter noção das Exceptions da biblioteca padrão da linguagem contribui
muito pra descobrir o que ocorreu - tipo as <code>NullPointerException</code>
que me fizeram sofrer pra entregar um trabalho em Java. Bônus: se você programa
em C, mesmo na faculdade, o compilador Clang exibe
mensagens de erro mais inteligíveis que o GCC.

