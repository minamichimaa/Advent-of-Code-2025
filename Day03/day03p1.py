def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parseInput(input: list[str]) -> list:
    banks = []
    for line in input:
        banks.append(tuple([int(x) for x in line.strip()]))
    return banks


def findMaximumJoltage(bank: tuple[int]) -> int:
    aPos = 0
    aVal = bank[aPos]

    for i in range(1, len(bank) - 1):
        # print(i)
        if bank[i] > aVal:
            aVal = bank[i]
            aPos = i

    bVal = bank[aPos + 1]

    for j in range(aPos + 2, len(bank)):
        # print(j)
        if bank[j] > bVal:
            bVal = bank[j]

    return int(str(aVal) + str(bVal))


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    banks = parseInput(textIn)

    totalJoltage = 0
    for bank in banks:
        totalJoltage += findMaximumJoltage(bank)

    return totalJoltage


if __name__ == "__main__":
    print(f"The answer is: {main()}")
