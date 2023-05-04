from assembly import assembly

with open('comparaison.asm') as input_file:
    hexcode = assembly(input_file)
    print(hexcode)
