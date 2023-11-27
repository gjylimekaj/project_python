class Human:
    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def return_name(self):
        return self.name

    def show_info(self):
        return f"My name is: {self.name}. I am {self.age} years old, and I am a {self.gender}."

h = Human('gjyli',26,'female')
print(h.show_info())
print(h.return_name())