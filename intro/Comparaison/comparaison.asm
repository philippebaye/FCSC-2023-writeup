CMP R5, R6 
JZR +3 ; si R5==R6 -> Z = true => jump vers le bon bloc, sinon poursuite instruction suivante

; bloc pour cas R5 != R6
MOV R0, #0x1
STP

; bloc pour cas R5 == R6
MOV R0, #0x0
STP
