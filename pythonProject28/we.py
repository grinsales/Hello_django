class Alphabet:
    def __init__(self,lang,letters):
        self.lang=lang
        self.letters=letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        i=0
        z=[]
        for i in self.letters:
            if i==",":
                continue
            else:
                z.append(i)
        return (len(z))

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__(lang="En",letters="abcdefghijklmnopqrstuvwxyz")
    def __letters_num():
        return len("abcdefghijklmnopqrstuvwxyz")
    def is_en_letter(self,b):
        self.b=b
        a=self.letters
        if a.count(b)==1:
            print(f"{b} является буквой английского языка")
        else:
            print(f"{b} не является буквой английского языка")
    def letters_num(self):
        return EngAlphabet._EngAlphabet__letters_num()
    @staticmethod
    def example():
        return "My name is Max"

if __name__ == '__main__':

    asv=EngAlphabet() #Создайте объект класса EngAlphabet
    print(asv.letters) #Напечатайте буквы алфавита для этого объектаs
    print(asv.letters_num()) #Выведите количество букв в алфавите
    asv.is_en_letter("f") #Проверьте, относится ли буква F к английскому алфавиту
    asv.is_en_letter("щ") #Проверьте, относится ли буква щ к английскому алфавиту
    print(EngAlphabet.example()) #Выведите пример текста на английском языке