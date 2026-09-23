'''Lists'''

results = ["Mario", "Luigi"]
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")
print(results)

# results.append(["Bowser", "Donkey Kong Jr."])
# results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."])
print(results)

results = ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']
results.remove("Bowser")
print(results)

results.insert(0, "Bowser")
print(results)

results.reverse()
print(1)
print(results)
