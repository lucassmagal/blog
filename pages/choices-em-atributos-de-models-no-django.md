title: Como especificar choices em atributos de models no Django?
published: 2012-12-01
slug: choices-em-atributos-de-models-no-django

No Django é possível especificar um conjunto de opções para um atributo de um
model, o [Choices](https://docs.djangoproject.com/en/1.4/ref/models/fields/#choices).
Em resumo, esta é a sintaxe:

<pre><code class="Python">
class Foo(models.Model):
    ESTADOS = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        # ...
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField(max_length=2, choices=ESTADOS)
</code></pre>

Fazendo isso, o form gerado a partir desse model terá um select box com
as opções descritas em ESTADOS, sendo que o segundo elemento das tuplas,
o nome dos estados, será exibido no HTML, e o primeiro elemento, as siglas,
é o que será armazenado no banco de dados.

É possível, naturalmente, especificar um *default* para um campo com
choices. É aí que está o primeiro dos problemas que eu enfrento, vejam:

<pre><code class="Python">
# Opção 1, hardcoded
estado = models.CharField(max_length=2, choices=ESTADOS, default='AC')

#Opção 2, índices numéricos, ESTADOS[0][0] = 'AC'
estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADOS[0][0])

#Opção 3, cada sigla é uma variável
AC = 'AC'
AL = 'AL'
# ...
ESTADOS = (
    (AC, 'Acre'),
    (AL, 'Alagoas'),
    # ...
)
estado = models.CharField(max_length=2, choices=ESTADOS, default=AC)
</code></pre>

Nem preciso comentar a opção 1, escrever *hardcoded* a opção default não é
uma boa ideia, afinal, se eu mudar as siglas por qualquer razão, de 'AC' pra
'AR', por exemplo, provavelmente acabarei com um bug. A opção 2 resolve o problema
 anterior, mas índices numéricos não são nada legíveis
neste caso. Você saberia a qual estado ESTADOS[12][0] se refere, de cara? Eu não.
Nos resta a opção 3, que é a sugerida na documentação do Django. Bastante legível
e *DRY*, mas, neste exemplo dos estados, me obrigaria a escrever muito código.

Isso não ocorre só na hora de definir uma opção default, o que me leva
ao segundo problema que enfrento: eu terei
que referenciar a um ou outro estado, eventualmente, em outras porções do código.
Faria como? ESTADOS[0][0]? Opção 3, AC? Curtiria muito usar dicts pra isso, se
liga:

<pre><code class="Python">
ESTADOS = {
    'Acre': 'AC',
    'Alagoas': 'AL'
    # ...
}

estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADOS['Acre'])
</code></pre>

Legal, melhorou. Resolveu meu problema de referenciamento tornando meu código
mais legível, ESTADOS['Acre'] retorna 'AC', que é um valor válido para o banco
de dados e é facilmente entendível por um humano. Fica mais fácil trabalhar
com as opções de estados em outras porções de código, também.

Mas, você já deve ter notado, o Django não aceita um dict como default, pois
não é um iterable. Outro detalhe: no Django, o valor que deve ser armazenado
no banco de dados deve ser o primeiro da chave-valor, e no exemplo acima eu
fiz uma inversão. Como resolver, então? Assim:

<pre><code class="Python">
def choices(_dict):
    return [(value, key) for key, value in _dict.items()]

ESTADOS = {
    'Acre': 'AC',
    'Alagoas': 'AL'
    # ...
}

# choices(ESTADOS) retorna [('AC', 'Acre'), ('AL', 'Alagoas')],
# que é um iterable e tem um formato aceitável para o Django

estado = models.CharField(max_length=2, choices=choices(ESTADOS),
                          default=ESTADOS['Acre'])
</code></pre>

Com a função choices eu consigo converter meu dict, que tem um formato aceitável
pra trabalhar da forma que eu quero, em um formato que o Django aceita. O problema
é que, obviamente, eu terei de programar essa função em todo projeto Django
que eu quiser essa feature. Nada irritante, mas bem que poderia ser uma feature
nativa do Django. Daí o objetivo desse post.

E aí, como vocês trabalham com choices? Têm notado os problemas que eu citei?
Como tem resolvido? Trocando emails breves com o
[Henrique Bastos](http://henriquebastos.net/), ele comentou usar o
[dj.choices](https://github.com/ambv/dj.choices) sempre que precisa de algo
mais elaborado que strings. Apesar de ter curtido a sugestão, gostaria que o
próprio Django suprisse essa lacuna, já que eu já posso usar um ForeignKey
em outros casos.

Minha ideia é juntar um feedback e, quem sabe, lançar um ticket (e implementar,
claro!) no código do Django.
