def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def validId(id: int) -> bool:
    strId = str(id)
    # print(id)
    for i in range(1, (len(strId)//2)+1):
        # check len is multiple of i
        if len(strId) % i != 0:
            continue
        
        # splice pattern
        pattern = strId[:i]

        # check all patterns from beginning
        for j in range(i, len(strId)+1, i):
            # doesn't match go next
            if pattern != strId[j:j+i]:
                break
        # got to end # found match
        if j == len(strId):
            print(f'found at {id}')
            return False
    # no matches found
    return True

def parseInput(input: str) -> list[tuple[int, int]]:
    # split into ranges
    idRanges = input.split(',')
    newIdRanges = []
    # split start and end ranges
    for idRange in idRanges:
        a, b = idRange.split('-')
        newIdRanges.append((int(a), int(b)))
    return newIdRanges

def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()
    
    invalidIdSum = 0
    idRanges = parseInput(textIn[0])

    for (startRange, endRange) in idRanges:
        for id in range(startRange, endRange+1):
            if not validId(id):
                invalidIdSum += id

    return invalidIdSum

if __name__ == '__main__':
    print(f'The answer is: {main()}')