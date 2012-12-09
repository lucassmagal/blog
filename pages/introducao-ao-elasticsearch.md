title: Introdução ao ElasticSearch
slug: introducao-ao-elasticsearch
published: 2012-12-09
order: 2

Desde a minha [palestra na PyBR8][1] havia prometido material mais extenso sobre
buscas usando [ElasticSearch][2] (ES) no Django. Nesse primeiro artigo vou fazer uso
*apenas* do ES através de sua API REST, pra demonstrar o quão simples é seu uso.

### O que é o ElasticSearch ###

O ES é um search engine escrito em Java e criado em cima do [Apache Lucene][3],
uma lib bem popular especializada em montar índices para buscas em texto, e
permite criar índices para buscas em um intervalo de datas, proximidade e por
aí vai. O Lucene, no entanto, não é distribuído para uso final\*, e é aí que
entram os servidores de full-text search.

Tanto o [Solr][4] e o ES são construídos em cima do Lucene, o objetivo é
envolver os benefícios do Lucene em um sistema completo, pronto pra uso,
na forma de um webserver que pode ser escalado horizontalmente \** pra suportar
uma carga crescente de buscas.

O ES foi criado para servir buscas e escalar de forma horizontal de forma simples,
sem perder sua eficiência e estabilidade, ao contrário do Solr, que é citado
em alguns posts como *[fácil de quebrar][5]*. Grandes empresas tem usado ES
com sucesso para melhorar a performance de suas buscas, como [SoundCloud][6]
e [FourSquare][7].

### Instalando e rodando ###

A instalação no meu Ubuntu foi muito simples, apenas precisei fazer download
de um deb do [último release][8], instalar e pronto. O problema é que dessa forma
eu fiquei no escuro quanto à forma de rodar, já que a documentação oficial ainda
é bem fraca. A instalação manual dá mais dicas sobre como iniciar o ES, mas
se tiver instalado pelo deb, pode iniciá-lo rodando:

<pre><code class="bash">
sudo /etc/init.d/elasticsearch start
</code></pre>

Se visitar <code>localhost:9200</code> verá o seguinte:

<pre><code>
{
  "ok" : true,
  "status" : 200,
  "name" : "White Queen",
  "version" : {
    "number" : "0.20.1",
    "snapshot_build" : false
  },
  "tagline" : "You Know, for Search"
}
</code></pre>

Pronto, o sistema está rodando =D Eu omiti algumas coisas como o YAML de configuração,
necessário pra execução do ES, pois o deb já instala um default em
<code>/etc/elasticseach/elasticsearch.yml</code>.

O ES funciona inteiramente através de uma interface REST, e é *schema-less*,
o que significa que não preciso fazer nenhuma configuração inicial para começar
a criar e fazer queries sobre meus índices. Nesse artigo vamos usar o curl
pra interagir com o sistema, inicialmente.

### Inserindo algumas entidades ###

Como disse anteriormente, não é preciso nenhuma configuração especial para
começar a criar índices, então começaremos os nossos. No ES dados são armazenados
como documentos, similar ao MongoDB, e estes documentos estão sempre dentro de
"containeres" chamados índices. Vamos supor que precisaremos montar um índice
de buscas sobre bares populares. Cada documento contém o nome do bar, endereço
e nome do dono:

<pre><code>
curl -XPUT 'http://localhost:9200/bares/bar/1' -d '{
    "nome": "Bar Foda",
    "endereco": "Rua da Passagem, Botafogo",
    "dono": "Lucas Sampaio"
}'
# output: {"ok":true,"_index":"bares","_type":"bar","_id":"1","_version":1}

curl -XPUT 'http://localhost:9200/bares/bar/2' -d '{
    "nome": "Bar do Lira",
    "endereco": "Rua Bartolomeu Mitre, Leblon",
    "dono": "Lucas Sampaio"
}'
# output: {"ok":true,"_index":"bares","_type":"bar","_id":"2","_version":1}
</code></pre>

Explicando agora: o que fiz em cada um desses comandos foi criar dois documentos.
Ambos foram criados dentro do índice "bares" e são do tipo "bar". No ES, a convenção
de URLs para índices é <br/>
<code>http://localhost:9200/&lt;index&gt;/&lt;documento&gt;/</code>.

Se for ao browser e acessar a url <code>http://localhost:9200/bares/bar/1</code>,
verá o seguinte:

<pre><code>
{"_index":"bares","_type":"bar","_id":"1","_version":1,"exists":true, "_source" : {
    "nome": "Bar Foda",
    "endereco": "Rua da Passagem, Botafogo",
    "dono": "Lucas Sampaio"
}}
</code></pre>

