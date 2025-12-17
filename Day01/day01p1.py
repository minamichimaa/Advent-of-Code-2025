def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def rotate(currentNum: int, direction: str, amount: int) -> int:
    if direction == 'L':
        newNum = (currentNum - amount) % 100
    else:
        newNum = (currentNum + amount) % 100

    return newNum

def parseInstruction(instruction: str) -> tuple[str, int]:
    direction = instruction[0]
    amount = int(instruction[1:])

    return (direction, amount)

def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()
    prettyPrint(textIn)

    currentNum = 50
    zeroCount = 0
    
    for instruction in textIn:
        dir, amount = parseInstruction(instruction)
        currentNum = rotate(currentNum, dir, amount)
        if currentNum == 0:
            zeroCount += 1
    
    return zeroCount

if __name__ == '__main__':
    print(f'The answer is: {main()}')