from assembly import assembly

with open('rsa1-1.asm') as input_file:
    hexcode = assembly(input_file)
    print(hexcode)