Bem auto-explicativo, mas vale notar uma coisa: no ES, é possível [versionar][10]
seus documentos. No caso de uma atualização, você precisa apenas enviar ao ES
os atributos alterados em uma nova version, e o índice passará a utilizar o
mais novo atributo.

Muito bem, agora a parte importante: buscas. A [Search API][11] é bem grande,
é possível variar um bocado o formato das suas buscas. É possível ordenar
os resultados, excluir documentos do resultado, fazer pesquisa em um determinado
range (numérico ou por datas, por exemplo), etc. Aqui abordarei a mais básica:

<pre><code>
curl -XGET 'http://localhost:9200/bares/_search?q=nome:Bar&pretty=true'

# output

{
  "took" : 14,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 0.19178301,
    "hits" : [ {
      "_index" : "bares",
      "_type" : "bar",
      "_id" : "1",
      "_score" : 0.19178301, "_source" : {
"nome": "Bar Foda",
"endereco": "Rua da Passagem, Botafogo",
"dono": "Lucas Sampaio"
}
    }, {
      "_index" : "bares",
      "_type" : "bar",
      "_id" : "2",
      "_score" : 0.15342641, "_source" : {
"nome": "Bar do Lira",
"endereco": "Rua Bartolomeu Mitre, Leblon",
"dono": "Lucas Sampaio"
}
    } ]
  }
}
</code></pre>

A query foi bem simples: procurei por documentos que continham "Bar" no nome,
seguindo essa sintaxe já dá pra montar outras queries básicas facilmente. Se
eu tivesse buscado
<code>curl -XGET 'http://localhost:9200/bares/_search?q=nome:Bar+do+Lira&pretty=true</code>,
então o documento 2, "Bar do Lira", seria o primeiro na lista, já que é o mais
relevante em relação à query.

E esse é o básico para trabalhar com o ES. Usando estes comandos já é possível
trabalhar com as funcionalidades mais simples de busca. Outros detalhes:

 - nas minhas inserções eu criei um ID explícito pra cada. É possível, também,
   permitir que o ES crie um automaticamente. Irei dar uma pesquisada, mas acho
   que essa não é a abordagem usada pelo HayStack, que deve criar IDs idênticos
   aos objetos usados no Django.
 - [Este site][12] contém um tutorial bem bacana, mais simples de entender do
   que o oficial, que, pra mim, serve mais para referência.

No próximo artigo irei usar direto o HayStack, que irá interfacear a minha
aplicação com o ElasticSearch. Nele irei abordar a criação de algumas queries
mais complexas. Pra encerrar, vou citar duas features do ES que valem uma
pesquisada:

 - [Percolator][13]: é o inverso do usual no ES. Ao invés de indexar documentos e
   enviar queries, você salva queries, envia documentos e sabe quais queries
   combinam com o documento.
 - [River][14]: uma interface no cluster do ES que permite "escutar" dados
   de uma fonte, que então são salvos no índice. Há rivers default para
   CouchDB, RabbitMQ, Twitter e Wikipedia.

E é isso. Como disse, foi básico, mas funcionou como um "5-min tutorial" sobre
o ES. A interface REST permite uma integração simples com diversos sistemas,
então se não houver uma lib como o HayStack pra fazer a integração, pode usar
as URLs sem problema. A propósito, se quiser desativar o ES, rode:

<pre><code class="bash">
sudo /etc/init.d/elasticsearch stop
</code></pre>

\* Na maioria dos casos

\** Segundo seus sites oficiais, não cheguei a testar os recursos de sharding do ES

[1]: http://www.lsmagalhaes.com/post/minha-palestra-na-pybr8/
[2]: http://www.elasticsearch.org/
[3]: http://lucene.apache.org/
[4]: http://lucene.apache.org/solr/
[5]: http://blog.socialcast.com/realtime-search-solr-vs-elasticsearch/
[6]: http://backstage.soundcloud.com/2012/12/architecture-behind-our-new-search-and-explore-experience/
[7]: http://engineering.foursquare.com/2012/08/09/foursquare-now-uses-elastic-search-and-on-a-related-note-slashem-also-works-with-elastic-search/
[8]: http://www.elasticsearch.org/download/2012/12/07/0.20.1.html
[9]: http://www.elasticsearch.org/tutorials/2010/07/02/setting-up-elasticsearch-on-debian.html
[10]: http://www.elasticsearch.org/guide/reference/api/index_.html
[11]: http://www.elasticsearch.org/guide/reference/api/search/
[12]: http://www.elasticsearchtutorial.com/index.html
[13]: http://www.elasticsearch.org/blog/2011/02/08/percolator.html
[14]: http://www.elasticsearch.org/guide/reference/river/
