users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "long4password")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)