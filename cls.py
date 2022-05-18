class parrot:
    #class attribute
    species = "barid" #مشترک برای همه

    #instance attribute
    def __init__(self, name, age):
        self.name =name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

#instantiate the parrot class

blu = parrot("blu", 10)
woo = parrot("woo", 15)
print(blu.sing("happy"))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

print("blu is a {}".format(blu.species))