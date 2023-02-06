from smartphone import Smartphone

smartphone_1 = Smartphone("Xiaomi", "8s", "+79922211195")
smartphone_2 = Smartphone("Xiaomi", "9s", "+79922211196")
smartphone_3 = Smartphone("Xiaomi", "10s", "+79922211197")
smartphone_4 = Smartphone("iPhone", "12 Pro", "+79922211198")
smartphone_5 = Smartphone("iPhone", "14 mini", "+79922211199")


catalog = [smartphone_1, smartphone_2, smartphone_3, smartphone_4, smartphone_5]

for x in catalog:
    x.say_smartphone()