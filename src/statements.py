playerMovement = 0
keyInput = input("Press a key to move the player: ")

if keyInput == 'w':
    playerMovement = playerMovement + 1
    print("The player moved " + playerMovement + " steps")
elif keyInput == 'a':
    print("Player moved left")
else:
    print("Invalid key")
