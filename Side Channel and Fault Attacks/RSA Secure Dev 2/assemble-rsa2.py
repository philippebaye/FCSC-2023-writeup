from assembly import assembly

with open('rsa2.asm') as input_file:
    hexcode = assembly(input_file)
    print(hexcode)

