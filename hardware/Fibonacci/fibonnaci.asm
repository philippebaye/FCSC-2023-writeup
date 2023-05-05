; Registres utilisés
; R0 = F(n)
; R1 = F(n-1)
; R2 = F(n-2)

; init n=2 : F(n-2)=F0=0 & F(n-1)=F1=1
MOV R2, #0x0	; F(0)
MOV R1, #0x1	; F(1)

; -------------------------
; cas particuliers
; n=0
CMP R5, R0
JNZR +2
MOV R0, R2
STP
; n=1
CMP R5, R1
JNZR +2
MOV R0, R1
STP

; -------------------------
; cas general
MOV R3, #0x01 	; pas de décrement

; R5 = nombre n de F(n) à calculer
SUB R5, R5, R3	; init on a déjà calculé F(0) et F(1)

; Calcul de F(n)
ADD R0, R1, R2  ; F(n) = F(n-1) + F(n-2)
; Préparation calcul de F(n+1)
MOV R2, R1		; F((n+1)-2) = F(n-1)
MOV R1, R0		; F((n+1)-1) = F(n)
; Décrément nombre de n restant à calculer
SUB R5, R5, R3
JNZR -5			; Tant que R5 != 1 => on continue à calculer
STP
