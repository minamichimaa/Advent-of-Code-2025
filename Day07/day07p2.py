from collections import defaultdict


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parse(input: list[str]) -> tuple[int, list[list[int]]]:
    startPos = None
    splitterPosList = []
    for i, line in enumerate(input):
        if i % 2 == 1:
            continue
        splitterPos = []
        for j, x in enumerate(line):
            if x == "S":
                startPos = j
            if x == "^":
                splitterPos.append(j)
        if len(splitterPos):
            splitterPosList.append(splitterPos)

    return (startPos, splitterPosList)


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    prettyPrint(textIn)

    startPos, splitterPos = parse(textIn)
    lasers = defaultdict(int)
    lasers[startPos] = 1

    for splitterLine in splitterPos:
        for splitter in splitterLine:
            if splitter in lasers:
                oldLaser = lasers.pop(splitter)
                lasers[splitter - 1] += oldLaser
                lasers[splitter + 1] += oldLaser

    return sum(lasers.values())


if __name__ == "__main__":
    print(f"The answer is: {main()}")
