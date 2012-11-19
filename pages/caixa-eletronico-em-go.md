title: Dojo do Caixa Eletrônico em Go
published: 2012-09-07
slug: caixa-eletronico-em-go

Pra mim não tem jeito melhor de aprender uma nova linguagem ou ferramenta do
que praticando. O meu roteiro pra entender uma nova linguagem é iniciar sempre
resolvendo alguns desafios lógicos, mais comuns em dojos, e então depois ir
aumentando a dificuldade, procurando algo que se pareça mais com um aplicativo
completo (site web, um programa com GUI, etc.).

Pra pegar o básico de Go, então, abri o [DojoPuzzles](http://dojopuzzles.com/)
e fui escolhendo alguns desafios que gostaria de resolver. O primeiro deles,
o [Caixa Eletrônico](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/),
é assim: dada uma quantia que o usuário queira sacar, o caixa eletrônico deve
entregar o menor número possível de cédulas. Na minha implementação a máquina
tinha uma quantidade infinita de todas as cédulas: 100, 50, 20, 10, 5, 2 e 1.

Para configuração inicial, criei uma pasta chamada "caixa-eletronico" com dois
arquivos: caixa_eletronico.go e caixa_eletronico_test.go. Como em todo dojo
que se preze, devemos começar o desenvolvimento escrevendo um teste que falhe,
então vamos começar escrevendo o código para caixa_eletronico_test.go.
(se não sabe como funciona um dojo,
[entenda aqui](http://pet.inf.ufsc.br/dojo/o-que-eh-dojo/)).

Uma parte interessante da linguagem Go é que ela já vem com um pacote chamado
[Testing](http://golang.org/pkg/testing/), que automatiza a execução de testes.
Basicamente, toda função com o nome TestXxx e que esteja dentro de um arquivo
_test.go é um teste, e será executado através do comando go test
(mais sobre ele depois). Um exemplo:

<pre><code class="go">
// arquivo soma_test.go
package soma

import "testing"

func TestSoma(t *testing.T) {
    if Soma(2,3) != 5 {
        t.Error("Soma(2,3)) devia dar 5!")
    }
}
</code></pre>

Escrever testes em Go funciona da seguinte forma: todo teste deve ter um nome
que siga a regra TestXxx e receber t *testing.T como parâmetro. Percebem o "*"?
Isso é passagem por referência (bons tempos de C... só que não). Se, em algum
momento dentro da função, t.Error ou t.Fail forem chamados, então o teste é
considerado uma falha. No exemplo acima, se Soma(2,3) for diferente de 5,
então t.Error é chamado e o teste falhará.

Ainda sobre o código acima, vale comentar algumas características da
linguagem: em Go o tipo vai depois da variável. Assim, "int foo" é "foo int".
Retornos de funções funcionam da mesma forma:

<pre><code class="go">
// Uma função sem retorno (algo como "void PrintHello() em C")
func PrintHello() {
    fmt.Print("Hello!")
}

// Uma função que retorna um int
func Soma(a int, b int) int {
    return a+b
}
</code></pre>

Em Go a visibilidade de uma função é definida se seu primeiro caractere é
maiúsculo ou não: funções em maiúsculo são acessíveis fora de seu pacote,
em minúsculo são funções privadas.

Beleza, sabendo como testes funcionam, vamos criar o nosso teste. Neste caso,
estou usando um novo [pacote](https://github.com/bmizerany/assert) para
validar os testes de forma menos verbosa.
Para usá-lo, você deve antes instalá-lo. Assumindo que você instalou o
ambiente Go adequadamente, rode no terminal:

<pre><code class="bash">
go get github.com/bmizerany/assert
</code></pre>

Agora, o teste em si:

<pre><code class="go">
// arquivo caixa_eletronico_test.go
package caixa_eletronico

import (
    "testing"
    "github.com/bmizerany/assert"
)

func TestSaque(t *testing.T) {
    assert.Equal(t, Saque(83), []int{50, 20, 10, 2, 1})
}
</code></pre>

Você pode tentar rodar o teste acima indo até sua pasta "caixa-eletronico" no
terminal e rodando "go test". O teste, obviamente, irá falhar, pois não há
nenhuma função Saque escrita, então vamos escrevê-la:

<pre><code class="go">
// arquivo caixa_eletronico.go
package caixa_eletronico

func Saque(valor int) []int {
    cedulas := [7]int{100, 50, 20, 10, 5, 2, 1}
    resultado := []int{}

    for _, cedula := range cedulas {
        for valor >= cedula {
            resultado = append(resultado, cedula)
            valor -= cedula
        }
    }

    return resultado
}
</code></pre>

Não vou explicar a lógica da função, apenas as características da linguagem. Notem:

 - a função recebe um <code>int</code> e retorna um slice <code>[]int</code>.
   Slices, em Go, são como arrays,
   mas com tamanho flexível. São de certa forma semelhantes às listas em Python
   ou aos ArrayLists em Java
 - Defini duas variáveis, "cedulas", um slice contendo as notas que meu caixa
   eletrônico possui, e "resultado", um slice vazio que conterá as cédulas que
   serão sacadas
 - O for mais externo itera sobre os valores do slice "cedulas". O keyword
   <code>range</code> retorna sempre dois valores, o primeiro é a posição de um elemento,
   e o segundo é o seu valor (em Go funções podem retornar mais de um valor).
   Como só estamos interessados nos valores (as cédulas em si), ignorei as
   posições usando "_".
 - O for mais interno se assemelha a um while: enquanto o valor a ser sacado
   for superior à cédula em questão, o código dentro dele será executado. Os
   comandos dentro deste for são mais triviais e conhecidos em outras linguagens,
   então não irei explicar

Se executarmos "go test" agora, o nosso teste irá, enfim, passar. Podemos agora
aumentar o nosso teste com outras asserções, só para garantir o funcionamento
da nossa lógica.

Para finalizar, uma alteração simples: em Go, os nossos retornos de funções
podem ser variáveis. Nesse caso, o último valor nessas variáveis será retornado
quando a função terminar, e é mais uma das formas de eliminar redundância na
linguagem. Reescrevendo nossa função anterior desta forma, ficaríamos assim:

<pre><code class="go">
// arquivo caixa_eletronico.go
package caixa_eletronico

func Saque(valor int) (resultado []int) {
    cedulas := [7]int{100, 50, 20, 10, 5, 2, 1}

    for _, cedula := range cedulas {
        for valor >= cedula {
            resultado = append(resultado, cedula)
            valor -= cedula
        }
    }

    return
}
</code></pre>

Obviamente, esse código funciona exatamente como o anterior. Deixei de lado
aqui a interação com o usuário, então está aberto a quem quiser complementar.
O código completo deste desafio pode ser acessado [aqui](https://gist.github.com/3660567).

Em outros posts devo entrar em detalhes sobre algumas características da
linguagem, como arrays vs slices, funções com retornos múltiplos, pacotes e
etc. Como próximo desafio, vou fazer um servidor de arquivos estáticos
(tipo um <code class="python">Python -m SimpleHTTPServer</code>) apenas para exercitar, nada para ser
usado em produção.
