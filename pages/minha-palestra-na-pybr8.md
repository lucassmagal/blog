title: Minha palestra na PyBR8
published: 2012-11-26
slug: minha-palestra-na-pybr8

Sexta passada (23/nov) fiz minha apresentação na
[Python Brasil 8](http://2012.pythonbrasil.org.br/), e preciso dizer: o
evento foi muito foda!

Antes da minha palestra acabei conhecendo e conversando com gente muito
bacana: almoçei com o [Bruno Rocha](http://rochacbruno.com.br/), que
fez uma apresentação sobre [Whoosh](https://bitbucket.org/mchaput/whoosh/wiki/Home),
o [Vinicius Assef](http://viniciusban.blogspot.com.br/),
parceiro do ES, e o [Massimo Di Pierro](http://www.cdm.depaul.edu/People/Pages/facultyinfo.aspx?fid=343),
criador do framework [Web2Py](http://www.web2py.com/), mas este eu
infelizmente não pude conversar muito, culpa do meu inglês pouco afiado
pra conversação =S. Também conheci brevemente o
[Henrique Bastos](http://henriquebastos.net/), que é muito gente fina e me
deu boas dicas em sua palestra, e curti bastante o [provy](http://heynemann.github.com/provy/),
uma ferramenta de deploy bem interessante e simples de entender.

A experiência foi certamente muito bacana: nunca tinha participado de um evento
de tal proporção, ter palestrado, então... como sou *muito* azarado, tinha que
ocorrer um probleminha durante a minha apresentação, mas tudo correu muito bem
no geral =D

A propósito, fiquei de publicar um material mais completo da integração com Django
e sistemas de Full-Text Search, neste blog. Vou me focar no ElasticSearch, que
é a ferramenta que usei durante a apresentação e a que mais curti usar.

### Django & Full-Text Search: Fazendo buscas rápidas ###

Na minha palestra eu demonstrei como integrar o [ElasticSearch](http://www.elasticsearch.org/),
um servidor para full-text-search criado em cima do [Lucene](http://lucene.apache.org/core/), com o Django,
através do [Haystack](http://haystacksearch.org/). A apresentação foi mais prática
e eu demonstrei como é simples otimizar as buscas de um sistema com pouca alteração
no código, o próprio Haystack e o ElasticSearch ajudam muito nisso.

Como a minha apresentação foi muito básica e rápida, pretendo abordar um bocado
de informação nova nos próximos posts, por isso eu não vou publicar os slides
que usei durante o evento - na verdade, a apresentação era pra ser mais prática
mesmo, então os slides acabaram ficando meio pobres =S

Os tópicos que irei abordar serão os seguintes, nesta ordem:

 - **ElasticSearch** e um panorama geral das soluções mais comuns no mercado.
   O que é, exatamente, é isso? Quais são os seus diferenciais? Como
   instalar e testar?
 - **Django & Haystack**, instalando e usando. Na minha palestra, o uso que fiz
   do Haystack foi muito, muito básico, mas serviu bem pra demonstrar o quão
   rápido dá pra implementar buscas eficientes e poderosas, com pouco esforço.
   Aqui, vou fazer um uso mais intenso do framework, como o uso do método
   <code>index_queryset</code>, índices real-time, que dispensam atualização
   manual, autocomplete e mais.

Eu deixei [um repositório](https://github.com/lucassmagal/search-pybr8) com
o código da apresentação no meu github, mas realmente confesso estar muito simples.
Nos próximos posts, irei reescrever o projeto Django em um novo repositório,
este mais completo e com mais features, então em breve irei deixar um link
com o conteúdo novo por aqui.

E é isso =D Pra quem assistiu minha palestra... **muito obrigado**! Se alguém tiver
alguma dúvida ou sugestão, pode comentar neste post que com certeza irei procurar
resolver a dúvida em posts futuros.
