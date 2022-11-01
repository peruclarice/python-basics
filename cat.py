from turtle import color


class Cat():
    species = ""
    eyeColor = ""
    weight = "5 kg"
    lifeSpan = 14
    age = 0

    def currentLifeSpan(self):
        lifeSpan = 21
        message = f"The cat's lifespan is {lifeSpan}"
        print(message)
    
    def diffSpecies(self, species):
        print(f"{species}")

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age


# Instanciating class Cat() with new object cat

cat = Cat("9kg", 5)
cat.species = "Turtle"
cat.eyeColor = "Green"

print(f"My cat's weight is {cat.weight}")
cat.currentLifeSpan()
cat.diffSpecies("calico")
print(f"Cat's age is {cat.age} and my cat's weight is {cat.weight}")
