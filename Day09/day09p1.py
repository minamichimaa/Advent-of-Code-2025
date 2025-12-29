from itertools import combinations


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parse(input: list[str]) -> list[list[int]]:
    coords = []
    for line in input:
        coords.append(tuple(int(x) for x in line.split(",")))

    return coords


def getArea(coords1: tuple[int, int], coords2: tuple[int, int]) -> int:
    xdiff = abs(coords2[0] - coords1[0]) + 1
    ydiff = abs(coords2[1] - coords1[1]) + 1

    return xdiff * ydiff


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    coordinates = parse(textIn)

    combos = combinations(coordinates, 2)

    largest = 0
    for a, b in combos:
        area = getArea(a, b)
        if area > largest:
            largest = area

    return largest


if __name__ == "__main__":
    print(f"The answer is: {main()}")
