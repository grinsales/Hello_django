class human:
    default_name = "no name"
    default_age = 0
    def __init__(self,name=default_name,age=default_age):
        self.name = name
        self.age = age
        self.__money=0
        self.__house='none'
    def info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"money: {self.__money}")
        print(f"house: {self.__house}")
    @staticmethod
    def default_info():
        print(f"default_name: {human.default_name}")
        print(f"default_age: {human.default_age}")
    def earn_money(self,earn):
        self.__money += earn
        print(self.__money)
        
ar=human("AR",25)
ar.default_info()
ar.earn_money(5000)
human.info(ar)




