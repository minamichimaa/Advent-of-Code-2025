import math

from itertools import combinations


class Circuit:
    def __init__(self, box1, box2):
        self.boxes = {box1, box2}

    def addBox(self, box):
        if isinstance(box, tuple):
            self.boxes.add(box)
        elif isinstance(box, list) or isinstance(box, set):
            self.boxes.update(box)

    def __len__(self):
        return len(self.boxes)

    def __repr__(self):
        return str(self.boxes)


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parse(input: list[str]):
    boxList = []
    for line in input:
        boxList.append(tuple([int(x) for x in line.split(",")]))

    return boxList


def getDistance(box1: tuple[int, int, int], box2: tuple[int, int, int]):
    x1, y1, z1 = box1
    x2, y2, z2 = box2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    boxList = parse(textIn)

    distances = []

    circuits = set()
    connectedBoxes = {}

    # get all combinations of boxes
    combos = combinations(boxList, 2)
    for box1, box2 in combos:
        distances.append([getDistance(box1, box2), (box1, box2)])

    sortedDistances = sorted(distances, key=lambda x: (x[0], x[1]))

    iterations = 1000

    for i, connection in enumerate(sortedDistances):
        # do for i iterations
        if i == iterations:
            break
        # connect
        distance, boxes = connection
        box1, box2 = boxes
        # neither box1 nor box2
        if not box1 in connectedBoxes and not box2 in connectedBoxes:
            newCircuit = Circuit(box1, box2)
            connectedBoxes[box1] = newCircuit
            connectedBoxes[box2] = newCircuit
            circuits.add(newCircuit)
        # only box2
        elif not box1 in connectedBoxes and box2 in connectedBoxes:
            connectedBoxes[box2].addBox(box1)
            connectedBoxes[box1] = connectedBoxes[box2]
        # only box1
        elif box1 in connectedBoxes and not box2 in connectedBoxes:
            connectedBoxes[box1].addBox(box2)
            connectedBoxes[box2] = connectedBoxes[box1]
        # both box1 and box2
        else:
            circuit1 = connectedBoxes[box1]
            circuit2 = connectedBoxes[box2]
            if circuit1 != circuit2:
                circuits.remove(circuit2)
                circuit1.addBox(circuit2.boxes)

                for c in circuit1.boxes:
                    connectedBoxes[c] = circuit1

    sortedCircuits = sorted(circuits, key=lambda x: len(x), reverse=True)

    numOfLargest = 3
    prodSizes = 1

    for i in range(numOfLargest):
        prodSizes *= len(sortedCircuits[i])

    return prodSizes


if __name__ == "__main__":
    print(f"The answer is: {main()}")
