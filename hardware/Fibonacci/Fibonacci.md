# Fibonacci

<img alt="énoncé du challenge" src="énoncé.png" width=300>

Le descriptif de fonctionnement de la VM : [documentation](/description-vm/documentation.md)

Les fichiers fournis :
- [assembly.py](/description-vm/assembly.py)
- [machine.py](/description-vm/machine.py)
- [challenge.py](challenge.py)

On a 2 cas particuliers à prendre en compte : `n=0` et `n=1`.

Pour le cas général, on va utiliser :
- `R0` pour stocker `Fib(n)`
- `R1` pour stocker `Fib(n-1)`
- `R2` pour stocker `Fib(n-2)`
- `R5` comme indicateur du nombre de `Fib(n)` restant à calculer. Une fois à zéro, cela veut dire que le travail est terminé.

Voici l'implémentation réalisée : [fibonnaci.asm](fibonnaci.asm)

Pour assembler et obtenir le bytecode hexadécimal correspondant on utilise un petit script python : [assemble-fibonnaci.py](assemble-fibonnaci.py)

```bash
$ python3 assemble-fibonnaci.py
80020000800100010605c902002014000615c90200101400800300014ced4a88001200014cedc9fb1400
```


Avant de soumettre sur le serveur, on peut vérifier en local le résultat du programme :
1. créer un fichier `flag.txt` (par exemple contenant : `the_flag`)
2. utiliser le script `challenge.py`

```bash
$ python3 challenge.py
Enter your bytecode in hexadecimal:
>>> 80020000800100010605c902002014000615c90200101400800300014ced4a88001200014cedc9fb1400
[+] Congrats! Here is the flag: the_flag
```

On peut maintenant en toute confiance utiliser notre programme sur le serveur pour obtenir le vrai flag :

```bash
nc challenges.france-cybersecurity-challenge.fr 2301
Enter your bytecode in hexadecimal:
>>> 80020000800100010605c902002014000615c90200101400800300014ced4a88001200014cedc9fb1400
[+] Congrats! Here is the flag: FCSC{770ac04f9f113284eeee2da655eba34af09a12dba789c19020f5fd4eff1b1907}
```
