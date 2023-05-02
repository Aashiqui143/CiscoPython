secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user = int(input("Enter the number = "))
while user!=secret_number:
    print("You are stuck in my loop")
    user=int(input("Enter the number = "))
print("Congrats, Now you are free")
