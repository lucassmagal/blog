title: Estilizando links com CSS... vejam só, a ordem importa
published: 2012-10-01
slug: estilizando-links-com-css

Revisando o tema do blog hoje para um layout mais claro, acabei batendo com um
problema simples: ao estilizar os links da página em seus quatro diferentes
estados, *:link*, *:hover*, *:visited* e *:active*, o resultado não ocorria
como esperado. A situação em que comecei é a seguinte:

<pre><code class="css">
/* Rode este exemplo em http://jsfiddle.net/HK9vu/ */

a:link {
    display: block;
    text-decoration: none;
}

a:hover { color: green; }
a:active { color:red; }
a:visited { color: grey; }
</code></pre>

Se você rodar o exemplo acima, vai perceber que links já visitados não possuem
mais os estilos *:hover* e *:active* aplicados, como se tivessem sido sobrescritos
pelo *:visited*.

Apenas para referência, os quatro estados de um link são:

 - UP (:link): situação inicial do link, quando a página é carregada e o link não foi visitado
 - OVER (:hover): quando o usuário passa o mouse sobre o link
 - ACTIVE (:active): quando o link é clicado
 - VISITED (:visited): quando o link foi visitado pelo usuário

Pesquisando pela internet, descobri que a ordem dos estados importa para a
execução perfeita do estilo: *:hover* deve ser inserido depois de *:link* e
*:visited*, e *:active* deve ser inserido depois de *:hover*. Agora, sim, tá tudo certo.

Se quiser, pode ver o resultado correto [clicando aqui](http://jsfiddle.net/HK9vu/2/)
ou saber mais no [Site do Maujor](http://maujor.com/tutorial/fund_links.php) e
no [w3schools](http://www.w3schools.com/css/css_link.asp).

**UPDATE**: Só pra informar, o tal redesign do tema que eu citei neste post
não existe mais.
