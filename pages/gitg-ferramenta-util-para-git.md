title: Gitg, ferramenta útil pra revisar alterações antes do commit
published: 2012-10-05
slug: gitg-ferramenta-util-para-git

Post bem rápido este: um tempinho atrás vi um colega utilizando uma ferramenta,
[gitx](http://gitx.frim.nl/seeit.html), para revisar alterações em seus projetos,
antes de dar commit no git.
Pelo site dá pra ver que o app é capaz de fazer mais coisas, como visualizar
e revisar o histórico de commits, mas não me interesso tanto por isso.

Apesar da ferramenta ser exclusiva para Mac OS, há um clone bastante
competente, [gitg](https://github.com/jessevdk/gitg), disponível para Linux.

<img src="/static/imgs/gitg.c.png" alt="gitg -c" />

Pelo Ubuntu, bastou <code>sudo apt-get install gitg</code> e já está instalado. O
funcionamento é bem simples, pelo terminal, execute gitg no seu repositório
git e então o histórico de commits se abrirá. É possível executar, também,
gitg -c, que abrirá o "modo de commit", como a imagem acima.

Através dessa janela é possível verificar todas as alterações feitas desde o
último commit. Ao clicar em uma delas, o diff se abre. Obviamente, como se
nota, é possível commitar direto do modo de commit.

Uso diversas vezes antes de commitar algo no git ;)
