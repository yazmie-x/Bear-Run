print(r'''       _
              (\\  _                      ___
             .-"`"(\\                _.""`   `"-.
            /      ` `-._        _.-"            `\__
           6   6)        `-.__.-'                    `",
          /                                         `;-`
         /     ,                                     |
        ()    /  /`                                  |
         `---`"~``\                                  |
                   \                                 |
                    \            \      /           /
                    /`,   ,      |     |           /
                   /   "-.|      |     |         /'
                  /     / |     /,__   |       /`\
             jgs /    /'  |    /    `"'\      (   \
              __/   /'    |   |         `\     \   \
              \    /      |   |           `\    \   \
               `-,/      /    |            /     |-"`
                        `"""^^^           `^^""""`
''')
print("Welcome to Bear Run.")
print("Your mission is to escape from a bear.")
start = input("Are you ready to begin? (Y/N) \n").upper()
if start == "Y" or start == "YES":
    print("You're at a cross road, Where do you want to go?")
    direction = input('Type "left" or "right": \n').lower()
    if direction == "left" or direction == "L":
        print("You see a river, Do you swim or stay on land?")
        river = input('Type "swim" or "stay": \n').lower()
        if river == "stay":
            print("You see 3 colored doors. White, Pink, or Black?")
            doors = input('Type "white" or "pink, or "black": \n').lower()
            if doors == "black" or doors == "b":
                print("The Black door looms silently. "
                      "You push it open, and beyond lies a safe passage. "
                      "You've Chosen Wisely")
                print("Congrats!")
            elif doors == "white" or doors == "w":
                print("The White door shines brightly. "
                      "You step through... The blinding light disorients you, "
                      "and you fall into a pit. Game Over.")
            elif doors == "pink" or doors == "p":
                print("The pink door looks cheerful. "
                      "Inside, sweet -smelling gas fills the room. "
                      "You collapse. Game Over")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        elif river == "swim":
            print("Something moved beneath the surface. Jaws snaps Shut. Game over.")
    elif direction == "right" or direction == "r":
        print('You fell into a hole. Game over.')
elif start == "N" or start == "NO":
    print("Oki Goodbye.")
else:
    print("You typed wrong.")