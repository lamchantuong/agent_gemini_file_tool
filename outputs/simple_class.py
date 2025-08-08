class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

# Example usage
my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
print(my_dog.bark())