import aocd
import argparse
import os
import requests
import shutil

from bs4 import BeautifulSoup
from datetime import date
from dotenv import load_dotenv

load_dotenv()
AOC_SESSION=os.getenv('AOC_SESSION')

def mostCurrentYear() -> int:
    # check month
    if date.today().month == 12:
        year = date.today().year
    else:
        year = date.today().year - 1
    
    return year

def getDay(day:int, year:int):
    # copy directory
    directoryName = f'Day{(str(day).rjust(2,'0'))}'
    shutil.copytree('template', directoryName)

    # rename python file
    shutil.move(f'{directoryName}/day00p1.py', f'{directoryName}/day{str(day).rjust(2,'0')}p1.py')

    # get and write input data
    with open(f'{directoryName}/input.txt', 'w', encoding='utf8') as f:
        data = aocd.get_data(day=day, year=year).strip()
        f.write(data)

    # get question
    url = f'https://adventofcode.com/{year}/day/{day}'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    desc = soup.find('article', {'class':'day-desc'})

    # write question
    with open(f'{directoryName}/question.txt', 'w', encoding='utf8') as f:
        question = desc.get_text().strip()
        f.write(question)

    # get and write text input data
    test = aocd.models.Puzzle(day=day, year=year).examples
    for i, data in enumerate(test):
        with open(f'{directoryName}/test{i}.txt', 'w', encoding='utf8') as f:
            f.write(data.input_data.strip())

if __name__ == '__main__':
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument( '-d', '--day')
    parser.add_argument('-y', '--year', nargs="?")
    args = parser.parse_args()

    day = int(args.day)
    # default most current year
    year = int(args.year) if args.year else mostCurrentYear()

    getDay(day, year)