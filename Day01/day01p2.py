def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def rotate(currentNum: int, direction: str, amount: int) -> tuple[int, int]:
    fullRotations = amount // 100
    remainder = amount - (100 * fullRotations)

    if direction == 'L':
        newNum = currentNum - remainder
    else:
        newNum = currentNum + remainder

    if newNum < 0 or newNum > 99:
        fullRotations += 1
    newNum = newNum % 100
    return newNum, fullRotations


def parseInstruction(instruction: str) -> tuple[str, int]:
    direction = instruction[0]
    amount = int(instruction[1:])

    return (direction, amount)

def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    currentNum = 50
    zeroCount = 0
    for instruction in textIn:
        dir, amount = parseInstruction(instruction)
        currentNum, passedZero = rotate(currentNum, dir, amount)
        print(dir+str(amount), currentNum, passedZero)
        if passedZero:
            zeroCount += passedZero
    
    return zeroCount

if __name__ == '__main__':
    print(f'The answer is: {main()}')