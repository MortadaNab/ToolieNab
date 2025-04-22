import random
import time
import string
import requests
from pytube import YouTube
from pytube.exceptions import RegexMatchError

# Color Variables
Red = "\033[31m"
Green = "\033[32m"
yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
White = "\033[37m"
Reset = "\033[0m"

# Tool Name Display
print("""
\n┏━━━━┓╋╋╋╋┏┓
┃┏┓┏┓┃╋╋╋╋┃┃
┗┛┃┃┣┻━┳━━┫┃┏┳━━┓
╋╋┃┃┃┏┓┃┏┓┃┃┣┫┃━┫
╋╋┃┃┃┗┛┃┗┛┃┗┫┃┃━┫
╋╋┗┛┗━━┻━━┻━┻┻━━┛
""")

# Display Tools Menu
def show_tools():
    print(f"{Green}Here is the set of tools you can use:")
    print("""
1. Multiplication Table
2. Unit Measurement
3. Youtube Downloader Video (Beta)
4. Simple Spam Tool
5. Normal Spam Tool
6. Professionalism Spam Tool (للكمبيوترات)
7. Generate Passwords
8. Generating TikTok Usernames (Soon...)
9. Generating Instagram Usernames (Soon...)
10. Generating Usernames
11. Rock, Paper, Scissors Game
12. Calculator
13. About us
14. Mental Math Game
15. Guess The Number Game
""")

# Tool Definitions
def multiplication_table():
    print(f"{Red}Welcome To Multiplication Table")
    number = int(input("Enter the number you want to see the multiplication table for: "))
    end = int(input("To which number do you want to see the table? "))
    for x in range(end + 1):
        print(f"{number} × {x} = {number * x}")

def unit_measurement():
    print(f"{Red}Welcome To Unit Measurement")
    print("""
1. Hours to Seconds
2. Centimeter to Meter
3. Meter to Kilometer
""")
    unit = int(input("Enter the number of the choice you want to run: "))
    if unit == 1:
        hour = int(input("How many hours you want to convert to seconds? "))
        result = hour * 3600
        print(f"{hour} × 3600 = {result}")
    elif unit == 2:
        cm = int(input("Enter the centimeters to convert to meters: "))
        result = cm / 100
        print(f"{cm} ÷ 100 = {result}")
    elif unit == 3:
        meter = int(input("Enter the meters to convert to kilometers: "))
        result = meter / 1000
        print(f"{meter} ÷ 1000 = {result}")
    else:
        print("Invalid selection")

def simple_spam():
    print(f"{Red}Welcome To Spam Tool")
    message = input("Enter the message you want to spam: ")
    count = int(input("How many times do you want to send this message? "))
    for x in range(count):
        print(message)

def normal_spam():
    print(f"{Red}Welcome To Normal Spam Tool")
    message = input("Enter the message you want to spam: ")
    count = int(input("How many times do you want to send this message? "))
    delay = int(input("How many seconds between each message? "))
    for x in range(count):
        print(message)
        time.sleep(delay)

def professionalism_spam():
    print(f"{Red}للكمبيوترات فقط")

def generate_password():
    print(f"{Red}Welcome To Generate Password Tool")
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"{Red}The Generated Password: {password}")

# Username Generator Tool
def generate_username():
    all_chars = string.ascii_lowercase + string.digits
    separator = random.choice([".", "_"])
    parts = random.choices(all_chars, k=4)
    insert_index = random.randint(1, 3)
    parts.insert(insert_index, separator)
    return ''.join(parts)

def generate_multiple_usernames(count):
    return [generate_username() for _ in range(count)]

def username_tool():
    print(f"{Red}Welcome to the Username Generator")
    try:
        count = int(input("How many usernames do you want to generate? "))
        usernames = generate_multiple_usernames(count)
        print("\nGenerated Usernames:")
        for username in usernames:
            print(username)
    except ValueError:
        print("Invalid number!")

# Rock, Paper, Scissors Game
def show_rules():
    print("""**** Rules ****
1. Rock defeats Scissors.
2. Scissors defeat Paper.
3. Paper defeats Rock.
4. First to 5 points wins!
""")

