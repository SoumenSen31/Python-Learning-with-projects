name = input("Enter Your Name: ")
print(f"Hello {name} Welcome to our Game ..!!")

should_we_play = input("Do you want to play? :").lower()
if should_we_play == "y" or should_we_play == "yes":
    print("Game Starting...")
    weapon = input("Choose a weapon(axe/sword): ").lower()

    direction = input("Choose Your Direction(Left/Right): ").lower()
    if direction == "left":
        print(f"You went left and fell of a cliff, game over, try again")
    elif direction == "right":
        choise = input(
            "Okay You are on the right direction.You now see a bridge. Do you want to swim or cross it?(Swim/Cross): "
        ).lower()

        if choise == "swim" and weapon == "axe":
            print(f"You are clever though.You kill the alligator, You Win!")
        elif choise == "swim" and weapon == "sword":
            print("You got eaten by an alligator, you die, the end!")
        else:
            print("You found the Gold and You Won..!!")

    else:
        print("sorry it's not a valid reply. You Die")
else:
    print("we are not playing")
