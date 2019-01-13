import random
x = 0

print("1: D4")
print("2: D6")
print("3: D8")
print("4: D10")
print("5: D20")
print("6: D100")
print("7: Coin Flip")
print("8: D custom")
a = int(input())

if(a == 1):
    b = int(input("how many do you want to roll "))
    while(x != b):
        print(int(random.randrange(4)) + 1)
        x = x + 1

if(a == 2):
    b = int(input("how many do you want to roll "))
    while(x != b):
        print(int(random.randrange(6)) + 1)
        x = x + 1

if(a == 3):
    b = int(input("how many do you want to roll"))
    while(x != b):
        print(int(random.randrange(8)) + 1)
        x = x + 1

if(a == 4):
    b = int(input("how many do you want to roll "))
    while(x != b):
        print(int(random.randrange(10)) + 1)
        x = x + 1

if(a == 5):
    b = int(input("how many do you want to roll "))
    while(x != b):
        print(int(random.randrange(20)) + 1)
        x = x + 1

if(a == 6):
    b = int(input("how many do you want to roll "))
    while(x != b):
        print(int(random.randrange(100)) + 1)
        x = x + 1

if (a == 7):
    b = int(input("how many do you want to flip "))
    while(x != b):
        c = int(random.randrange(2))
        if (c == 0):
            print("you got heads")
        if (c == 1):
            print("you got tails")
        x = x + 1

if (a == 8):
    b = int(input("how many sides do you need "))
    c = int(input("how many do you want to roll "))
    while(x != c):
        print(int(random.randrange(b)) + 1)
        x = x + 1
