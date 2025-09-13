from medievalKingdom.utils import helpers as h
from medievalKingdom.utils import save as s
import start as st
# import keyboard

data = {

}

s.load(st.currentSave)
actionCount = 3
def gameloop(actions=actionCount):
    for _ in range(actions):
        print(f"you have {actions} actions.")
        command = h.inputadv(f"{h.settings["actionMsg"]}")

        if command == "quit":
            s.save(data)
            print("thanks for playing!")
            h.sleepadv(1)
            exit()
        elif command == "workers" or command == "worker":
            print("workers as of version 1.0:"
                  "1. scout"
                  "2. soldier"
                  "3. farmer"
                  "4. builder"
                  "5. blacksmith"
                  "6. scholar"
                  "7. diplomat"
                  "8. merchant"
                  "9. alchemist"
                  "10. gatherer")

        elif command == "cmds":
            cmd_help_ans = h.inputadv(
            "would you like to view:\n"
            "1. strategic commands [strategy]\n"
            "2. game commands [game] \n"
            "3. help commands [help]\n"
            "4. miscellaneous commands [misc]\n"
            "[b] to leave").strip().lower()
            if cmd_help_ans == "strategy":
                print("1. build [structure] - \n"
                      "2. train [number] - train your soldiers!\n"
                      "3. potion [number] - use a potion to gain strength!\n"
                      "4. scout [war/warnings] - send a scout to see nearby kingdoms\n"
                      "5. declare (declare war!!!)\n"
                      "6. status [game, population, structures] - see your stats\n"
                      "7. inv - check your resources\n"
                      "8. answer - answer requests from your population!\n"
                      "9. hire [job] - hire a worker\n")
                h.sleepadv(2)
                choice = h.inputadv("[b] to leave")
                if choice == "b":
                    return gameloop()
                else:
                    return
            elif cmd_help_ans == "game":
                print("1. end day - resets to a new day, giving you all of your bonuses from your workers!\n"
                      "2. quit - leaves the game\n"
                      "3. start/begin - returns to the start menu\n")
                h.sleepadv(2)
                choice = h.inputadv("[b] to leave")
                if choice == "b":
                    return gameloop()
                else:
                    return
            elif cmd_help_ans == "help":
                print("1. cmds - a list of commands and their function\n"
                      "2. help - learn how to play!\n"
                      "3. workers - a list of jobs\n")
                h.sleepadv(2)
                choice = h.inputadv("[b] to leave")
                if choice == "b":
                    return gameloop()
                else:
                    return
            elif cmd_help_ans == "misc":
                print("1. command - see how many commands you have left before the day ends\n"
                      "2. ver - see what version it is\n"
                      "3. suggest - suggest something to me!\n"
                      "4. bug - report a bug to me!\n"
                      "5. achievement - [WIP] check your achievement list!\n"
                      "6. join - join the discord!\n"
                      "7. ↑ ↑ ↓ ↓ ← → ← → b a - just, don't...\n")
                h.sleepadv(2)
                choice = h.inputadv("[b] to leave")
                if choice == "b":
                    return gameloop()
                else:
                    return
            elif cmd_help_ans == "b" or cmd_help_ans == "back":
                return gameloop()
            else:
                print("did not understand.")
                return
        elif command == "help":
            print("use commands (see input 'cmds') to strategize and build your kingdom.\n"
              "the goal of the game is to conquer and rule the land of scandinavia!!!\n"
              "finally, use 'quit' to end the game. gl and have fun!")
        elif command == "ver":
            print("ver 1.00 infdev\n"
              "current todo: skill tree + exploring!!!")
        elif command == "suggest":
            print("want to suggest something in the game? message me @pleasantblue556 on discord!")
            h.sleepadv(1)
            print("you can suggest features, commands, achievements, etc.")
            h.sleepadv(1)
            print("make sure to join the discord server so i know who you are (mutual server)")
        elif command == "bug" or command == "bugs":
            print("got any bugs? message me @pleasantblue556 on discord!")
        elif (command == "up up down down left right left right b a" or command == "↑↑↓↓←→←→ba" or
              command == "↑ ↑ ↓ ↓ ← → ← → b a"):
            print("--ex win32 sys.downloads.MedievalKingdom.values = echo $(( 2**64 - 1))")
            h.sleepadv(1)
            print(".")
            h.sleepadv(1)
            print("..")
            h.sleepadv(1)
            print("...")
            h.sleepadv(1)
            print("....")
            h.sleepadv(1)
            print(".....")
            h.sleepadv(1)
            print("jk lol")

        elif command == "invite":
            print("discord server invite is [ https://discord.gg/yCXRVB4jnP. ]\n"
                  "copy and paste it into your browser!!!")
        actions -= 1

gameloop()

# todo [1] // turn-based combat during war
# todo [NOW] // explore + secrets
# todo [3] // upgrade buildings before building new ones
# todo [4] // merchant economy
# todo [5] // army armor
# todo [bg] // skill tree

# next release [1.1]
# todo [] // tighter strategy
# todo [] // EXPAND JOBS!! pls :3
# todo [] // fertility affecting pop
# todo [] (l) // crafting.