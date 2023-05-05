# Zéro pointé

<img alt="énoncé du challenge" src="énoncé.png" width=300>

Les fichiers fournis :
- [zero-pointe.c](zero-pointe.c)
- [zero-pointe](zero-pointe)

La fonction `flag()` permet d'afficher le contenu du fichier `flag.txt`.

Au niveau du `main`, l'appel à cette fonction `flag()` est réalisée si un signal [`SIGFPE`](https://www.gnu.org/software/libc/manual/html_node/Program-Error-Signals.html) est émis :

```c
if (signal(SIGFPE, flag) == SIG_ERR) {
    ...
}
```

Ce signal `SIGFPE` est émis lorsqu'une erreur se produit sur un calcul arithmétique, par exemple lorsqu'une division par zéro est réalisée, ou un débordement.

La division est réalisée comme suit :

```c
c = b ? a / b : 0;
```

On est donc protégé contre le cas où le diviseur est nul. Il faut donc chercher un moyen de réaliser un débordement.

`a` et `b` étant des `long`, leurs plages de valeurs possibles est `[-9.223.372.036.854.775.808, 9.223.372.036.854.775.807]`

Pour réaliser un débordement on va jouer sur l'asymétrie des bornes `LONG_MIN` et `LONG_MAX` : `LONG_MIN = -LONG_MAX - 1`. Un débordement se produit donc quand on réalise l'opération  `LONG_MIN / -1` :

```bash
$ nc challenges.france-cybersecurity-challenge.fr 2050
-9223372036854775808
-1
FCSC{0366ff5c59934da7301c0fc6cf7d617c99ad6f758831b1dc70378e59d1e060bf}
```

En complément, la page suivante indique comment se prémunir de ce cas de figure : https://wiki.sei.cmu.edu/confluence/display/c/INT33-C.+Ensure+that+division+and+remainder+operations+do+not+result+in+divide-by-zero+errors
