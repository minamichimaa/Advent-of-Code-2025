def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def validId(id: int) -> bool:
    strId = str(id)
    # odd number of digits
    if len(strId) % 2 == 1:
        return True

    # even number of digits
    # split in half and compare
    halfLen = len(strId) // 2
    if strId[:halfLen] == strId[halfLen:]:
        return False
    return True


def parseInput(input: str) -> list[tuple[int, int]]:
    idRanges = input.split(",")
    newIdRanges = []
    for idRange in idRanges:
        a, b = idRange.split("-")
        newIdRanges.append((int(a), int(b)))
    return newIdRanges


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    invalidIdSum = 0
    idRanges = parseInput(textIn[0])

    for startRange, endRange in idRanges:
        for id in range(startRange, endRange + 1):
            if not validId(id):
                invalidIdSum += id

    return invalidIdSum


if __name__ == "__main__":
    print(f"The answer is: {main()}")
