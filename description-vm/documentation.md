# Machine virtuelle

<p>La machine virtuelle décrite dans cette page concerne les cinq épreuves suivantes :</p>
<ul>
<li><code>Comparaison</code> (<em>intro</em>)</li>
<li><code>Fibonacci</code> (<em>hardware</em>)</li>
<li><code>RSA Secure Dev (1/3)</code> (<em>Side-Channel and Fault Attacks</em>)</li>
<li><code>RSA Secure Dev (2/3)</code> (<em>Side-Channel and Fault Attacks</em>)</li>
<li><code>RSA Secure Dev (3/3)</code> (<em>Side-Channel and Fault Attacks</em>)</li>
</ul>
<p>Ces cinq épreuves partagent deux fichiers :</p>
<ul>
<li><a href="machine.py">machine.py</a> : le fichier Python évaluant les instructions de cette machine.</li>
<li><a href="assembly.py">assembly.py</a> : un assembleur décrit plus bas.</li>
</ul>
<p>On donne aussi les sha256 de ces deux fichiers :</p>
<ul>
<li>SHA256(<code>machine.py</code>)  = <code>316e7c9abdc83c5e586368cc1af75eb7cb7f7131eab3baa049361c65e2d3fcb4</code>.</li>
<li>SHA256(<code>assembly.py</code>) = <code>dcaa8e80eedfe2c86c0554fdb107bc87c2c907f32625430c43062fdec590e7fd</code>.</li>
</ul>
<h2>Assembleur</h2>
<p>Un assembleur sommaire écrit en Python est fourni (<code>assembly.py</code>) afin de générer le code machine qui sera interprêté (<em>bytecode</em>).
Cet assembleur supporte la reconnaissance des étiquettes afin de faciliter les sauts dans le code.
Le caractère pour les commentaires est le <code>;</code>.</p>
<h2>Description de la machine virtuelle</h2>
<p>La machine contient 16 registres pouvant contenir des nombres aussi grands qu'on le souhaite.
Les registres sont numérotés de <code>0</code> à <code>F</code>.
On utilise un système hexadécimal pour désigner les registres (<code>RA</code> au lieu de <code>R10</code> par exemple).</p>
<p>Lors de son initialisation, la machine s'attend à recevoir (sans vérifier la cohérence des nombres) :</p>
<ol>
<li>un message qui sera placé dans le registre <code>R5</code>.</li>
<li>un nombre premier <code>p</code> qui sera placé dans le registre <code>R6</code>.</li>
<li>un nombre premier <code>q</code> qui sera placé dans le registre <code>R7</code>.</li>
<li>un nombre <code>iq</code> qui sera placé dans le registre <code>R8</code> (<code>iq = q**(-1) mod p</code>).</li>
<li>un nombre <code>dp</code> qui sera placé dans le registre <code>R9</code> (<code>dp = e**(-1) mod (p-1)</code>).</li>
<li>un nombre <code>dq</code> qui sera placé dans le registre <code>RA</code> (<code>dq = e**(-1) mod (q-1)</code>).</li>
<li>un nombre <code>e</code> qui sera placé dans le registre <code>RB</code>.</li>
<li>un nombre <code>d</code> qui sera placé dans le registre <code>RC</code> (<code>d = e**(-1) mod (p-1)(q-1)</code>).</li>
<li>une séquence d'instructions qui sera le code interprété par la machine. Cette séquence est découpée en mots de 16 bits dans un tableau, le premier mot étant à l'indice <code>0</code> du tableau.</li>
</ol>
<h2>Exécution de la machine virtuelle</h2>
<p>La machine virtuelle interprète la séquence en commençant par le premier mot de 16 bits qui se trouve à l'adresse <code>0</code> de la séquence.</p>
<p>La machine virtuelle positionne toujours le compteur du programme (<code>PC</code>) sur la prochaine instruction après le chargement et le décodage d'une instruction.
Après ce chargement, l'instruction est exécutée, mettant à jour les valeurs des registres de la machine.</p>
<h2>Liste des instructions</h2>
<h3>Tableau synthétique</h3>
<table>
<thead>
<tr>
<th>Family</th>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th>Operation</th>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th align="left">Assembler</th>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th align="center">Updates</th>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th>Action</th>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
<th>Error</th>
</tr>
</thead>
<tbody>
<tr>
<td>Move</td>
<td></td>
<td>Move</td>
<td></td>
<td align="left"><code>MOV Rj, op2</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = op2</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Load</td>
<td></td>
<td>Move from code (<code>1</code> word)</td>
<td></td>
<td align="left"><code>MOVCW Rj</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = @Rj</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Move from code (<code>Ri</code> words)</td>
<td></td>
<td align="left"><code>MOVC Rj, Ri</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = @Rj</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Logical</td>
<td></td>
<td>AND</td>
<td></td>
<td align="left"><code>AND Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm &amp; Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>OR</td>
<td></td>
<td align="left"><code>OR  Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm | Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>XOR</td>
<td></td>
<td align="left"><code>XOR Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm ^ Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Shift right</td>
<td></td>
<td align="left"><code>SRL Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm &gt;&gt; Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Shift left</td>
<td></td>
<td align="left"><code>SLL Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm &lt;&lt; Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Arithmetic</td>
<td></td>
<td>Bit length</td>
<td></td>
<td align="left"><code>BTL Rj, Ri</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = bit_length(Ri)</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Add</td>
<td></td>
<td align="left"><code>ADD Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm + Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Subtract</td>
<td></td>
<td align="left"><code>SUB Ro, Rm, Rn</code></td>
<td></td>
<td align="center"><code>Z</code> <code>C</code></td>
<td></td>
<td><code>Ro = Rm - Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Comparison</td>
<td></td>
<td align="left"><code>CMP Rj, Ri</code></td>
<td></td>
<td align="center"><code>Z</code> <code>C</code></td>
<td></td>
<td><code>Rj - Ri</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Multiplication</td>
<td></td>
<td align="left"><code>MUL Ro, Rm, Rn</code></td>
<td></td>
<td align="center"><code>Z</code></td>
<td></td>
<td><code>Ro = Rm * Rn</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Division</td>
<td></td>
<td align="left"><code>DIV Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = Rm // Rn</code></td>
<td></td>
<td><code>Rn=0</code></td>
</tr>
<tr>
<td></td>
<td></td>
<td>GCD</td>
<td></td>
<td align="left"><code>GCD Ro, Rm, Rn</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Ro = gcd(Rm,Rn)</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Modular</td>
<td></td>
<td>Modular reduction</td>
<td></td>
<td align="left"><code>MOD Rj, Ri</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = Ri mod RD</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Modular exponentiation</td>
<td></td>
<td align="left"><code>POW Rj, Ri</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = Ri**RC mod RD</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Modular inversion</td>
<td></td>
<td align="left"><code>INV Rj, Ri</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = Ri**(-1) mod RD</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Random</td>
<td></td>
<td>Random</td>
<td></td>
<td align="left"><code>RND Rj</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>Rj = rand &lt; 2**Rj</code></td>
<td></td>
<td><code>Rj=0</code></td>
</tr>
<tr>
<td>Branch (Absolute)</td>
<td></td>
<td>Jump if <code>Z</code> set</td>
<td></td>
<td align="left"><code>JZA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = dest if Z=0</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>Z</code> not set</td>
<td></td>
<td align="left"><code>JNZA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = dest if Z=1</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>C</code> set</td>
<td></td>
<td align="left"><code>JCA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = dest if C=0</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>C</code> not set</td>
<td></td>
<td align="left"><code>JNCA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = dest if C=1</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump</td>
<td></td>
<td align="left"><code>JA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = dest</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Branch (Relative)</td>
<td></td>
<td>Jump if <code>Z</code> set</td>
<td></td>
<td align="left"><code>JZR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC += dest if Z=0</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>Z</code> not set</td>
<td></td>
<td align="left"><code>JNZR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC += dest if Z=1</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>C</code> set</td>
<td></td>
<td align="left"><code>JCR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC += dest if C=0</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump if <code>C</code> not set</td>
<td></td>
<td align="left"><code>JNCR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC += dest if C=1</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Jump</td>
<td></td>
<td align="left"><code>JR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC += dest</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Call (Absolute)</td>
<td></td>
<td>Call</td>
<td></td>
<td align="left"><code>CA dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>LR = PC, PC = dest</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Call (Relative)</td>
<td></td>
<td>Call</td>
<td></td>
<td align="left"><code>CR dest</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>LR = PC, PC += dest</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Return</td>
<td></td>
<td>Return</td>
<td></td>
<td align="left"><code>RET</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td><code>PC = LR</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>End</td>
<td></td>
<td>Stop</td>
<td></td>
<td align="left"><code>STP</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Tabular</td>
<td></td>
<td>allocate constants</td>
<td></td>
<td align="left"><code>.word cst, ...</code></td>
<td></td>
<td align="center">-</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Notations :</p>
<ul>
<li><code>Ri  = R[0-9A-F]</code></li>
<li><code>Rj  = R[0-9A-F]</code></li>
<li><code>Rm  = R[0-7]</code></li>
<li><code>Rn  = R[0-7]</code></li>
<li><code>Ro  = R[0-7]</code></li>
<li><code>op2 = Ri, #[0-9]+, #0x[0-9a-fA-F]+, =[a-zA-Z]+</code></li>
<li><code>dest = Ri, [a-zA-Z]+, #[0-9]+, #0x[0-9a-fA-F]+</code></li>
<li><code>cst = [0-9]+, 0x[0-9a-fA-F]+</code></li>
</ul>
<p>Après un <code>#</code> le nombre doit pouvoir être représenté sur au plus 16 bits.</p>
<p>Registres Spéciaux:</p>
<ul>
<li><code>RC</code> est utilisé comme exposant</li>
<li><code>RD</code> est utilisé comme module</li>
<li><code>RE</code> est utilisé comme Link Register</li>
<li><code>RF</code> est utilisé comme Program Counter</li>
</ul>
<h3>Détails des instructions</h3>
<p><strong>MOV Rj, op2</strong></p>
<pre><code>Rj = op2
</code></pre>
<p><strong>MOV Rj, =label</strong></p>
<pre><code>Rj = @label
</code></pre>
<p><strong>AND Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm &amp; Rn
</code></pre>
<p><strong>OR  Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm | Rn
</code></pre>
<p><strong>XOR  Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm ^ Rn
</code></pre>
<p><strong>SRL Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm &gt;&gt; Rn
</code></pre>
<p><strong>SLL Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm &lt;&lt; Rn
</code></pre>
<p><strong>BTL Rj, Ri</strong></p>
<pre><code>Rj = bit_len(Ri)
</code></pre>
<p><strong>ADD Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm + Rn
</code></pre>
<p><strong>SUB Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm - Rn
</code></pre>
<p>Met à jour deux booléens <code>Z</code> et <code>C</code> :</p>
<ul>
<li><code>Z = True</code> si <code>Rm == Rn</code>, sinon <code>Z = False</code></li>
<li><code>C = False</code> si <code>Rm&lt; Rn</code>, sinon <code>C = True</code></li>
</ul>
<p><strong>MUL Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm*Rn
</code></pre>
<p>Met à jour un booléen <code>Z</code> :</p>
<ul>
<li><code>Z = True</code> si <code>Rm == 0</code> ou <code>Rn == 0</code>, sinon Z<code> = False</code></li>
</ul>
<p><strong>DIV Ro, Rm, Rn</strong></p>
<pre><code>Ro = Rm//Rn = quotient(Rm,Rn)
</code></pre>
<p>Si <code>Rn == 0</code>, cela génère une erreur (qui arrête le programme).</p>
<p><strong>MOD Rj, Ri</strong></p>
<pre><code>Rj = Ri mod module
</code></pre>
<p><strong>POW Rj, Ri</strong></p>
<pre><code>Rj = Ri**exponent mod module
</code></pre>
<p><strong>GCD Ro, Rm, Rn</strong></p>
<pre><code>Ro = gcd(Rm,Rn)
</code></pre>
<p><strong>INV Rj, Ri</strong></p>
<pre><code>Rj = Ri**(-1) mod module
</code></pre>
<p><strong>RND Rj</strong></p>
<pre><code>Rj = random de taille Rj bits (au plus 4096 octets)
</code></pre>
<p>Si <code>Rj == 0</code>, cela génère une erreur (qui arrête le programme).</p>
<p><strong>CMP Rj, Ri</strong></p>
<p>Met à jour deux booléens <code>Z</code> et <code>C</code> :</p>
<ul>
<li><code>Z = True</code> si <code>Rj == Ri</code>, sinon <code>Z = False</code></li>
<li><code>C = False</code> si <code>Rj&lt; Ri</code>, sinon <code>C = True</code></li>
</ul>
<p><strong>MOVCW Rj</strong></p>
<pre><code>Rj = @Rj
</code></pre>
<p>Lit 1 mot (2 octets) à partir de l'adresse <code>Rj</code>.
Le mot à l'adresse <code>Rj</code> est le poids fort de la valeur considérée.</p>
<p><strong>MOVC Rj, Ri</strong></p>
<pre><code>Rj = @Rj
</code></pre>
<p><code>Ri</code> indique le nombre de mots à lire à partir de l'adresse <code>Rj</code>.
Le mot à l'adresse <code>Rj</code> est le poids fort de la valeur considérée.</p>
<p><strong>JZA dest</strong></p>
<pre><code>PC = dest si Z = True
</code></pre>
<p><strong>JNZA dest</strong></p>
<pre><code>PC = dest si Z = False
</code></pre>
<p><strong>JZR dest</strong></p>
<pre><code>PC += dest si Z = True
</code></pre>
<p><strong>JNZR dest</strong></p>
<pre><code>PC += dest si Z = False
</code></pre>
<p><strong>JCA dest</strong></p>
<pre><code>PC = dest si C = True
</code></pre>
<p><strong>JNCA dest</strong></p>
<pre><code>PC = dest si C = False
</code></pre>
<p><strong>JCR dest</strong></p>
<pre><code>PC += dest si C = True
</code></pre>
<p><strong>JNCR dest</strong></p>
<pre><code>PC += op2 si C = False
</code></pre>
<p><strong>JA dest</strong></p>
<pre><code>PC = dest
</code></pre>
<p><strong>JR dest</strong></p>
<pre><code>PC += dest
</code></pre>
<p><strong>CA op2</strong></p>
<pre><code>LR = adresse de retour (PC)
PC = dest
</code></pre>
<p><strong>CR dest</strong></p>
<pre><code>LR = adresse de retour (PC)
PC += dest
</code></pre>
<p><strong>RET</strong></p>
<pre><code>PC = LR
</code></pre>
<p><strong>STP</strong></p>
<pre><code>Fin du programme
</code></pre>
