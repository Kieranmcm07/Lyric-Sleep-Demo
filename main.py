import sys
from rich import print
from time import sleep



def print_intro():
    print("\n[cyan][!] Welcome to the Lyric Sleep Demo![/cyan]")
    print("\nThis script prints song lyrics with delays between each character and line to show off the sleep function.\n")
    print("[red][!] Created by Kieranmcm07 on GitHub.\n")

def display_menu():
    print("[bold][green]Menu:[/green][/bold]")
    print("1. Run lyric sleep demo")
    print("2. Test custom sleep delay")
    print("3. Exit")

def lyric_sleep_demo():
    # List of (lyric, delay per character)
    lyric_lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]
    # Delay after each line
    line_pauses = [0.2, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5]

    for idx, (lyric, char_pause) in enumerate(lyric_lines):
        for letter in lyric:
            # Special color for chorus line
            if lyric == '(Rock your body)':
                print(f"[orange4]{letter}[/orange4]", end='')
            else:
                print(f"[bold][gold3]{letter}[/bold][/gold3]", end='')
            sys.stdout.flush()
            sleep(char_pause)
        print()  # Newline after each lyric line
        sleep(line_pauses[idx])

def custom_sleep_test():
    try:
        delay = float(input("Enter a delay in seconds (e.g. 0.5): "))
        print(f"Sleeping for {delay} seconds...")
        sleep(delay)
        print("Done!")
    except ValueError:
        print("[red]Invalid input. Please enter a number.[/red]")

def main():
    print_intro()
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            lyric_sleep_demo()
        elif choice == '2':
            custom_sleep_test()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("[red]Invalid choice. Please try again.[/red]")

if __name__ == "__main__":
    main()