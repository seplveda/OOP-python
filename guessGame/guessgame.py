guess = 1

while True:
    num = input("Please guess a number between 0@100: ")
    try:
        num = int(num)
    except:
        print("Not even close!, try next time please!")
        continue

    if num < 69:
        print("under the hood!!")
    elif num > 69:
        print("over the hood!!")
    else:
        break

    guess += 1

print(f"You got it!, total attempts: {guess}")
