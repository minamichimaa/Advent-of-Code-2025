from math import prod


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parse(input: list[str]) -> tuple[list[list[int]], list[str]]:
    numbersList = None
    signsList = []

    for line in input:
        newLine = line.split()
        if numbersList == None:
            numbersList = [[] for x in range(len(newLine))]
        for i, x in enumerate(newLine):
            if x.isdigit():
                numbersList[i].append(int(x))
            else:
                signsList.append(x)
    return (numbersList, signsList)


def solve(numbersList, signsList) -> int:
    total = 0

    for i, sign in enumerate(signsList):
        if sign == "*":
            total += prod(numbersList[i])
        else:
            total += sum(numbersList[i])

    return total


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    numbersList, signsList = parse(textIn)

    return solve(numbersList, signsList)


if __name__ == "__main__":
    print(f"The answer is: {main()}")
