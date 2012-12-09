title: Free your technical aesthetic from the 2010s
published: 2012-12-09
slug: free-your-technical-aesthetic-from-the-2010s
link: http://www.storytotell.org/essays/74-response.html

Ultimamente ando dando muita atenção a tecnologias "do passado", em especial
[Smalltalk][1], [Self][2], Lisp e seu dialeto que mais me interessa,
[Clojure][3] - este, na verdade, é bem recente. Talvez seja porque eu já
nasci na *era moderna*, ou porque o senso comum diz que, se é mais novo,
é provavelmente melhor, mas olhando um pouco o que inspirou as tecnologias
que uso hoje, tenho a impressão de que não evoluímos tanto assim.

Pode ser só impressão, claro, eu *ainda* não fui capaz de programar
algo em smalltalk, então não posso dizer muito. De volta ao passado, o
artigo cita um projeto, [SHRDLU][4], que permitia interagir com o sistema
usando inglês puro. Em 1970. Um trecho do artigo demonstra isso de forma
bem interessante:

> Person: Is there anything which is bigger than every pyramid but is not as
wide as the thing that supports it?<br />
> Computer: Yes, the blue block.<br />
> Person: Does a steeple<br />
> Computer interrupting: Sorry, I don't know the word "steeple".<br />
> Person: A "steeple" is a stack which contains two green cubes and a pyramid.<br />
> Computer: I understand.<br />
> Person: Are there any steeples now?<br />
> Computer: No.<br />
> Person: Build one.<br />
> Computer: OK. (does it)
> <br /> <br />
> This is not a fantasy, this is an actual program with actual source code you can download today. Look at everything that happened there:

> - Someone gave a very complex query and got an exact answer
  - They then defined a new term declaratively
  - They asked the computer to figure out how to do something based on that definition—which it then actually did.

Certamente vale o download. Fico imaginando o esforço necessário pra fazer
algo assim nos dias de hoje, certamente valeria um TCC. Mais:

> The standard debugging procedure for a Smalltalk app is:

> 1. Something goes awry: message not understood or something happens
  2. The app pops up a dialog with the debugger window
  3. You enter some code and hit proceed
  4. The app continues like nothing happened

> How does this pan out in a web app? Similarly, only this time between 2 and 3
there is a 2.5: you VNC to the Smalltalk image running your web app on the remote server.

> This sounds awesome enough, right? But apparently it gets better. You can
replace that "pop up a dialog" machinery with a "serialize the entire current
context to a log." If you've ever debugged a Java web app, you are used to
rooting around in the logs reading exception traces. This is like that—except,
instead of reading an exception trace, you get to load the actual moment the
exception was triggered into your local debugger and pick up from there as if
it just happened locally! Have you ever had a problem you couldn't debug
because you just didn't know how to reproduce the bug locally? That problem
isn't even meaningful in Smalltalk!

> Cocoa doesn't have this. C# doesn't have this. Nothing else has this.

Olha a diferença: ao invés de ler um log e tentar reproduzir o bug localmente,
o que nem sempre funciona, em Smalltalk o momento em que a exceção ocorreu
é carregado e executado localmente. Como me deu uma vontade de
programar em Smalltalk agora, só pra ver como isso funciona, na prática.

[1]: http://www.smalltalk.org/main/
[2]: http://selflanguage.org/
[3]: http://clojure.org/
[4]: http://hci.stanford.edu/~winograd/shrdlu/
