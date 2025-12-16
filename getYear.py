import argparse
from getDay import getDay, mostCurrentYear
from time import sleep

def numberOfDays(year: int) -> int:
    if year >= 2025:
        return 12
    else: 
        return 25

if __name__ == '__main__':
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', nargs="?")
    args = parser.parse_args()

    # default most current year
    year = int(args.year) if args.year else mostCurrentYear()

    for i in range(1, numberOfDays(year) + 1):
        getDay(i, year)
        sleep(0.6)