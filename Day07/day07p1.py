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
    lasers = {startPos}

    splitCount = 0

    for splitterLine in splitterPos:
        for splitter in splitterLine:
            if splitter in lasers:
                lasers.remove(splitter)
                lasers.add(splitter - 1)
                lasers.add(splitter + 1)
                splitCount += 1

    return splitCount


if __name__ == "__main__":
    print(f"The answer is: {main()}")
