import random

print("This program will help you to generate a random password!!")


capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_letters = [x.lower() for x in capitals]
all_letters = ['1','2','3','4','5','6','7','8','9','0','@','$','%','&','*']
all_letters = capitals + small_letters + all_letters
random.shuffle(all_letters)

password = ""

while 1:
    try:
        size = int(input("Enter the minimum size of the password needed (8+ Recommended) : "))
        break
    except:
        print("Only Numbes Allowed !!\n")

for i in range(size):
    rand = random.choice(all_letters)
    password = password + rand

print("\nYour Password : "+password)


