def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def rotate(currentNum: int, direction: str, amount: int) -> tuple[int, int]:
    passedZero = 0
    newNum = currentNum
    if direction == "L":
        for i in range(amount):
            newNum = (newNum - 1) % 100
            if newNum == 0:
                passedZero += 1
    else:
        for i in range(amount):
            newNum = (newNum + 1) % 100
            if newNum == 0:
                passedZero += 1

    return (newNum, passedZero)


def parseInstruction(instruction: str) -> tuple[str, int]:
    direction = instruction[0]
    amount = int(instruction[1:])

    return (direction, amount)


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()
    # prettyPrint(textIn)

    currentNum = 50
    zeroCount = 0
    for instruction in textIn:
        dir, amount = parseInstruction(instruction)
        currentNum, passedZero = rotate(currentNum, dir, amount)
        print(dir + str(amount), currentNum, passedZero)
        if passedZero:
            zeroCount += passedZero

    return zeroCount


if __name__ == "__main__":
    print(f"The answer is: {main()}")
