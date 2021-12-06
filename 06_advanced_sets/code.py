friends = {"Rolf"}
abroad = {"Bob", "Anne"}

local_friends = friends.union(abroad)
print(local_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam"}
bot = art.intersection(science)
print(bot)