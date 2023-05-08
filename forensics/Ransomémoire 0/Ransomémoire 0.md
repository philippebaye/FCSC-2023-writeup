# Ransomémoire 0/3 - Pour commencer

<img alt="énoncé du challenge" src="énoncé.png" width=300>

Le fichier `fcsc.7z` contient un dump mémoire `fcsc.dmp`

On utilise [Volatility 3](https://github.com/volatilityfoundation/volatility3) pour l'analyser.

Parmi les processus présent, `brave.exe` attire l'attention :
```bash
$ python3 vol.py -f fcsc.dmp windows.pstree

PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime
...
6808    6612    brave.exe       0x818688160300  10      -       1       False   2023-04-17 17:16:19.000000      N/A
* 3144  6808    brave.exe       0x8186880f4080  0       -       1       False   2023-04-17 17:18:04.000000      2023-04-17 17:18:58.000000
960     1528    BraveUpdate.ex  0x818688718080  3       -       0       True    2023-04-17 17:16:26.000000      N/A
....
```

Une recherche sur internet montre que [Brave](https://brave.com) est un Navigateur.

Le processus principal associé à `brave.exe` semble être celui dont le PID est `6808`. On peut lister les variables d'environnement qui lui sont associés :

```bash
$ python3 vol.py -f fcsc.dmp windows.envars.Envars --pid 6808

PID     Process Block   Variable        Value
...
6808    brave.exe       0x1252c931bf0   COMPUTERNAME    DESKTOP-PI234GP
...
6808    brave.exe       0x1252c931bf0   HOMEPATH        \Users\Admin
6808    brave.exe       0x1252c931bf0   LOCALAPPDATA    C:\Users\Admin\AppData\Local
6808    brave.exe       0x1252c931bf0   LOGONSERVER     \\DESKTOP-PI234GP
...
6808    brave.exe       0x1252c931bf0   USERDOMAIN      DESKTOP-PI234GP
6808    brave.exe       0x1252c931bf0   USERDOMAIN_ROAMINGPROFILE       DESKTOP-PI234GP
6808    brave.exe       0x1252c931bf0   USERNAME        Admin
6808    brave.exe       0x1252c931bf0   USERPROFILE     C:\Users\Admin
```

Le compte utilisé semble être Admin (d'après la variable `USERNAME`) et la machine DESKTOP-PI234GP (d'après la variable `COMPUTERNAME`).

On peut donc constituer le flag tel que demandé : `FCSC{Admin:DESKTOP-PI234GP:Brave}`
