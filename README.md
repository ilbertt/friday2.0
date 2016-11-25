# friday 2.0
La repo per il nuovo Friday, la nuova IA.

#Il software
Il software è (per ora) un semplice programma in Python che analizza un testo in input: calcola la probabilità con cui ogni parola si trova vicino alla sua successiva e lo scrive in un semplice file in JSON che funge da semplice database non relazionale.

Con questo testo in input:
<code>Ciao Mondo, come va? Cosa sei? Ciao Friday! Ciao Mondo!</code>

Si ha questo database in output (dove <code>'k'</code> è il numero totale di volte con cui si è trovata la parola di chiave):<br>
<code>{"come": {"k": 1, "va": 0},     
  "sei": {"ciao": 0, "k": 1},     
  "mondo": {"come": 0, "k": 1},     
  "cosa": {"k": 1, "sei": 0},     
  "ciao": {"k": 3, "friday": 0.25, "mondo": 0.6667},     
  "friday": {"ciao": 0, "k": 1},     
  "va": {"cosa": 0, "k": 1}}</code>

#L'algoritmo
<p>L'algoritmo che calcola la probabilità è molto semplice. Si assuma come <strong>p</strong> una parola del testo (che nel db è la 'chiave') e come <em>a</em>,<em>b</em>,<em>c</em>, ecc. le parole che risultano successive a <strong>p</strong>. <code>k</code> è lo spazio degli eventi, quante volte <strong>p</strong> si trova nel testo, <code>p_0</code> è la probabilità con cui <strong>p</strong> è legata ad <em>a</em> (che si trova già scritta nel db oppure risulta 0 se non vi è scritta). Quando il software ritrova <strong>p</strong> nel testo, ricalcola tutte le probabilità con cui <strong>p</strong> è legata ad <em>a</em>,<em>b</em>,<em>c</em>,ecc. secondo questo algoritmo:</p>

<p><code>p = (k * p_0 +1)/(k + 1)</code></p>

#Il training
Il training è fondamentale per Friday 2.0, in quanto affina le probabilità nel suo db. Pertanto si cercano tanti testi (milioni e milioni :)) corretti che possano essere analizzati dal programma.

#Gli autori
<p>Gli autori che lavorano al progetto sono <a href="https://github.com/ccol168" class="user-mention">@ccol168</a>, <a href="https://github.com/guest928" class="user-mention">@guest928</a>, <a href="https://github.com/tancre99" class="user-mention">@tancre99</a>.</p>
