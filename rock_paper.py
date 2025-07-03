import random    # we have to input a random choice from computer from the tuple (option)
import pygame
from colorama import Fore, Style, init,Back
init(autoreset=True)

pygame.mixer.init()
pygame.mixer.music.load('356-8-bit-chiptune-game-music-357518.mp3')
pygame.mixer.music.play(-1)

option = ("rock", "paper", "scissor")
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}
playing = True

while playing == True:
    # generate a random choice from a tuple
    computer_choice = random.choice(option)
    user_choice = None

    # ask for the user to input their choice
    while user_choice not in option:
        user_choice = input(Fore.BLUE+"\n \n Enter your choice to play rock paper scissor  :   ").lower()

    print(Fore.MAGENTA+f"\n \tcomputer choice is {computer_choice}{emoji[computer_choice]}")  # to display the both value
    print(Fore.MAGENTA+f"\n\tYour choice is {user_choice}{emoji[user_choice]}")

    if computer_choice == user_choice:
        print(Fore.YELLOW+"\n suprisingly it is a tie🥶🥶")

    elif computer_choice == "paper" and user_choice == "rock":
        print(Fore.RED +"\n you lost😭")

    elif computer_choice == "paper" and user_choice == "scissor":
        print(Fore.GREEN +"\n congratulation you won 🔥🔥!!!"+Style.BRIGHT)

    elif computer_choice == "rock" and user_choice == "paper":
        print(Fore.GREEN +"\n congratulation you won 🔥🔥!!!"+Style.BRIGHT+Back.YELLOW)

    elif computer_choice == "rock" and user_choice == "scissor":
        print(Fore.RED +"\n you lost😭")

    elif computer_choice == "scissor" and user_choice == "paper":
        print(Fore.RED +"\n you lost😭")

    elif computer_choice == "scissor" and user_choice == "rock":
        print(Fore.GREEN +"\n congratulation you won 🔥🔥!!!"+Style.BRIGHT+Back.YELLOW)

    
    replay = input(Fore.CYAN+"\n Do you want to play next round? 😅😅     Yes/N0: ").lower()
    if replay not in ["yes", "y"]:
        playing = False
        print("\n NO PROBLEM !! Thanks for playing!😍😍")
