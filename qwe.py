class Ex1:
    def __init__(self, plaintext):
        self.text = plaintext

    def encrypt(self, cryptogram):
        tabofconsonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "x", "z"]
        consonant = ""
        for x in range(len(self.text)):
            a = x
            for y in range(len(tabofconsonants)):
                if self.text[a] == tabofconsonants[y]:
                    cryptogram[a] = consonant
                    consonant = self.text[x]
            for z in range(len(tabofconsonants)):
                if self.text[0] == tabofconsonants[z]:
                    cryptogram[0] = consonant
                if self.text[1] == tabofconsonants[z]:
                    cryptogram[1] = consonant
        return cryptogram, plaintext.lower()


plaintext = input("Napisz slowo które chcesz zmienić: ")
tab = list(plaintext.lower())
tab2 = list(plaintext.lower())

a1 = Ex1(tab)
print(a1.encrypt(tab2))



