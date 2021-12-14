numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Jen"]
starts_s = [x for x in friends if x.startswith("S")]
print(starts_s)
