num = str(raw_input("Number:"))
word = str(raw_input("Object:"))
print(num)
print(word)
if num == 0 or int > 1 and word[-3:] == "ife":
    print(num + " " + word[:-3] + "ves")
elif num == 0 or int > 1 and word[-2:] == "sh":
    print(num + " " + word[:-2] + "shes")
elif num == 0 or int > 1 and word[-2:] == "ch":
    print(num + " " + word[:-2] + "ches")
elif num == 0 or int > 1 and word[-2:] == "us":
    print(num + " " + word[:-2] + "i")
elif num == 0 or int > 1 and word[-2:] == "ay":
    print(num + " " + word[:-2] + "ays")
elif num == 0 or int > 1 and word[-2:] == "oy":
    print(num + " " + word[:-2] + "oys")
elif num == 0 or int > 1 and word[-2:] == "ey":
    print(num + " " + word[:-2] + "eys")
elif num == 0 or int > 1 and word[-2:] == "uy":
    print(num + " " + word[:-2] + "uys")
elif num == 0 or int > 1 and word[-1:] == "y":
    print(num + " " + word[:-1] + "ies")
elif num == 0 or int > 1:
    print(num + " " + word + 's')
else:
    print(num + word)
