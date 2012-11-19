title: Usando o terminal com ZSH
published: 2012-10-07
slug: usando-o-terminal-com-zsh

Certa vez eu vi uma dica no twitter sobre como customizar o prompt do bash para
exibir o branch do git em questão. Imediatamente, claro, fui tentar fazer o
mesmo com o meu PC. Tirando a sintaxe esquisita usada pra formatar o output,
até que deu certo. Daí eu conheci o ZSH e, mais importante, o framework
[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh).

O legal desse framework são os vários plugins, mais de 40, no momento, e mais
de 80 (OITENTA!) temas, tudo community-driven, se liga nos meus preferidos:

### Gallois

<img alt="Gallois theme" src="https://a248.e.akamai.net/camo.github.com/468926301e7fa2ff208a3930ac5e91f370eb4efe/687474703a2f2f692e696d6775722e636f6d2f47545a58342e706e67" />

### Nanotech

<img alt="Nanotech theme" src="https://a248.e.akamai.net/camo.github.com/1fcca65252afc62529a1e355bbd2c2a3f70a7f57/687474703a2f2f6e616e6f746563682e6e616e6f74656368636f72702e6e65742f646f776e6c6f6164732f6e616e6f746563682e7a73682d7468656d652e706e67" />

### Agnoster

<img alt="Agnoster theme" src="https://raw.github.com/gist/3712874/5d28e2d9fe2e4d0a4fda0315ad97bdafa399425c/screenshot.png" />

[Neste link](https://github.com/robbyrussell/oh-my-zsh/wiki/themes) tem
screenshots de mais temas.

A outra parte legal, como disse, são os plugins. Boa parte deles adicionam
alias e funções bastante úteis. O
[plugin do git](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/git/git.plugin.zsh)
dá um bom exemplo das funcionalidades adicionadas.

O readme do projeto é bastante competente e ensina como instalar o framework,
o que, a propósito, é muito fácil. Há também o [meu fork](https://github.com/lucassmagal/oh-my-zsh)
do projeto, com algumas inclusões no plugin do mercurial e um fork do tema
gallois (chamado liquid), o que uso, para exibir tanto branches de git quanto
hg no prompt. Só rodar isso:

<pre><code class="bash">
curl -L https://raw.github.com/lucassmagal/oh-my-zsh/master/tools/install_fork.sh | sh
</code></pre>

Referências:
<div class="ref">

 - [ZSH o melhor shell - configuração](http://blog.dmitrynix.com/zsh-o-melhor-shell-configuracao/)
 - [Turbinando o terminal com ZSH](http://www.mafagrafos.net/2012/04/26/turbinando-o-terminal-com-o-zsh/)

</div>