def rock_paper_scissors():
    tools = ["Rock", "Paper", "Scissor"]
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        print(f"\nScore: You [{player_score}] - Computer [{computer_score}]")
        rule = input("Press [Enter] to play, type 'help' for rules, or 'exit' to quit: ").lower()

        if rule == "help":
            show_rules()
            continue
        elif rule == "exit":
            print("Thanks for playing! Goodbye!")
            break

        computer = random.choice(tools)
        player = input("Your Choice (Rock, Paper, Scissors): ").capitalize()

        if player not in tools:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        print(f"Computer Chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "Rock" and computer == "Scissor") or \
             (player == "Scissor" and computer == "Paper") or \
             (player == "Paper" and computer == "Rock"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        if player_score == 5:
            print("\nYou won the game!")
            break
        elif computer_score == 5:
            print("\nComputer won the game!")
            break

# Calculator
def calculator():
    print("Welcome to the Simple Calculator!")
    print("You can perform any operation (e.g., 2 + 2, 5 * 3, etc.)")

    while True:
        expression = input("Enter the operation (or type 'exit' to quit): ")

        if expression.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            result = eval(expression)
            print(f"The result of '{expression}' is: {result}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid operation.")

# YouTube Downloader
def youtube_downloader():
    print(f"{Red}Welcome to YouTube Video Downloader")
    url = input("Enter YouTube video URL: ")
    
    try:
        if "youtube.com/shorts/" in url:
            video_id = url.split('/')[-1].split('?')[0]
            url = f"https://www.youtube.com/watch?v={video_id}"
        
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        if video_stream:
            video_stream.download()
            print("Download completed successfully!")
        else:
            print("No suitable video stream found.")
    
    except RegexMatchError:
        print("Error: Invalid YouTube URL format.")
    except Exception as e:
        print(f"Error: {e}")

def about_us():
    print("""
    
    تم تطوير و برمجة هذه الاداة من قبل MortadaNab
    الاداة قيد تطوير حاليا 
    اذا وجدت اي خطا ابلغنا عبر ايميل da0571004@gmail.com
    
    شكر خاص لنفسي
    
""")

# Mental Math Game (fix)
def Mental():
    print("Welcome To Mental Math Game")
    Score = 0
    for _ in range(5):
        n1 = random.randint(1, 12)
        n2 = random.randint(1, 12)
        result = n1 * n2
        print(f"{n1} × {n2} = ?")
        start_time = time.time()
        try:
            answer = int(input("Answer: "))
            elapsed = time.time() - start_time
            if elapsed > 5:
                print("Too slow!")
            elif answer == result:
                print("Correct!")
                Score += 1
            else:
                print(f"Wrong! The answer was {result}")
        except:
            print("Invalid input")
    print(f"Final Score: {Score}/5")

# Guess The Number Game (NEW TOOL #15)
def guess_the_number():
    print("Welcome to Guess The Number!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except:
            print("Enter a valid number!")

# Main Program
def run_tool():
    while True:
        show_tools()
        choice = input("Enter the number of the tool you want to run: ")

        if choice == "1":
            multiplication_table()
        elif choice == "2":
            unit_measurement()
        elif choice == "3":
            youtube_downloader()
        elif choice == "4":
            simple_spam()
        elif choice == "5":
            normal_spam()
        elif choice == "6":
            professionalism_spam()
        elif choice == "7":
            generate_password()
        elif choice == "8":
            print("Coming soon...")
        elif choice == "9":
            print("Coming soon...")
        elif choice == "10":
            username_tool()
        elif choice == "11":
            rock_paper_scissors()
        elif choice == "12":
            calculator()
        elif choice == "13":
            about_us()
        elif choice == "14":
            Mental()
        elif choice == "15":
            guess_the_number()
        else:
            print("Tool not available yet.")

        again = input(f"{yellow}Do you want to go back to the tools menu? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

# Start or Exit
def start_program():
    start = input(f"{Cyan}Please press space to start or 'exit' to leave: ").lower()

    if start == "exit":
        print("Goodbye!")
        exit()
    elif start == " " or start == "":
        print("Welcome to Toolie")
        run_tool()
    else:
        print("Invalid selection")
        exit()

start_program()