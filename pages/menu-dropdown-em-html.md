title: Fazendo um Menu Dropdown em HTML (com CSS e/ou JS)
published: 2012-09-11
slug: menu-dropdown-em-html

Acabei de fazer uma revisão no tema deste blog: a intenção era criar um menu
drop-down simples para deixar o visual mais limpo e, de quebra, já deixar o
caminho pavimentado para um layout responsivo.

Passei o fim de semana pesquisando e aprendi duas formas de se fazer, uma
usando apenas CSS e a pseudo-classe :hover e outra usando javascript. Como
ambas as formas são relativamente simples, irei explicar cada uma delas aqui
e então você decide de qual forma implementar =D

Vamos montar o nosso menu da seguinte maneira: uma lista não-ordenada, onde
cada item contem uma sub-lista. Veja:

<pre><code class="html">
&lt;!-- Execute este trecho em http://jsfiddle.net/aMRMF/ --&gt;
&lt;ul&gt;
  &lt;li&gt;
    &lt;a href="#"&gt;Menu 1&lt;/a&gt;
    &lt;ul&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 1&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 2&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 3&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/li&gt;
  &lt;li&gt;
    &lt;a href="#"&gt;Menu 2&lt;/a&gt;
    &lt;ul&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 4&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 5&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 6&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="#"&gt;Sub-item 7&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/li&gt;
&lt;/ul&gt;
</code></pre>

Vamos adicionar alguns estilos a este layout, a fim de deixar o layout mais
apresentável e bonito. A ideia aqui é fazer um menu horizontal com sub-menus
em vertical (não vou explicar isso pois já existe
[um bom artigo](http://tableless.com.br/criando-um-menu-horizontal-com-css/)
a respeito). O código é:

<pre><code class="css">
/* Execute este trecho em http://jsfiddle.net/aMRMF/4/ */
.menu {
    display: inline;
    position: relative;
    border: 1px solid green;
}

.menu li a { white-space:nowrap; }

.menu ul {
    position: absolute;
    top: 1.1em;
    left: 0px;
    border: 1px solid red;
}
</code></pre>

Beleza, chegamos na metade do caminho. O menu principal já está na horizontal,
e os sub-menus posicionados corretamente na vertical. Mas como? Assim:

<pre><code class="css">
.menu {
    display: inline;
    position: relative;
}
</code></pre>

Neste trecho de código, duas coisas foram feitas:

 - display: inline organizou o nosso menu na horizontal (apenas os elementos
   "Menu 1" e "Menu 2", no caso)
 - position: relative fez com que o posicionamento do elemento na página fosse
   calculado em relação à ele mesmo. Confuso? Significa que é possível posicionar
   o elemento em relação à posição que ele ocupada antes. (Ainda confuso? Tem
   explicação mais detalhada [aqui](http://www.cssnolanche.com.br/diferenca-entre-position-static-relative-absolute-e-fixed/))

Quanto aos sub-menus na vertical:

<pre><code class="css">
.menu ul {
    position: absolute;
    top: 1.1em;
    left: 0px;
}
</code></pre>

Nos sub-menus, o posicionamento é absoluto. Significa que sua posição na
página é feita em relação ao seu elemento pai, que, neste caso, são os nossos
menus principais.

As propriedades top e left servem apenas para dizer onde os nossos sub-menus
devem estar. No caso, cada sub-menu deve estar posicionado 1.1em a partir do
topo e 0px a partir da esquerda. A medida em, para quem não sabe, é uma medida
relativa ao tamanho da fonte no elemento pai. Se a fonte em .menu tiver 16px,
então 1em=16px e 1.1em, como no exemplo, é 17.6px. Mais detalhes
[aqui](http://www.maujor.com/tutorial/medidascss.php).

Agora, só falta fazer os nossos sub-menus aparecerem somente quando necessário.
Usando css:

<pre><code class="css">
/* Execute este trecho em http://jsfiddle.net/aMRMF/5/ */
.menu ul {
    display: none;
}

.menu:hover ul {
    display: block;
}
</code></pre>

O que o trecho acima faz é simples: oculta o sub-menu (display:none) e só o
exibe quando passamos o mouse em cima do menu (:hover). Simples, não?

Como disse no início do post, também é possível fazer o menu usando javascript.
A diferença é que o menu só aparece quando clicado, ao invés do hover. Neste
exemplo estarei usando Zepto.js, uma lib bem compatível com o jQuery mas muito
menor, ideal para mobile. O "problema" é que ela não funciona no IE. Só estou
usando pra "aprender" mesmo, pois o código abaixo se dá bem com ambas as
bibliotecas:

<pre><code class="javascript">
/* Execute este trecho em http://jsfiddle.net/aMRMF/6/ */
$('.menu').on('click', function(e) {
    $(this).children('ul').toggle();

    return false;
});
</code></pre>

O exemplo acima é bem simples: quando um menu é clicado, seu sub-menu, o
elemento filho ul, será exibido. Clicando novamente, o sub-menu é
ocultado. A proposito, o método toggle serve exatamente para isso: se
o elemento estiver oculto (display: none), então será exibido. Caso contrário
(display: block), será ocultado.

E é isso, com esse básico já dá para escrever alguns menus drop-downs,
como o que uso aqui (já clicou no ícone com três pontos ao lado do meu
nome, no topo?). **UPDATE**: Usava.

Pra finalizar este layout, só falta o layout responsivo. Não sabe o que é?
Leia [aqui](http://tableless.com.br/introducao-ao-responsive-web-design/) sobre,
e [aqui](http://mediaqueri.es/) tem exemplos bem legais =D
