# students = ["Alice", "Javi", "Damien"]
# students.append("Delijah")
# print(students)
#
# students = ["Alice", "Javi", "Damien"]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Jorge", "Omar", "Eduardo", "Selina"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# count = 0
# for name in smith_siblings:
#     count = count + 1
# print(count)
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Jorge", "Omar", "Eduardo", "Selina"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
#
# print(smith_siblings)
#
# superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
#
# demoted_hero = str(raw_input("what superhero do you want to elimate from the top 5?"))
#
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found.")

names  = ["Rickon", "Bran", "Arya", "Sanasa","Jon", "Robb"]
print(names[::-1])
print(names[4:2:-1])
