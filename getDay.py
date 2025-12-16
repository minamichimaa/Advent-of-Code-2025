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

def mostCurrentYear():
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
    test = sorted(desc.find_all('code'), key=lambda x: len(x.get_text()), reverse=True)
    with open(f'{directoryName}/test.txt', 'w', encoding='utf8') as f:
        data = test[0].get_text().strip()
        f.write(data)

if __name__ == '__main__':
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument('--day')
    parser.add_argument('--year', nargs="?")
    args = parser.parse_args()

    day = int(args.day)
    # default most current year
    year = int(args.year) if args.year else mostCurrentYear()

    getDay(day, year)