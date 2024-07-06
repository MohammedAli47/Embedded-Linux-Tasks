bits = ["0" for i in range(0, 8)]
for i in range(len(bits)):
    bits[i] = input("Enter bit number %d: " % i)
byte = "".join(bits)
with open("DIO_init.c", "w") as file:
    file.write("void DIO_init() {\n \tDDRA = 0b%s;\n}" % byte)
