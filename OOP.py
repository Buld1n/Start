class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name
    def get_age_and_name(self):
        return self.age, self.get_name()

Human_1 =  Human(age=25, name='Tim', gender='male')

print(Human_1.get_age_and_name())
