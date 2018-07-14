def rules():
    print("""RPG GAME
========
Get to the garden with
key and Toolkit.

Commands:
  go[direction]
  get[item]
  go[up] or go[down]

------------------------------------""")


currentRoom = "Hall"
Inventory = []

ways = {

    "Hall": {
        "south": "Kitchen",
        "east": "Dining Room",
        "item": "key",
    },

    "Hall Terrace": {

    },

    "Kitchen": {
        "north": "Hall",
        "east": "Lobby"
    },

    "Kitchen Terrace": {
        "item": "Toolkit",
        "up": "True",
        "down": "Kitchen"
    },

    "Dining Room": {
        "west": "Hall",
        "south": "Lobby",
        "up": "Dining Room Terrace"
    },

    "Dining Room Terrace": {
        "item": "Toolkit",
        "down": "Dining Room"
    },

    "Lobby": {
        "north": "Dining Room",
        "west": "Kitchen",
        "east": "Garden"
    },

    "Lobby Terrace": {
        "item": "Toolkit",
        "up": "True",
        "down": "Dining Room"
    },

    "Garden": {
        "west": "Lobby"
    },
}


def show_status():
    print("You are in the " + currentRoom)
    print("Inventory: " + str(Inventory))
    if "item" in ways[currentRoom]:
        print("There is a " + ways[currentRoom]["item"])
    print("------------------------------------")


def get_directions():
    try:
        action, direction = input("> ").split(" ")
    except ValueError:
        print("------------------------------------")
        print("Wrong command!!!")
        print("------------------------------------")
        show_status()
    except UnboundLocalError:
        print("------------------------------------")
        print("Wrong command!!!")
        print("------------------------------------")
        show_status()
    else:
        print("------------------------------------")
        if action == "go":
            if direction in ways[currentRoom]:
                global currentRoom
                currentRoom = ways[currentRoom][direction]
                show_status()
            else:
                print("There is no direction named " + direction)
                print("------------------------------------")
                show_status()

        if action == "get":
            if "item" in ways[currentRoom]:
                if direction == ways[currentRoom]["item"]:
                    global Inventory
                    Inventory.append(ways[currentRoom]["item"])
                    del ways[currentRoom]["item"]
                    show_status()
                else:
                    print("There is no item named " + direction)
                    print("------------------------------------")
                    show_status()
            else:
                print("There is no item named: " + direction)
                print("------------------------------------")
                show_status()

        if action == "go" and direction == "up":
            if direction in ways[currentRoom]:
                currentRoom = ways[currentRoom][direction]
                show_status()
            else:
                print("No way to go up.")
                print("------------------------------------")
                show_status()

        if action == "go" and direction == "down":
            if direction in ways[currentRoom]:
                currentRoom = ways[currentRoom][direction]
                show_status()
            else:
                print("There is no way to go down")
                print("------------------------------------")
                show_status()


if __name__ == "__main__":
    rules()
    show_status()

    while True:
        if "key" and "Toolkit" in Inventory and currentRoom == "Garden":
            print("Congratulations!! You made it")
            break
        else:
            get_directions()
