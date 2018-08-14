""" Eveey Connolly """
MIN_PASSWORD_LENGTH = 3
password = input("Enter Password:")

while len(password) < MIN_PASSWORD_LENGTH:
    password = input("Enter Password:")

for i in range(0, len(password)):
    print("*", end="")
