capitals = ["Amsterdam", "Tokyo", "London", "Cape Town"]
print(capitals)
print(capitals[0])

capitals.append("Paris")
print(capitals)
print(capitals[1:3])
print(capitals[::-1])
capitals.append("Cape Town")
print(capitals)
print(capitals.count("Cape Town"))
print(len(capitals))
capitals.remove("Cape Town")
print(capitals)
capitals.insert(0, "100")
print(capitals)
capitals[0] = "Washington"
print(capitals)