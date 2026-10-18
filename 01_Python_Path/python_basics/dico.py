stuff = {"food": 15, "energy": 100, "enemies":3}
print(stuff.get("food"))

print(stuff.items())

print(stuff.keys())
print(stuff.values())

print(stuff.popitem())
print(stuff)

print(stuff.setdefault("friends", 123))
print(stuff)