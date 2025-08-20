import random
# *-* coding: UTF-8 *-*

''' Esté é um script em linguagem python desenvolvido por Caio Ramos
    Ele foi pensado em um tipo de criptografia Cesar.
    Adicione uma senha, como funciona o tipo de criptografia o
    Cesar acrescenta um caractere após outro, até finalizar a senha. '''

def main():

    try:

        print("oOo...... Hackers Square Room ......oOo\n")
        print("(0) Encrypted")
        print("(1) Descrypted")
        option = int(input("\n#: "))

        if(option == 0):
            __Encrypted__()

        else:
            __Descrypted__()

    except Exception as error:
        print("=> error in input", error)
        quit()

def __Encrypted__():

    # funcionara apenas com senhas 8 igual a 8.
    p = str(input("=> digit an password: ")) #iloveyou
    if len(p) >= 8:
        cifer = ['&', 'a', 'e', 'i', 'o', 'u','w' ,'0' ,'1' ,'@']
        encripy0 = random.choice(cifer)
        encripy1 = random.choice(cifer)
        encripy2 = random.choice(cifer)
        encripy3 = random.choice(cifer)
        encripy4 = random.choice(cifer)
        encripy5 = random.choice(cifer)
        encripy6 = random.choice(cifer)
        encripy7 = random.choice(cifer)
        saved = (p[0]+encripy0+p[1]+encripy1+p[2]+encripy2+p[3]+encripy3+p[4]+encripy4+p[5]+encripy5+p[6]+encripy6+p[7]+encripy7)
        with open("cesar.txt", "w", encoding="utf8")as w:
            w.write(f"{saved}\n")
            w.close()
            print("=> saved and encripyted file\n")

    else:
        print("(x) error in program\n")
        quit()

def __Descrypted__():

    hashes = "cesar.txt"
    text = str(input("=> hash: "))

    try:

	# O Nosso laço for so pode ler 1 arquivo da lista. se houver 2 hashes, ele não encontrara o segundo :(
        with open(hashes, "r") as file:
            for numberLine, line in enumerate(file, 1):
                if text in line:
                    print("[!] password\n")
                    print(numberLine, line[0]+line[2]+line[4]+line[6]+line[8]+line[10]+line[12]+line[14])

                else:
                    print("=> hash not found")
                    quit()

    except Exception as error:
        print("=> not found list", error)


if __name__ == "__main__":
    main()
