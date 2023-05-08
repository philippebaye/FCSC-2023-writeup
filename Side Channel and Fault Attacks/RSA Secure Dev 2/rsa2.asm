; https://www.di.ens.fr/~jv/HomePage/pdf/rsa.pdf
; https://cryptobourrin.wordpress.com/2014/09/11/rsa-et-le-reste-chinois/
; https://www.researchgate.net/figure/The-RSA-CRT-signature-generation-with-Garners-algorithm_fig1_48412713 

; https://www.matthieurivain.com/files/slides-thesis.pdf

; message = R5
; p = R6
; q = R7
; d = RC
; dp = R9
; dq = RA
; iq = R8
; e = RB

; Sp = M**dp mod p
; Sq = M**dq mod q
; t = Sp - Sq
; si t<0, t = t + p
; h = iq.t mod p
; S = Sq + h.q


; Sq = message**dq mod q
MOV RC, RA
MOV RD, R7
POW R2, R5

; Sp = message**dp mod p
MOV RC, R9
MOV RD, R6
POW R1, R5

; t = Sp - Sq
SUB R1, R1, R2
; C = False si R1< R2, sinon C = True
JCR +1
; si Sp - Sq, alors : t = t + p
ADD R1, R1, R6

; h = iq.t mod p
; On met iq dans un registre R0 à R7, car MUL utilise uniquement ces registres
MOV R3, R8
MUL R1, R3, R1
MOD R1, R1

; S = Sq + h*q
MUL R1, R1, R7
ADD R0, R2, R1

; Vérif message = S**e mod N
; positionne e
MOV RC, RB
; calcule N et postionne N
MUL R2, R6, R7
MOV RD, R2
; Calcule message de vérif
POW R1, R0
; Check message = message de vérif
CMP R5, R1
; si Z=True, les 2 sont égaux => Fin OK
JZR +2

; Z=False, les 2 ne sont égaux => KO
; Génération message aléatoire.
RND R2
MOV R0, R2

; Fin
STP