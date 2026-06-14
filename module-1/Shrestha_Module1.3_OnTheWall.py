"""
Author:      Rakesh Shrestha
Date:        June 14, 2026
Course:      CSD-325
Assignment:  Module 1.3 – On the Wall
Description: Prompts the user for a starting number of bottles, then calls a
             countdown function that prints the "Bottles of Beer on the Wall"
             lyrics counting down to 1, using correct singular/plural grammar.
             After the countdown the main program reminds the user to buy more
             beer.
"""


def countdown(bottles):
    """
    Count down from `bottles` to 1, printing the song lyrics for each step.

    Parameters
    ----------
    bottles : int
        The number of bottles to start the countdown from (must be >= 1).
    """
    count = bottles

    while count >= 1:
        if count == 1:
            # Singular form for the last bottle
            print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.\n")
        else:
            # Plural form for all other counts
            next_count = count - 1
            next_label = "1 bottle" if next_count == 1 else f"{next_count} bottles"
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            print(f"Take one down, pass it around, {next_label} of beer on the wall.\n")

        count -= 1


def main():
    """Prompt the user for input, call the countdown function, then sign off."""
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles < 1:
                print("Please enter a positive whole number.\n")
                continue
            break
        except ValueError:
            print("Invalid input – please enter a whole number.\n")

    print()  # blank line before lyrics begin
    countdown(bottles)
    print("Time to go buy more beer!")

        
if __name__ == "__main__":
    main()
