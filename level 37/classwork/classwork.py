print([x for x in range(1, 101)])
print([x for x in range(1, 101, 2)])
names = ["Ana", "Giorgi", "Luka", "Nino", "Sandro"]
new_names = ["#" + name for name in names if "a" not in name.lower()]
print(new_names)