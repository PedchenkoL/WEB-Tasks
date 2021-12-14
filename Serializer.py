import json

class A:
	def __init__(self, name, surname, age):
	    self.name = name
	    self.surname = surname
	    self.age = age


pers = A('qwe', 'rty', 12)
mas = {
                "name": pers.name, "surname": pers.surname, "age": pers.age
                }
print(pers.__dict__)

with open("data_file.json", "w") as write_file:
    json.dump(pers.__dict__, write_file)



print(type(pers.__dict__))