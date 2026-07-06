"""
Rakesh Shrestha
CSD325-T301 Advanced Python
Module 4.2 Assignment: High/Low Temperatures
Date : 07/04/2026

This program reads Sitka weather data from a CSV file and lets the user
choose whether to graph daily high temperatures, graph daily low temperatures,
or exit the program. The menu repeats until the user chooses to exit.

Changes made from the original sitka_highs.py program:
1. Added a menu with Highs, Lows, and Exit options.
2. Added a loop so the program continues until the user exits.
3. Added low temperature graphing in blue.
4. Added high temperature graphing in red.
5. Added functions to organize the code and improve readability.
6. Added an exit message.
"""

import csv
import sys
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt


CSV_FILENAME = "sitka_weather_2018_simple.csv"


def load_weather_data(filename):
    #Read dates, high temperatures, and low temperatures from a CSV file.
    dates, highs, lows = [], [], []
    file_path = Path(__file__).with_name(filename)

    with open(file_path, newline="") as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {row[2]}. Skipping this row.")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


def display_menu():
    #Display the program menu to the user.
    print("\nSitka Weather Menu")
    print("H - View high temperatures")
    print("L - View low temperatures")
    print("E - Exit")


def plot_temperatures(dates, temperatures, title, color):
    #Create and display a temperature graph.
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def main():
    #Run the menu-driven Sitka weather graph program.
    dates, highs, lows = load_weather_data(CSV_FILENAME)

    print("\nWelcome to the Sitka Weather Program.")
    print("Use the menu to view daily high temperatures, daily low temperatures, or exit.")

    while True:
        display_menu()
        choice = input("\nRS: ").strip().lower()

        if choice in ("h", "high", "highs"):
            plot_temperatures(dates, highs, "Daily high temperatures - 2018", "red")
        elif choice in ("l", "low", "lows"):
            plot_temperatures(dates, lows, "Daily low temperatures - 2018", "blue")
        elif choice in ("e", "exit", "q", "quit"):
            print("Thank you for using the Sitka Weather Program. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please enter H for highs, L for lows, or E to exit.")


if __name__ == "__main__":
    main()
