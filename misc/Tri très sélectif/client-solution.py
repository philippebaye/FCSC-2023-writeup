#!/usr/bin/env python3

# python3 -m pip install pwntools
from pwn import *

# Paramètres de connexion
#HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2051
HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2052

def comparer(x, y):
	io.sendlineafter(b">>> ", f"comparer {x} {y}".encode())
	return int(io.recvline().strip().decode())

def echanger(x, y):
	io.sendlineafter(b">>> ", f"echanger {x} {y}".encode())

def longueur():
	io.sendlineafter(b">>> ", b"longueur")
	return int(io.recvline().strip().decode())

def verifier():
	io.sendlineafter(b">>> ", b"verifier")
	r = io.recvline().strip().decode()
	if "flag" in r:
		print(r)
	else:
		print(io.recvline().strip().decode())
		print(io.recvline().strip().decode())

def trier(offset, N):
	#############################
	#   ... Complétez ici ...   #
	# Ajoutez votre code Python #
	#############################
    if N < 2:
        pass
    else:
        current_pivot_index = N - 1;
        greater_than_pivot = [index for index in range(current_pivot_index) if not comparer(offset + index, offset + current_pivot_index)]

        next_pivot_index = current_pivot_index - len(greater_than_pivot)
        echanger(offset + next_pivot_index, offset + current_pivot_index)
        if next_pivot_index in greater_than_pivot:
            greater_than_pivot.remove(next_pivot_index)
            greater_than_pivot.append(current_pivot_index)
        
        greaters_to_move = [index for index in range(next_pivot_index) if index in greater_than_pivot]
        smallers_to_move = [index for index in range(next_pivot_index+1, N, 1) if index not in greater_than_pivot]
        for greater, smaller in zip(greaters_to_move, smallers_to_move):
            echanger(offset + greater, offset + smaller)
        
        trier(offset, next_pivot_index)
        trier(offset + next_pivot_index + 1, len(greater_than_pivot))

# Ouvre la connexion au serveur
io = remote(HOST, PORT)

# Récupère la longueur du tableau
N = longueur()

# Appel de la fonction de tri que vous devez écrire
trier(0, N)

# Verification
verifier()

# Fermeture de la connexion
io.close()
