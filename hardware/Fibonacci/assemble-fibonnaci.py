from assembly import assembly

with open('fibonnaci.asm') as input_file:
    hexcode = assembly(input_file)
    print(hexcode)

